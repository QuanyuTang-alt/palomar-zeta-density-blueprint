# 书目真实性、格式与使用范围核查

本文件区分 **题录核验** 与 **结论原文核读**。一篇文献真实存在、DOI一致，并不证明它支持当前所有数学主张。新稿共16条参考资料，全部在正文引用；按首作者/机构的字母顺序排列，同一作者的两篇按年代排列。期刊条目统一为作者、题名、期刊、卷、年、期号（有意义时）、页码、DOI；书籍为书名、丛书卷号、出版社和年份；软件与注册源采用明确revision，不虚构期刊出处。

## 16项逐条记录

1. **Atkinson** — F. V. Atkinson, *The mean-value of the Riemann zeta function*, Acta Mathematica 81 (1949), 353–376, DOI 10.1007/BF02395027。Crossref的title/author/volume/pages/year一致。用作局部二次矩振荡方法的历史来源；没有宣称原论文的每一细节与本地Voronoi重建相同。
   - 元数据 https://api.crossref.org/works/10.1007/BF02395027
   - 原文 https://projecteuclid.org/journals/acta-mathematica/volume-81/issue-none/The-mean-value-of-the-Riemann-zeta-function/10.1007/BF02395027.pdf

2. **Bourgain** — J. Bourgain, *On the distribution of Dirichlet sums. II*, in *Number Theory for the Millennium, I*, A K Peters, Natick, MA (2002), 87–109。LOC目录确认标题/作者，TTY与ANTDB引文确认书目信息与历史指数范围。不是期刊文章，不强行补卷期或DOI。该篇未全文独立核读；历史指数归属由已定位TTY/数据库支撑。
   - 目录 http://catdir.loc.gov/catdir/toc/fy036/2002029343.html
   - 交叉资料 https://api.crossref.org/works/10.1090/mcom/4138
   - 指数关系 https://teorth.github.io/expdb/blueprint/zero-density-chapter.html

3. **Guth–Maynard** — L. Guth and J. Maynard, *New large value estimates for Dirichlet polynomials*, Annals of Mathematics (2) 203 (2026), no.2, 623–675, DOI 10.4007/annals.2026.203.2.6。Crossref给print date2026-03-01、卷页和完整作者一致。不是只写2024 preprint或“to appear”。本文只将其用于大值阈值的历史背景，不用它无条件替代Theorem4.2。
   - https://api.crossref.org/works/10.4007/annals.2026.203.2.6
   - https://arxiv.org/pdf/2405.20552

4. **Heath-Brown 1978** — D. R. Heath-Brown, *The twelfth power moment of the Riemann zeta-function*, Quarterly Journal of Mathematics, Oxford Ser.(2), 29 (1978), no.4, 443–462, DOI 10.1093/qmath/29.4.443。Crossref题名丢失ζ字样，不能照机器题名改成错误数学；原扫描明确为Riemann zeta-function。实际查看原扫描印刷p444 Theorem1、p455 Lemma3、p456 (44)、p457后续及p462书目。Theorem1给U²(log U)^17，足以支持Theorem1.3；Lemma3与(44)是附录B的具体来源。
   - https://api.crossref.org/works/10.1093/qmath/29.4.443
   - https://wiki.math.ntnu.no/_media/ma3001/2025h/analyticnumbertheory/heathbrowntwelfthmoment.pdf

5. **Heath-Brown 1979** — D. R. Heath-Brown, *Zero density estimates for the Riemann zeta-function and Dirichlet L-functions*, Journal of the London Mathematical Society (2) 19 (1979), no.2, 221–232, DOI 10.1112/jlms/s2-19.2.221。题名、卷期、页码和1979年由publisher/Crossref核验；上界max{3/(10σ−7),4/(4σ−1)}的比较以TTY/ANTDB所列结论为依据。没有声称全文核读该篇所有证明。
   - https://api.crossref.org/works/10.1112/jlms/s2-19.2.221
   - https://teorth.github.io/expdb/blueprint/zero-density-chapter.html

6. **Ingham四次矩** — A. E. Ingham, *Mean-value theorems in the theory of the Riemann zeta-function*, Proceedings of the London Mathematical Society (2) 27, 273–300, DOI 10.1112/plms/s2-27.1.273。存在年份差异：Wiley与Crossref给print1928；Atkinson及Heath-Brown等经典引文传统写1926。新版采用publisher的1928，citation key改ingham28，本记录保留差异，而不宣称传统写法毫无疑问是笔误。用于四次矩背景；精确本地contour proof保留。
   - https://api.crossref.org/works/10.1112/plms/s2-27.1.273
   - https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/plms/s2-27.1.273
   - 传统1926引文 https://api.crossref.org/works/10.1007/BF02395027

7. **Ingham零密度** — A. E. Ingham, *On the estimation of N(σ,T)*, Quarterly Journal of Mathematics, Oxford Ser., 11 (1940), 201–202, DOI 10.1093/qmath/os-11.1.201。注意TTY Crossref参考列表误给first-page291，不能照搬；独立原条目的201–202为本稿采用页码。A(σ)≤3/(2−σ)的历史说明来自已定位经典汇总。
   - https://api.crossref.org/works/10.1093/qmath/os-11.1.201
   - https://academic.oup.com/qjmath/article-abstract/os-11/1/201/1574975

