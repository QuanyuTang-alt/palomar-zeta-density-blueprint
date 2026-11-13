# 逐命题审查与文献简化记录

## 范围和结论的含义

本记录覆盖原 `zeta-density-blueprint.tex` 的全部 **25 个 theorem/lemma/proposition 环境及 3 个 definition 环境**。新增的 Conjecture 1.1 只是历史背景，另行说明。原稿未编号的重要推导仍保留在新版正文或附录中，其 81 组源码对应也全部保留；`study-source-map.json` 给出新版行号。

检查内容包括陈述的量词、变量范围、积分/级数的收敛、符号和端点、证明中的标量代数、后续使用的假设，以及已定位文献是否在相同条件下可替代相应步骤。已重读原稿与新版全文，并对关键源码定义和证明作定向核读。下列“保留”表示未在此次检查中发现必须改变该数学结论的问题，**不是每个证明已获独立认证或保证无漏洞**。没有重新执行 Lean kernel replay；没有声称逐行复核全部 448 个本地模块及所有 mathlib 依赖。

编号取新版 LaTeX 环境编号；原行号定位旧稿，后续新版行号由机器映射给出。

## 原稿25个正式命题

1. **原行131：Registered zero-density endpoint → Theorem 1.2，证明在 §7.3。** 保留 σ>3/4、ε>0、所有 T≥2、双符号 ordinate 和解析重数。将有限集见证、编码转换移到 §2 和最终证明，而主陈述只写需要的数值界。检查短/长集合互补、12η≤ε、σ≥1空集分支、闭边界和紧初段。Kerr Theorem 6 只覆盖 σ≥23/29，不能替代完整 σ>3/4 范围；已定位文献比较不等于穷尽优先权审查。

2. **原行149：Registered actual twelfth moment → Theorem 1.3，详细证明在附录E.3。** 主线直接引用 Heath-Brown (1978), Theorem 1：上界 U²(log U)^17；U=3T 后吸收对数得到本稿需要的 ε-loss 版本。这是确定可行的大幅阅读简化。保留附录中四次矩、高值、layer cake 和零起点 dyadic induction 供学习。局部可积性改放 analytic preliminaries，而不是与主矩定理堆叠。

3. **原行186：Finiteness and local factorization → Lemma 2.2。** 修复紧球可能包含1的极点问题：使用 F(z)=(z−1)ζ(z) 的 entire 延拓，F(1)=1，应用 identity theorem 与紧性。局部分解、正有限 vanishing order 保留。这是补足英文解释，不是发现固定 Lean 源有同一漏洞。可以引用一般解析函数理论，但短证明本身更利于学习。

4. **原行216：Exact membership → Lemma 2.3。** 检查 σ>3/4 给正实部、Re ρ≥1 的非零性、|Im ρ|≤T 与双边不等式等价、σ≥1空集。保留直接证明，不需要引入另一个零计数定理。

5. **原行289：Actual critical-line Weyl growth → Proposition 3.1，附录F.1/F.4。** Weyl bound 是经典结果，可以在首次阅读时引用 Ivić/Titchmarsh。保留正式开发使用的有限差分、partial summation 和 sharp AFE 详细路径。核对 cutoff gaps、Gamma-Laplace damping、正负 heights 与紧初段。没有把一般 coarse growth 当成 t^(1/6) 的证明。

6. **原行380：Independent Type I estimate → Theorem 4.2，证明在 §4.3。** 保留 N∈[T^(1/3),T]、V≥N^(3/4+κ)、任意平移区间和 one-separation。核对 M=ceil(b√T) 的整数舍入、NM范围、divisor loss、空集/有界高度。Kerr 的相关大值结论具有额外参数条件；未定位到可无条件删掉本独立论证的完全同条件结论，所以保留完整证明。不把 Guth–Maynard 或书中的 generic mean square 误当成它的直接替代。

7. **原行411：Comparison with kernel energy → Lemma 4.3。** 核对 complete pair Gram expansion、M|U|² 对角下界、插入非零 D(t)、乘积 n q 的 divisor multiplicity、cutoff plateau、one-separated row sum 和 xy≤(x²+y²)/2 吸收。属于 Halász–Montgomery 型比较方法；经典来源可解释思想，但本稿的 kernel、support 和 scale normalization 仍需展示。保留。

8. **原行482：All-frequency estimate → Lemma 4.4。** 检查任意实 τ、a>0、stationary window 两边积分分部，以及 s²=2πa 导出的中间区间2/s。没有偷加 |τ| 或 Mellin-frequency restriction。可视作标准 first-derivative 方法的具体实现，证明很短，直接保留。

