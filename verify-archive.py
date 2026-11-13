"""Rebuild navigation and integrity records for the pinned Lean source.
This script does text/import analysis; it is not a Lean parser or kernel replay.
Run from any directory with Python 3.9+.
"""
from pathlib import Path
import hashlib, json, re, tarfile
BASE=Path(__file__).resolve().parent
PIN='804bdb55b1fc40e6a1a6878fd96078644a70e288'
ROOT=BASE/('zeta-density-three-over-two-sigma-lean-'+PIN)
LEAN=ROOT/'lean'
files={p.relative_to(LEAN).with_suffix('').as_posix().replace('/','.'):p for p in LEAN.rglob('*.lean')}
ordered=[];seen=set();external=set()
def visit(mod):
    if mod in seen:return
    seen.add(mod)
    if mod not in files:
        external.add(mod);return
    text=files[mod].read_text(encoding='utf-8')
    for dep in re.findall(r'^(?:public )?import\s+(\S+)',text,re.M):visit(dep)
    ordered.append(mod)
visit('Solution')
records=[];byname={};byfile={};bybase={}
for mod in ordered:
    p=files[mod];text=p.read_text(encoding='utf-8');decls=[]
    starts=list(re.finditer(r'^(?:(?:private|protected|noncomputable)\s+)*(?:def|theorem|lemma|structure|class|instance|abbrev)\s+([^\s:{(]+)',text,re.M))
    for i,a in enumerate(starts):
        end=starts[i+1].start() if i+1<len(starts) else len(text)
        body=text[a.start():end]
        sig=re.split(r':=\s*(?:by\b)?',body,maxsplit=1)[0].strip()
        d={'name':a.group(1),'line':text[:a.start()].count('\n')+1,'statement':sig}
        decls.append(d)
        byname.setdefault(d['name'],[]).append((p.relative_to(ROOT).as_posix(),d['line']))
    r={'module':mod,'file':p.relative_to(ROOT).as_posix(),'lines':len(text.splitlines()),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'declarations':decls}
    records.append(r);byfile[r['file']]=r;bybase.setdefault(p.name,[]).append(r)
tex=(BASE/'zeta-density-blueprint.tex').read_text(encoding='utf-8')
refs=[];unresolved=[];ledger=['# Source ledger','',f'Pinned source revision: `{PIN}`.','',
'This is text/import navigation, not a logical dependency closure or a kernel certificate. Declaration starts are recognized by a regular expression; generated and unusually formatted declarations may be omitted. The human-readable mathematical proof is in `zeta-density-blueprint.tex`.','',
'## Blueprint correspondences','']
for m in re.finditer(r'\\src\{([^{}]*)\}\{([^{}]*)\}',tex):
    line=tex[:m.start()].count('\n')+1
    fs=[x.strip() for x in m[1].split(';')];ns=[x.strip() for x in m[2].split(';')]
    resolvedfiles=[];directory=''
    for f in fs:
        candidates=[f,'lean/'+f,'lean/MathCollab/Density/'+f]
        if directory:candidates.insert(0,directory+'/'+f)
        hits=[c for c in candidates if c in byfile]
        if hits:
            r=byfile[hits[0]];resolvedfiles.append(r['file']);directory=str(Path(r['file']).parent)
        elif len(bybase.get(Path(f).name,[]))==1:
            r=bybase[Path(f).name][0];resolvedfiles.append(r['file'])
        else:unresolved.append({'line':line,'file':f})
    entries=[]
    ledger.extend([f'### Blueprint line {line}','',f'Files: '+', '.join('`'+x+'`' for x in resolvedfiles)+'.',''])
    for n in ns:
        matches=byname.get(n,byname.get(n.split('.')[-1],[]))
        chosen=[x for x in matches if x[0] in resolvedfiles] or matches
        if not chosen:unresolved.append({'line':line,'name':n})
        entries.append({'display_name':n,'locations':[{'file':f,'line':l} for f,l in chosen]})
        ledger.append('- `'+n+'`: '+', '.join(f'`{f}:{l}`' for f,l in chosen))
    ledger.append('')
    refs.append({'tex_line':line,'files':resolvedfiles,'declarations':entries})
ledger.extend(['## External import roots','',
'The external import names below are read from the local import closure. Their mathematical interfaces are discussed in the blueprint. This list is not an audit of their entire transitive code.',''])
ledger.extend('- `'+x+'`' for x in sorted(external))
ledger.extend(['','## Local import inventory',''])
for r in records:
    ledger.extend([f"### {r['module']}",'',f"File: `{r['file']}`; {r['lines']} source lines; SHA-256 `{r['sha256']}`.",''])
    ledger.extend('- `'+d['name']+'` at line '+str(d['line']) for d in r['declarations'])
    ledger.append('')
(BASE/'source-ledger.md').write_text('\n'.join(ledger)+'\n',encoding='utf-8')
labels=re.findall(r'\\label\{([^}]+)\}',tex)
uses=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',tex)
controls=[{'line':tex[:i].count('\n')+1,'codepoint':ord(c)} for i,c in enumerate(tex) if ord(c)<32 and c not in '\r\n\t']
archive=BASE/'registered-source.tar.gz';mismatch=[];count=0
with tarfile.open(archive) as tf:
    members=tf.getmembers();prefix=members[0].name.split('/')[0]
    for m in members:
        if m.isfile():
            rel=m.name.removeprefix(prefix+'/');p=ROOT/rel;count+=1
            if not p.is_file() or p.read_bytes()!=tf.extractfile(m).read():mismatch.append(rel)
registry=json.loads((BASE/'registry-v1.json').read_text())
solutionhash=hashlib.sha256((LEAN/'Solution.lean').read_bytes()).hexdigest()
report={'method':'Text/import traversal and regex declaration recognition, not Lean kernel replay.',
    'source_commit':PIN,'local_import_modules':len(records),'local_import_lines':sum(x['lines'] for x in records),'regex_declarations':sum(len(x['declarations']) for x in records),'total_lean_files':len(files),'total_lean_lines':sum(len(p.read_text().splitlines()) for p in files.values()),
    'archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'archive_regular_files':count,'snapshot_mismatches':mismatch,
    'solution_sha256':solutionhash,'solution_matches_registry':solutionhash==registry['verification']['solution_sha256'],
    'tex_lines':len(tex.splitlines()),'tex_whitespace_words':len(tex.split()),'source_correspondence_groups':len(refs),'unresolved_correspondences':unresolved,
    'undefined_labels':sorted(set(uses)-set(labels)),'duplicate_labels':sorted({x for x in labels if labels.count(x)>1}),'unexpected_control_characters':controls,
    'references':refs}
(BASE/'source-reference-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(BASE/'source-import-inventory.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='references'},indent=2))
if unresolved or mismatch or not report['solution_matches_registry'] or report['undefined_labels'] or report['duplicate_labels'] or controls:
    raise SystemExit('An integrity/navigation check failed; inspect source-reference-audit.json.')
