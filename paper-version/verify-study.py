#!/usr/bin/env python3
"""Editorial/integrity checks only; this is not a mathematics verifier."""
from pathlib import Path
import collections
import hashlib
import json
import re
import tarfile
import pymupdf

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SNAPSHOT = ROOT / 'zeta-density-three-over-two-sigma-lean-804bdb55b1fc40e6a1a6878fd96078644a70e288'
OLD_HASH = 'c24fcaffecda5d00e5dcbab00e2d211cdfb95e2cad4223e9aeb9a84734c25ced'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def no_comments(text):
    return '\n'.join(re.split(r'(?<!\\)%', line, maxsplit=1)[0] for line in text.splitlines())

def pairs(text, original=False):
    pattern = r'(?m)^\\src\{([^\n]*)\}\{([^\n]*)\}$' if original else r'(?m)^% Source correspondence: (.+)\}\{(.+)\}$'
    return [(m.group(1), m.group(2), text[:m.start()].count('\n') + 1) for m in re.finditer(pattern, text)]

tex_path = HERE / 'zeta-density-study.tex'
pdf_path = HERE / 'zeta-density-study.pdf'
text = tex_path.read_text(encoding='utf-8', errors='strict')
clean = no_comments(text)
old = (ROOT / 'zeta-density-blueprint.tex').read_text(encoding='utf-8', errors='strict')
old_pairs, new_pairs = pairs(old, True), pairs(text)
history = json.loads((ROOT / 'source-reference-audit.json').read_text())
old_by_key = {(a,b): line for a,b,line in old_pairs}
refs_by_line = {r['tex_line']: r for r in history['references']}
source_map = []
for files, declarations, line in new_pairs:
    old_line = old_by_key.get((files,declarations))
    ref = refs_by_line.get(old_line, {})
    source_map.append({'study_tex_line':line, 'original_tex_line':old_line,
                       'displayed_files':files, 'displayed_declarations':declarations,
                       'resolved_files':ref.get('files',[]),
                       'resolved_declarations':ref.get('declarations',[])})

