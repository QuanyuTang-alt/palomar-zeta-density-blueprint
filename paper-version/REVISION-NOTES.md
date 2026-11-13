# 学习版修订说明

## 定位与交付结构

新版是 **论文式英文学习讲义**，旨在供用户与朋友学习 Mark Lewko 及上游署名贡献者的证明方法，不是用户的原创论文，也不是实际投稿。没有abstract、MSC或keywords。原49页蓝图、固定Lean源码、原审计与历史上传回执保持原样，新稿独立放在 `paper-version/`。

正文采用“零密度主线优先，矩论证细节在附录”的阅读顺序：Introduction → zeros/multiplicity → analytic preliminaries → independent large-values estimate → smooth detector → short blocks → long blocks/final density。附录A–F完整保留四次矩、点均值、Voronoi与两signed stationary contributions、maximal-prefix Gram、peak occupancy/high-low twelfth、AFE/Bessel/Fresnel等学习细节。TeX中的81组原源码对应改为comments，不打断阅读；新行号见`study-source-map.json`。

## 主要改动位置

1. **Introduction（§1）**：增加背景、density hypothesis的明确陈述、原结果归属、精确主定理、参数范围与历史比较、proof ideas、数学依赖图、organization。只把猜想作为背景，不虚称full density hypothesis或RH已经解决。没有强行加入与本项目无关的“非唯一选取定理”。
2. **历史比较（§1）**：Kerr2019 Theorem6已给相同指数，范围σ≥23/29。相对于已定位TTY Table2/Kerr/数据库，新结果的严格leading-exponent改进区间为(3/4,23/29)；[23/29,7/8]相同；(7/8,1)已有界更强。这不是穷尽所有文献/未发表工作的优先权判断。无需因此取消作为学习材料的整理。
3. **大幅阅读简化（Theorem1.3）**：直接引用Heath-Brown1978 Theorem1，U=3T并吸收(log U)^17得到本稿所需twelfth moment。附录仍给原formal路线，不把经典矩定理写成新贡献。独立large-values argument暂不能用已定位Kerr较窄范围结论无条件替代，因此保留。
4. **紧集零有限性（Lemma2.2）**：旧说明跨过ζ在1的极点而没有解释；补F(z)=(z−1)ζ(z)的entire延拓、F(1)=1、非零entire函数紧集零有限。正有限vanishing order与local factorization显式说明。
5. **记号（§1.2、§5、§6、附录C/D/F）**：定义μ、Dirichlet convolution与fixed-family coefficient；Euler常数γ_E与ordinateγ区分，Mellin权Ω与ordinate set W区分；有限dyadic index set改mathcal J_R，prefix dyadic count保留J(N)；J(0)=J(1)=0避免log0。Mellin derivative明确写(Mg)'而不是M(g')。为Gaussian和signed-saddle计算标明T,G,L>0与零索引约定。
6. **Taylor边界（§6.1）**：保留r≤J_T的组件，tail从J_T+1开始，消除文字重叠；weighted extraction保持绝对权重总质量≤3/2，因此不多花一个J_T因子。
7. **half-scale（§6.1）**：显式写出natural truncated subtraction的非负指数，非零block中j>0时仍为2^(j−1)、2^j，不在一般整数j处产生错误负指数。
8. **variation（附录C.5）**：定义combined variation quantity为uniform norm与increment sum的max。不是只写未定义Var，也不是将源中的两独立界误当单一total variation；partial summation factor2保持。
9. **phase/derivative（附录D.2）**：将“positive difference”改成phase difference has positive second derivative；函数值的符号与curvature的符号不混淆。near/far gap、triangle branch和prefix endpoint+2条件保留。
10. **contour/genuine tails（§5/§7、附录A/B/C/F）**：显式区分finite/无限prefix-tail、Mellin continuation与实际convergence strip、moving double pole、physical weighted tail、Fresnel Abel limit。补AFE端点amplitude H/H1及coefficient bound的具体定义，不用未定义“minus-square tail”等占位术语。
11. **命题与标题（全篇）**：theorem/lemma/proposition/definition/proof环境后不再有optional方括号标题，改为前导句。将定义中的系数推导、主定理的见证/编码说明、bootstrap吸收、stationary应用等移到定义外或证明。命题不含Consequently推导；必要的双identity/收敛属性仍并列陈述，避免为了形式拆成无意义命题。
12. **非标准术语与语言（全篇）**：用maximal prefixes、local second-moment excesses、mean-square estimates等代替Native/packet/producer/consumer等代码术语；源码名保留comments和导航。修复重排产生的主谓一致、大小写、重复local和Mellin权残留；统一英语、ASCII TeX accents、数学标点与期刊格式。
13. **公式和引文（全篇）**：仅被实际引用的display编号，其他改star/un-numbered；检查label存在、重复、引用双向与bibliography字母排序。所有16条文献有正文引用。编译/导航检查不等同数学证明认证。
14. **书目（References）**：增加经典来源、正规DOI、卷页、出版类型。Ingham四次矩publisher1928与传统1926差异如实保留在核查说明；TTY终核查发现journal-issue print date2026-11，新稿采用95(2026)并另注online2025。Kerr用真实arXiv preprint，不采用自动误配的另一Kerr。
15. **存档**：现GitHub仓库已按用户要求公开。新增paper-version，不更改旧源码/蓝图；当前README说明public，历史private回执仍真实保存。原旧ZIP不自动声称包含新版。

## 每个命题是否检查

详见 `PROPOSITION-REVIEW.md`：原25个正式命题及三个定义逐项列出位置、核心条件、校订与文献简化决定，未编号推导另列范围。详见 `BIBLIOGRAPHY-CHECK.md`：16项题录逐项与结论支持范围核对。

## 最后编译与文件检查

最新版PDF为44页。LaTeX编译没有错误、未解析引用、overfull或underfull box警告。33组编号display全部有实际引用，16条书目全部被引用；25个正式命题、3个定义及81组原源码对应保留。全部44页经过正文/链接出界检查；标题、依赖图、卷积family、contour和参考文献等代表页另作视觉检查。这些只证明对应文件和排版检查结果，不证明数学正确性。

## 认证边界

这是经过原稿/新版通读、逐命题审查、重点Lean源对照与特定经典文献核读的学习稿；**不保证英文证明零漏洞，不声称新的Lean kernel replay或独立人类同行评审**。源中Lean通过的历史记录不自动证明本英文改写完全正确。通用英文写作工具的Markdown workflow不能完整验收纯数学TeX，未虚报其PASS；实际LaTeX编译、引用/编码与PDF边界检查另有`editorial-check.json`与编译log。