9. **原行575：Bootstrap inequality → Lemma 4.5。** 陈述只给 B≤C0+C1Nb²log(2T)B，uniform absorption 放证明。检查 supremum 非空且有限，但 scale family 非有限；比较中的反射整数 M′满足 N≤NM′≤8(T+1)，local windows 的三重覆盖，gap shells 和误差归一化。正κ与 divisor subpower 使递归系数趋零。这是关键方法，不用抽象 absorption 一句话替代全部前提。

10. **原行696：Exact source decomposition → Lemma A.1。** 将 J_c、B_t、R 的定义移到命题前；陈述 contour identity 和 Z²=2Re R，四次不等式移到证明。核对 entire pole-cleared numerator、唯一1/w极点、反射方向、critical completed value实性和 Gamma factors。可通过经典 approximate functional equation 得到相关矩结论，但这不替代本稿精确 one-sided identity，保留。

11. **原行828：Dyadic mean square → Lemma A.2。** Iwaniec–Kowalski 的 Dirichlet mean-value theorem 是可用标准替代。为学习保留 finite Fourier orthogonality、sawtooth Hilbert form 和 reciprocal-log error。特别核对主 Hilbert form 缩放的是共轭的第一个系数族、两个 endpoint forms 的 factor2 和平移不变性。

12. **原行886：Native fourth moment → Proposition A.3。** 可直接引用 Ingham 的经典四次矩。保留 contour/truncation/mean-square proof，因为它与附录C重用 squared-zeta representation。q=min(η,1)/20 不是 min(η,1/20)，固定源无此错误；核对 tail line b=2+2/q、N≈H^(1+q)、1+5q+2q²≤1+7q。

13. **原行960：Point-to-mean → Proposition B.1。** 定位 Heath-Brown Lemma 3 (印刷p455)，可以直接引用其 local-mean bound。保留矩形、双重卷积、全均值到截断均值、compact completion。注明 δ=1/log t 的 δ≤1/4 估计只在足够大 t 使用，剩余 t≥10 紧段单独处理；最初 rectangle 的 ζ moving pole 在 Re w=1/2 外。两极点 Mellin shift 的 double residue 保留。

14. **原行1044：Exponential overlap/finite peaks → Lemma B.2。** 定位 Heath-Brown equation (44) (p456)。核对 separation、G/2+L≤G、每个局部区间都装进[c−G,c+G]、log t≤log T 和非负被积函数的交换。几何级数 overlap 的证明短，保留，不能省略 width fit 条件。

15. **原行1205：Compact-test divisor Voronoi → Lemma C.1。** 这是经典 divisor Voronoi identity，可引用标准解析数论教材作为方法来源；保留其本地精确 proof，以保障后续两支符号、−2πY0 与+4K0 normalization。核对 genuine compact test、double pole 的导数、Mellin 记号 (Mg)' 与 M(g') 的区别、Y0 absolute convergence strip 与13/16 dual line。没有在发散域使用未延拓的 Mellin 积分。双 dual series 明确为绝对收敛。

16. **原行1356：Fourth-root stationary error → Lemma C.2。** 一般 stationary-phase 文献只有核对相同 amplitude/width/remainder 才能代替；未确认可直接替代本 lemma 的同常数同条件结论。保留 x=y² 的 Jacobian、root phase、odd cubic/linear cancellation、Fresnel phase e^(−iπ/4)、h=T^(1/4)/(12√G) 和错误界。将 b=±√n 的应用移出陈述。四个 residual terms 明确，不把标准 stationary phase 的笼统引用当作误差证明。

17. **原行1633：Physical prefix packet budget → Lemma D.1。** 改用标准 maximal-prefix/Gram terminology。检查每个 height 自选 j_t、Gram 中 min(j_t,j_u)、near harmonic rows、far gap 的 triangle branch、dyadic J(N)² 和 cutoff-plus-two geometry。定义 J(0)=J(1)=0，G-separation 明确。经典 large sieve 的想法不能消除本稿的 height-dependent phase calculation，保留。

18. **原行1674：Actual local-mean packet → Proposition D.2。** 命名改为 local second-moment excess sum。核对 t-wise width assumptions、N*=ceil(36T(log T/G)²)、其单调性、74Hlog²(2H)/G² ceiling bound、三项 physical budget、spare logarithmic loss 和空集分支。Heath-Brown 原文通过 Atkinson formula 的路线相关，但没有确认其精确 weights 可与本地 signed representation 无条件互换，保留生产链。