labels = re.findall(r'\\label\{([^}]+)\}', clean)
ref_keys = re.findall(r'\\(?:eqref|ref|pageref)\{([^}]+)\}', clean)
citations = [key.strip() for m in re.finditer(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}', clean) for key in m.group(1).split(',')]
bib = re.findall(r'\\bibitem\{([^}]+)\}', clean)
expected_bib = ['atkinson','bourgain','gm','hb78','hb79','ingham28','ingham','ivic','ik','kerr','source','mathlib','montgomery','registry','tty','titchmarsh']
numbered = []
for m in re.finditer(r'\\begin\{(equation|align|gather)\}([\s\S]*?)\\end\{\1\}', clean):
    keys = re.findall(r'\\label\{([^}]+)\}', m.group(2))
    numbered.append({'environment':m.group(1), 'labels':keys,
                     'all_labels_referenced':bool(keys) and all(k in ref_keys for k in keys)})
counts = {name:len(re.findall(r'\\begin\{'+name+r'\}',clean)) for name in ['theorem','lemma','proposition','definition','conjecture','proof']}
stack=[]
env_errors=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',clean):
    action, name = m.groups()
    if action=='begin': stack.append(name)
    elif not stack or stack[-1]!=name: env_errors.append(m.group(0))
    else: stack.pop()
env_errors.extend(stack)

snapshot_mismatches=[]
regular=0
with tarfile.open(ROOT/'registered-source.tar.gz','r:gz') as archive:
    for member in archive.getmembers():
        if not member.isfile(): continue
        regular+=1
        rel=Path(*Path(member.name).parts[1:])
        target=SNAPSHOT/rel
        if not target.is_file() or archive.extractfile(member).read()!=target.read_bytes():
            snapshot_mismatches.append(str(rel))

pdf_checks=[]
with pymupdf.open(pdf_path) as document:
    for i,page in enumerate(document,1):
        blocks=page.get_text('blocks',sort=True)
        out=[list(b[:4]) for b in blocks if b[0]<0 or b[1]<0 or b[2]>page.rect.width+0.5 or b[3]>page.rect.height+0.5]
        links=[str(link['from']) for link in page.get_links() if not page.rect.contains(link['from'])]
        pdf_checks.append({'page':i,'text_characters':len(page.get_text('text',sort=True)),
                           'out_of_page_text':out,'out_of_page_links':links})
log=(HERE/'zeta-density-study.log').read_text(errors='strict')
log_issues=[line for line in log.splitlines() if re.search(r'Overfull|undefined|multiply defined|^!|Missing character',line)]
underfull=[line for line in log.splitlines() if 'Underfull' in line]

checks={
 'original_blueprint_unchanged':digest(ROOT/'zeta-density-blueprint.tex')==OLD_HASH,
 'snapshot_regular_files':regular,
 'snapshot_mismatches':snapshot_mismatches,
 'preserved_source_groups':len(new_pairs),
 'missing_source_groups':[list(k) for k in set((a,b) for a,b,_ in old_pairs)-set((a,b) for a,b,_ in new_pairs)],
 'extra_source_groups':[list(k) for k in set((a,b) for a,b,_ in new_pairs)-set((a,b) for a,b,_ in old_pairs)],
 'unresolved_source_map':[r['study_tex_line'] for r in source_map if r['original_tex_line'] is None or not r['resolved_files']],
 'environment_counts':counts,
 'environment_balance_errors':env_errors,
 'optional_statement_or_proof_titles':re.findall(r'\\begin\{(?:theorem|lemma|proposition|definition|proof|conjecture)\}\[[^\]]*\]',clean),
 'undefined_labels':sorted(set(ref_keys)-set(labels)),
 'duplicate_labels':[k for k,v in collections.Counter(labels).items() if v>1],
 'numbered_displays':numbered,
 'unreferenced_numbered_labels':[k for k in labels if k.startswith('eq:') and k not in ref_keys],
 'bibliography_entries':len(bib),
 'bibliography_key_order':bib,
 'expected_author_alphabetical_order':bib==expected_bib,
 'uncited_bibliography_entries':sorted(set(bib)-set(citations)),
 'undefined_citation_keys':sorted(set(citations)-set(bib)),
 'non_ascii_tex_characters':sorted(set(c for c in text if ord(c)>127)),
 'unexpected_controls':[ord(c) for c in text if ord(c)<32 and c not in '\n\r\t'],
 'abstract_msc_keywords_present':bool(re.search(r'\\begin\{abstract\}|MSC|[Kk]eywords',clean)),
 'tex_log_issues':log_issues,
 'underfull_box_warnings':underfull,
 'pdf_pages':len(pdf_checks),
 'pdf_page_checks':pdf_checks,
}
failures=[]
for key in ['snapshot_mismatches','missing_source_groups','extra_source_groups','unresolved_source_map','environment_balance_errors','optional_statement_or_proof_titles','undefined_labels','duplicate_labels','unreferenced_numbered_labels','uncited_bibliography_entries','undefined_citation_keys','unexpected_controls','tex_log_issues']:
    if checks[key]: failures.append(key)
for key in ['original_blueprint_unchanged','expected_author_alphabetical_order']:
    if not checks[key]: failures.append(key)
if counts['theorem']+counts['lemma']+counts['proposition']!=25 or counts['definition']!=3: failures.append('environment_counts')
if not all(item['all_labels_referenced'] for item in numbered): failures.append('numbered_displays')
if any(p['out_of_page_text'] or p['out_of_page_links'] or not p['text_characters'] for p in pdf_checks): failures.append('pdf_boundaries')
if checks['abstract_msc_keywords_present']: failures.append('excluded_front_matter')
result={'scope':'Deterministic editorial, artifact and navigation checks only. Not a mathematical, literature-support or Lean-kernel certificate.',
        'editorial_status':'PASS' if not failures else 'FAIL', 'failures':failures,
        'file_sha256':{p.name:digest(p) for p in [tex_path,pdf_path,ROOT/'zeta-density-blueprint.tex']},
        'checks':checks}
(HERE/'study-source-map.json').write_text(json.dumps(source_map,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(HERE/'editorial-check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'editorial_status':result['editorial_status'],'failures':failures,'pdf_pages':len(pdf_checks),'source_groups':len(new_pairs),'numbered_displays':len(numbered),'bibliography_entries':len(bib),'underfull_warnings':len(underfull)},ensure_ascii=False,indent=2))
raise SystemExit(bool(failures))