8. **Ivić** — A. Ivić, *The Riemann Zeta-Function: Theory and Applications*, Dover, Mineola, NY, 2003；1985 Wiley版的重印。Dover官方页面给作者、题名、2003-06-16出版；作为标准背景教材使用，不声称已全文读完该书。
   - https://store.doverpublications.com/products/9780486428130?srsltid=AfmBOorRN6V4TShNSNMI7Wlfsylx8OjD6auvF4nxnvRP-eNHjDasx1xC
   - https://www.maths.dur.ac.uk/users/pankaj.vishe/ANT_4H.html

9. **Iwaniec–Kowalski** — H. Iwaniec and E. Kowalski, *Analytic Number Theory*, AMS Colloquium Publications 53, AMS, Providence, RI, 2004, DOI 10.1090/coll/053。Crossref确认两作者、题名、出版社、出版地与2004年；卷53同时由TTY书目与DOI系列编码核对。标准Dirichlet mean value是LemmaA.2可采用的文献替代；本稿仍保留证明的具体常数。未全文读该书，不把此书泛引当作所有本地结果已验证。
   - https://api.crossref.org/works/10.1090/coll/053
   - https://api.crossref.org/works/10.1090/mcom/4138

10. **Kerr** — B. (Bryce) Kerr, *Large values of Dirichlet polynomials and zero density estimates for the Riemann zeta function*, arXiv:1909.12075v1, 2019。arXiv元数据明确作者、2019-09-26、v1；未给journal reference，因此按preprint引用。原文Theorem6明确相同指数范围σ≥23/29；核心Theorems6/7与方法相关内容已核读。自动脚本曾误匹配Anthony John Kerr2026 SSRN，那个候选被排除，未进入本文。
   - https://arxiv.org/abs/1909.12075
   - https://arxiv.org/pdf/1909.12075

11. **Lewko及上游贡献者** — 非期刊文章，是固定Lean开发。用描述性档案题名，保留commit804bdb55b1fc40e6a1a6878fd96078644a70e288。Mark Lewko为registered author；McColm、Grogan及其他贡献的具体notices/provenance保留在原snapshot。没有把用户或本学习稿整理者列为原定理作者。
   - https://github.com/mrklwk/zeta-density-three-over-two-sigma-lean/tree/804bdb55b1fc40e6a1a6878fd96078644a70e288
   - https://data.palomar-registry.org/entries/PALOMAR-2026-10-09-000005-v1.json

12. **mathlib community** — 软件/数学库条目，固定revision065356127b1dc0016f66b7283ce0ce2c4055aa55。用软件引用格式，不虚构journal/volume/pages。本文的Mellin/Fourier/integral基础是它的已引用接口，不声称重建了所有transitive proofs。
   - https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55

13. **Montgomery** — H. L. Montgomery, *Topics in Multiplicative Number Theory*, Lecture Notes in Mathematics 227, Springer, Berlin–New York, 1971。Princeton图书馆记录确认作者、题名、出版地/出版社/1971；TTY书目确认LNM227。用于density hypothesis和经典方法背景，没有声称全文核读该书。
   - https://catalog.princeton.edu/catalog/SCSB-9383324
   - https://api.crossref.org/works/10.1090/mcom/4138

14. **Palomar Registry** — version1的注册记录，非研究论文或期刊条目。保留实际读取的JSON地址及用户permalink。历史verification不等同于本轮新的replay。
   - https://data.palomar-registry.org/entries/PALOMAR-2026-10-09-000005-v1.json
   - https://palomar-registry.org/entry?id=PALOMAR-2026-10-09-000005&version=1

15. **Tao–Trudgian–Yang** — T. Tao, T. Trudgian and A. Yang, *New exponent pairs, zero density estimates, and zero additive energy estimates: A systematic approach*, Mathematics of Computation 95 (2026), no.362, 2941–2990, DOI 10.1090/mcom/4138；online2025-11-06。最终核查发现print year不在顶层published-print，而在journal-issue.published-print为2026-11，所以新版已明确采用2026卷年并另注online日期。此前“无print-year”的阶段性判断已撤回。比较使用已核读arXiv全文及ANTDB对应行；AMS访问受限的页面未重试绕过。
   - https://api.crossref.org/works/10.1090/mcom/4138
   - https://arxiv.org/pdf/2501.16779
   - https://teorth.github.io/expdb/blueprint/zero-density-chapter.html

16. **Titchmarsh** — E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, second edition revised by D. R. Heath-Brown, Oxford University Press/Clarendon Press, Oxford, 1986。UConn library的second edition/creation1986与扫描书名前言一致；OUP当前paperback listing为1987，属于版本/发行日期差异，不改掉1986本版书目。作为标准背景使用，未全文独立核读整书。
   - https://search.lib.uconn.edu/discovery/fulldisplay?adaptor=Local%20Search%20Engine&context=L&docid=alma99523533502432&lang=en&vid=01UCT_STORRS%3A01UCT
   - https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf

## 不作的过度声明

- 文献覆盖比较：限定到已定位的TTY Table2、Kerr与ANTDB等，不宣称全世界所有未发表结果均已排查。
- 未找到期刊归档不能推出preprint从未出版，故Kerr仅按实际可确认版本引用。
- 自动检索脚本的title匹配、authority质量筛选与人工数学原文核查是不同工作。初次工具因同姓作者误配和纯数学authority覆盖不足未完整通过；没有改报告、阈值或检查脚本伪造PASS。当前通用Markdown workflow仍不能代表完整TeX交付或数学认证。
- 题录、编号、编译、source-name resolution与数学正确性是四种不同的检查。