19. **原行1727：Local-to-global absorption → Lemma E.1。** 核对 L*、√(GL*)=Y²/(4A)、quadratic term absorption、floor bins 捕获闭右端、2AH/(GY²)+32A³H²/Y^6。纯有限覆盖代数，引用外部定理不会明显缩短或改善，保留。

20. **原行1821：High-value finite-set bound → Proposition E.2。** 主线可由整体经典矩路线绕开，本附录仍保留。检查 G=V²/(K log²(3H))、κ/δ/ν、V≥H^(1/8+ε)、非空时Weyl upper bound、8η≤ε、threshold precedes V,W。不能只数一个 cluster representative；integer occupancy layer cake 恢复全部 peaks。

21. **原行1852：Finite separated sets to measure → Lemma E.3。** 检查最大有限 cardinality 的存在、closed unit balls cover、Lebesgue length≤2B 和 superlevel measurability。标准 packing argument 已短，直接保留。

22. **原行1873：Truncated high moment → Lemma E.4。** 标准 layer-cake/Cavalieri 方法可引用 measure theory，但本文给出的 max(V^12,s) 分布函数上界和对数积分解释更直观，保留。检查 C≥0、V^12≤M、upper truncation 和所有U≥V的量词，没有用单一 level bound 代替全尾界。

23. **原行1988：Exponentially smoothed contour identity → Lemma 5.2。** 核对 initial right line、ρ+w实部>1、Γ(0) pole 因ζ(ρ)=0被消去、唯一 moving ζ pole、正确 residue 和 left line。Mellin inversion/contour shift 是标准工具，但 exact formula 是 zero detector 的关键，应保留。X 不必正时截断和定义仍有效；指数衰减使 detector series 绝对收敛。

24. **原行2020：Uniform large tail → Lemma 5.3。** 核对 c(β−1/2)≥1/4、δ≤1/8、Weyl positive θ<1/48、T^(−1/48+θ) 衰减、residue exponential bound、unit term反三角不等式。这是具体参数选择，外部 zero detector 的较宽泛陈述不能替代 uniformity 和 removed-unit-term 检查，保留。

25. **原行2229：Uniform local multiplicity → Lemma 6.1。** 标准 Jensen zero count 可引用，但保留 radius3/2与7/4、center2+i(k+1/2)、Mobius inverse |ζ(center)|≥3/5、growth sphere、multiplicity bridge 和 bounded heights。经典 O(log T) 的文字引用不解释重数恢复，故保留短证明。

## 原稿三个定义

- **原行170 → Definition 2.1。** 非平凡零、vanishing order、inclusive slabs 和对称计数。补充局部分解定义，避免“natural analytic order”被视为未定义名词。有限性在Lemma2.2建立。
- **原行356 → Definition 4.1。** D、admissible data、one-separated、local diameter、Δ和b。区别(N,2N]与[M,2M)，保留 empty-diameter convention，不把有限U误当无限集。
- **原行1968 → Definition 5.1。** 定义μ、natural floor、M_X、b_X、D/T detector。系数取消与mollifier norm等推导已移出definition。Dirichlet convolution在§6.2显式定义，family coefficient具体写出。

## 未编号推导的检查范围

§4的Poisson band/Mellin separation/reflection与supremum；§5 smooth partition与指数tail；§6 binomial normalization、tail从J_T+1起、bounded power、convolution support、fixed family与short accounting；§7 q≥0 uniform damping、moving residue、weighted Hölder、physical T^(-113) tail、long saving、最终compact/dyadic/conjugation；附录A Gamma shift与prefix/true-tail；附录B convolution；附录C Gaussian freeze/lattice phase/两signed saddles/variation；附录D index curvature与physical budget；附录E cluster occupancy；附录F AFE/Bessel/Fresnel/finite cancellation与full-series majorants。它们没有因“不是命题环境”而被删除；81组对应记录是导航覆盖，不是语义认证。

## 背景猜想与历史比较

Conjecture 1.1明确只作density hypothesis背景。这里没有声称解决full conjecture或RH，也不将本学习稿或其整理者写成新定理作者。引言给出的严格改进区间只相对于明确定位的TTY Table2与Kerr等来源；零密度研究的全部最新和未发表结果没有被穷尽。

## 尚未取得的认证

没有新Lean replay、没有独立人类同行审读。主要英文证明已作逐命题与参数检查，发现的解释缺口已在稿中修正；仍不将“可编译/labels resolve/已通读”等同于“英文证明必然正确”。通用英文Markdown写作流程不能完整验收本纯数学TeX成品，其状态不作为数学或LaTeX认证。
