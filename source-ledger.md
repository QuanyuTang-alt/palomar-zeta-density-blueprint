# Source ledger

Pinned source revision: `804bdb55b1fc40e6a1a6878fd96078644a70e288`.

This is text/import navigation, not a logical dependency closure or a kernel certificate. Declaration starts are recognized by a regular expression; generated and unusually formatted declarations may be omitted. The human-readable mathematical proof is in `zeta-density-blueprint.tex`.

## Blueprint correspondences

### Blueprint line 147

Files: `lean/Solution.lean`.

- `DensityStronger.density_bound`: `lean/Solution.lean:36`
- `exact_membership`: `lean/Solution.lean:13`
- `exact_multiplicity`: `lean/Solution.lean:26`

### Blueprint line 158

Files: `lean/Solution.lean`.

- `DensityStronger.twelfth_moment`: `lean/Solution.lean:62`
- `actual_moment_integrable`: `lean/Solution.lean:55`

### Blueprint line 184

Files: `lean/MathCollab/Density/ZetaCounting.lean`.

- `IsNontrivialZetaZero`: `lean/MathCollab/Density/ZetaCounting.lean:19`
- `zetaMultiplicity`: `lean/MathCollab/Density/ZetaCounting.lean:24`
- `zetaZeroRegion`: `lean/MathCollab/Density/ZetaCounting.lean:56`
- `zetaZeroFinset`: `lean/MathCollab/Density/ZetaCounting.lean:75`
- `zetaSlabCount`: `lean/MathCollab/Density/ZetaCounting.lean:83`
- `zetaDensityCount`: `lean/MathCollab/Density/ZetaCounting.lean:87`

### Blueprint line 214

Files: `lean/MathCollab/Density/ZetaCounting.lean`.

- `zetaZeroRegion_finite`: `lean/MathCollab/Density/ZetaCounting.lean:59`
- `zeta_analyticOrder_ne_top`: `lean/MathCollab/Density/ZetaCounting.lean:26`
- `zetaMultiplicity_pos`: `lean/MathCollab/Density/ZetaCounting.lean:43`
- `zetaMultiplicity_cast`: `lean/MathCollab/Density/ZetaCounting.lean:39`
- `zetaMultiplicity_local_factorization`: `lean/MathCollab/Density/ZetaCounting.lean:49`

### Blueprint line 232

Files: `lean/Solution.lean`, `lean/MathCollab/Density/DensityConclusion.lean`.

- `exact_membership`: `lean/Solution.lean:13`
- `zetaDensityCount_eq_zero_of_one_le`: `lean/MathCollab/Density/DensityConclusion.lean:28`

### Blueprint line 251

Files: `lean/MathCollab/Density/ZetaCounting.lean`, `lean/MathCollab/Density/ZetaConjugation.lean`.

- `zetaSlabCount_mono`: `lean/MathCollab/Density/ZetaCounting.lean:101`
- `zetaDensityCount_mono`: `lean/MathCollab/Density/ZetaCounting.lean:109`
- `zetaDensityCount_le_twice_positive`: `lean/MathCollab/Density/ZetaConjugation.lean:83`
- `zetaSlabCount_split_le`: `lean/MathCollab/Density/ZetaConjugation.lean:66`

### Blueprint line 342

Files: `lean/WeylPort/Block.lean`, `lean/WeylPort/ShortSum.lean`, `lean/WeylPort/ActualZeta.lean`, `lean/MathCollab/Density/WeylInput.lean`.

- `norm_criticalLine_cpow_block_le`: `lean/WeylPort/Block.lean:25`
- `norm_critical_sum_le_log`: `lean/WeylPort/ShortSum.lean:103`
- `eventually_norm_riemannZeta_critical_lt_rpow`: `lean/WeylPort/ActualZeta.lean:31`
- `exists_riemannZeta_critical_dyadic_weyl`: `lean/WeylPort/ActualZeta.lean:124`
- `actual_zeta_weyl_input`: `lean/MathCollab/Density/WeylInput.lean:16`

### Blueprint line 352

Files: `lean/MathCollab/Density/Stronger/MomentGrowth.lean`, `lean/MathCollab/Density/Stronger/PointMean/Native.lean`.

- `zetaMomentCriticalNorm_le_linear`: `lean/MathCollab/Density/Stronger/WeightedTwelfth.lean:19`
- `zetaMomentCriticalNorm_twelfth_eventually_le_cube`: `lean/MathCollab/Density/Stronger/MomentGrowth.lean:41`
- `exists_zetaMomentCriticalNorm_sq_le_quadratic`: `lean/MathCollab/Density/Stronger/PointMean/Native.lean:28`

### Blueprint line 378

Files: `lean/MathCollab/Density/LargeValueDefinitions.lean`.

- `detectingPolynomial`: `lean/MathCollab/Density/LargeValueDefinitions.lean:19`
- `oneSeparated`: `lean/MathCollab/Density/LargeValueDefinitions.lean:25`
- `localDiameter`: `lean/MathCollab/Density/LargeValueDefinitions.lean:31`
- `divisorMaximum`: `lean/MathCollab/Density/LargeValueDefinitions.lean:33`
- `bootstrapScalar`: `lean/MathCollab/Density/LargeValueDefinitions.lean:36`
- `LargeValueData`: `lean/MathCollab/Density/LargeValueDefinitions.lean:40`

### Blueprint line 389

Files: `lean/MathCollab/Density/LargeValues.lean`.

- `large_values_data`: `lean/MathCollab/Density/LargeValues.lean:17`
- `large_values`: `lean/MathCollab/Density/LargeValues.lean:81`

### Blueprint line 409

Files: `lean/MathCollab/Density/ReflectionDefinitions.lean`, `lean/MathCollab/Density/ComparisonCutoff.lean`.

- `ReflectionCutoff`: `lean/MathCollab/Density/ReflectionDefinitions.lean:21`
- `ComparisonCutoff`: `lean/MathCollab/Density/ComparisonCutoff.lean:19`
- `comparisonCutoff`: `lean/MathCollab/Density/ComparisonCutoff.lean:25`
- `cutoffIntegral`: `lean/MathCollab/Density/ReflectionDefinitions.lean:33`
- `hKernel`: `lean/MathCollab/Density/ReflectionDefinitions.lean:37`
- `dyadicPolynomial`: `lean/MathCollab/Density/ReflectionDefinitions.lean:41`
- `completePairEnergy`: `lean/MathCollab/Density/ReflectionDefinitions.lean:44`
- `kernelEnergy`: `lean/MathCollab/Density/LargeValueDefinitions.lean:22`

### Blueprint line 456

Files: `lean/MathCollab/Density/CompletePairs.lean`, `lean/MathCollab/Density/Comparison.lean`.

- `completePairEnergy_gram`: `lean/MathCollab/Density/ComparisonAlgebra.lean:19`
- `completePairEnergy_diagonal_lower`: `lean/MathCollab/Density/ComparisonAlgebra.lean:30`
- `comparison_extension_bound`: `lean/MathCollab/Density/Comparison.lean:18`
- `comparison_continuous_bound`: `lean/MathCollab/Density/Comparison.lean:83`
- `comparison_remainder_bound`: `lean/MathCollab/Density/Comparison.lean:132`
- `uniform_comparison`: `lean/MathCollab/Density/Comparison.lean:173`

### Blueprint line 480

Files: `lean/MathCollab/Density/UniformIBP.lean`, `lean/MathCollab/Density/CutoffTransforms.lean`, `lean/MathCollab/Density/FixedBandError.lean`.

- `ibpIntegral_recurrence`: `lean/MathCollab/Density/UniformIBP.lean:214`
- `uniform_offBand_decay`: `lean/MathCollab/Density/UniformIBP.lean:310`
- `hKernel_poisson`: `lean/MathCollab/Density/CutoffTransforms.lean:176`
- `uniform_fixedBand_and_diagonal_error`: `lean/MathCollab/Density/FixedBandError.lean:86`

### Blueprint line 510

Files: `lean/MathCollab/Density/Oscillatory.lean`, `lean/MathCollab/Density/AllFrequency.lean`.

- `norm_gmReflectionIntegral_le_left`: `lean/MathCollab/Density/Oscillatory.lean:279`
- `norm_gmReflectionIntegral_le_right`: `lean/MathCollab/Density/Oscillatory.lean:309`
- `norm_gmReflectionIntegral_le_six_div_sqrt`: `lean/MathCollab/Density/AllFrequency.lean:23`

### Blueprint line 559

Files: `lean/MathCollab/Density/MellinKernel.lean`, `lean/MathCollab/Density/BandEnergy.lean`, `lean/MathCollab/Density/LocalCover.lean`, `lean/MathCollab/Density/Reflection.lean`.

- `band_modeIntegral_mellin`: `lean/MathCollab/Density/MellinKernel.lean:221`
- `norm_reflectionKernel_sq_le`: `lean/MathCollab/Density/MellinKernel.lean:246`
- `norm_bandContribution_sq_le`: `lean/MathCollab/Density/BandEnergy.lean:66`
- `sum_card_localSet`: `lean/MathCollab/Density/LocalCover.lean:142`
- `uniform_reflection`: `lean/MathCollab/Density/Reflection.lean:97`

### Blueprint line 573

Files: `lean/MathCollab/Density/BootstrapDomain.lean`, `lean/MathCollab/Density/BootstrapSupremum.lean`.

- `bootstrapFamily`: `lean/MathCollab/Density/BootstrapDomain.lean:36`
- `crude_kernel_bound`: `lean/MathCollab/Density/BootstrapSupremum.lean:19`
- `bootstrapValues_bddAbove`: `lean/MathCollab/Density/BootstrapSupremum.lean:67`
- `bootstrapBound`: `lean/MathCollab/Density/BootstrapSupremum.lean:59`
- `kernelEnergy_le_bootstrapBound`: `lean/MathCollab/Density/BootstrapSupremum.lean:102`

### Blueprint line 634

Files: `lean/MathCollab/Density/BootstrapShell.lean`, `lean/MathCollab/Density/BootstrapAbsorption.lean`, `lean/MathCollab/Density/UniformThreshold.lean`.

- `bootstrap_one_shell`: `lean/MathCollab/Density/BootstrapShell.lean:121`
- `bootstrap_preabsorption`: `lean/MathCollab/Density/BootstrapAbsorption.lean:18`
- `bootstrap_absorption_inequality`: `lean/MathCollab/Density/BootstrapAbsorption.lean:84`
- `uniform_scalar_decay`: `lean/MathCollab/Density/UniformThreshold.lean:40`
- `uniform_absorbed_kernel`: `lean/MathCollab/Density/UniformThreshold.lean:102`

### Blueprint line 666

Files: `lean/MathCollab/Density/LargeValuesOptimization.lean`, `lean/MathCollab/Density/LargeValues.lean`.

- `cardinality_at_length`: `lean/MathCollab/Density/LargeValuesOptimization.lean:17`
- `optimal_integer_scale`: `lean/MathCollab/Density/LargeValuesOptimization.lean:53`
- `large_values_with_divisors`: `lean/MathCollab/Density/LargeValuesOptimization.lean:100`
- `large_values_data`: `lean/MathCollab/Density/LargeValues.lean:17`

### Blueprint line 694

Files: `lean/MathCollab/Density/Stronger/Fourth/SquareSource.lean`.

- `completedXiNumerator`: `lean/MathCollab/Density/Stronger/Fourth/SquareSource.lean:94`
- `hughesYoungAuxiliaryZero`: `lean/MathCollab/Density/Stronger/Fourth/SquareSource.lean:140`
- `zetaSquarePoleNormalization`: `lean/MathCollab/Density/Stronger/Fourth/SquareSource.lean:187`
- `zetaSquareContourNumerator`: `lean/MathCollab/Density/Stronger/Fourth/SquareSource.lean:217`
- `zetaSquareContourIntegrand`: `lean/MathCollab/Density/Stronger/Fourth/SquareSource.lean:263`

### Blueprint line 733

Files: `lean/MathCollab/Density/Stronger/Fourth/SquareSource.lean`, `lean/MathCollab/Density/Stronger/Fourth/SquareContour.lean`, `lean/MathCollab/Density/Stronger/Fourth/SquareNormalized.lean`.

- `zetaSquare_finiteRectangle`: `lean/MathCollab/Density/Stronger/Fourth/SquareSource.lean:278`
- `completedZeta_square_eq_vertical_integrals`: `lean/MathCollab/Density/Stronger/Fourth/SquareContour.lean:258`
- `zetaSquareNorm_eq_two_re_fourthRightPiece`: `lean/MathCollab/Density/Stronger/Fourth/SquareNormalized.lean:159`
- `zeta_fourth_le_four_mul_rightPiece_sq`: `lean/MathCollab/Density/Stronger/Fourth/SquareNormalized.lean:174`

### Blueprint line 756

Files: `lean/MathCollab/Density/Stronger/Fourth/SquareSource.lean`, `lean/MathCollab/Density/Stronger/Fourth/SquareNormalized.lean`, `lean/MathCollab/Density/Stronger/Fourth/SquareDivisorSeries.lean`.

- `riemannZeta_sq_eq_divisorLSeries`: `lean/MathCollab/Density/Stronger/Fourth/SquareSource.lean:49`
- `zetaFourthKernel`: `lean/MathCollab/Density/Stronger/Fourth/SquareNormalized.lean:283`
- `zetaFourthRightPiece_eq_divisor_integral`: `lean/MathCollab/Density/Stronger/Fourth/SquareNormalized.lean:328`
- `hasSum_zetaSquareDivisorContribution`: `lean/MathCollab/Density/Stronger/Fourth/SquareDivisorSeries.lean:179`

### Blueprint line 791

Files: `lean/MathCollab/Density/Stronger/Fourth/DigammaSeries.lean`, `lean/MathCollab/Density/Stronger/Fourth/DigammaLog.lean`, `lean/MathCollab/Density/Stronger/Fourth/GammaShiftAmplitude.lean`, `lean/MathCollab/Density/Stronger/Fourth/SquareKernel.lean`.

- `hasSum_digamma_of_re_pos`: `lean/MathCollab/Density/Stronger/Fourth/DigammaSeries.lean:230`
- `norm_digamma_sub_log_le`: `lean/MathCollab/Density/Stronger/Fourth/DigammaLog.lean:187`
- `norm_gammaReal_shift_sq_le_exp`: `lean/MathCollab/Density/Stronger/Fourth/GammaShiftAmplitude.lean:136`
- `exists_norm_zetaFourthKernel_le`: `lean/MathCollab/Density/Stronger/Fourth/SquareKernel.lean:125`

### Blueprint line 825

Files: `lean/MathCollab/Density/Stronger/Fourth/SquareTerm.lean`, `lean/MathCollab/Density/Stronger/Fourth/SquareLineShift.lean`, `lean/MathCollab/Density/Stronger/Fourth/SquareTruncation.lean`, `lean/MathCollab/Density/Stronger/Fourth/SquareTail.lean`.

- `zetaFourthRightPiece_eq_prefix_add_tail`: `lean/MathCollab/Density/Stronger/Fourth/SquareTruncation.lean:107`
- `tsum_nat_rpow_tail_le`: `lean/MathCollab/Density/Stronger/Fourth/SquareTail.lean:26`
- `exists_norm_fourthRightPiece_sub_cutoff_le`: `lean/MathCollab/Density/Stronger/Fourth/SquareTail.lean:129`

### Blueprint line 884

Files: `lean/MathCollab/Density/Stronger/Fourth/MeanValueCore.lean`, `lean/MathCollab/Density/Stronger/Fourth/PrefixMean.lean`.

- `hilbertForm_norm_le`: `lean/MathCollab/Density/Stronger/Fourth/MeanValueCore.lean:368`
- `abs_inv_log_sub_sub_div_le_one`: `lean/MathCollab/Density/Stronger/Fourth/MeanValueCore.lean:439`
- `logHilbertQuad_norm_le`: `lean/MathCollab/Density/Stronger/Fourth/MeanValueCore.lean:676`
- `integral_norm_sq_dirichletTime_le`: `lean/MathCollab/Density/Stronger/Fourth/MeanValueCore.lean:911`
- `integral_norm_sq_dirichletPrefix_reflected_le`: `lean/MathCollab/Density/Stronger/Fourth/PrefixMean.lean:190`

### Blueprint line 941

Files: `lean/MathCollab/Density/Stronger/Fourth/GaussianProducer.lean`, `lean/MathCollab/Density/Stronger/Fourth/SquarePrefix.lean`, `lean/MathCollab/Density/Stronger/Fourth/FourthMoment.lean`.

- `exists_integral_gaussian_fourthPolynomial_le`: `lean/MathCollab/Density/Stronger/Fourth/GaussianProducer.lean:111`
- `exists_norm_sq_fourthPrefix_le_gaussian`: `lean/MathCollab/Density/Stronger/Fourth/SquarePrefix.lean:60`
- `exists_fourth_dyadic_budget`: `lean/MathCollab/Density/Stronger/Fourth/GaussianProducer.lean:160`
- `zeta_fourth_dyadic`: `lean/MathCollab/Density/Stronger/Fourth/FourthMoment.lean:25`

### Blueprint line 1042

Files: `lean/MathCollab/Density/Stronger/PointMean/FiniteRectangle.lean`, `lean/MathCollab/Density/Stronger/PointMean/MellinShift.lean`, `lean/MathCollab/Density/Stronger/PointMean/DoubleConvolution.lean`, `lean/MathCollab/Density/Stronger/PointMean/VerticalEdges.lean`, `lean/MathCollab/Density/Stronger/PointMean/Native.lean`.

- `heathBrownLemmaThree_finiteRectangle`: `lean/MathCollab/Density/Stronger/PointMean/FiniteRectangle.lean:160`
- `heathBrown_twoPole_vertical_shift`: `lean/MathCollab/Density/Stronger/PointMean/MellinShift.lean:255`
- `integral_strongKernel_mul_strongMoment_le`: `lean/MathCollab/Density/Stronger/PointMean/DoubleConvolution.lean:352`
- `exists_eventually_heathBrownLemmaThree_fullMoment`: `lean/MathCollab/Density/Stronger/PointMean/VerticalEdges.lean:433`
- `heathBrownLemmaThree_native`: `lean/MathCollab/Density/Stronger/PointMean/Native.lean:264`

### Blueprint line 1065

Files: `lean/MathCollab/Density/Stronger/PointMean/ExponentialOverlap.lean`, `lean/MathCollab/Density/Stronger/PointMean/IntegralOverlap.lean`, `lean/MathCollab/Density/Stronger/PointMean/Equation44.lean`.

- `sum_exp_neg_abs_sub_le_four`: `lean/MathCollab/Density/Stronger/PointMean/ExponentialOverlap.lean:116`
- `sum_truncated_exp_kernel_zeta_sq_le_localSecondMoment`: `lean/MathCollab/Density/Stronger/PointMean/IntegralOverlap.lean:116`
- `heathBrown_equation44_native`: `lean/MathCollab/Density/Stronger/PointMean/Equation44.lean:104`

### Blueprint line 1102

Files: `lean/MathCollab/Density/Stronger/Atkinson/DivisorWeightKernel.lean`, `lean/MathCollab/Density/Stronger/Atkinson/DivisorWeightReflection.lean`, `lean/MathCollab/Density/Stronger/Atkinson/DivisorWeightVariation.lean`.

- `zetaDivisorWeight`: `lean/MathCollab/Density/Stronger/Atkinson/DivisorWeightKernel.lean:30`
- `zetaDivisorWeight_add_neg`: `lean/MathCollab/Density/Stronger/Atkinson/DivisorWeightReflection.lean:219`
- `exists_norm_zetaDivisorWeight_min_le`: `lean/MathCollab/Density/Stronger/Atkinson/DivisorWeightReflection.lean:236`
- `exists_norm_zetaDivisorWeight_real_sub_min_le`: `lean/MathCollab/Density/Stronger/Atkinson/DivisorWeightVariation.lean:108`

### Blueprint line 1125

Files: `lean/MathCollab/Density/Stronger/Atkinson/KernelApproximation.lean`, `lean/MathCollab/Density/Stronger/Atkinson/DivisorWeightSource.lean`, `lean/MathCollab/Density/Stronger/Atkinson/DivisorWeightFreezing.lean`, `lean/MathCollab/Density/Stronger/Atkinson/RealFrozenSource.lean`.

- `exists_integral_norm_zetaSquareRightKernel_error_le`: `lean/MathCollab/Density/Stronger/Atkinson/KernelApproximation.lean:181`
- `zetaSquareLeadingDivisorContribution_eq_weight`: `lean/MathCollab/Density/Stronger/Atkinson/DivisorWeightSource.lean:67`
- `exists_abs_zetaSquareNorm_sub_frozen_le`: `lean/MathCollab/Density/Stronger/Atkinson/RealFrozenSource.lean:25`

### Blueprint line 1155

Files: `lean/MathCollab/Density/Stronger/Atkinson/QuadraticGaussian.lean`, `lean/MathCollab/Density/Stronger/Atkinson/GammaQuadratic.lean`, `lean/MathCollab/Density/Stronger/Atkinson/GammaGaussianTransform.lean`, `lean/MathCollab/Density/Stronger/Atkinson/FrozenDivisorGaussian.lean`.

- `zetaGaussianQuadraticIntegral_eq`: `lean/MathCollab/Density/Stronger/Atkinson/QuadraticGaussian.lean:48`
- `norm_zetaGaussianQuadraticIntegral_le`: `lean/MathCollab/Density/Stronger/Atkinson/QuadraticGaussian.lean:102`
- `norm_zetaSquareGammaGaussianTransform_sub_quadratic_le`: `lean/MathCollab/Density/Stronger/Atkinson/GammaGaussianTransform.lean:115`
- `hasSum_zetaFrozenDivisorGaussianMean`: `lean/MathCollab/Density/Stronger/Atkinson/FrozenDivisorGaussian.lean:83`

### Blueprint line 1181

Files: `lean/MathCollab/Density/Stronger/Atkinson/DivisorBandCutoff.lean`, `lean/MathCollab/Density/Stronger/Atkinson/SmoothDivisorTest.lean`, `lean/MathCollab/Density/Stronger/Atkinson/DivisorLatticePhase.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonAmplitude.lean`.

- `zetaDivisorBandCutoff`: `lean/MathCollab/Density/Stronger/Atkinson/DivisorBandCutoff.lean:70`
- `zetaSmoothDivisorVoronoiTest`: `lean/MathCollab/Density/Stronger/Atkinson/SmoothDivisorTest.lean:64`
- `zetaAtkinsonDivisorTest`: `lean/MathCollab/Density/Stronger/Atkinson/DivisorLatticePhase.lean:27`
- `zetaAtkinsonDivisorTest_eq_amplitude_phase`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonAmplitude.lean:57`

### Blueprint line 1202

Files: `lean/MathCollab/Density/Stronger/Atkinson/GaussianAveraging.lean`, `lean/MathCollab/Density/Stronger/Atkinson/SmoothDivisorSource.lean`.

- `exists_zetaSquareGaussianMean_smooth_approximation`: `lean/MathCollab/Density/Stronger/Atkinson/SmoothDivisorSource.lean:25`
- `exists_zetaSquareLocalMean_le_smooth_divisor`: `lean/MathCollab/Density/Stronger/Atkinson/SmoothDivisorSource.lean:59`

### Blueprint line 1273

Files: `lean/MathCollab/Density/Stronger/Atkinson/OrdinaryDivisorVoronoi.lean`, `lean/MathCollab/Density/Stronger/Atkinson/BesselK0Mellin.lean`, `lean/MathCollab/Density/Stronger/Atkinson/BesselY0Mellin.lean`, `lean/MathCollab/Density/Stronger/Atkinson/BesselTransformBridge.lean`, `lean/MathCollab/Density/Stronger/Atkinson/VoronoiMinusTransport.lean`, `lean/MathCollab/Density/Stronger/Atkinson/ZetaAtkinsonVoronoi.lean`.

- `ordinaryDivisorVoronoi_native`: `lean/MathCollab/Density/Stronger/Atkinson/OrdinaryDivisorVoronoi.lean:88`
- `dfiVoronoiPlusTransform_mellin_eq_bessel`: `lean/MathCollab/Density/Stronger/Atkinson/BesselTransformBridge.lean:198`
- `verticalIntegral_dfiVoronoiMinus_mellin_thirteenSixteenths_eq_bessel`: `lean/MathCollab/Density/Stronger/Atkinson/BesselTransformBridge.lean:331`
- `ordinaryDivisorVoronoi_bessel`: `lean/MathCollab/Density/Stronger/Atkinson/ZetaAtkinsonVoronoi.lean:25`

### Blueprint line 1286

Files: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonK0Scales.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonMainIntegral.lean`, `lean/MathCollab/Density/Stronger/Atkinson/ZetaAtkinsonMinusSource.lean`.

- `exists_zetaAtkinsonBesselPlus_powerSaving`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonK0Scales.lean:49`
- `exists_zetaSquareLocalMean_le_atkinson_minus`: `lean/MathCollab/Density/Stronger/Atkinson/ZetaAtkinsonMinusSource.lean:50`

### Blueprint line 1307

Files: `lean/MathCollab/Density/Stronger/Atkinson/NeumannTwoTermExpansion.lean`, `lean/MathCollab/Density/Stronger/Atkinson/ZetaNeumannSeries.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonCorrectionSeries.lean`, `lean/MathCollab/Density/Stronger/Atkinson/ZetaAtkinsonTwoTermSource.lean`.

- `abs_dfiBesselY0_sub_neumannTwoTerm_le`: `lean/MathCollab/Density/Stronger/Atkinson/NeumannTwoTermExpansion.lean:51`
- `exists_zetaAtkinsonBesselMinus_twoTerm_log_bound`: `lean/MathCollab/Density/Stronger/Atkinson/ZetaAtkinsonTwoTermSource.lean:33`
- `exists_zetaSquareLocalMean_le_atkinson_twoTerm`: `lean/MathCollab/Density/Stronger/Atkinson/ZetaAtkinsonTwoTermSource.lean:75`

### Blueprint line 1331

Files: `lean/MathCollab/Density/Stronger/Atkinson/ZetaAtkinsonSaddle.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSaddleNormalization.lean`.

- `zetaAtkinsonPhase_stationary_iff`: `lean/MathCollab/Density/Stronger/Atkinson/ZetaAtkinsonSaddle.lean:87`
- `zetaAtkinsonPhase_secondDeriv_saddle_neg`: `lean/MathCollab/Density/Stronger/Atkinson/ZetaAtkinsonSaddle.lean:122`
- `atkinsonSaddleRoot_mul_neg`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSaddleNormalization.lean:38`
- `zetaAtkinsonSaddle_log_argument`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSaddleNormalization.lean:77`

### Blueprint line 1354

Files: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonPowerWeight.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonRootIntegral.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonQuadraticKernel.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonStationaryMain.lean`, `lean/MathCollab/Density/Stronger/Atkinson/FresnelEvaluation.lean`.

- `atkinsonPowerWeight`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonPowerWeight.lean:25`
- `atkinsonPowerIntegral`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonPowerIntegral.lean:38`
- `atkinsonStationaryMain`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonStationaryMain.lean:31`
- `fresnelGaussianValue_eq_phase`: `lean/MathCollab/Density/Stronger/Atkinson/FresnelEvaluation.lean:52`

### Blueprint line 1415

Files: `lean/MathCollab/Density/Stronger/Atkinson/StationaryOddRemainder.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSymmetricStationary.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSymmetricBalance.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonFourthRootRadius.lean`.

- `integral_atkinsonRootQuadratic_odd`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSymmetricStationary.lean:40`
- `IntervalC2Bound.atkinsonLocalSymmetric`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSymmetricStationary.lean:74`
- `exists_atkinsonPowerIntegral_symmetric_balance`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSymmetricBalance.lean:105`
- `exists_atkinsonPowerIntegral_fourthRoot_pair`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonFourthRootRadius.lean:102`

### Blueprint line 1447

Files: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonStationarySeries.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonFiniteStationaryError.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonTwoTermStationary.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonNativeLocalMean.lean`.

- `atkinsonStationaryLeadingSum_eq_finite`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonStationarySeries.lean:59`
- `exists_norm_atkinsonLeadingFiniteSum_sub_stationary_le`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonFiniteStationaryError.lean:99`
- `exists_tsum_zetaAtkinsonTwoTerm_sub_stationary_above_fourthRoot`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonTwoTermStationary.lean:49`
- `localMeanStationaryInput_native`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonNativeLocalMean.lean:64`

### Blueprint line 1487

Files: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonEvaluatedPhases.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonCoefficientVariation.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSaddleProfileNormalization.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSignedPhaseSeries.lean`.

- `atkinsonStationaryMain_neg_sqrt`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonEvaluatedPhases.lean:60`
- `atkinsonFourthRootCoefficient_eq`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonCoefficientVariation.lean:49`
- `atkinsonStationaryLeadingSum_eq_signed`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSignedPhaseSeries.lean:67`

### Blueprint line 1530

Files: `lean/MathCollab/Density/Stronger/Atkinson/FiniteWeightVariation.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonMainVariation.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonStationaryBlockBound.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonDampedDyadic.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonStationaryDyadic.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonStationarySourceAssembly.lean`.

- `exists_finiteVariationBound_atkinsonMainWeights`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonMainVariation.lean:32`
- `exists_norm_atkinsonStationarySum_le_undamped`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonStationaryDyadic.lean:96`
- `localMeanSourceToPrefix_of_stationary`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonStationarySourceAssembly.lean:36`

### Blueprint line 1564

Files: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonPrefixVectors.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonPrefixMax.lean`, `lean/MathCollab/Density/Stronger/Atkinson/FiniteWeightedGram.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonDyadicGramBudget.lean`.

- `atkinsonMaskedPhaseVector_gram`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonPrefixVectors.lean:93`
- `sum_atkinsonPhaseBlockMax_sq_le_gramMax`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonWeightedGram.lean:80`
- `sum_atkinsonUndampedDyadicPhaseBound_sq_le_budget`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonDyadicGramBudget.lean:54`

### Blueprint line 1631

Files: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonIndexCurvature.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonIndexScales.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonIndexBProcess.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonPrefixCancellation.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonNearGap.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonFarGap.lean`.

- `hasDerivAt_deriv_atkinsonIndexRealPhase`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonIndexCurvature.lean:75`
- `atkinsonIndexPositiveDifference_B_process`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonIndexBProcess.lean:212`
- `atkinsonPrefixGramMax_le_firstDerivative`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonPrefixCancellation.lean:135`
- `atkinsonPrefixGapMajorant_le_near`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonNearGap.lean:104`
- `atkinsonPrefixGapMajorant_le_far`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonFarGap.lean:48`

### Blueprint line 1672

Files: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonNearGapBudget.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonPowerGapBudget.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonPhysicalCutoff.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonLocalizedGram.lean`.

- `exists_atkinsonPhysicalCutoff_prefix_geometry`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonPhysicalCutoff.lean:100`
- `exists_sum_atkinsonUndampedDyadicPhaseBound_sq_le_power`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonLocalizedGram.lean:64`

### Blueprint line 1722

Files: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonPhysicalBudget.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSourceAssembly.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonStationarySourceAssembly.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonNativeLocalMean.lean`.

- `exists_atkinsonPhysicalGapBudget_le_twoTerm`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonPhysicalBudget.lean:271`
- `localMeanPacketInput_of_sourceToPrefix`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSourceAssembly.lean:53`
- `localMeanPacketInput_of_stationary`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonStationarySourceAssembly.lean:68`
- `localMeanStationaryInput_native`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonNativeLocalMean.lean:64`

### Blueprint line 1750

Files: `lean/MathCollab/Density/Stronger/AtkinsonCardinalityAbsorption.lean`, `lean/MathCollab/Density/Stronger/AtkinsonHeightCover.lean`, `lean/MathCollab/Density/Stronger/AtkinsonGlobalCardinality.lean`.

- `atkinsonAbsorptionLength`: `lean/MathCollab/Density/Stronger/AtkinsonCardinalityAbsorption.lean:33`
- `atkinson_card_le_of_packet`: `lean/MathCollab/Density/Stronger/AtkinsonCardinalityAbsorption.lean:58`
- `atkinson_card_le_of_local_packets`: `lean/MathCollab/Density/Stronger/AtkinsonGlobalCardinality.lean:32`

### Blueprint line 1798

Files: `lean/MathCollab/Density/Stronger/Peaks/Clusters.lean`, `lean/MathCollab/Density/Stronger/Peaks/ClusterCount.lean`, `lean/MathCollab/Density/Stronger/FiniteOccupancy.lean`.

- `pointClusterCenter`: `lean/MathCollab/Density/Stronger/Peaks/Clusters.lean:36`
- `pointClusterCenters_separated`: `lean/MathCollab/Density/Stronger/Peaks/Clusters.lean:105`
- `exists_pointCluster_superlevel_entry`: `lean/MathCollab/Density/Stronger/Peaks/ClusterCount.lean:119`
- `exists_pointCluster_superlevel_count`: `lean/MathCollab/Density/Stronger/Peaks/ClusterCount.lean:153`
- `sum_nat_occupancy_le_of_superlevels`: `lean/MathCollab/Density/Stronger/FiniteOccupancy.lean:61`
- `exists_pointValue_card_le_with_width`: `lean/MathCollab/Density/Stronger/Peaks/ClusterCount.lean:241`

### Blueprint line 1819

Files: `lean/MathCollab/Density/Stronger/Peaks/WidthRanges.lean`.

- `pointValueWidth_error_absorption`: `lean/MathCollab/Density/Stronger/Peaks/WidthRanges.lean:53`
- `pointValueWidth_count_identity`: `lean/MathCollab/Density/Stronger/Peaks/WidthRanges.lean:64`
- `exists_pointValue_card_le_source_range`: `lean/MathCollab/Density/Stronger/Peaks/WidthRanges.lean:71`

### Blueprint line 1850

Files: `lean/MathCollab/Density/Stronger/Peaks/WidthRanges.lean`, `lean/MathCollab/Density/Stronger/NativePeaks.lean`.

- `exists_pointValue_twelfth_weighted_card_le_of_inputs`: `lean/MathCollab/Density/Stronger/Peaks/WidthRanges.lean:238`
- `pointValue_peak_card_of_inputs`: `lean/MathCollab/Density/Stronger/Peaks/WidthRanges.lean:298`
- `pointValue_peak_card_native`: `lean/MathCollab/Density/Stronger/NativePeaks.lean:25`

### Blueprint line 1870

Files: `lean/MathCollab/Density/Stronger/SeparatedVolume.lean`, `lean/MathCollab/Density/Stronger/NativePeaks.lean`.

- `exists_unitSeparated_closedBall_cover_of_card_bound`: `lean/MathCollab/Density/Stronger/SeparatedVolume.lean:24`
- `volume_le_two_mul_of_separated_card_bound`: `lean/MathCollab/Density/Stronger/SeparatedVolume.lean:74`
- `pointValue_volume_native`: `lean/MathCollab/Density/Stronger/NativePeaks.lean:34`

### Blueprint line 1895

Files: `lean/MathCollab/Density/Stronger/TruncatedLayerCake.lean`, `lean/MathCollab/Density/Stronger/CriticalMoment.lean`.

- `integral_le_log_of_truncated_tail`: `lean/MathCollab/Density/Stronger/TruncatedLayerCake.lean:57`
- `pointValue_power_tail_measure_le`: `lean/MathCollab/Density/Stronger/CriticalMoment.lean:67`
- `zeta_twelfth_high_integral_le_log`: `lean/MathCollab/Density/Stronger/CriticalMoment.lean:101`

### Blueprint line 1944

Files: `lean/MathCollab/Density/Stronger/ConditionalMoment.lean`, `lean/MathCollab/Density/Stronger/DyadicMoment.lean`, `lean/MathCollab/Density/Stronger/NativeMoment.lean`, `lean/Solution.lean`.

- `zeta_twelfth_high_eventually_of_tail`: `lean/MathCollab/Density/Stronger/ConditionalMoment.lean:47`
- `zeta_twelfth_dyadic_of_fourth_and_tail`: `lean/MathCollab/Density/Stronger/ConditionalMoment.lean:97`
- `integral_zero_le_of_dyadic`: `lean/MathCollab/Density/Stronger/DyadicMoment.lean:63`
- `zeta_twelfth_physical_native`: `lean/MathCollab/Density/Stronger/NativeMoment.lean:29`
- `actual_moment_integrable`: `lean/Solution.lean:55`

### Blueprint line 1966

Files: `lean/MathCollab/Density/Stronger/Parameters.lean`.

- `lowerExponent`: `lean/MathCollab/Density/Stronger/Parameters.lean:17`
- `smoothingExponent`: `lean/MathCollab/Density/Stronger/Parameters.lean:20`
- `densityExponent`: `lean/MathCollab/Density/Stronger/Parameters.lean:23`
- `exists_detector_exponent`: `lean/MathCollab/Density/Stronger/Parameters.lean:60`
- `short_exponent_identities`: `lean/MathCollab/Density/Stronger/Parameters.lean:70`
- `long_exponent_identity`: `lean/MathCollab/Density/Stronger/Parameters.lean:77`

### Blueprint line 1986

Files: `lean/MathCollab/Density/MollifierCoefficients.lean`, `lean/MathCollab/Density/MollifierBound.lean`, `lean/MathCollab/Density/Stronger/InitialDetector.lean`.

- `zetaMollifier`: `lean/MathCollab/Density/MollifierCoefficients.lean:20`
- `mollifierCoefficient_vanishes`: `lean/MathCollab/Density/MollifierCoefficients.lean:39`
- `mollifierCoefficient_norm_le`: `lean/MathCollab/Density/MollifierCoefficients.lean:58`
- `norm_zetaMollifier_le_two_sqrt`: `lean/MathCollab/Density/MollifierBound.lean:34`
- `detectorTail`: `lean/MathCollab/Density/Stronger/InitialDetector.lean:91`

### Blueprint line 2018

Files: `lean/MathCollab/Density/DetectorMellin.lean`, `lean/MathCollab/Density/DetectorContour.lean`, `lean/MathCollab/Density/DetectorEstimates.lean`, `lean/MathCollab/Density/DetectorIdentity.lean`.

- `smoothedDetector_eq_rightContour`: `lean/MathCollab/Density/DetectorMellin.lean:454`
- `detector_finite_rectangle_kernel`: `lean/MathCollab/Density/DetectorContour.lean:235`
- `summable_zeta_detector_series`: `lean/MathCollab/Density/DetectorIdentity.lean:70`
- `zeta_detector_identity`: `lean/MathCollab/Density/DetectorIdentity.lean:79`

### Blueprint line 2049

Files: `lean/MathCollab/Density/Stronger/InitialDetector.lean`, `lean/MathCollab/Density/Stronger/Parameters.lean`.

- `detector_eventually_small`: `lean/MathCollab/Density/Stronger/InitialDetector.lean:46`
- `detector_error_scale`: `lean/MathCollab/Density/Stronger/Parameters.lean:92`
- `detectorTail_decomposition`: `lean/MathCollab/Density/Stronger/InitialDetector.lean:94`
- `detectorTail_eventually_large`: `lean/MathCollab/Density/Stronger/InitialDetector.lean:112`

### Blueprint line 2073

Files: `lean/MathCollab/Density/Stronger/SmoothPartition.lean`, `lean/MathCollab/Density/Stronger/SmoothExpansion.lean`, `lean/MathCollab/Density/Stronger/SmoothDetector.lean`.

- `dyadicStep`: `lean/MathCollab/Density/Stronger/SmoothPartition.lean:22`
- `smoothDyadicWeight`: `lean/MathCollab/Density/Stronger/SmoothPartition.lean:50`
- `tsum_smoothDyadicWeight`: `lean/MathCollab/Density/Stronger/SmoothPartition.lean:163`
- `tsum_smoothDyadicBlock`: `lean/MathCollab/Density/Stronger/SmoothExpansion.lean:71`
- `smoothDetectorBlock_zero_of_small`: `lean/MathCollab/Density/Stronger/SmoothDetector.lean:51`

### Blueprint line 2099

Files: `lean/MathCollab/Density/Stronger/SmoothDetector.lean`.

- `tsum_norm_detector_tail_le`: `lean/MathCollab/Density/Stronger/SmoothDetector.lean:67`
- `smoothDetectorBlock_scale_tail_le_two_rpow`: `lean/MathCollab/Density/Stronger/SmoothDetector.lean:122`
- `smoothScaleIndices`: `lean/MathCollab/Density/Stronger/SmoothDetector.lean:165`
- `exists_smoothDetectorBlock`: `lean/MathCollab/Density/Stronger/SmoothDetector.lean:248`
- `smoothDetector_eventually_large`: `lean/MathCollab/Density/Stronger/SmoothDetector.lean:302`

### Blueprint line 2116

Files: `lean/MathCollab/Density/Stronger/SmoothShortBlock.lean`, `lean/MathCollab/Density/Stronger/ShortFixedFamily.lean`.

- `smoothShortCoefficient`: `lean/MathCollab/Density/Stronger/SmoothShortBlock.lean:17`
- `smoothHalfScale`: `lean/MathCollab/Density/Stronger/ShortFixedFamily.lean:20`
- `smoothDetectorBlock_eq_halves`: `lean/MathCollab/Density/Stronger/ShortFixedFamily.lean:58`
- `exists_smoothShort_half`: `lean/MathCollab/Density/Stronger/SmoothShortBlock.lean:127`

### Blueprint line 2138

Files: `lean/MathCollab/Density/DetectorTaylorFamily.lean`, `lean/MathCollab/Density/DetectorBinomial.lean`, `lean/MathCollab/Density/Stronger/GenericTaylorFamily.lean`.

- `detectorTaylorRatio`: `lean/MathCollab/Density/DetectorTaylorFamily.lean:24`
- `detectorTaylorWeight`: `lean/MathCollab/Density/DetectorTaylorFamily.lean:27`
- `hasSum_detector_binomial`: `lean/MathCollab/Density/DetectorBinomial.lean:46`
- `hasSum_genericTaylorPolynomial`: `lean/MathCollab/Density/Stronger/GenericTaylorFamily.lean:111`
- `genericBlock_eq_normalized`: `lean/MathCollab/Density/Stronger/GenericTaylorFamily.lean:87`

### Blueprint line 2156

Files: `lean/MathCollab/Density/DetectorFamilyScales.lean`, `lean/MathCollab/Density/Stronger/GenericTaylorFamily.lean`, `lean/MathCollab/Density/Stronger/ShortTaylorCover.lean`.

- `detectorTaylorCutoff`: `lean/MathCollab/Density/DetectorFamilyScales.lean:16`
- `norm_fixedGenericTaylor_tail_le`: `lean/MathCollab/Density/Stronger/GenericTaylorFamily.lean:156`
- `exists_genericTaylor_component`: `lean/MathCollab/Density/Stronger/GenericTaylorFamily.lean:177`
- `smoothTaylorIndices_card_le_log`: `lean/MathCollab/Density/Stronger/ShortTaylorCover.lean:26`
- `smooth_short_Taylor_cover`: `lean/MathCollab/Density/Stronger/ShortTaylorCover.lean:56`

### Blueprint line 2176

Files: `lean/MathCollab/Density/Stronger/PowerScales.lean`.

- `bounded_power_exponent`: `lean/MathCollab/Density/Stronger/PowerScales.lean:19`
- `bounded_power_scale`: `lean/MathCollab/Density/Stronger/PowerScales.lean:43`
- `short_scale_bounded_power`: `lean/MathCollab/Density/Stronger/PowerScales.lean:74`
- `smoothPowerBound`: `lean/MathCollab/Density/Stronger/ShortPoweredFamily.lean:16`

### Blueprint line 2215

Files: `lean/MathCollab/Density/Stronger/FiniteConvolution.lean`, `lean/MathCollab/Density/Stronger/ShortFixedFamily.lean`, `lean/MathCollab/Density/Stronger/ShortPoweredHeight.lean`.

- `exists_finiteBlock_powered_piece`: `lean/MathCollab/Density/Stronger/FiniteConvolution.lean:108`
- `smoothPoweredCoefficient`: `lean/MathCollab/Density/Stronger/ShortFixedFamily.lean:146`
- `normalizedSmoothPoweredCoefficient_eventually`: `lean/MathCollab/Density/Stronger/ShortPoweredHeight.lean:90`
- `exists_normalizedSmoothPowered_height`: `lean/MathCollab/Density/Stronger/ShortPoweredHeight.lean:111`

### Blueprint line 2226

Files: `lean/MathCollab/Density/Stronger/ShortPoweredFamily.lean`.

- `smoothPoweredIndices`: `lean/MathCollab/Density/Stronger/ShortPoweredFamily.lean:23`
- `smoothPoweredFamilyCoefficient`: `lean/MathCollab/Density/Stronger/ShortPoweredFamily.lean:30`
- `smoothPoweredIndices_card_eventually`: `lean/MathCollab/Density/Stronger/ShortPoweredFamily.lean:70`
- `smooth_long_or_short_powered_cover`: `lean/MathCollab/Density/Stronger/ShortPoweredFamily.lean:120`

### Blueprint line 2259

Files: `lean/MathCollab/Density/ZetaJensenInputs.lean`, `lean/MathCollab/Density/LocalZeroCount.lean`.

- `euler_product_lower_bound_2`: `lean/MathCollab/Density/ZetaJensenInputs.lean:176`
- `finset_analyticOrderNatAt_le_finsum_divisor`: `lean/MathCollab/Density/ZetaJensenInputs.lean:26`
- `zeta_unit_bin_sum_le_jensen`: `lean/MathCollab/Density/LocalZeroCount.lean:24`
- `zeta_local_multiplicity_bound`: `lean/MathCollab/Density/LocalZeroCount.lean:164`

### Blueprint line 2271

Files: `lean/MathCollab/Density/ZeroSeparation.lean`.

- `ordinateBin`: `lean/MathCollab/Density/ZeroSeparation.lean:19`
- `occupied_bins_parity`: `lean/MathCollab/Density/ZeroSeparation.lean:26`
- `weighted_separated_extraction`: `lean/MathCollab/Density/ZeroSeparation.lean:61`

### Blueprint line 2299

Files: `lean/MathCollab/Density/Stronger/ShortZeroCount.lean`, `lean/MathCollab/Density/Stronger/ShortExponentAccounting.lean`.

- `smoothShortZeroFinset`: `lean/MathCollab/Density/Stronger/ShortZeroCount.lean:86`
- `zetaSubset_large_values_cover_indexed`: `lean/MathCollab/Density/Stronger/ShortZeroCount.lean:22`
- `smoothPoweredFamily_largeValues_admissible`: `lean/MathCollab/Density/Stronger/ShortExponentAccounting.lean:28`

### Blueprint line 2320

Files: `lean/MathCollab/Density/Stronger/ShortExponentAccounting.lean`, `lean/MathCollab/Density/Stronger/ShortZeroCount.lean`.

- `smooth_largeValue_term_le`: `lean/MathCollab/Density/Stronger/ShortExponentAccounting.lean:59`
- `smooth_family_sum_eventually`: `lean/MathCollab/Density/Stronger/ShortExponentAccounting.lean:117`
- `smoothShortZeroCount_bound`: `lean/MathCollab/Density/Stronger/ShortZeroCount.lean:105`

### Blueprint line 2344

Files: `lean/MathCollab/Density/Stronger/DampedCutoff.lean`, `lean/MathCollab/Density/Stronger/UniformMellin.lean`, `lean/MathCollab/Density/Stronger/MellinEntire.lean`.

- `dampedCutoff_uniform_derivatives`: `lean/MathCollab/Density/Stronger/DampedCutoff.lean:68`
- `dampedCutoff_uniform_mellin_decay`: `lean/MathCollab/Density/Stronger/UniformMellin.lean:233`
- `dampedCutoff_uniform_mellin_weighted_L1`: `lean/MathCollab/Density/Stronger/UniformMellin.lean:320`
- `dampedCutoff_mellin_entire`: `lean/MathCollab/Density/Stronger/MellinEntire.lean:53`

### Blueprint line 2365

Files: `lean/MathCollab/Density/Stronger/SmoothMellinIdentity.lean`, `lean/MathCollab/Density/Stronger/SmoothContourIdentity.lean`, `lean/MathCollab/Density/Stronger/SmallResidue.lean`, `lean/MathCollab/Density/Stronger/SmoothDetector.lean`.

- `smoothMollifierBlock_eq_rightContour`: `lean/MathCollab/Density/Stronger/SmoothMellinIdentity.lean:159`
- `smoothMollifierBlock_contour_identity`: `lean/MathCollab/Density/Stronger/SmoothBlockContour.lean:19`
- `smoothDetectorResidue_eventually_small`: `lean/MathCollab/Density/Stronger/SmallResidue.lean:17`
- `smoothDetectorBlock_eq_smoothMollifierBlock`: `lean/MathCollab/Density/Stronger/SmoothDetector.lean:358`

### Blueprint line 2386

Files: `lean/MathCollab/Density/Stronger/WeightedCriticalMean.lean`, `lean/MathCollab/Density/Stronger/LongBlockDetection.lean`, `lean/MathCollab/Density/Stronger/LongMeanCounting.lean`.

- `weightedCriticalMean`: `lean/MathCollab/Density/Stronger/WeightedCriticalMean.lean:15`
- `uniform_smoothMollifierBlock_mean_bound`: `lean/MathCollab/Density/Stronger/WeightedCriticalMean.lean:80`
- `smoothMollifierBlock_eventually_detects_mean`: `lean/MathCollab/Density/Stronger/LongBlockDetection.lean:31`
- `smooth_long_mean_or_short_powered_cover`: `lean/MathCollab/Density/Stronger/LongMeanCounting.lean:44`

### Blueprint line 2425

Files: `lean/MathCollab/Density/Stronger/MomentPower.lean`, `lean/MathCollab/Density/Stronger/SeparatedMoment.lean`, `lean/MathCollab/Density/Stronger/PhysicalTwelfthTail.lean`, `lean/MathCollab/Density/Stronger/SeparatedCriticalSampling.lean`.

- `integral_weighted_twelfth`: `lean/MathCollab/Density/Stronger/MomentPower.lean:45`
- `momentDecay_mass_bounds`: `lean/MathCollab/Density/Stronger/SeparatedMoment.lean:56`
- `weightedCriticalTwelfth_tail_pointwise`: `lean/MathCollab/Density/Stronger/PhysicalTwelfthTail.lean:35`
- `separated_weightedCriticalMean_twelfth_le`: `lean/MathCollab/Density/Stronger/SeparatedCriticalSampling.lean:66`

### Blueprint line 2444

Files: `lean/MathCollab/Density/Stronger/LongMeanCounting.lean`, `lean/MathCollab/Density/Stronger/LongMultiplicityReduction.lean`.

- `long_mean_twelfth_count`: `lean/MathCollab/Density/Stronger/LongMeanCounting.lean:19`
- `long_mean_count_le_physical_moment`: `lean/MathCollab/Density/Stronger/LongMeanCounting.lean:105`
- `smoothLongZeroCount_physical_moment_reduction`: `lean/MathCollab/Density/Stronger/LongMultiplicityReduction.lean:56`

### Blueprint line 2465

Files: `lean/MathCollab/Density/Stronger/LongScalarBudget.lean`, `lean/MathCollab/Density/Stronger/ConditionalDensity.lean`.

- `long_count_scale_identity`: `lean/MathCollab/Density/Stronger/LongScalarBudget.lean:29`
- `long_count_scalar_log_eventually`: `lean/MathCollab/Density/Stronger/LongScalarBudget.lean:40`
- `smoothLongZeroCount_bound_of_twelfth_moment`: `lean/MathCollab/Density/Stronger/ConditionalDensity.lean:20`

### Blueprint line 2522

Files: `lean/MathCollab/Density/Stronger/FinalParameters.lean`, `lean/MathCollab/Density/Stronger/ConditionalDensity.lean`, `lean/MathCollab/Density/Stronger/NativeDensity.lean`, `lean/MathCollab/Density/DensityDyadicSummation.lean`, `lean/Solution.lean`.

- `exists_stronger_loss_parameters`: `lean/MathCollab/Density/Stronger/FinalParameters.lean:15`
- `stronger_slab_bound_of_twelfth_moment`: `lean/MathCollab/Density/Stronger/ConditionalDensity.lean:56`
- `zetaDensity_bound_of_eventual_slabs`: `lean/MathCollab/Density/DensityDyadicSummation.lean:94`
- `stronger_density_bound_native`: `lean/MathCollab/Density/Stronger/NativeDensity.lean:24`
- `DensityStronger.density_bound`: `lean/Solution.lean:36`

### Blueprint line 2742

Files: `lean/WeylPort/AFE/Objects.lean`, `lean/WeylPort/AFE/DampedWeightedKernel.lean`, `lean/WeylPort/AFE/ChiGammaFactor.lean`, `lean/WeylPort/AFE/UniformError.lean`, `lean/WeylPort/CutoffSelection.lean`.

- `afeRemainder`: `lean/WeylPort/AFE/Objects.lean:45`
- `weightedIntegralTail_zero_eq_gamma`: `lean/WeylPort/AFE/DampedWeightedKernel.lean:244`
- `gamma_factor_eq_chi_mul_one_add`: `lean/WeylPort/AFE/ChiGammaFactor.lean:114`
- `norm_critical_afe_uniform`: `lean/WeylPort/AFE/UniformError.lean:186`
- `exists_afe_cutoffs_all_heights`: `lean/WeylPort/CutoffSelection.lean:87`

### Blueprint line 2798

Files: `lean/MathCollab/Density/Stronger/Atkinson/NeumannContourShift.lean`, `lean/MathCollab/Density/Stronger/Atkinson/NeumannSchlafliEntry.lean`, `lean/MathCollab/Density/Stronger/Atkinson/NeumannLaplaceRepresentation.lean`, `lean/MathCollab/Density/Stronger/Atkinson/NeumannRayFactorization.lean`, `lean/MathCollab/Density/Stronger/Atkinson/NeumannLaplaceAmplitude.lean`, `lean/MathCollab/Density/Stronger/Atkinson/NeumannLaplaceRemainder.lean`.

- `neumann_schlafli_complex_identity`: `lean/MathCollab/Density/Stronger/Atkinson/NeumannLaplaceRepresentation.lean:42`
- `dfiBesselY0_eq_neumannLaplaceIntegral`: `lean/MathCollab/Density/Stronger/Atkinson/NeumannRayFactorization.lean:121`
- `norm_neumannLaplaceAmplitude_sub_linear_le`: `lean/MathCollab/Density/Stronger/Atkinson/NeumannLaplaceAmplitude.lean:60`
- `norm_neumannLaplaceIntegral_sub_approximation_le`: `lean/MathCollab/Density/Stronger/Atkinson/NeumannLaplaceRemainder.lean:87`

### Blueprint line 2848

Files: `lean/MathCollab/Density/Stronger/Atkinson/FresnelAbelLimit.lean`, `lean/MathCollab/Density/Stronger/Atkinson/FresnelEvaluation.lean`, `lean/MathCollab/Density/Stronger/Atkinson/StationaryOddRemainder.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSymmetricStationary.lean`.

- `norm_atkinsonQuadraticWindow_sub_gaussianValue_le`: `lean/MathCollab/Density/Stronger/Atkinson/FresnelAbelLimit.lean:84`
- `fresnelGaussianValue_eq_phase`: `lean/MathCollab/Density/Stronger/Atkinson/FresnelEvaluation.lean:52`
- `integral_atkinsonRootQuadratic_odd`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSymmetricStationary.lean:40`
- `IntervalC2Bound.atkinsonLocalSymmetric`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSymmetricStationary.lean:74`

### Blueprint line 2894

Files: `lean/GuthMaynard/VanDerCorput.lean`, `lean/GuthMaynard/SecondDerivative.lean`.

- `kusminLandau_one_period`: `lean/GuthMaynard/VanDerCorput.lean:350`
- `kusminLandau_one_period_decreasing`: `lean/GuthMaynard/VanDerCorput.lean:412`
- `filter_card_bound`: `lean/GuthMaynard/SecondDerivative.lean:48`
- `period_count_bound`: `lean/GuthMaynard/SecondDerivative.lean:191`
- `vanDerCorput_second_derivative`: `lean/GuthMaynard/SecondDerivative.lean:237`
- `vanDerCorput_B_process`: `lean/GuthMaynard/SecondDerivative.lean:404`

### Blueprint line 2937

Files: `lean/GuthMaynard/Weyl.lean`, `lean/GuthMaynard/WeylExplicit.lean`, `lean/GuthMaynard/WeylZeta.lean`, `lean/WeylPort/Block.lean`.

- `interval_weyl_differencing_complex`: `lean/GuthMaynard/Weyl.lean:23`
- `logarithmicDifferenceCurvature_bounds`: `lean/GuthMaynard/Weyl.lean:124`
- `logarithmic_weyl_exponent_pair_prefix`: `lean/GuthMaynard/WeylExplicit.lean:476`
- `norm_weighted_sum_le_of_antitone`: `lean/GuthMaynard/WeylZeta.lean:22`
- `norm_criticalLine_cpow_block_le`: `lean/WeylPort/Block.lean:25`

### Blueprint line 2988

Files: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonK0Integral.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonK0Series.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonCorrectionBounds.lean`, `lean/MathCollab/Density/Stronger/Atkinson/NeumannRemainderSeries.lean`, `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonMainIntegral.lean`.

- `exists_norm_integral_zetaAtkinsonK0_le`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonK0Integral.lean:60`
- `exists_norm_zetaAtkinsonBesselPlus_le`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonK0Series.lean:68`
- `exists_norm_atkinsonCorrectionTerm_le`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonCorrectionBounds.lean:95`
- `exists_norm_zetaAtkinsonVoronoiMain_le`: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonMainIntegral.lean:74`

## External import roots

The external import names below are read from the local import closure. Their mathematical interfaces are discussed in the blueprint. This list is not an audit of their entire transitive code.

- `Mathlib`
- `Mathlib.Algebra.BigOperators.Group.Finset.Basic`
- `Mathlib.Algebra.BigOperators.Module`
- `Mathlib.Algebra.Field.GeomSum`
- `Mathlib.Algebra.Order.Archimedean.Basic`
- `Mathlib.Algebra.Order.BigOperators.Ring.Finset`
- `Mathlib.Algebra.Order.Chebyshev`
- `Mathlib.Algebra.Order.Floor.Semiring`
- `Mathlib.Algebra.QuadraticDiscriminant`
- `Mathlib.Analysis.Analytic.Binomial`
- `Mathlib.Analysis.Analytic.IsolatedZeros`
- `Mathlib.Analysis.Calculus.BumpFunction.FiniteDimension`
- `Mathlib.Analysis.Calculus.ContDiff.Deriv`
- `Mathlib.Analysis.Calculus.Deriv.MeanValue`
- `Mathlib.Analysis.Calculus.Deriv.Pow`
- `Mathlib.Analysis.Calculus.Deriv.Shift`
- `Mathlib.Analysis.Calculus.Deriv.Star`
- `Mathlib.Analysis.Calculus.Deriv.Support`
- `Mathlib.Analysis.Calculus.IteratedDeriv.FaaDiBruno`
- `Mathlib.Analysis.Calculus.IteratedDeriv.Lemmas`
- `Mathlib.Analysis.Calculus.MeanValue`
- `Mathlib.Analysis.Calculus.ParametricIntegral`
- `Mathlib.Analysis.Calculus.UniformLimitsDeriv`
- `Mathlib.Analysis.Complex.Basic`
- `Mathlib.Analysis.Complex.CauchyIntegral`
- `Mathlib.Analysis.Complex.Convex`
- `Mathlib.Analysis.Complex.ExponentialBounds`
- `Mathlib.Analysis.Complex.JensenFormula`
- `Mathlib.Analysis.Complex.LocallyUniformLimit`
- `Mathlib.Analysis.Complex.PhragmenLindelof`
- `Mathlib.Analysis.Complex.RealDeriv`
- `Mathlib.Analysis.Complex.RemovableSingularity`
- `Mathlib.Analysis.Distribution.SchwartzSpace.Fourier`
- `Mathlib.Analysis.Fourier.PoissonSummation`
- `Mathlib.Analysis.InnerProductSpace.Basic`
- `Mathlib.Analysis.InnerProductSpace.Calculus`
- `Mathlib.Analysis.MeanInequalities`
- `Mathlib.Analysis.MellinInversion`
- `Mathlib.Analysis.MellinTransform`
- `Mathlib.Analysis.Normed.Group.FunctionSeries`
- `Mathlib.Analysis.Normed.Group.InfiniteSum`
- `Mathlib.Analysis.Normed.Group.Tannery`
- `Mathlib.Analysis.ODE.Gronwall`
- `Mathlib.Analysis.PSeries`
- `Mathlib.Analysis.RCLike.Sqrt`
- `Mathlib.Analysis.Real.Pi.Bounds`
- `Mathlib.Analysis.Real.Sqrt`
- `Mathlib.Analysis.SpecialFunctions.Arsinh`
- `Mathlib.Analysis.SpecialFunctions.Artanh`
- `Mathlib.Analysis.SpecialFunctions.Complex.Log`
- `Mathlib.Analysis.SpecialFunctions.Complex.LogBounds`
- `Mathlib.Analysis.SpecialFunctions.Complex.LogDeriv`
- `Mathlib.Analysis.SpecialFunctions.Exp`
- `Mathlib.Analysis.SpecialFunctions.ExpDeriv`
- `Mathlib.Analysis.SpecialFunctions.Gamma.Basic`
- `Mathlib.Analysis.SpecialFunctions.Gamma.Beta`
- `Mathlib.Analysis.SpecialFunctions.Gamma.BohrMollerup`
- `Mathlib.Analysis.SpecialFunctions.Gamma.Deriv`
- `Mathlib.Analysis.SpecialFunctions.Gamma.Digamma`
- `Mathlib.Analysis.SpecialFunctions.Gaussian.FourierTransform`
- `Mathlib.Analysis.SpecialFunctions.Gaussian.GaussianIntegral`
- `Mathlib.Analysis.SpecialFunctions.ImproperIntegrals`
- `Mathlib.Analysis.SpecialFunctions.Integrals.Basic`
- `Mathlib.Analysis.SpecialFunctions.Log.Base`
- `Mathlib.Analysis.SpecialFunctions.Log.Deriv`
- `Mathlib.Analysis.SpecialFunctions.Pow.Asymptotics`
- `Mathlib.Analysis.SpecialFunctions.Pow.Complex`
- `Mathlib.Analysis.SpecialFunctions.Pow.Continuity`
- `Mathlib.Analysis.SpecialFunctions.Pow.Deriv`
- `Mathlib.Analysis.SpecialFunctions.Pow.NNReal`
- `Mathlib.Analysis.SpecialFunctions.Pow.Real`
- `Mathlib.Analysis.SpecialFunctions.SmoothTransition`
- `Mathlib.Analysis.SpecialFunctions.Sqrt`
- `Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic`
- `Mathlib.Analysis.SpecialFunctions.Trigonometric.Bounds`
- `Mathlib.Analysis.SpecialFunctions.Trigonometric.Cotangent`
- `Mathlib.Analysis.SpecialFunctions.Trigonometric.DerivHyp`
- `Mathlib.Analysis.SpecialFunctions.Trigonometric.Inverse`
- `Mathlib.Analysis.SpecialFunctions.Trigonometric.Series`
- `Mathlib.Analysis.SpecificLimits.Basic`
- `Mathlib.Analysis.SpecificLimits.Normed`
- `Mathlib.Analysis.SumIntegralComparisons`
- `Mathlib.Data.Nat.Log`
- `Mathlib.MeasureTheory.Integral.Asymptotics`
- `Mathlib.MeasureTheory.Integral.Bochner.Basic`
- `Mathlib.MeasureTheory.Integral.DominatedConvergence`
- `Mathlib.MeasureTheory.Integral.IntegralEqImproper`
- `Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic`
- `Mathlib.MeasureTheory.Integral.IntervalIntegral.DistLEIntegral`
- `Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus`
- `Mathlib.MeasureTheory.Integral.IntervalIntegral.IntegrationByParts`
- `Mathlib.MeasureTheory.Integral.Layercake`
- `Mathlib.MeasureTheory.Integral.Prod`
- `Mathlib.MeasureTheory.Measure.Haar.NormedSpace`
- `Mathlib.MeasureTheory.Measure.Lebesgue.Basic`
- `Mathlib.NumberTheory.AbelSummation`
- `Mathlib.NumberTheory.ArithmeticFunction.Misc`
- `Mathlib.NumberTheory.ArithmeticFunction.Moebius`
- `Mathlib.NumberTheory.Divisors`
- `Mathlib.NumberTheory.Harmonic.Bounds`
- `Mathlib.NumberTheory.Harmonic.Defs`
- `Mathlib.NumberTheory.Harmonic.EulerMascheroni`
- `Mathlib.NumberTheory.Harmonic.ZetaAsymp`
- `Mathlib.NumberTheory.LSeries.Basic`
- `Mathlib.NumberTheory.LSeries.Dirichlet`
- `Mathlib.NumberTheory.LSeries.HurwitzZetaValues`
- `Mathlib.NumberTheory.LSeries.MellinEqDirichlet`
- `Mathlib.NumberTheory.LSeries.RiemannZeta`
- `Mathlib.NumberTheory.LSeries.SumCoeff`
- `Mathlib.NumberTheory.LSeries.ZetaZeros`
- `Mathlib.Tactic`
- `Mathlib.Topology.Algebra.InfiniteSum.ENNReal`
- `Mathlib.Topology.Algebra.InfiniteSum.NatInt`
- `Mathlib.Topology.Algebra.InfiniteSum.Real`
- `Mathlib.Topology.Algebra.IsUniformGroup.Basic`
- `Mathlib.Topology.Order.Compact`

## Local import inventory

### MathCollab.Density.RectangleResidue

File: `lean/MathCollab/Density/RectangleResidue.lean`; 346 source lines; SHA-256 `f370817ca7083031cffffa7190bde523556885741ec80a80a28504465793375b`.

- `RectangleBorder` at line 30
- `mem_Rect` at line 34
- `Set.left_not_mem_uIoo` at line 40
- `Set.right_not_mem_uIoo` at line 43
- `Set.ne_left_of_mem_uIoo` at line 46
- `Set.ne_right_of_mem_uIoo` at line 49
- `rectangleBorder_subset_rectangle` at line 52
- `rectangleBorder_disjoint_singleton` at line 60
- `rectangle_mem_nhds_iff` at line 68
- `mapsTo_rectangleBorder_left_re` at line 73
- `mapsTo_rectangleBorder_right_re` at line 78
- `mapsTo_rectangleBorder_left_im` at line 83
- `mapsTo_rectangleBorder_right_im` at line 88
- `not_mem_rectangleBorder_of_rectangle_mem_nhds` at line 93
- `HIntegral` at line 101
- `VIntegral` at line 105
- `HIntegral'` at line 109
- `VIntegral'` at line 113
- `RectangleIntegral` at line 116
- `RectangleIntegral'` at line 122
- `HolomorphicOn` at line 125
- `HolomorphicOn.vanishesOnRectangle` at line 128
- `RectangleIntegral_congr` at line 135
- `RectangleIntegral'_congr` at line 145
- `RectangleBorderIntegrable` at line 149
- `RectangleBorderIntegrable.add` at line 155
- `ContinuousOn.rectangleBorder_integrable` at line 167
- `ContinuousOn.rectangleBorderIntegrable` at line 175
- `ContinuousOn.rectangleBorderNoPIntegrable` at line 180
- `HolomorphicOn.rectangleBorderIntegrable'` at line 186
- `HolomorphicOn.rectangleBorderIntegrable` at line 191
- `RectangleIntegral.translate` at line 194
- `RectangleIntegral.translate'` at line 200
- `Complex.inv_re_add_im` at line 204
- `sq_add_sq_ne_zero` at line 208
- `continuous_self_div_sq_add_sq` at line 211
- `integral_self_div_sq_add_sq` at line 215
- `integral_const_div_sq_add_sq` at line 228
- `integral_const_div_self_add_im` at line 239
- `integral_const_div_re_add_self` at line 262
- `ResidueTheoremAtOrigin'` at line 280
- `ResidueTheoremInRectangle` at line 302
- `ResidueTheoremOnRectangleWithSimplePole` at line 314

### MathCollab.Density.Oscillatory

File: `lean/MathCollab/Density/Oscillatory.lean`; 389 source lines; SHA-256 `cea775144b3e93e6acb3a795bc2fac9e2599d4d52158985cb24d0c4e92a2aeda`.

- `gmReflectionIntegral` at line 22
- `gmReflectionPrimitive` at line 29
- `gmReflectionRatio` at line 35
- `gmReflectionRatioReal` at line 39
- `hasDerivAt_gmReflectionPrimitive` at line 42
- `hasDerivAt_gmReflectionRatio` at line 60
- `hasDerivAt_gmReflectionRatioReal` at line 76
- `gmReflectionRatio_mul_primitiveDeriv` at line 90
- `gmReflectionIntegral_eq_parts` at line 111
- `norm_gmReflectionPrimitive` at line 177
- `norm_gmReflectionRatio` at line 181
- `norm_gmReflectionIntegrand` at line 189
- `norm_gmReflectionIntegral_le_endpoint_variation` at line 198
- `norm_gmReflectionIntegral_le_left` at line 279
- `norm_gmReflectionIntegral_le_right` at line 309
- `norm_gmReflectionIntegral_le_length_div` at line 347
- `intervalIntegrable_gmReflectionIntegrand` at line 369

### MathCollab.Density.UniformIBP

File: `lean/MathCollab/Density/UniformIBP.lean`; 334 source lines; SHA-256 `35b5a4ac05fb4781c396623260637a2175e40e794d11659924005b55c02ffda4`.

- `phaseQuotient` at line 20
- `ibpAmplitude` at line 24
- `phaseQuotient_contDiffAt` at line 28
- `ibpAmplitude_contDiffAt` at line 36
- `ibpAmplitude_tsupport_subset` at line 57
- `offBandParameters` at line 65
- `offBandParameters_isCompact` at line 69
- `ibpAmplitude_uniform_bound` at line 94
- `offBand_denominator_gap` at line 113
- `normalized_offBand_mem` at line 149
- `logOscillation` at line 169
- `norm_logOscillation` at line 172
- `hasDerivAt_logOscillation` at line 176
- `ibpAmplitude_contDiffAt_slice` at line 190
- `phaseQuotient_contDiffAt_slice` at line 197
- `offBandParameters_ne` at line 203
- `ibpIntegral` at line 210
- `ibpIntegral_recurrence` at line 214
- `ibpIntegral_norm_recurrence` at line 274
- `uniform_normalized_decay` at line 283
- `uniform_offBand_decay` at line 310

### MathCollab.Density.ReflectionDefinitions

File: `lean/MathCollab/Density/ReflectionDefinitions.lean`; 239 source lines; SHA-256 `ce4c86d987e374e357fd966686d9b53d38c0ea49ddca9f50201da2db8955dd06`.

- `dirichletPhase` at line 17
- `ReflectionCutoff` at line 21
- `modeIntegral` at line 29
- `cutoffIntegral` at line 33
- `hKernel` at line 37
- `dyadicPolynomial` at line 41
- `completePairEnergy` at line 44
- `shellEnergy` at line 47
- `inReflectionBand` at line 51
- `localSet` at line 56
- `discardedMode` at line 59
- `modeIntegral_eq_interval` at line 62
- `uniform_offBand_modeIntegral` at line 87
- `outsideBand_scaled` at line 98
- `integerPowerMajorant` at line 118
- `summable_integerPowerMajorant` at line 120
- `uniform_discarded_modes` at line 126
- `zero_normalized_mem` at line 169
- `uniform_zero_modeIntegral` at line 181
- `nonzeroMode` at line 199
- `uniform_zero_modes` at line 203

### MathCollab.Density.AnalyticTransforms

File: `lean/MathCollab/Density/AnalyticTransforms.lean`; 276 source lines; SHA-256 `bc78f929c5f32533cbd6933965ea37a9d41c12e288178bb5faa978d26e5adb82`.

- `sourcePhase` at line 25
- `schwartz_poisson_at_zero` at line 28
- `fourier_scaled_modulated` at line 32
- `scaled_modulated_poisson` at line 78
- `mellinConvergent_one_of_compactSupport` at line 121
- `verticalIntegrable_mellin_of_quadratic_decay` at line 136
- `mellin_inversion_line_one` at line 151
- `mellinLogLift` at line 165
- `mellinLogLift_contDiff` at line 168
- `mellinLogLift_hasCompactSupport` at line 181
- `mellinLogLiftSchwartz` at line 204
- `mellin_line_one_eq_fourier_logLift` at line 213
- `scaledPower_mul_norm_mellin_line_one_le_seminorm` at line 233
- `norm_mellin_line_one_le_seminorm_div_scaledPower` at line 259

### MathCollab.Density.CutoffTransforms

File: `lean/MathCollab/Density/CutoffTransforms.lean`; 181 source lines; SHA-256 `b5e548edcacf34fc33789353a2acac5b6fd15632aa1bfe4870655b65ef6d40be`.

- `logCutoff` at line 17
- `compactSupport_of_cutoff_support` at line 19
- `logCutoff_hasCompactSupport` at line 23
- `logCutoff_contDiff` at line 28
- `fourier_logCutoff` at line 45
- `scaled_log_poisson` at line 67
- `integrable_mellin_line_one` at line 78
- `cutoff_mellin_inversion` at line 92
- `summable_modeIntegral` at line 102
- `summable_nat_logCutoff` at line 116
- `tsum_int_logCutoff_eq_nat` at line 127
- `poisson_nonzero_modes` at line 147
- `ReflectionCutoff.complex_smooth` at line 162
- `ReflectionCutoff.complex_support` at line 166
- `modeIntegral_zero_frequency` at line 170
- `hKernel_poisson` at line 176

### MathCollab.Density.FixedBandError

File: `lean/MathCollab/Density/FixedBandError.lean`; 104 source lines; SHA-256 `0eabc882c909e79aa48a87a416d1f2ebf30a320b0ccaa735be4828c928f346bd`.

- `retainedMode` at line 15
- `reflectionBand` at line 19
- `mem_reflectionBand` at line 22
- `tsum_retainedMode_eq_finite` at line 33
- `bandContribution` at line 42
- `summable_retainedMode` at line 45
- `summable_discardedMode` at line 56
- `nonzeroMode_eq_retained_add_discarded` at line 67
- `hKernel_sub_bandContribution` at line 77
- `uniform_fixedBand_and_diagonal_error` at line 86

### MathCollab.Density.AllFrequency

File: `lean/MathCollab/Density/AllFrequency.lean`; 109 source lines; SHA-256 `4b5c72234a85e20d6f156dd9bae85f68f8cce0cee8cce7d2d233eea22e4290b7`.

- `gmReflectionIntegral_add` at line 14
- `norm_gmReflectionIntegral_le_six_div_sqrt` at line 23
- `norm_oscillatoryIntegral_le` at line 102

### MathCollab.Density.MellinKernel

File: `lean/MathCollab/Density/MellinKernel.lean`; 294 source lines; SHA-256 `b0fb2f018cf73799fa55b5df207ebe4b4050d171c556d9ddcc40bdbf842701fb`.

- `mellinLine` at line 17
- `oscillatoryKernel` at line 19
- `norm_dirichletPhase` at line 22
- `norm_oscillatoryKernel` at line 25
- `mellin_cpow_eq` at line 28
- `cutoff_mellin_inversion_phase` at line 36
- `scaled_mellin_phase` at line 43
- `integrable_mellin_kernel` at line 61
- `integrable_mellin_kernel_slice` at line 83
- `mellin_kernel_integral_swap` at line 96
- `modeIntegral_scaled` at line 111
- `scaled_cutoff_mellin` at line 164
- `modeIntegral_mellin_common` at line 192
- `reflectionKernel` at line 210
- `reflection_interval_pos` at line 213
- `reflection_interval_order` at line 216
- `band_modeIntegral_mellin` at line 221
- `integrable_reflection_kernel` at line 236
- `norm_reflectionKernel_sq_le` at line 246
- `measurable_reflectionKernel` at line 261
- `mellinLine_eq_cutoffIntegral` at line 273
- `dirichletPhase_eq_cpow` at line 286

### MathCollab.Density.WeightedSquare

File: `lean/MathCollab/Density/WeightedSquare.lean`; 63 source lines; SHA-256 `49423389f7faacbbe1f34bbc474bee765ab2d31d969c292a879ff23e2b77cfd0`.

- `weighted_integral_sq_le` at line 16
- `integrable_weighted_norm_sq` at line 42
- `norm_integral_mul_sq_le` at line 51

### MathCollab.Density.BandEnergy

File: `lean/MathCollab/Density/BandEnergy.lean`; 106 source lines; SHA-256 `f2f964988d8b6d8c93ea3d44ffae2df459d020fa9f9235d40abd7eab4e69e15e`.

- `mellinMass` at line 15
- `bandPhaseSum` at line 17
- `mellinMass_nonneg` at line 20
- `measurable_bandPhaseSum` at line 23
- `norm_bandPhaseSum_le` at line 27
- `bandContribution_mellin` at line 33
- `norm_bandContribution_sq_le` at line 66

### MathCollab.Density.CompletePairs

File: `lean/MathCollab/Density/CompletePairs.lean`; 93 source lines; SHA-256 `3336f574abe7f2cca09f2cc9b7cf52555a2a24b0c1771a73ded0ab88663a881c`.

- `complete_pair_expansion` at line 16
- `complete_pair_coefficient_domination` at line 41
- `dirichletPhase_sub` at line 75
- `completePairEnergy_coefficient_domination` at line 85

### MathCollab.Density.DyadicBlocks

File: `lean/MathCollab/Density/DyadicBlocks.lean`; 219 source lines; SHA-256 `0d6ae69573c8444ad17fff47289b968f57ad239342d8d23a54c849764e22e2a8`.

- `reflectionNatBand` at line 17
- `mem_reflectionNatBand` at line 20
- `sum_reflectionBand_eq_nat` at line 30
- `dyadicExponents` at line 50
- `reflectionBlocks` at line 52
- `log2_block_bounds` at line 54
- `mem_dyadicExponents` at line 60
- `dyadicExponent_scale_bounds` at line 64
- `dyadicExponents_card_le` at line 82
- `reflectionBlocks_card_le` at line 106
- `reflectionBlock_scale_bounds` at line 110
- `log2_eq_iff_block` at line 117
- `natBand_filter_log2` at line 127
- `dirichletPhase_add` at line 142
- `dirichletPhase_mul` at line 150
- `blockCoefficient` at line 158
- `blockPolynomial` at line 161
- `norm_blockCoefficient_le` at line 164
- `fiber_phaseSum_eq` at line 170
- `sum_reflectionBlocks` at line 195
- `mem_reflectionBlocks_iff` at line 202

### MathCollab.Density.LocalCover

File: `lean/MathCollab/Density/LocalCover.lean`; 176 source lines; SHA-256 `9d463012f775155c1bb88b2722be29017ba606002314171ee4f9fdddacf8cf44`.

- `localIndices` at line 15
- `mem_localSet_iff_floor` at line 18
- `mem_localIndices_iff` at line 37
- `localSet_eq_empty_of_notMem` at line 46
- `pair_mem_localSet` at line 53
- `sum_pairs_indicator` at line 79
- `close_pairs_le_local_pairs` at line 94
- `tsum_completePairEnergy_localSet` at line 122
- `localIndices_filter_point` at line 130
- `sum_card_localSet` at line 142
- `tsum_card_localSet` at line 162
- `localSet_pair_distance` at line 169

### MathCollab.Density.ReflectionAssembly

File: `lean/MathCollab/Density/ReflectionAssembly.lean`; 200 source lines; SHA-256 `b49c3093b63e0b2f8ac321d1d103dedab79a8203e7cfe6fb743f9d3e5879c689`.

- `norm_bandPhaseSum_sq_le_blocks` at line 17
- `complete_pairs_block_le` at line 44
- `close_pairs_block_le_local` at line 52
- `localReflectionEnergy` at line 62
- `positiveShell` at line 65
- `localReflectionEnergy_nonneg` at line 68
- `positiveShell_bandPhaseSum_le` at line 76
- `positiveShell_integral` at line 104
- `integrable_positiveShell` at line 129
- `positiveShell_const_mul` at line 141
- `positiveShell_mono` at line 151
- `positiveShell_bandContribution_le` at line 163

### MathCollab.Density.Reflection

File: `lean/MathCollab/Density/Reflection.lean`; 138 source lines; SHA-256 `97f7eef55eef172eca504ede0e3f9c4bf6c181c53327391ef39817c83aeec78d`.

- `dirichletPhase_neg` at line 15
- `hKernel_neg` at line 23
- `norm_hKernel_neg` at line 29
- `shellEnergy_eq_twice_positive` at line 33
- `positiveShell_add` at line 54
- `positiveShell_const_le` at line 64
- `error_power_eq` at line 78
- `hKernel_sq_le_band_error` at line 85
- `uniform_reflection` at line 97

### MathCollab.Density.LargeValueDefinitions

File: `lean/MathCollab/Density/LargeValueDefinitions.lean`; 81 source lines; SHA-256 `cdb886f223bc57f13877191d10ee9495c283fc492b3ac01c19a4026bf7e50f4a`.

- `detectingPolynomial` at line 19
- `kernelEnergy` at line 22
- `oneSeparated` at line 25
- `intervalSpan` at line 28
- `localDiameter` at line 31
- `divisorMaximum` at line 33
- `bootstrapScalar` at line 36
- `LargeValueData` at line 40
- `detectingPolynomial_norm_le` at line 58
- `LargeValueData.height_le_length` at line 69
- `kernelEnergy_nonneg` at line 74
- `oneSeparated_subset` at line 78

### MathCollab.Density.ComparisonCutoff

File: `lean/MathCollab/Density/ComparisonCutoff.lean`; 82 source lines; SHA-256 `26ac986f12f4bac9028b884c58fe8a6ca82d560034dadba2a4803d72c95af18d`.

- `ComparisonCutoff` at line 19
- `comparisonCutoff` at line 25
- `cutoffIntegral_quadratic_decay` at line 49

### MathCollab.Density.ProductGrouping

File: `lean/MathCollab/Density/ProductGrouping.lean`; 140 source lines; SHA-256 `efd6ba31537a307e2fee4b84941a93800956a138b8eaa4efb0da6b44a691ddcb`.

- `productPairs` at line 17
- `productMultiplicity` at line 20
- `productMultiplicity_le_divisors` at line 23
- `product_range` at line 39
- `divisorMaximum_ge_one` at line 53
- `original_product_divisors_le` at line 63
- `product_cutoff_one` at line 76
- `product_grouping_cutoff` at line 89

### MathCollab.Density.DivisorGrowth

File: `lean/MathCollab/Density/DivisorGrowth.lean`; 131 source lines; SHA-256 `73bf352929e82a3ba68b1faab337c0ebfe1dde58f99ddd94c7d85e51f2f51b75`.

- `exponent_linear_le_geometric` at line 20
- `exponent_linear_le_two_pow` at line 41
- `divisor_card_subpower` at line 51
- `divisorMaximum_subpower` at line 106

### MathCollab.Density.Stronger.Fourth.Coefficients

File: `lean/MathCollab/Density/Stronger/Fourth/Coefficients.lean`; 134 source lines; SHA-256 `98926c828c3d7feea324629e3b2dd78f8c54e31aa5b8fcf2002e0cb33b544926`.

- `divisorWeight` at line 24
- `afeCriticalPoint` at line 26
- `divisorDirichletTerm` at line 28
- `divisorDirichletTerm_eq_divisorWeight_mul_cpow` at line 33
- `norm_fourth_divisorTerm_vertical` at line 42
- `zetaFourthCoeff` at line 56
- `zetaFourthCoeff_zero` at line 59
- `zetaFourthCoeff_one` at line 62
- `norm_zetaFourthCoeff` at line 65
- `exists_norm_sq_zetaFourthCoeff_le` at line 70
- `sum_rpow_sub_one_dyadic_le` at line 97
- `exists_sum_sq_zetaFourthCoeff_dyadic_le` at line 118

### MathCollab.Density.Stronger.TruncatedLayerCake

File: `lean/MathCollab/Density/Stronger/TruncatedLayerCake.lean`; 81 source lines; SHA-256 `6e52238192510904c1089a7ab0ecbb82adcf9beeb15985b98bab0e907a8f64e2`.

- `continuous_const_div_max` at line 23
- `integral_const_div_max` at line 28
- `integral_le_log_of_truncated_tail` at line 57

### MathCollab.Density.Stronger.CriticalMoment

File: `lean/MathCollab/Density/Stronger/CriticalMoment.lean`; 167 source lines; SHA-256 `e461c7f53cce3b465fbe57328a2de9f9e93f4d12f462bdb28463db96d1288a89`.

- `zetaMomentCriticalNorm` at line 22
- `continuous_zetaMomentCriticalNorm` at line 25
- `pointValueSuperlevel` at line 40
- `isClosed_pointValueSuperlevel` at line 43
- `measurableSet_pointValueSuperlevel` at line 53
- `pointValueSuperlevel_subset_Icc` at line 58
- `integrableOn_zeta_twelfth_pointValueSuperlevel` at line 62
- `pointValue_power_tail_measure_le` at line 67
- `zeta_twelfth_high_integral_le_log` at line 101
- `zeta_twelfth_low_integral_le_fourth` at line 117
- `zeta_twelfth_integral_le_high_add_fourth` at line 150

### MathCollab.Density.Stronger.Fourth.SquareSource

File: `lean/MathCollab/Density/Stronger/Fourth/SquareSource.lean`; 457 source lines; SHA-256 `0564eac82d84a06364816534b9087683eca7c219568cb7569516c3ab3eb07060`.

- `arithmeticZeta_mul_self_eq_sigma_zero` at line 30
- `riemannZeta_sq_eq_divisorLSeries` at line 49
- `divisorLSeries_summable` at line 78
- `completedXiNumerator` at line 94
- `completedXiNumerator_eq` at line 99
- `completedXiNumerator_one_sub` at line 107
- `differentiable_completedXiNumerator` at line 113
- `afeCriticalPoint_ne_zero` at line 128
- `afeCriticalPoint_ne_one` at line 133
- `hughesYoungAuxiliaryZero` at line 140
- `hughesYoungAuxiliaryZero_zero` at line 144
- `hughesYoungAuxiliaryZero_neg` at line 148
- `differentiable_hughesYoungAuxiliaryZero` at line 152
- `completedRiemannZeta_eq_zeta_mul_GammaR` at line 159
- `afeCriticalPoint_neg_eq_star` at line 172
- `riemannZeta_afeCriticalPoint_neg_eq_star` at line 178
- `zetaSquarePoleNormalization` at line 187
- `zetaSquarePoleNormalization_ne_zero` at line 190
- `zetaSquarePoleNormalization_neg` at line 196
- `zetaSquarePoleNormalization_eq` at line 205
- `zetaSquarePoleNormalization_norm_lower` at line 210
- `zetaSquareContourNumerator` at line 217
- `differentiable_zetaSquareContourNumerator` at line 223
- `zetaSquareContourNumerator_neg` at line 237
- `zetaSquareContourNumerator_zero` at line 251
- `zetaSquareContourIntegrand` at line 263
- `zetaSquareContourIntegrand_neg` at line 268
- `zetaSquare_finiteRectangle` at line 278
- `hIntegral_zetaSquare_bottom` at line 316
- `vIntegral_zetaSquare_left` at line 344
- `zetaSquareAFE_truncated_native` at line 380
- `zetaSquareGammaNormalization` at line 407
- `zetaSquareGammaNormalization_ne_zero` at line 410
- `zetaSquareGammaNormalization_neg` at line 416
- `completedZeta_square_eq_norm_mul_gamma` at line 420
- `zetaSquareNorm_eq_truncated_source` at line 445

### MathCollab.Density.AbelZetaGrowth

File: `lean/MathCollab/Density/AbelZetaGrowth.lean`; 325 source lines; SHA-256 `c7bd84f791b5e8d20cad4e6a0122f3a704689a61f472441658fb61e06789b908`.

- `abelZetaKernel` at line 29
- `abelZetaKernel_eq_of_one_lt` at line 32
- `abelZetaKernel_eq_zero_of_le_one` at line 36
- `norm_abelZetaKernel_le_one` at line 40
- `measurable_abelZetaKernel` at line 48
- `locallyIntegrableOn_abelZetaKernel` at line 53
- `abelZetaKernel_isBigO_atTop` at line 62
- `abelZetaKernel_isBigO_zero` at line 69
- `abelZetaRemainder` at line 77
- `differentiableAt_abelZetaRemainder` at line 80
- `mellinConvergent_abelZetaKernel` at line 89
- `abelZetaRemainder_eq_integral` at line 96
- `integrableOn_abelZetaRemainder_integrand` at line 125
- `regularizedRiemannZeta` at line 142
- `regularizedAbelZeta` at line 146
- `differentiableAt_regularizedRiemannZeta` at line 149
- `differentiableAt_regularizedAbelZeta` at line 172
- `sum_one_Icc` at line 179
- `sum_one_Icc_isBigO` at line 183
- `natFloor_cast_complex` at line 190
- `integral_Ioi_cpow_neg` at line 197
- `riemannZeta_eq_abel_of_one_lt_re` at line 203
- `regularized_zeta_eq_abel_of_one_lt_re` at line 235
- `regularized_zeta_eq_abel` at line 245
- `riemannZeta_eq_abel` at line 265
- `norm_abelZetaRemainder_le` at line 274
- `norm_riemannZeta_le_five_mul_norm` at line 299

### MathCollab.Density.Stronger.Fourth.SquareGrowth

File: `lean/MathCollab/Density/Stronger/Fourth/SquareGrowth.lean`; 148 source lines; SHA-256 `4550f0ff0a1d414cb54384328271cc73d7371d754ecf83562e7f22e0c00836e2`.

- `norm_Gamma_le_realGamma_re` at line 27
- `norm_GammaR_le_realGamma_re` at line 46
- `exists_norm_GammaR_strip_le` at line 64
- `norm_completedXiNumerator_right_strip_le` at line 80
- `exists_completedXiNumerator_strip_cubic_high` at line 101
- `exists_completedXiNumerator_strip_cubic` at line 129

### MathCollab.Density.Stronger.Fourth.SquareContour

File: `lean/MathCollab/Density/Stronger/Fourth/SquareContour.lean`; 273 source lines; SHA-256 `ce31b69c2755a719c01bb6c6c98d98fe93c06a5b4f9858cfb7f9cce80b99d5f9`.

- `norm_hughesYoungAuxiliaryZero_le_polynomial` at line 27
- `gaussianPolynomial` at line 47
- `gaussianPolynomial_nonneg` at line 49
- `exists_zetaSquareNumerator_strip_gaussian` at line 54
- `continuous_zetaSquareContour_vertical` at line 108
- `gaussianPolynomial_le` at line 119
- `integrable_gaussianPolynomial` at line 138
- `tendsto_gaussianPolynomial_zero` at line 150
- `norm_zetaSquareContour_le_of_lower` at line 164
- `integrable_zetaSquareContour_vertical` at line 178
- `tendsto_hIntegral_zetaSquare_top_zero` at line 190
- `tendsto_hIntegral'_zetaSquare_top_zero` at line 214
- `zetaSquareAFE_vertical_limit` at line 222
- `zetaSquareVerticalIntegral` at line 241
- `tendsto_zetaSquare_vertical_integral` at line 244
- `completedZeta_square_eq_vertical_integrals` at line 258
- `zetaSquareNorm_eq_vertical_integrals` at line 265

### MathCollab.Density.Stronger.Fourth.SquareNormalized

File: `lean/MathCollab/Density/Stronger/Fourth/SquareNormalized.lean`; 358 source lines; SHA-256 `7cbbe74756eb63e6e583e9a5c198a760fc7f0b8cdd6ce9c0c4afd751b26f6232`.

- `gammaReal_conj` at line 21
- `continuous_GammaR_afe_vertical` at line 29
- `zetaSquareRightKernel` at line 48
- `continuous_zetaSquareRightKernel` at line 55
- `zetaSquareContourIntegrand_eq_rightKernel_mul_divisor` at line 72
- `zetaSquareRightKernel_conj` at line 91
- `zetaSquareDivisorIntegral` at line 103
- `completedZeta_square_eq_divisor_integrals` at line 105
- `zetaSquareContour_right_conj` at line 110
- `zetaSquareDivisorIntegral_conj` at line 124
- `conj_zetaSquareGammaNormalization` at line 133
- `zetaSquareNorm_eq_reflected_source` at line 140
- `zetaFourthRightPiece` at line 156
- `zetaSquareNorm_eq_two_re_fourthRightPiece` at line 159
- `zetaFourthRightPiece_neg` at line 163
- `zetaFourthRightPiece_re_nonneg` at line 169
- `zeta_fourth_le_four_mul_rightPiece_sq` at line 174
- `norm_zetaSquareGammaNormalization` at line 182
- `norm_gammaSquare_div_zetaSquareGammaNormalization` at line 192
- `zetaSquarePoleShift` at line 201
- `criticalPoint_pole_product` at line 205
- `zetaSquarePoleShift_eq_source` at line 212
- `poleShift_sub_one_identity` at line 219
- `norm_poleShift_linear_sub_one_le` at line 233
- `norm_zetaSquarePoleShift_le` at line 249
- `norm_zetaSquarePoleShift_sub_one_le` at line 262
- `zetaFourthKernel` at line 283
- `zetaFourthKernel_one` at line 289
- `continuous_zetaFourthKernel_vertical` at line 300
- `norm_zetaFourthKernel_vertical` at line 313
- `zetaFourthRightPiece_eq_divisor_integral` at line 328
- `integrable_zetaFourthKernel_mul_divisor` at line 346

### MathCollab.Density.Stronger.Fourth.DigammaSeries

File: `lean/MathCollab/Density/Stronger/Fourth/DigammaSeries.lean`; 361 source lines; SHA-256 `560b79405f62e98daac244117285dbe15619e7aa8a9ca5c85a70a949817a07be`.

- `norm_natCast_add_one` at line 42
- `sum_inv_natCast_add_one` at line 48
- `inv_add_one_sub_inv_eq` at line 55
- `norm_inv_add_one_sub_inv_le` at line 63
- `summable_one_div_natCast_add_one_sq` at line 84
- `logGammaSeq` at line 90
- `logGammaSeq_succ_sub` at line 94
- `cauchySeq_logGammaSeq` at line 130
- `exp_logGammaSeq` at line 210
- `hasSum_digamma_of_re_pos` at line 230

### MathCollab.Density.Stronger.Fourth.DigammaLog

File: `lean/MathCollab/Density/Stronger/Fourth/DigammaLog.lean`; 250 source lines; SHA-256 `ce29fa24637e9168001f096f44dc0f444ea62ecb20d1bdeef5dda9fa8e925d72`.

- `shift_ne_zero` at line 34
- `integral_shift_inv` at line 41
- `norm_shift_mono` at line 59
- `norm_reciprocal_log_step_le` at line 67
- `sum_reciprocal_sq_le` at line 115
- `norm_sum_reciprocal_sub_log_le` at line 139
- `tendsto_log_nat_shift_sub_log` at line 157
- `norm_digamma_sub_log_le` at line 187
- `abs_re_digamma_sub_log_im_le` at line 220

### MathCollab.Density.Stronger.Fourth.GammaShiftLog

File: `lean/MathCollab/Density/Stronger/Fourth/GammaShiftLog.lean`; 165 source lines; SHA-256 `41222ed0dfd44c0f10715bae38a5b95368a644aa124e8ac8d9c09e66964559a1`.

- `hasDerivAt_Gamma_eq_mul_digamma_of_re_pos` at line 24
- `hasDerivAt_gammaReal` at line 38
- `norm_log_sub_le_of_im_le_neg` at line 57
- `zetaGammaLeadingLog` at line 88
- `zetaGammaHalfShift` at line 91
- `zetaGammaHalfShift_re_pos` at line 94
- `zetaGammaHalfShift_im_le` at line 101
- `log_negative_height_eq` at line 110
- `norm_zetaGammaHalfShift_sub_negative_height_le` at line 122
- `norm_zetaGammaHalfShift_digamma_sub_le` at line 138

### MathCollab.Density.Stronger.Atkinson.GammaPhase

File: `lean/MathCollab/Density/Stronger/Atkinson/GammaPhase.lean`; 141 source lines; SHA-256 `2839c12749c12db22bd7ebe181687f9961d13da5a9b3d850aa82713b368ac809`.

- `digamma_conj` at line 27
- `zetaSquareReflectedGammaPhase` at line 38
- `zetaSquareGammaFrequency` at line 41
- `norm_zetaSquareReflectedGammaPhase` at line 44
- `zetaSquareReflectedGammaPhase_zero` at line 51
- `zetaSquareReflectedGammaPhase_mul_zeta` at line 56
- `zetaSquareGammaNormalization_reflected_factor` at line 71
- `hasDerivAt_gammaCritical` at line 83
- `hasDerivAt_zetaSquareReflectedGammaPhase` at line 92
- `abs_zetaSquareGammaFrequency_add_log_le` at line 119

### MathCollab.Density.Stronger.Fourth.GammaShiftAmplitude

File: `lean/MathCollab/Density/Stronger/Fourth/GammaShiftAmplitude.lean`; 154 source lines; SHA-256 `0b27ef7775ba37983f53d7a3e73075ad0288fba6d37f1357899caae215ce4e4e`.

- `zetaGammaShiftAmplitude` at line 24
- `zetaGammaShiftError` at line 29
- `zetaGammaShiftError_nonneg` at line 31
- `zetaGammaShiftAmplitude_zero` at line 34
- `hasDerivAt_zetaGammaShiftAmplitude` at line 40
- `amplitude_derivative_norm_le` at line 60
- `norm_zetaGammaShiftAmplitude_le` at line 74
- `norm_zetaGammaShiftAmplitude_sub_one_le` at line 95
- `norm_gammaReal_shift_sq_sub_exp_le` at line 117
- `zetaGammaLeadingLog_mul_re` at line 132
- `norm_gammaReal_shift_sq_le_exp` at line 136

### MathCollab.Density.Stronger.Atkinson.NearKernel

File: `lean/MathCollab/Density/Stronger/Atkinson/NearKernel.lean`; 187 source lines; SHA-256 `a1b3ab34ea1626b3c826e6f60402844a1fac62ae2668df1465c4c7b26d782360`.

- `norm_poleShift_gammaReal_sq_sub_exp_le` at line 25
- `zetaSquareLeadingRightKernel` at line 59
- `zetaSquareRightKernel_normalized_reflected` at line 66
- `norm_rightContour_shift_le` at line 82
- `near_shift_exponent_le` at line 88
- `norm_near_pole_gamma_error_le` at line 105
- `norm_zetaSquareRightKernel_sub_leading_near_le` at line 142

### MathCollab.Density.Stronger.Atkinson.GaussianPolynomial

File: `lean/MathCollab/Density/Stronger/Atkinson/GaussianPolynomial.lean`; 67 source lines; SHA-256 `71ec1212c0d0985d5f6b6c41da0e8941a8e560eb98f4f3a54c0c4bdf5ce3eff0`.

- `integrable_abs_pow_mul_exp_neg_mul_sq` at line 23
- `integrable_exp_sub_mul_sq_mul_add_abs_pow` at line 44

### MathCollab.Density.Stronger.Fourth.SquareKernelFar

File: `lean/MathCollab/Density/Stronger/Fourth/SquareKernelFar.lean`; 232 source lines; SHA-256 `abd84220bc616fc6e57dc00b94f9aff5a6e1704d1a5be119462e6aee589c7116`.

- `abs_polynomial_mul_exp_le_gaussian` at line 23
- `norm_vertical_shift_le` at line 40
- `vertical_shift_re_le_norm` at line 46
- `norm_complex_sin_le_exp_abs_im` at line 52
- `norm_inv_gamma_critical_half_le` at line 66
- `exists_norm_inv_gammaReal_critical_le` at line 97
- `exists_norm_inv_zetaSquareGammaNormalization_le` at line 115
- `norm_zetaSquarePoleShift_le_polynomial` at line 129
- `exists_norm_zetaFourthKernel_far_le` at line 156

### MathCollab.Density.Stronger.Fourth.SquareDivisorSeries

File: `lean/MathCollab/Density/Stronger/Fourth/SquareDivisorSeries.lean`; 213 source lines; SHA-256 `19efffe4830b5dbbf85bfacb009ce006d9ef866b26bf436889dc6c0a6d40c955`.

- `exists_zetaSquareRightKernel_uniform_gaussian_bound` at line 24
- `integrable_zetaSquareRightKernel` at line 87
- `summable_divisorDirichletTerm` at line 113
- `tsum_divisorDirichletTerm` at line 117
- `continuous_divisorDirichletTerm_vertical` at line 121
- `zetaSquareDivisorTerm` at line 137
- `norm_zetaSquareDivisorTerm` at line 141
- `integrable_zetaSquareDivisorTerm` at line 147
- `integral_norm_zetaSquareDivisorTerm` at line 157
- `summable_integral_norm_zetaSquareDivisorTerm` at line 163
- `tsum_zetaSquareDivisorTerm` at line 168
- `zetaSquareDivisorContribution` at line 174
- `hasSum_zetaSquareDivisorContribution` at line 179
- `completedZeta_square_eq_divisor_series` at line 189
- `zetaSquareNormalizedContribution` at line 196
- `hasSum_zetaSquareNormalizedContribution` at line 200
- `zetaSquareNorm_eq_divisor_series` at line 209

### MathCollab.Density.Stronger.Atkinson.KernelApproximation

File: `lean/MathCollab/Density/Stronger/Atkinson/KernelApproximation.lean`; 195 source lines; SHA-256 `e89b1de03e3cf9368f23413f714a6dc099d82fd1c1872c5e8e8033d28be1e60f`.

- `zetaSquareKernelErrorMajorant` at line 27
- `zetaSquareKernelErrorMajorant_nonneg` at line 30
- `integrable_zetaSquareKernelErrorMajorant` at line 33
- `gaussian_fusion_le` at line 38
- `exists_norm_normalized_zetaSquareRightKernel_far_le` at line 43
- `continuous_zetaSquareLeadingRightKernel` at line 73
- `norm_zetaSquareLeadingRightKernel` at line 84
- `exists_norm_zetaSquareLeadingRightKernel_far_le` at line 100
- `exists_norm_zetaSquareRightKernel_sub_leading_le` at line 134
- `integrable_zetaSquareRightKernel_error` at line 160
- `integrable_zetaSquareLeadingRightKernel` at line 170
- `exists_integral_norm_zetaSquareRightKernel_error_le` at line 181

### MathCollab.Density.Stronger.Atkinson.LeadingDivisor

File: `lean/MathCollab/Density/Stronger/Atkinson/LeadingDivisor.lean`; 141 source lines; SHA-256 `00e1e5125db6cf863042a2d2e4bf4df70c2d4307bc615d436e9f201864cd5c76`.

- `zetaSquareLeadingDivisorTerm` at line 25
- `zetaSquareLeadingDivisorContribution` at line 29
- `zetaSquareLeadingDivisorIntegral` at line 32
- `norm_zetaSquareLeadingDivisorTerm` at line 37
- `integrable_zetaSquareLeadingDivisorTerm` at line 43
- `summable_integral_norm_zetaSquareLeadingDivisorTerm` at line 53
- `hasSum_zetaSquareLeadingDivisorContribution` at line 58
- `norm_zetaSquareDivisorTerm_error` at line 65
- `exists_norm_zetaSquareDivisorContribution_error_le` at line 78
- `exists_norm_zetaSquareDivisorIntegral_sub_leading_le` at line 115

### MathCollab.Density.Stronger.Atkinson.DivisorWeightKernel

File: `lean/MathCollab/Density/Stronger/Atkinson/DivisorWeightKernel.lean`; 150 source lines; SHA-256 `eb4aadd8d2000350d7c1858b317d0d7805112bc47887b9214b3c7f0ea0aa3f59`.

- `zetaDivisorWeightNumerator` at line 25
- `zetaDivisorWeightKernel` at line 28
- `zetaDivisorWeight` at line 30
- `zetaDivisorWeightEnvelope` at line 33
- `differentiable_zetaDivisorWeightNumerator` at line 35
- `zetaDivisorWeightNumerator_zero` at line 41
- `zetaDivisorWeightNumerator_neg` at line 44
- `zetaDivisorWeightKernel_neg` at line 48
- `continuous_zetaDivisorWeightKernel_right` at line 52
- `integrable_zetaDivisorWeightEnvelope` at line 61
- `norm_zetaDivisorWeightNumerator_right` at line 66
- `norm_zetaDivisorWeightNumerator_right_le` at line 85
- `norm_zetaDivisorWeightKernel_right_le` at line 108
- `integrable_zetaDivisorWeightKernel_right` at line 119
- `exists_norm_zetaDivisorWeight_le` at line 127

### MathCollab.Density.Stronger.Atkinson.DivisorWeightSmooth

File: `lean/MathCollab/Density/Stronger/Atkinson/DivisorWeightSmooth.lean`; 92 source lines; SHA-256 `ce973893af1892aa959fd08a5156d54d466ff26d813e8d5eddfb3d94724c0015`.

- `hasDerivAt_zetaDivisorWeightKernel_complex` at line 27
- `norm_zetaDivisorWeightNumerator_local_le` at line 38
- `hasDerivAt_zetaDivisorWeight` at line 57
- `differentiable_zetaDivisorWeight` at line 83
- `contDiff_zetaDivisorWeight_complex` at line 86
- `contDiff_zetaDivisorWeight` at line 89

### MathCollab.Density.Stronger.Atkinson.DivisorWeightReflection

File: `lean/MathCollab/Density/Stronger/Atkinson/DivisorWeightReflection.lean`; 258 source lines; SHA-256 `f8713d4d0933a7ce165c8d99c62f2ccb6f6bca7f65254d1ad3a6b4575884daa0`.

- `zetaDivisorWeight_finiteRectangle` at line 25
- `norm_zetaDivisorWeightKernel_horizontal_le` at line 55
- `tendsto_zetaDivisorWeight_horizontal_zero` at line 99
- `hIntegral_zetaDivisorWeight_bottom` at line 141
- `vIntegral_zetaDivisorWeight_left` at line 160
- `zetaDivisorWeight_truncated_reflection` at line 183
- `tendsto_zetaDivisorWeight_vertical` at line 203
- `zetaDivisorWeight_add_neg` at line 219
- `zetaDivisorWeight_zero` at line 229
- `exists_norm_zetaDivisorWeight_min_le` at line 236

### MathCollab.Density.Stronger.Atkinson.DivisorWeightSource

File: `lean/MathCollab/Density/Stronger/Atkinson/DivisorWeightSource.lean`; 106 source lines; SHA-256 `d676937b1e75fd23cc6b9b43c7e8cb9cc6add3600221ee2e78995c75f487860e`.

- `zetaDivisorWeightArgument` at line 25
- `zetaDivisorWeightArgument_re` at line 28
- `zetaDivisorWeightArgument_im` at line 33
- `divisorDirichletTerm_add_eq_mul_exp` at line 38
- `zetaSquareLeadingDivisorTerm_eq_weightKernel` at line 53
- `zetaSquareLeadingDivisorContribution_eq_weight` at line 67
- `hasSum_zetaSquareLeadingDivisor_weighted` at line 77
- `exp_neg_zetaDivisorWeightArgument_re` at line 85
- `exists_norm_source_zetaDivisorWeight_min_le` at line 94

### MathCollab.Density.Stronger.Atkinson.QuadraticGaussian

File: `lean/MathCollab/Density/Stronger/Atkinson/QuadraticGaussian.lean`; 174 source lines; SHA-256 `002046db64d39f74137901ffac7b27240f6b562632f2ea6b56712d8c7c689739`.

- `zetaGaussianQuadraticCoefficient` at line 24
- `zetaGaussianQuadraticIntegral` at line 27
- `zetaGaussianQuadraticCoefficient_re` at line 31
- `zetaGaussianQuadraticCoefficient_im` at line 37
- `zetaGaussianQuadraticCoefficient_re_pos` at line 43
- `zetaGaussianQuadraticIntegral_eq` at line 48
- `integrable_zetaGaussianQuadraticIntegrand` at line 54
- `inverse_re_lower_of_im_le_re` at line 65
- `norm_fourierGaussian_le_of_im_le_re` at line 78
- `norm_zetaGaussianQuadraticIntegral_le` at line 102
- `norm_zetaGaussianQuadraticIntegral_tail` at line 121
- `hasDerivAt_zetaGaussianQuadraticIntegral` at line 134
- `inverse_norm_zetaGaussianQuadraticCoefficient_le` at line 149
- `norm_deriv_zetaGaussianQuadraticIntegral_le` at line 156

### MathCollab.Density.Stronger.Atkinson.GammaQuadratic

File: `lean/MathCollab/Density/Stronger/Atkinson/GammaQuadratic.lean`; 229 source lines; SHA-256 `84f64f91c939fc44f754b2e25dc0e7a881dacb3f3cbfe962fda5e435b4d1b963`.

- `abs_log_shift_sub_linear_le` at line 26
- `zetaSquareGammaQuadraticAngle` at line 56
- `hasDerivAt_zetaSquareGammaQuadraticAngle` at line 59
- `abs_zetaSquareGammaFrequency_linear_error_le` at line 68
- `demodulatedGammaPhase` at line 96
- `hasDerivAt_demodulatedGammaPhase` at line 100
- `norm_zetaSquareReflectedGammaPhase_sub_quadratic_le` at line 114
- `zetaSquareGammaQuadratic_gaussian_identity` at line 153
- `norm_integral_zetaSquareGammaPhase_sub_quadratic_le` at line 168

### MathCollab.Density.Stronger.Atkinson.DivisorWeightVariation

File: `lean/MathCollab/Density/Stronger/Atkinson/DivisorWeightVariation.lean`; 189 source lines; SHA-256 `43c0c3ebee4703e991d8952f8d0fef5303987748d7764baf28fe585a5bcbd480`.

- `hasDerivAt_zetaDivisorWeightKernel_real` at line 26
- `norm_zetaDivisorWeightKernel_real_sub_le` at line 37
- `exists_norm_zetaDivisorWeight_real_sub_le` at line 65
- `exists_norm_zetaDivisorWeight_real_sub_min_le` at line 108
- `abs_log_height_shift_le` at line 128
- `zetaDivisorWeightArgument_height_shift` at line 143
- `exp_zetaDivisorWeightArgument_re` at line 153
- `exists_norm_source_zetaDivisorWeight_height_sub_le` at line 162

### MathCollab.Density.Stronger.Atkinson.DivisorWeightMass

File: `lean/MathCollab/Density/Stronger/Atkinson/DivisorWeightMass.lean`; 161 source lines; SHA-256 `cd218a319d736bd939f5fd2e928475c69a779e2fbc84c30f48e1083089305ae9`.

- `min_one_le_rpow` at line 25
- `norm_divisorCritical_mul_ratio_rpow` at line 33
- `norm_divisorCritical_mul_min_le` at line 45
- `summable_divisorCritical_min` at line 56
- `tsum_divisorCritical_min_le` at line 64
- `summable_norm_source_divisor_weight` at line 74
- `exists_tsum_norm_source_divisor_weight_le` at line 90
- `exists_tsum_divisorCritical_min_height_le` at line 133

### MathCollab.Density.Stronger.Atkinson.DivisorWeightFreezing

File: `lean/MathCollab/Density/Stronger/Atkinson/DivisorWeightFreezing.lean`; 136 source lines; SHA-256 `036867f7282a394002b4bb3a8fafda26ba3ff3825cdb3868736f87add4706edb`.

- `zetaSquareFrozenDivisorContribution` at line 25
- `zetaSquareFrozenDivisorIntegral` at line 29
- `summable_zetaSquareFrozenDivisorContribution` at line 32
- `norm_zetaSquareDivisor_freezing_error` at line 39
- `min_self_inv_le_min_one` at line 48
- `exists_norm_zetaSquareDivisor_freezing_error_le` at line 56
- `exists_norm_zetaSquareLeadingDivisor_sub_frozen_le` at line 81
- `exists_norm_zetaSquareSource_sub_frozen_le` at line 123

### MathCollab.Density.Stronger.Atkinson.GammaGaussianTransform

File: `lean/MathCollab/Density/Stronger/Atkinson/GammaGaussianTransform.lean`; 168 source lines; SHA-256 `0b79f1f1bdb67e56a351280d5cc1fee9110c39aac6bc8bec9ea9e9b6003b226d`.

- `integrable_physical_gaussian` at line 23
- `physical_gaussian_tail_le` at line 31
- `norm_integral_sub_window_le` at line 66
- `zetaSquareGammaGaussianIntegrand` at line 78
- `zetaSquareGammaGaussianTransform` at line 82
- `norm_zetaSquareGammaGaussianIntegrand` at line 85
- `integrable_zetaSquareGammaGaussianIntegrand` at line 90
- `norm_quadratic_gaussian_integrand` at line 100
- `norm_zetaSquareGammaGaussianTransform_sub_quadratic_le` at line 115
- `norm_zetaSquareGammaGaussianTransform_le` at line 152

### MathCollab.Density.Stronger.Atkinson.FrozenDivisorGaussian

File: `lean/MathCollab/Density/Stronger/Atkinson/FrozenDivisorGaussian.lean`; 168 source lines; SHA-256 `179058422fe09aa9751fdf6f023f56f8bf78d21cd43f3c6386a5e82f915d7ace`.

- `zetaFrozenDivisorCoefficient` at line 25
- `zetaFrozenDivisorGaussianMean` at line 29
- `zetaFrozenDivisorQuadraticSum` at line 32
- `divisorDirichletTerm_height_shift` at line 36
- `zetaSquareFrozenDivisorContribution_eq_phase` at line 48
- `zetaSquareFrozenDivisorContribution_mul_gaussian` at line 55
- `summable_norm_zetaFrozenDivisorCoefficient` at line 62
- `integrable_zetaFrozenDivisorGaussianTerm` at line 67
- `summable_integral_norm_zetaFrozenDivisorGaussianTerm` at line 74
- `hasSum_zetaFrozenDivisorGaussianMean` at line 83
- `norm_zetaGaussianQuadraticIntegral_le_mass` at line 95
- `summable_zetaFrozenDivisorQuadraticTerm` at line 102
- `norm_zetaFrozenDivisorGaussianMean_sub_quadratic_le` at line 117
- `exists_norm_zetaFrozenDivisorGaussianMean_sub_quadratic_le` at line 154

### MathCollab.Density.Stronger.Atkinson.QuadraticDivisorBand

File: `lean/MathCollab/Density/Stronger/Atkinson/QuadraticDivisorBand.lean`; 99 source lines; SHA-256 `645ecbc8bc9cda212fa5eec71be28d8e711f13c272f42c2a7f74577d593c7dce`.

- `zetaQuadraticDivisorBand` at line 26
- `zetaShortQuadraticDivisorSum` at line 30
- `divisor_index_bounds_of_frequency` at line 35
- `mem_zetaQuadraticDivisorBand_iff` at line 53
- `zero_not_mem_zetaQuadraticDivisorBand` at line 64
- `zetaQuadraticDivisorBand_index_bounds` at line 69
- `frequency_le_of_not_mem_zetaQuadraticDivisorBand` at line 76
- `zetaFrozenDivisorCoefficient_zero` at line 83
- `norm_zetaQuadraticDivisorTerm_off_band_le` at line 86

### MathCollab.Density.Stronger.Atkinson.RealFrozenSource

File: `lean/MathCollab/Density/Stronger/Atkinson/RealFrozenSource.lean`; 44 source lines; SHA-256 `9563509708ce0d06c6eb2f80376e4cf1604bbca10bab2e77db4a7e5da0480cca`.

- `exists_abs_zetaSquareNorm_sub_frozen_le` at line 25

### MathCollab.Density.Stronger.Atkinson.LocalDivisorMean

File: `lean/MathCollab/Density/Stronger/Atkinson/LocalDivisorMean.lean`; 181 source lines; SHA-256 `fe0b3623b0dbd7fd12d2794d2a044d6f452d405e779bb58a10fdded5d170fa55`.

- `continuous_zetaSquareRightKernel_height` at line 25
- `continuous_zetaSquareDivisorTerm_height` at line 44
- `exists_zetaSquareRightKernel_compact_majorant` at line 55
- `continuous_zetaSquareDivisorContribution` at line 70
- `exists_zetaSquareDivisorContribution_compact_bound` at line 90
- `continuous_zetaSquareGammaNormalization` at line 112
- `continuous_zetaSquareNormalizedContribution` at line 118
- `exists_zetaSquareNormalizedContribution_compact_bound` at line 124
- `summable_local_integral_norm_zetaSquareNormalizedContribution` at line 147
- `hasSum_zetaSquareLocalMean` at line 167
- `zetaSquareLocalMean_eq_divisor_series` at line 176

### MathCollab.Density.Stronger.Atkinson.GaussianAveraging

File: `lean/MathCollab/Density/Stronger/Atkinson/GaussianAveraging.lean`; 124 source lines; SHA-256 `7e1c9928235aafcd2c39dd41b466721665d92bc15f4531f05a829aa5fe00a2ed`.

- `summable_weighted_local_integral_norm_zetaSquareNormalizedContribution` at line 24
- `hasSum_zetaSquareWeightedLocalMean` at line 44
- `zetaGaussianWeight` at line 57
- `continuous_zetaGaussianWeight` at line 59
- `zetaGaussianWeight_pos` at line 63
- `zetaGaussianWeight_le_one` at line 65
- `zetaGaussianWeight_local_lower` at line 68
- `zetaSquareGaussianWindow` at line 78
- `hasSum_zetaSquareGaussianWindow` at line 81
- `zetaSquareLocalMean_le_gaussian_window` at line 89
- `zetaSquareLocalMean_le_gaussian_divisor_series` at line 116

### MathCollab.Density.Stronger.Atkinson.GaussianZetaTail

File: `lean/MathCollab/Density/Stronger/Atkinson/GaussianZetaTail.lean`; 255 source lines; SHA-256 `dfd6465a801af67dccd4156c7aaecda814ccaa9ceea23b5fb5ba214c5ad4c467`.

- `exists_zetaMomentCriticalNorm_linear_bound` at line 26
- `zetaSquareCenteredGaussian` at line 50
- `continuous_zetaSquareCenteredGaussian` at line 53
- `zetaSquareCenteredGaussian_nonneg` at line 60
- `zetaSquareCenteredGaussian_majorant` at line 64
- `integrable_zetaSquareCenteredGaussian` at line 81
- `zetaGaussianWeight_affine` at line 93
- `zetaSquareGaussianWindow_eq_centered` at line 97
- `zetaSquareGaussianMean` at line 106
- `integrable_zetaSquareGaussian_physical` at line 108
- `zetaSquareGaussianMean_eq_physical` at line 116
- `zetaSquareCenteredGaussian_tail_majorant` at line 133
- `exists_zetaSquareGaussian_tail_bound` at line 152
- `exists_zetaSquareGaussian_log_tail_bound` at line 202
- `exists_zetaSquareGaussian_source_approximation` at line 239

### MathCollab.Density.Stronger.Atkinson.FrozenWindow

File: `lean/MathCollab/Density/Stronger/Atkinson/FrozenWindow.lean`; 182 source lines; SHA-256 `158be8185b364f46acd4b97f0a2c021a6600dec6ea051b4081c96cf7d0730f0a`.

- `norm_zetaSquareFrozenDivisorContribution` at line 27
- `continuous_zetaSquareFrozenDivisorIntegral` at line 35
- `norm_zetaSquareFrozenDivisorIntegral_le_mass` at line 47
- `integrable_zetaSquareFrozenDivisor_gaussian` at line 52
- `norm_zetaFrozenDivisorGaussianMean_sub_window_le` at line 63
- `zetaSquareGaussianWindow_eq_height_shift` at line 84
- `exists_abs_zetaSquareGaussianWindow_sub_frozen_window_le` at line 94
- `exists_abs_zetaSquareGaussianWindow_sub_quadratic_le` at line 152

### MathCollab.Density.Stronger.Atkinson.QuadraticDivisorShortening

File: `lean/MathCollab/Density/Stronger/Atkinson/QuadraticDivisorShortening.lean`; 95 source lines; SHA-256 `e3574d6dbe97813c80d54092f67710e46650953defe3e7412f726b41977aa1ec`.

- `norm_zetaFrozenDivisorQuadraticSum_sub_short_le` at line 26
- `exists_norm_zetaFrozenDivisorQuadraticSum_sub_short_le` at line 53
- `exists_abs_zetaSquareGaussianWindow_sub_short_le` at line 71

### MathCollab.Density.Stronger.Atkinson.SourceLogScales

File: `lean/MathCollab/Density/Stronger/Atkinson/SourceLogScales.lean`; 123 source lines; SHA-256 `15baf781157f92167cbd02956ddd501c06b3cafb0c66dc40c8db7d0d9b1dc9e5`.

- `exists_logGaussian_power_tail_bound` at line 26
- `exists_zetaQuadraticDivisor_log_tail_bound` at line 55
- `eventually_const_log_pow_le_rpow` at line 74
- `gaussian_width_sq_le_height` at line 83
- `eventually_zeta_source_log_window_scales` at line 94

### MathCollab.Density.Stronger.Atkinson.SourceErrorScales

File: `lean/MathCollab/Density/Stronger/Atkinson/SourceErrorScales.lean`; 157 source lines; SHA-256 `ee3eb7b0ad39931db584daef21dffdc8847c56443c1258d2b8f729cca2137a20`.

- `source_log_monomial_le_one` at line 25
- `source_scaled_window_square_le` at line 38
- `source_window_square_le_height` at line 52
- `source_scaled_window_fourth_le` at line 62
- `source_scaled_quadratic_phase_error_le` at line 76
- `exists_zetaSquareGaussianWindow_log_error` at line 90

### MathCollab.Density.Stronger.Atkinson.ShortDivisorSource

File: `lean/MathCollab/Density/Stronger/Atkinson/ShortDivisorSource.lean`; 110 source lines; SHA-256 `646a8d2cc5477e5c6ca0d1a01d2573a3d3728be858bfda856c8b7ef96ba91cb7`.

- `exists_zetaSquareGaussianMean_short_approximation` at line 27
- `exists_zetaSquarePhysicalGaussian_short_approximation` at line 67
- `exists_zetaSquareLocalMean_le_short_divisor` at line 81

### MathCollab.Density.Stronger.Atkinson.ShortDivisorGeometry

File: `lean/MathCollab/Density/Stronger/Atkinson/ShortDivisorGeometry.lean`; 118 source lines; SHA-256 `95ee06c88915bfb040353c210d8dd3a086b709a8bfcf1f572c429a86c0af076a`.

- `exp_sub_one_le_two_mul` at line 25
- `zetaQuadraticDivisorBand_abs_sub_center_le` at line 33
- `exists_zetaQuadraticDivisorBand_physical_bounds` at line 51
- `zetaShortDivisorTestFunction` at line 94
- `zetaQuadraticDivisorTerm_eq_testFunction` at line 100
- `zetaShortQuadraticDivisorSum_eq_divisor_test` at line 112

### MathCollab.Density.Stronger.Atkinson.DivisorTestSmooth

File: `lean/MathCollab/Density/Stronger/Atkinson/DivisorTestSmooth.lean`; 66 source lines; SHA-256 `a32073bfce786988eeca7d55540c8d90f0dba9e44b8c197e0c8bd9085aeb9850`.

- `contDiff_zetaGaussianQuadraticIntegral` at line 26
- `contDiffAt_ofReal_cpow_positive` at line 37
- `contDiffAt_zetaShortDivisorTestFunction` at line 48
- `contDiffOn_zetaShortDivisorTestFunction` at line 62

### MathCollab.Density.Stronger.Atkinson.DivisorBandCutoff

File: `lean/MathCollab/Density/Stronger/Atkinson/DivisorBandCutoff.lean`; 100 source lines; SHA-256 `1d32dab35871c7a19bb24919fa5b83e1d57f95c44d19752321a5d4696d703d54`.

- `zetaBandCutoff` at line 26
- `zetaBandCutoff_nonneg` at line 30
- `zetaBandCutoff_le_one` at line 33
- `contDiff_zetaBandCutoff` at line 37
- `zetaBandCutoff_eq_one` at line 41
- `zetaBandCutoff_eq_zero_left` at line 47
- `zetaBandCutoff_eq_zero_right` at line 53
- `support_zetaBandCutoff` at line 59
- `zetaDivisorBandEdge` at line 68
- `zetaDivisorBandCutoff` at line 70
- `zetaDivisorBandEdge_pos` at line 74
- `zetaDivisorBandEdge_strictMono` at line 77
- `zetaDivisorBandCutoff_eq_one` at line 84
- `support_zetaDivisorBandCutoff` at line 91
- `contDiff_zetaDivisorBandCutoff` at line 97

### MathCollab.Density.Stronger.Atkinson.VoronoiTest

File: `lean/MathCollab/Density/Stronger/Atkinson/VoronoiTest.lean`; 40 source lines; SHA-256 `b7e240faeb36cdf02e6656f8f78ac9aa5fbc21bc0c104c71c58daed66341d2fc`.

- `DFIVoronoiTestFunction` at line 22
- `DFIVoronoiTestFunction.continuous` at line 32
- `DFIVoronoiTestFunction.hasCompactSupport` at line 36

### MathCollab.Density.Stronger.Atkinson.SmoothDivisorTest

File: `lean/MathCollab/Density/Stronger/Atkinson/SmoothDivisorTest.lean`; 106 source lines; SHA-256 `4e660049b14936807226209d877c4173a530a491e6d67fff2cef029862fdd687`.

- `zetaSmoothDivisorTest` at line 27
- `zetaSmoothDivisorSum` at line 30
- `zetaSmoothDivisorTest_eq_zero_left` at line 33
- `support_zetaSmoothDivisorTest` at line 41
- `contDiff_zetaSmoothDivisorTest` at line 50
- `zetaSmoothDivisorVoronoiTest` at line 64
- `zetaSmoothDivisorTerm_eq_cutoff` at line 74
- `norm_zetaSmoothDivisorTerm_le` at line 83
- `summable_zetaSmoothDivisorTerm` at line 91
- `zetaSmoothDivisorTerm_eq_on_band` at line 97

### MathCollab.Density.Stronger.Atkinson.SmoothDivisorSupport

File: `lean/MathCollab/Density/Stronger/Atkinson/SmoothDivisorSupport.lean`; 73 source lines; SHA-256 `6328cb585ce093e8ee3f571ed952635b39635a9a846162fa5edd4fa58c436779`.

- `zetaDivisorBandEdge_outer_bounds` at line 25
- `support_zetaSmoothDivisorTest_physical` at line 45
- `eventually_zetaSmoothDivisorTest_support_physical` at line 59

### MathCollab.Density.Stronger.Atkinson.SmoothDivisorMass

File: `lean/MathCollab/Density/Stronger/Atkinson/SmoothDivisorMass.lean`; 104 source lines; SHA-256 `6b30aeb45e6874e44f6c018641c17036f4dcc2b27356ad4da9d6b5c06104ee45`.

- `exists_norm_zetaShortDivisorTestFunction_le` at line 25
- `exists_norm_zetaSmoothDivisorTest_le` at line 53
- `integrable_zetaSmoothDivisorTest` at line 70
- `zetaSmoothDivisorTest_integral_norm_eq_physical` at line 75
- `exists_integral_norm_zetaSmoothDivisorTest_le` at line 87

### MathCollab.Density.Stronger.Atkinson.DivisorLatticePhase

File: `lean/MathCollab/Density/Stronger/Atkinson/DivisorLatticePhase.lean`; 83 source lines; SHA-256 `330079b34c4538bf5e7b8150febaa69498f00611c3e03d4606e284ad8d0cfe70`.

- `zetaDivisorLatticePhase` at line 25
- `zetaAtkinsonDivisorTest` at line 27
- `norm_zetaDivisorLatticePhase` at line 30
- `zetaDivisorLatticePhase_nat` at line 33
- `contDiff_zetaDivisorLatticePhase` at line 40
- `norm_zetaAtkinsonDivisorTest` at line 46
- `zetaAtkinsonDivisorTest_nat` at line 50
- `support_zetaAtkinsonDivisorTest` at line 54
- `contDiff_zetaAtkinsonDivisorTest` at line 61
- `zetaAtkinsonDivisorVoronoiTest` at line 65
- `zetaSmoothDivisorSum_eq_atkinson_test` at line 77

### MathCollab.Density.Stronger.Atkinson.BesselK0

File: `lean/MathCollab/Density/Stronger/Atkinson/BesselK0.lean`; 114 source lines; SHA-256 `3d272a6817daf2d0a5f6d53646c4d648054e84b98ccbd38b8dc0c18a48f6440c`.

- `dfiBesselK0` at line 25
- `one_add_sq_div_two_le_cosh` at line 29
- `dfiBesselK0_integrand_le_gaussian` at line 43
- `integrableOn_dfiBesselK0_integrand` at line 56
- `abs_dfiBesselK0_le` at line 70
- `abs_dfiBesselK0_le_two_div_sqrt` at line 89

### MathCollab.Density.Stronger.Atkinson.BesselY0

File: `lean/MathCollab/Density/Stronger/Atkinson/BesselY0.lean`; 86 source lines; SHA-256 `5c672c57815b34ca1621a9666269cb5b16f4b3d89104579e81887a45318dcdf3`.

- `dfiBesselY0Tail` at line 25
- `dfiBesselY0Osc` at line 33
- `dfiBesselY0` at line 43
- `integrableOn_dfiBesselY0Tail_integrand` at line 47
- `intervalIntegrable_dfiBesselY0Osc_integrand` at line 80

### MathCollab.Density.Stronger.Atkinson.AtkinsonVoronoiTerms

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonVoronoiTerms.lean`; 38 source lines; SHA-256 `06b4e17a9ec3e4045e74a5e96c057e017e5e034b00e562998a500c509aa62d75`.

- `zetaAtkinsonVoronoiMain` at line 23
- `zetaAtkinsonBesselMinus` at line 27
- `zetaAtkinsonBesselPlusTerm` at line 32
- `zetaAtkinsonBesselPlus` at line 36

### MathCollab.Density.Stronger.Atkinson.BesselK0Decay

File: `lean/MathCollab/Density/Stronger/Atkinson/BesselK0Decay.lean`; 106 source lines; SHA-256 `35e109e3f38de1a97dc90826d8aa11efab1ef5dfb84bc785a92f3685619844be`.

- `dfiBesselK0_nonneg` at line 21
- `dfiBesselK0_le_exp_mul_half` at line 24
- `abs_dfiBesselK0_exp_le` at line 37
- `exp_neg_le_factorial_div_pow` at line 49
- `zetaBesselK0PowerConstant` at line 59
- `zetaBesselK0PowerConstant_pos` at line 62
- `abs_dfiBesselK0_pow_le` at line 66
- `abs_dfiBesselK0_source_le` at line 81

### MathCollab.Density.Stronger.Atkinson.BesselK0SourceIntegral

File: `lean/MathCollab/Density/Stronger/Atkinson/BesselK0SourceIntegral.lean`; 90 source lines; SHA-256 `5fd636b29e68ea4c6adbf753950697ecd1b84109b1fa49d0b3b66e6b5ffb2eed`.

- `zetaBesselK0SourceIntegrand` at line 23
- `stronglyMeasurable_dfiBesselK0` at line 26
- `norm_zetaBesselK0SourceIntegrand_le` at line 31
- `integrable_zetaBesselK0SourceIntegrand` at line 48
- `norm_integral_zetaBesselK0SourceIntegrand_le` at line 60
- `exists_norm_integral_zetaBesselK0SourceIntegrand_le` at line 74

### MathCollab.Density.Stronger.Atkinson.AtkinsonK0Integral

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonK0Integral.lean`; 77 source lines; SHA-256 `93cafaf7d81560105ffc6b8b3c32fc06eab190c4a3337d60f930fe281437bd94`.

- `norm_zetaAtkinsonK0_integrand` at line 22
- `integrable_zetaAtkinsonK0_integrand` at line 28
- `norm_integral_zetaAtkinsonK0_le` at line 40
- `exists_norm_integral_zetaAtkinsonK0_le` at line 60

### MathCollab.Density.Stronger.Atkinson.AtkinsonK0Series

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonK0Series.lean`; 92 source lines; SHA-256 `eb46848aacec96bc118ed304fad4960d277d1702e542f3ddb772aa2acba663f8`.

- `norm_divisorDirichletTerm_two` at line 22
- `exists_norm_zetaAtkinsonBesselPlusTerm_le` at line 29
- `summable_zetaAtkinsonBesselPlusTerm` at line 54
- `hasSum_zetaAtkinsonBesselPlusTerm` at line 62
- `exists_norm_zetaAtkinsonBesselPlus_le` at line 68

### MathCollab.Density.Stronger.Atkinson.AtkinsonK0Scales

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonK0Scales.lean`; 76 source lines; SHA-256 `8ad2d6d5c8bfa2a588a1ccc9bdd378f08157360cb6e49439cf78eafdd98f34b3`.

- `besselK0_source_power_absorb` at line 22
- `exists_norm_zetaAtkinsonBesselPlus_le_mul_G` at line 37
- `exists_zetaAtkinsonBesselPlus_powerSaving` at line 49

### MathCollab.Density.Stronger.Atkinson.VoronoiInverseWeights

File: `lean/MathCollab/Density/Stronger/Atkinson/VoronoiInverseWeights.lean`; 113 source lines; SHA-256 `fe9768ae87187aa7290970e72b7da8ab1074e2254beca7d9a83e73546efc509e`.

- `dfiVoronoiInvWeight` at line 24
- `DFIVoronoiTestFunction.invWeight` at line 28
- `DFIVoronoiTestFunction.mellin_invWeight_add_one` at line 54
- `dfiVoronoiInvWeightIterate` at line 76
- `dfiVoronoiInvWeightIterate_zero` at line 82
- `dfiVoronoiInvWeightIterate_succ` at line 86
- `DFIVoronoiTestFunction.invWeightIterate` at line 92
- `DFIVoronoiTestFunction.mellin_invWeightIterate_add_nat` at line 102

### MathCollab.Density.Stronger.Atkinson.VoronoiMellinKernel

File: `lean/MathCollab/Density/Stronger/Atkinson/VoronoiMellinKernel.lean`; 165 source lines; SHA-256 `b46d3b8d2de48e6d5653107102dabe20248931b37c93810fc55adb818f6d72b9`.

- `dfiVoronoiMellinKernel` at line 27
- `DFIVoronoiTestFunction.contDiff_mellinKernel` at line 31
- `DFIVoronoiTestFunction.hasCompactSupport_mellinKernel` at line 42
- `dfiVoronoiMellinKernelSchwartz` at line 68
- `DFIVoronoiTestFunction.mellinKernelSchwartz_apply` at line 74
- `DFIVoronoiTestFunction.mellin_eq_fourier_mellinKernel` at line 79
- `DFIVoronoiTestFunction.verticalIntegrable_mellin` at line 95
- `DFIVoronoiTestFunction.integrable_sqWeight_norm_mellin` at line 112

### MathCollab.Density.Stronger.Atkinson.VoronoiMellinInversion

File: `lean/MathCollab/Density/Stronger/Atkinson/VoronoiMellinInversion.lean`; 96 source lines; SHA-256 `114dad04c5995b4a3f5c04479444723a6331e6b68bdcf1c4383a2c613f3f7108`.

- `DFIVoronoiTestFunction.eventuallyEq_zero_atTop` at line 23
- `DFIVoronoiTestFunction.eventuallyEq_zero_atZero` at line 31
- `DFIVoronoiTestFunction.isBigO_atTop` at line 43
- `DFIVoronoiTestFunction.isBigO_atZero` at line 49
- `DFIVoronoiTestFunction.mellinConvergent` at line 57
- `DFIVoronoiTestFunction.mellinInversion` at line 67
- `DFIVoronoiTestFunction.mellin_hasDerivAt_one` at line 77
- `mellin_apply_one` at line 86
- `mellin_log_smul_apply_one` at line 90

### MathCollab.Density.Stronger.Atkinson.VoronoiMellinDecay

File: `lean/MathCollab/Density/Stronger/Atkinson/VoronoiMellinDecay.lean`; 344 source lines; SHA-256 `11b065cbeaaa36fd1c07edd9d4ae2f5e2b88135b14a3f98063a45b317bd1cffa`.

- `DFIVoronoiTestFunction.mellin_polynomial_decay` at line 26
- `DFIVoronoiTestFunction.exists_mellin_interval_bound` at line 62
- `DFIVoronoiTestFunction.exists_mellin_one_add_abs_pow_line_bound` at line 114
- `DFIVoronoiTestFunction.exists_mellin_strip_bound` at line 141
- `DFIVoronoiTestFunction.differentiable_mellin` at line 148
- `DFIVoronoiTestFunction.exists_mellin_pow_boundary_bound` at line 159
- `DFIVoronoiTestFunction.exists_mellin_pow_strip_bound` at line 203
- `DFIVoronoiTestFunction.exists_mellin_weighted_strip_bound` at line 319

### MathCollab.Density.Stronger.PointMean.DoublePole

File: `lean/MathCollab/Density/Stronger/PointMean/DoublePole.lean`; 218 source lines; SHA-256 `802d7a73534be7cb3817d9c03a7a16936a01e0c3fa6b69de044e4a420b5e664a`.

- `hasDerivAt_ofReal` at line 25
- `hIntegral_const_div_sq` at line 29
- `vIntegral_const_div_sq` at line 63
- `rectangleIntegral'_const_div_sq_eq_zero` at line 109
- `rectangleIntegral'_div_sq_eq_deriv` at line 131

### MathCollab.Density.Stronger.Atkinson.OrdinaryDivisorResidue

File: `lean/MathCollab/Density/Stronger/Atkinson/OrdinaryDivisorResidue.lean`; 99 source lines; SHA-256 `0b9314628d41c4718f371bbee7eff0de0d411045f20009d6c3be2d3eb7fffa4e`.

- `ordinaryDivisorMellinIntegrand` at line 24
- `ordinaryDivisorMellinNumerator` at line 27
- `ordinaryDivisorVoronoiMain` at line 30
- `ordinaryDivisorMellinIntegrand_eq_poleCleared` at line 33
- `DFIVoronoiTestFunction.differentiable_ordinaryDivisorMellinNumerator` at line 40
- `ordinaryDivisorMellinNumerator_one` at line 45
- `DFIVoronoiTestFunction.deriv_ordinaryDivisorMellinNumerator_one` at line 49
- `DFIVoronoiTestFunction.ordinaryDivisor_laurent_mainTerm` at line 61
- `DFIVoronoiTestFunction.ordinaryDivisor_finiteRectangle` at line 81

### MathCollab.Density.Stronger.PointMean.FiniteRectangle

File: `lean/MathCollab/Density/Stronger/PointMean/FiniteRectangle.lean`; 203 source lines; SHA-256 `17adfa5881039c1a9e2df61440921d74b0f1030760df79bc3dfeef8a2c25da9f`.

- `heathBrownZetaSquareMellinIntegrand` at line 29
- `heathBrownGammaPoleNumerator` at line 33
- `heathBrownGammaPoleNumerator_zero` at line 36
- `heathBrownZetaSquareMellinIntegrand_eq_gammaPoleCleared` at line 40
- `heathBrown_gammaPole_finite_rectangle` at line 51
- `exp_two_le_eight_heathBrown` at line 127
- `two_lt_log_of_ten_le` at line 131
- `heathBrownLemmaThreeDelta` at line 137
- `heathBrownLemmaThreeRadius` at line 140
- `heathBrownLemmaThreeDelta_pos` at line 143
- `heathBrownLemmaThreeDelta_lt_half` at line 149
- `heathBrownLemmaThreeRadius_pos` at line 154
- `heathBrownLemmaThree_finiteRectangle` at line 160
- `heathBrownLemmaThree_rectangle_eq_edges` at line 186

### MathCollab.Density.Stronger.PointMean.MovingPole

File: `lean/MathCollab/Density/Stronger/PointMean/MovingPole.lean`; 198 source lines; SHA-256 `bdb0ca532e8c14346d9339d1c6e543a1d49af12b2b4fef81871ec6c37f1e1cfb`.

- `riemannZetaPoleRemoved` at line 29
- `riemannZetaPoleRemoved_zero` at line 31
- `riemannZetaPoleRemoved_eq_mul_riemannZeta` at line 34
- `differentiable_riemannZetaPoleRemoved` at line 39
- `heathBrownMovingPole` at line 44
- `heathBrownMovingPoleNumerator` at line 47
- `heathBrownMovingPoleNumerator_at_pole` at line 51
- `heathBrownZetaSquareMellinIntegrand_eq_poleCleared` at line 58
- `differentiableOn_heathBrownMovingPoleNumerator` at line 77
- `heathBrownMovingPoleResidue` at line 97
- `heathBrownMovingPoleResidue_eq` at line 101
- `heathBrown_movingPole_finite_rectangle` at line 150

### MathCollab.Density.GammaMellin

File: `lean/MathCollab/Density/GammaMellin.lean`; 234 source lines; SHA-256 `a0666522654259ee38f6080811e23649f7f6389bdb2dfca9ddf055006652fbf8`.

- `norm_Gamma_le_realGamma_re` at line 24
- `im_sq_mul_norm_Gamma_vertical_le` at line 43
- `norm_Gamma_vertical_le_inv_one_add_sq` at line 88
- `verticalIntegrable_Gamma` at line 110
- `mellinConvergent_exp_neg` at line 131
- `verticalIntegrable_mellin_exp_neg` at line 138
- `mellinInv_GammaIntegral_eq_exp_neg` at line 150
- `mellinInv_Gamma_eq_exp_neg` at line 162
- `exp_neg_eq_gamma_vertical_integral` at line 183
- `cpow_neg_div_eq_reverse_cpow` at line 196
- `exp_neg_nat_div_eq_detector_right_line` at line 213

### MathCollab.Density.Stronger.PointMean.DivisorMellin

File: `lean/MathCollab/Density/Stronger/PointMean/DivisorMellin.lean`; 271 source lines; SHA-256 `c30034edc5edc5b3ac2a65f7d2a0aa98eae31c0d053e5115004a274b72810dbd`.

- `continuous_Gamma_two_vertical` at line 26
- `integrable_Gamma_two_vertical` at line 37
- `inverseMellin_exp_neg` at line 41
- `heathBrownSmoothedDivisorTerm` at line 49
- `heathBrownSmoothedDivisorSeries` at line 54
- `heathBrownDivisorMellinSeriesTerm` at line 57
- `heathBrownDivisorMellinIntegrand` at line 64
- `continuous_heathBrownDivisorMellinSeriesTerm` at line 69
- `norm_heathBrownDivisorMellinSeriesTerm_le` at line 87
- `integrable_heathBrownDivisorMellinSeriesTerm` at line 148
- `summable_integral_norm_heathBrownDivisorMellinSeriesTerm` at line 160
- `integral_heathBrownDivisorMellinSeriesTerm` at line 185
- `tsum_heathBrownDivisorMellinSeriesTerm_eq` at line 222
- `heathBrown_smoothed_divisor_eq_right_mellin` at line 249

### MathCollab.Density.Stronger.PointMean.MellinHorizontal

File: `lean/MathCollab/Density/Stronger/PointMean/MellinHorizontal.lean`; 261 source lines; SHA-256 `5e8d59434df1317a74db62ef222390fbaec478abae1cf44add4c52776bddcbf0`.

- `heathBrown_Gamma_wide_strip_decay` at line 27
- `heathBrown_Gamma_wide_strip_norm_le` at line 71
- `heathBrownMellinHorizontalSize` at line 79
- `norm_heathBrownZetaSquareMellinIntegrand_horizontal_le` at line 82
- `norm_heathBrownMellin_HIntegral'_le` at line 124
- `tendsto_heathBrownMellin_HIntegral'_zero` at line 167
- `tendsto_heathBrownMellin_HIntegral'_neg_zero` at line 211

### MathCollab.Density.GammaStrip

File: `lean/MathCollab/Density/GammaStrip.lean`; 370 source lines; SHA-256 `d294e8759b22dfa0a72d7d19c7493f90898ea1092f007a6f2c295e40f41f8871`.

- `centralPoint` at line 24
- `one_sub_centralPoint` at line 26
- `sin_pi_mul_centralPoint` at line 31
- `norm_Gamma_centralPoint_sq` at line 41
- `two_mul_cosh_abs` at line 56
- `exp_abs_le_two_mul_cosh` at line 61
- `norm_Gamma_centralPoint_le_exp` at line 66
- `norm_betaIntegral_le_real_integral` at line 104
- `betaIntegral_ofReal_eq_ofReal_integral` at line 127
- `real_beta_integral_eq_Gamma_div` at line 146
- `norm_betaIntegral_le_Gamma_div` at line 161
- `Gamma_half_sq` at line 172
- `one_le_Gamma_half` at line 179
- `Gamma_half_le_two` at line 183
- `Gamma_real_Icc_half_three_half_le_two` at line 187
- `stripPoint` at line 230
- `stripPoint_re` at line 232
- `stripPoint_im` at line 234
- `stripPoint_add_real` at line 236
- `Gamma_three_half_ge_half` at line 240
- `norm_Gamma_stripPoint_le_four_upper` at line 246
- `centralPoint_add_one` at line 285
- `norm_centralPoint_le_one_add_abs` at line 290
- `norm_Gamma_upperPoint_le_exp` at line 298
- `norm_Gamma_positive_strip_le_exp` at line 318
- `stripPoint_add_one` at line 331
- `norm_Gamma_compactStrip_le_exp` at line 337

### MathCollab.Density.Stronger.PointMean.GammaKernel

File: `lean/MathCollab/Density/Stronger/PointMean/GammaKernel.lean`; 150 source lines; SHA-256 `bc6ec68d8d14b6e4839c3add6c9438b0bc5155012b38753e3b7e4c04f79f51c2`.

- `norm_Gamma_half_vertical_le_exp` at line 26
- `add_one_mul_exp_neg_pi_half_le` at line 58
- `norm_Gamma_positive_strip_strong` at line 79
- `Gamma_displaced_strong_bound` at line 113
- `heathBrown_Gamma_shift_kernel_strong_bound` at line 138

### MathCollab.Density.Stronger.PointMean.MellinVertical

File: `lean/MathCollab/Density/Stronger/PointMean/MellinVertical.lean`; 400 source lines; SHA-256 `09744a09ba751584bc54dd01f10c771e718df7ba385b2c2485f13f5bc31448b9`.

- `exists_heathBrown_Gamma_shift_kernel_bound` at line 28
- `integrable_Gamma_two_vertical_for_zetaSquare` at line 42
- `ford_norm_eq_re_of_nonneg` at line 46
- `ford_norm_riemannZeta_le_real` at line 53
- `continuous_heathBrownZetaSquareMellinIntegrand_vertical` at line 86
- `integrable_abs_sq_mul_exp_neg_abs` at line 130
- `integrable_heathBrownZetaSquareMellinIntegrand_of_exp` at line 157
- `integrable_heathBrownZetaSquareMellinIntegrand_plus` at line 301
- `integrable_heathBrownZetaSquareMellinIntegrand_minus` at line 332
- `integrable_heathBrownZetaSquareMellinIntegrand_right` at line 364

### MathCollab.Density.Stronger.PointMean.MellinShift

File: `lean/MathCollab/Density/Stronger/PointMean/MellinShift.lean`; 305 source lines; SHA-256 `2787bbd6231b8a1e62d468e69cf8e0e1552e561e603523486cee2db5f9d93780`.

- `VerticalIntegral` at line 28
- `VerticalIntegral'` at line 31
- `pintz2023_RectangleIntegral'_eq_edges` at line 34
- `tendsto_rectangleIntegral'_vertical_sub` at line 49
- `verticalIntegral'_sub_eq_of_eventual_rectangle` at line 106
- `heathBrownIntermediateLine` at line 122
- `heathBrown_intermediateLine_pos` at line 125
- `heathBrown_intermediateLine_le_quarter` at line 131
- `heathBrown_movingPole_vertical_shift` at line 137
- `heathBrown_gammaPole_vertical_shift` at line 194
- `heathBrown_twoPole_vertical_shift` at line 255
- `heathBrownSmoothedDivisorSeries_eq_rightVertical` at line 268
- `heathBrown_zetaSquare_eq_smoothed_sub_residue_sub_leftVertical` at line 282

### MathCollab.Density.Stronger.Atkinson.VoronoiTransforms

File: `lean/MathCollab/Density/Stronger/Atkinson/VoronoiTransforms.lean`; 103 source lines; SHA-256 `a98e46fba7952bd6b4215ae79c0c227e19965b47b4794d9b53ff613b67186ea5`.

- `dfiPeriodicArchimedeanFactor` at line 21
- `differentiableAt_dfiPeriodicArchimedeanFactor_of_re_pos` at line 28
- `dfiVoronoiMinusMultiplier` at line 42
- `dfiVoronoiPlusMultiplier` at line 48
- `differentiableAt_dfiVoronoiMinusMultiplier_of_re_lt_one` at line 54
- `differentiableAt_dfiVoronoiPlusMultiplier_of_re_lt_one` at line 65
- `dfiVoronoiMinusTransform` at line 79
- `dfiVoronoiPlusTransform` at line 88
- `verticalIntegral'_eq_realIntegral` at line 96

### MathCollab.Density.Stronger.Atkinson.VoronoiZetaFunctional

File: `lean/MathCollab/Density/Stronger/Atkinson/VoronoiZetaFunctional.lean`; 63 source lines; SHA-256 `099f5b603dc315c0c729d4c0660bbd1a50d561ba968bb3d9a98d8a56d3b5bce0`.

- `four_mul_cos_half_sq` at line 21
- `riemannZeta_eq_voronoiFactor` at line 28
- `riemannZeta_sq_eq_voronoiMultipliers` at line 45

### MathCollab.Density.Stronger.Atkinson.VoronoiZetaGrowth

File: `lean/MathCollab/Density/Stronger/Atkinson/VoronoiZetaGrowth.lean`; 148 source lines; SHA-256 `c6dd56cf52f9604af19495ff21f09ede8d75aeebda8e8082eac7fbbe86c8b8b3`.

- `norm_Gamma_voronoi_strip_sharp` at line 22
- `norm_complex_cos_le_exp_abs_im` at line 53
- `norm_voronoiFactor_one_le` at line 69
- `norm_voronoiFactor_one_mul_cos_le` at line 84
- `norm_riemannZeta_voronoi_strip` at line 102

### MathCollab.Density.Stronger.Atkinson.VoronoiContourBounds

File: `lean/MathCollab/Density/Stronger/Atkinson/VoronoiContourBounds.lean`; 125 source lines; SHA-256 `8e080ac7538d5e097e84cff42becf42b3783e21d0a50e19dfb9849e8951367f4`.

- `DFIVoronoiTestFunction.exists_ordinaryDivisorMellin_strip_decay` at line 24
- `DFIVoronoiTestFunction.continuous_ordinaryDivisorMellin_vertical` at line 41
- `integrable_of_continuous_quadratic_tail` at line 58
- `DFIVoronoiTestFunction.integrable_ordinaryDivisorMellin_vertical` at line 76
- `DFIVoronoiTestFunction.ordinaryDivisor_horizontal_limits` at line 84

### MathCollab.Density.Stronger.Atkinson.OrdinaryDivisorMellin

File: `lean/MathCollab/Density/Stronger/Atkinson/OrdinaryDivisorMellin.lean`; 145 source lines; SHA-256 `71be846159ca187ac5d9992c2fb610c78aa04d124e9f24cdd30876deb67f347f`.

- `ordinaryDivisorMellinTerm` at line 25
- `DFIVoronoiTestFunction.integrable_ordinaryDivisorMellinTerm` at line 29
- `DFIVoronoiTestFunction.integral_norm_ordinaryDivisorMellinTerm` at line 54
- `DFIVoronoiTestFunction.summable_integral_norm_ordinaryDivisorMellinTerm` at line 71
- `divisorWeight_mul_mellinInv` at line 88
- `DFIVoronoiTestFunction.ordinaryDivisorSum_eq_zetaSquareMellinIntegral` at line 122

### MathCollab.Density.Stronger.Atkinson.OrdinaryDivisorContourShift

File: `lean/MathCollab/Density/Stronger/Atkinson/OrdinaryDivisorContourShift.lean`; 150 source lines; SHA-256 `2e507b0ac30628637df44d831ec5c069f3fb3ffb6990520ab354b2f8c751d44b`.

- `voronoi_tendsto_rectangleIntegral'_vertical_sub` at line 25
- `voronoi_verticalIntegral'_sub_eq_of_eventual_rectangle` at line 82
- `DFIVoronoiTestFunction.ordinaryDivisor_vertical_shift` at line 100
- `DFIVoronoiTestFunction.ordinaryDivisorSum_eq_main_add_left` at line 122
- `DFIVoronoiTestFunction.ordinaryDivisorSum_eq_main_add_reflected` at line 134

### MathCollab.Density.Stronger.Atkinson.OrdinaryDivisorDualSeries

File: `lean/MathCollab/Density/Stronger/Atkinson/OrdinaryDivisorDualSeries.lean`; 137 source lines; SHA-256 `7b39f24e33231889c51062cc924437c1dc717e852e508809c71b0b79b6f7820a`.

- `ordinaryDivisorDualTerm` at line 24
- `norm_divisorDirichletTerm_reflected` at line 28
- `continuous_divisorDirichletTerm_reflected` at line 34
- `integrable_ordinaryDivisorDualTerm` at line 45
- `integral_norm_ordinaryDivisorDualTerm` at line 53
- `summable_integral_norm_ordinaryDivisorDualTerm` at line 62
- `tsum_ordinaryDivisorDualTerm` at line 67
- `integrable_zetaSquare_dualMultiplier` at line 77
- `divisorWeight_mul_dualTransform` at line 99
- `summable_divisorWeight_dualTransform` at line 115
- `tsum_divisorWeight_dualTransform` at line 124

### MathCollab.Density.Stronger.Atkinson.VoronoiMultiplierBounds

File: `lean/MathCollab/Density/Stronger/Atkinson/VoronoiMultiplierBounds.lean`; 139 source lines; SHA-256 `4d0f870503819ee4c70ac8c9692f94a9899686d0ed64e80b261181b425ec52a0`.

- `norm_Gamma_voronoi_extended_strip` at line 21
- `norm_dfiPeriodicArchimedeanFactor_strip_le` at line 59
- `norm_dfiVoronoiMinusMultiplier_strip_le` at line 88
- `norm_dfiVoronoiPlusMultiplier_strip_le` at line 122

### MathCollab.Density.Stronger.Atkinson.OrdinaryDivisorVoronoi

File: `lean/MathCollab/Density/Stronger/Atkinson/OrdinaryDivisorVoronoi.lean`; 115 source lines; SHA-256 `af871e366ca7fd74a3edbdfa8599773b117301d002364fed840752f8793c0a0d`.

- `DFIVoronoiTestFunction.integrable_dualMultiplier_of_quadratic_bound` at line 27
- `DFIVoronoiTestFunction.integrable_voronoiMinusMultiplier` at line 46
- `DFIVoronoiTestFunction.integrable_voronoiPlusMultiplier` at line 59
- `DFIVoronoiTestFunction.summable_divisorWeight_voronoiMinus` at line 73
- `DFIVoronoiTestFunction.summable_divisorWeight_voronoiPlus` at line 80
- `ordinaryDivisorVoronoi_native` at line 88

### MathCollab.Density.Stronger.Atkinson.VoronoiMinusConvergence

File: `lean/MathCollab/Density/Stronger/Atkinson/VoronoiMinusConvergence.lean`; 133 source lines; SHA-256 `df7c98de2dfa2edce5dc2be4b68ac7d677a7da28e431a5c2c79727fecdba3b29`.

- `dfiVoronoiMinusIntegrand` at line 24
- `differentiableAt_dfiVoronoiMinusIntegrand` at line 27
- `norm_voronoiNatPower_le_one` at line 37
- `DFIVoronoiTestFunction.exists_minusIntegrand_strip_decay` at line 44
- `DFIVoronoiTestFunction.continuous_minusIntegrand_vertical` at line 69
- `DFIVoronoiTestFunction.integrable_minusIntegrand_vertical` at line 79
- `DFIVoronoiTestFunction.minusIntegrand_horizontal_limits` at line 94

### MathCollab.Density.Stronger.Atkinson.BesselMellinBeta

File: `lean/MathCollab/Density/Stronger/Atkinson/BesselMellinBeta.lean`; 345 source lines; SHA-256 `794a54d2c03605bdb92c1c74c136d41983cf5e0506d7a436e5a7a66d08f14a54`.

- `dfiBesselK0MellinSymbol` at line 26
- `dfiBesselY0MellinSymbol` at line 30
- `dfiBesselK0MellinSymbol_two_mul` at line 34
- `dfiBesselY0MellinSymbol_two_mul` at line 41
- `integral_cpow_mul_exp_neg_mul_Ioi_eq` at line 52
- `image_sq_Ioo_zero_one` at line 62
- `betaIntegral_eq_integral_Ioo` at line 78
- `betaIntegral_square_substitution` at line 87
- `abs_two_mul_smul_sq_cpow_neg_half` at line 110
- `integral_one_sub_sq_cpow_Ioo_eq_half_beta` at line 127
- `image_tanh_Ioi_zero` at line 150
- `hasDerivAt_tanh_recip_cosh_sq` at line 165
- `one_sub_tanh_sq_eq_inv_cosh_sq` at line 178
- `inv_sq_mul_inv_sq_cpow_sub_one` at line 185
- `tanh_jacobian_smul_one_sub_sq_cpow` at line 231
- `integral_cosh_cpow_neg_two_mul_Ioi_eq` at line 241
- `integrableOn_one_sub_sq_cpow_Ioo` at line 273
- `integrableOn_cosh_cpow_neg_two_mul_Ioi` at line 321

### MathCollab.Density.Stronger.Atkinson.BesselK0Convergence

File: `lean/MathCollab/Density/Stronger/Atkinson/BesselK0Convergence.lean`; 234 source lines; SHA-256 `a3a0ef156dca2dfdf3712997bd71381b67fcea03df0bd081b4959a5ab3f50da3`.

- `integrableOn_cpow_mul_exp_neg_mul_Ioi` at line 21
- `norm_cpow_mul_exp_neg_cosh` at line 43
- `integral_norm_cpow_mul_exp_neg_cosh_Ioi` at line 53
- `integrableOn_inv_cosh_rpow_Ioi` at line 71
- `integrableOn_dfiBesselK0_mellin_joint` at line 93
- `integral_inv_cosh_cpow_Ioi_eq` at line 141
- `dfiBesselK0_ofReal_eq_integral` at line 164
- `mellinConvergent_dfiBesselK0` at line 183
- `mellinConvergent_dfiBesselK0_mul_sqrt` at line 209

### MathCollab.Density.Stronger.Atkinson.BesselK0Mellin

File: `lean/MathCollab/Density/Stronger/Atkinson/BesselK0Mellin.lean`; 185 source lines; SHA-256 `3d01cd46785684fc7374a1f3fe6613ec616fa94882eda95b8b0758b74a2e6faa`.

- `integral_cpow_mul_dfiBesselK0_Ioi_eq_beta` at line 23
- `half_beta_mul_Gamma_eq_besselK0MellinSymbol` at line 71
- `integral_cpow_mul_dfiBesselK0_Ioi_eq` at line 139
- `mellin_dfiBesselK0_mul_sqrt` at line 150

### MathCollab.Density.Stronger.Atkinson.BesselComplexLaplace

File: `lean/MathCollab/Density/Stronger/Atkinson/BesselComplexLaplace.lean`; 203 source lines; SHA-256 `e2aacdf62302681171a2df6cb56efebe52de05f5b13f032ba2afae84a2e971a4`.

- `integrableOn_cpow_mul_cexp_neg_complex_mul_Ioi` at line 34
- `dfiComplexLaplace` at line 53
- `hasDerivAt_dfiComplexLaplace` at line 56
- `analyticOnNhd_dfiComplexLaplace` at line 134
- `dfiComplexLaplace_ofReal` at line 143
- `dfiComplexLaplace_eq` at line 163

### MathCollab.Density.Stronger.Atkinson.BesselY0Abel

File: `lean/MathCollab/Density/Stronger/Atkinson/BesselY0Abel.lean`; 214 source lines; SHA-256 `679151f0355e2488cbfde4e54ec57a89aaa3c1dfa08993aa11b744fde3ad3d6d`.

- `integral_cpow_mul_damped_cexp_Ioi` at line 31
- `integral_cpow_mul_damped_cexp_neg_Ioi` at line 54
- `integral_cpow_mul_damped_sin_Ioi` at line 77
- `tendsto_dfiDampedSineFactor` at line 150
- `dfiDampedSineFactor_limit_eq` at line 180

### MathCollab.Density.Stronger.Atkinson.BesselY0Beta

File: `lean/MathCollab/Density/Stronger/Atkinson/BesselY0Beta.lean`; 276 source lines; SHA-256 `238bdcb5ade8c8b749996fe4f6f227bcf516fbe8e319f52479c935668a82d482`.

- `image_sin_Ioo_zero_halfPi` at line 25
- `cos_mul_one_sub_sin_sq_cpow` at line 46
- `integral_cos_cpow_neg_eq_beta` at line 82
- `abs_two_mul_smul_sq_cpow_general` at line 114
- `integral_beta_tail_Ioo` at line 156
- `tanh_jacobian_beta_integrand` at line 172
- `integral_sinh_cpow_neg_Ioi_eq_beta` at line 200
- `image_sinh_Ioi_zero` at line 225
- `sinh_tail_jacobian` at line 234
- `integral_tail_power_eq_beta` at line 251

### MathCollab.Density.Stronger.Atkinson.NeumannContourKernel

File: `lean/MathCollab/Density/Stronger/Atkinson/NeumannContourKernel.lean`; 160 source lines; SHA-256 `cea8acf199ae482547a0608df1c9178fa73a3e9efcdbd880f7bc3875885bdc3e`.

- `neumannContourKernel` at line 35
- `differentiableAt_neumannContourKernel` at line 39
- `norm_neumannContourKernel` at line 46
- `neumannContourKernel_slit_vertical` at line 60
- `norm_neumannContourKernel_vertical_le` at line 74
- `norm_neumannContourKernel_horizontal_le` at line 96
- `continuousOn_neumannContourKernel_vertical` at line 117
- `integrableOn_neumannContourKernel_vertical` at line 126
- `neumannContourKernel_finite_rectangle` at line 138

### MathCollab.Density.Stronger.Atkinson.NeumannContourShift

File: `lean/MathCollab/Density/Stronger/Atkinson/NeumannContourShift.lean`; 82 source lines; SHA-256 `6f650a17ae5417604b19d5c812465d2b2b0d703bc06f644da54c48fe288dc015`.

- `neumannVerticalIntegral` at line 33
- `norm_neumannContourKernel_horizontal_integral_le` at line 36
- `tendsto_neumannContourKernel_horizontal_integral` at line 46
- `neumannContourKernel_infinite_rectangle` at line 57

### MathCollab.Density.Stronger.Atkinson.NeumannSchlafliEntry

File: `lean/MathCollab/Density/Stronger/Atkinson/NeumannSchlafliEntry.lean`; 147 source lines; SHA-256 `b02238f19862a950bb294a8e3497390aef042c51ec33deb153109a2961dfd771`.

- `continuousAt_neumannVerticalIntegral` at line 33
- `neumannContourHalfPowers_imaginary_axis` at line 52
- `neumannContourKernel_imaginary_axis` at line 77
- `neumannVerticalIntegral_zero_eq_tail` at line 90
- `neumannContourHalfPowers_sine` at line 96
- `neumannContourKernel_angular_change` at line 120

### MathCollab.Density.Stronger.Atkinson.NeumannLaplaceRepresentation

File: `lean/MathCollab/Density/Stronger/Atkinson/NeumannLaplaceRepresentation.lean`; 92 source lines; SHA-256 `f0ca18914aa27065d506688557f43f0f387bb827323dadc471fa7d716a64be81`.

- `neumann_sine_integral_eq_cosine` at line 34
- `neumann_schlafli_complex_identity` at line 42
- `dfiBesselY0_eq_neumannVerticalIntegral` at line 75

### MathCollab.Density.Stronger.Atkinson.NeumannLaplaceAmplitude

File: `lean/MathCollab/Density/Stronger/Atkinson/NeumannLaplaceAmplitude.lean`; 111 source lines; SHA-256 `d2759bac9f213bcbc20529ef954ecaaf7d681db183bd6707c9366ec745ffb004`.

- `neumannLaplaceAmplitude` at line 33
- `neumannLaplaceAmplitude_zero` at line 36
- `norm_neumannLaplaceAmplitude_le_one` at line 39
- `neumann_sqrt_re_ge_one` at line 51
- `norm_neumannLaplaceAmplitude_sub_linear_le` at line 60

### MathCollab.Density.Stronger.Atkinson.NeumannRayFactorization

File: `lean/MathCollab/Density/Stronger/Atkinson/NeumannRayFactorization.lean`; 126 source lines; SHA-256 `2da62086fe821a03adfce4d5e14983ccd190a934b33b9996040bfea12c7dc50d`.

- `neumann_cpow_positive_real_mul` at line 32
- `neumannRayCoefficient` at line 41
- `neumannLaplaceIntegrand` at line 43
- `neumannLaplaceIntegral` at line 46
- `continuous_neumannLaplaceAmplitude` at line 49
- `neumannContourKernel_unit_ray` at line 57
- `norm_neumannLaplaceIntegrand_le` at line 91
- `integrableOn_neumannLaplaceIntegrand` at line 97
- `neumannVerticalIntegral_one_eq_laplace` at line 112
- `dfiBesselY0_eq_neumannLaplaceIntegral` at line 121

### MathCollab.Density.Stronger.Atkinson.NeumannLaplaceMoments

File: `lean/MathCollab/Density/Stronger/Atkinson/NeumannLaplaceMoments.lean`; 115 source lines; SHA-256 `46b45f6ee68f735c8a785e062bedee8fbc4c3a0973541f13f137f905723b12af`.

- `neumannLaplaceMomentIntegrand` at line 31
- `neumannLaplaceMoment` at line 34
- `integrableOn_neumannLaplaceMomentIntegrand` at line 37
- `neumannLaplaceMomentIntegrand_nonneg` at line 44
- `neumannLaplaceMomentIntegrand_eq_mul` at line 49
- `neumannLaplaceMoment_eq_gamma` at line 57
- `neumannLaplaceMoment_zero` at line 67
- `neumannLaplaceMoment_one` at line 72
- `neumannLaplaceMoment_two` at line 81
- `neumannRayCoefficient_eq` at line 93
- `norm_neumannRayCoefficient_le_one` at line 109

### MathCollab.Density.Stronger.Atkinson.BesselY0Bounds

File: `lean/MathCollab/Density/Stronger/Atkinson/BesselY0Bounds.lean`; 62 source lines; SHA-256 `f1c050dd7d84f8f033e4bc26b63b28adb6b1b79bae02f6b719b7d4195790ab95`.

- `norm_neumannLaplaceIntegral_le` at line 20
- `abs_dfiBesselY0_le_seven_div_sqrt` at line 32

### MathCollab.Density.Stronger.Atkinson.BesselY0Near

File: `lean/MathCollab/Density/Stronger/Atkinson/BesselY0Near.lean`; 77 source lines; SHA-256 `535a6d9916ed5ab83cf1971b0a5c109511cf4f5bea21ff6eef0a397eddecbe2e`.

- `abs_dfiBesselY0Tail_le_quarter` at line 21

### MathCollab.Density.Stronger.Atkinson.BesselY0Mellin

File: `lean/MathCollab/Density/Stronger/Atkinson/BesselY0Mellin.lean`; 1485 source lines; SHA-256 `6bf764de34df2989fed05c2db522cc23d97acc8d343ed97dd6377d7fb68231a0`.

- `probe_dfiBesselY0Osc_eq_integral_sin_real` at line 23
- `probe_dfiBesselY0Osc_eq_integral_sin` at line 51
- `probe_abs_dfiBesselY0Osc_le_halfPi` at line 56
- `probe_aestronglyMeasurable_dfiBesselY0Osc` at line 69
- `probe_aestronglyMeasurable_dfiBesselY0Tail` at line 85
- `probe_aestronglyMeasurable_dfiBesselY0` at line 109
- `probe_abs_dfiBesselY0_le_quarter_near` at line 120
- `probe_mellinConvergent_dfiBesselY0` at line 153
- `probe_tendsto_damped_dfiBesselY0_mellin` at line 243
- `probe_integrableOn_cos_cpow_neg_Ioc` at line 303
- `probe_integrableOn_cos_rpow_neg_Ioc` at line 339
- `probe_integrableOn_tail_rpow_div_sqrt` at line 358
- `probe_tendsto_damped_tail_factor` at line 411
- `probe_norm_damped_sineFactor_le` at line 478
- `probe_tendsto_damped_osc_factor` at line 538
- `probe_integrableOn_damped_osc_joint` at line 618
- `probe_integrableOn_eps_add_rpow_div_sqrt` at line 683
- `probe_integrableOn_damped_tail_joint` at line 747
- `probe_integral_cpow_mul_damped_y0Osc_Ioi` at line 886
- `probe_integral_cpow_mul_damped_y0Tail_Ioi` at line 940
- `probe_integrableOn_damped_y0Osc_mellin` at line 1051
- `probe_integrableOn_damped_y0Tail_mellin` at line 1078
- `probe_integral_cpow_mul_damped_y0_Ioi` at line 1114
- `probe_integral_cpow_mul_dfiBesselY0_Ioi_eq_beta` at line 1170
- `probe_y0_beta_combination_eq_k0_beta` at line 1229
- `probe_integral_cpow_mul_dfiBesselY0_Ioi_eq` at line 1372
- `mellinConvergent_dfiBesselY0_mul_sqrt` at line 1418
- `mellin_dfiBesselY0_mul_sqrt` at line 1448

### MathCollab.Density.Stronger.Atkinson.BesselMellinPairing

File: `lean/MathCollab/Density/Stronger/Atkinson/BesselMellinPairing.lean`; 236 source lines; SHA-256 `7ce789dc7f2a646df4e4bdfd984bd56498310c1d98f2aae98737bd8cdfb1b315`.

- `MellinConvergent.aestronglyMeasurable_positive` at line 36
- `MellinConvergent.integrableOn_rpow_mul_norm` at line 64
- `DFIVoronoiTestFunction.continuous_mellin_vertical` at line 82
- `verticalIntegral'_mellin_mul_mellin_one_sub` at line 98

### MathCollab.Density.Stronger.Atkinson.BesselTransforms

File: `lean/MathCollab/Density/Stronger/Atkinson/BesselTransforms.lean`; 37 source lines; SHA-256 `61fa39fb665a67c777c6dda9af807108be56109ca448bcbf54361e234999c9eb`.

- `dfiVoronoiPlusBesselTransform` at line 21
- `dfiVoronoiMinusBesselTransform` at line 30

### MathCollab.Density.Stronger.Atkinson.BesselTransformBridge

File: `lean/MathCollab/Density/Stronger/Atkinson/BesselTransformBridge.lean`; 408 source lines; SHA-256 `82dce9eca918340c94991d1f6410cff3ab440cc5ee25d0b8fb7e13061de78c09`.

- `dfiVoronoiPlusMultiplier_eq_scaled_K0_mellin` at line 22
- `verticalIntegral'_congr_line` at line 176
- `verticalIntegral'_const_mul_bridge` at line 188
- `dfiVoronoiPlusTransform_mellin_eq_bessel` at line 198
- `dfiBesselY0MellinSymbol_eq_cos_mul_K0` at line 268
- `dfiVoronoiMinusMultiplier_eq_scaled_Y0_symbol` at line 288
- `verticalIntegral_dfiVoronoiMinus_mellin_thirteenSixteenths_eq_bessel` at line 331

### MathCollab.Density.Stronger.Atkinson.VoronoiMinusTransport

File: `lean/MathCollab/Density/Stronger/Atkinson/VoronoiMinusTransport.lean`; 139 source lines; SHA-256 `3e27adf9589cdc3ce209462241b2d93ac478db382bbfebc13e34fdd11b0b0ebf`.

- `tendsto_rectangleIntegral'_vertical_sub` at line 25
- `verticalIntegral'_sub_eq_of_eventual_rectangle` at line 82
- `DFIVoronoiTestFunction.minusIntegrand_finite_rectangle` at line 98
- `DFIVoronoiTestFunction.minusTransform_eq_thirteenSixteenths` at line 116
- `dfiVoronoiMinusTransform_mellin_eq_bessel` at line 133

### MathCollab.Density.Stronger.Atkinson.SmoothDivisorTail

File: `lean/MathCollab/Density/Stronger/Atkinson/SmoothDivisorTail.lean`; 89 source lines; SHA-256 `e6d6a2a86e226df407e2e94d2f5179cc21f241fe7f51f8f08dcd7ff15e5e4fcb`.

- `norm_zetaSmoothDivisorSum_sub_short_le` at line 25
- `exists_norm_zetaSmoothDivisorSum_sub_short_le` at line 54
- `exists_zetaSmoothDivisor_log_tail_bound` at line 69

### MathCollab.Density.Stronger.Atkinson.SmoothDivisorSource

File: `lean/MathCollab/Density/Stronger/Atkinson/SmoothDivisorSource.lean`; 103 source lines; SHA-256 `54f1c415c33390020690cc9597cedd667e37fc683dcfcc2d238f9c2ae73f003d`.

- `exists_zetaSquareGaussianMean_smooth_approximation` at line 25
- `exists_zetaSquareLocalMean_le_smooth_divisor` at line 59
- `exists_zetaSquarePhysicalGaussian_smooth_approximation` at line 92

### MathCollab.Density.Stronger.Atkinson.ZetaAtkinsonVoronoi

File: `lean/MathCollab/Density/Stronger/Atkinson/ZetaAtkinsonVoronoi.lean`; 87 source lines; SHA-256 `14f4a95a69b0ba7a80ea1698460a2de1f1da5edfa5c579347512ce0e4f3535c3`.

- `ordinaryDivisorVoronoi_bessel` at line 25
- `zetaSmoothDivisorSum_eq_atkinson_bessel` at line 51
- `exists_zetaSquarePhysicalGaussian_atkinson_approximation` at line 58
- `exists_zetaSquareLocalMean_le_atkinson_bessel` at line 73

### MathCollab.Density.Stronger.Atkinson.ZetaAtkinsonReducedSource

File: `lean/MathCollab/Density/Stronger/Atkinson/ZetaAtkinsonReducedSource.lean`; 98 source lines; SHA-256 `e003c3704b51eb5a6e1a4c606a7b67f601bb0c1a73bb140a514e1ce0def3ec86`.

- `exists_zetaSquarePhysicalGaussian_atkinson_reduced` at line 35
- `exists_zetaSquareLocalMean_le_atkinson_reduced` at line 66

### MathCollab.Density.Stronger.Atkinson.IntervalAmplitudeBounds

File: `lean/MathCollab/Density/Stronger/Atkinson/IntervalAmplitudeBounds.lean`; 180 source lines; SHA-256 `e913ae55077b2b0bee1a2e31cc13cb0871e869e046765f5df17b5856ac29c3ec`.

- `IntervalC1Bound` at line 33
- `IntervalC1Bound.derivative_integrable` at line 39
- `IntervalC1Bound.mono` at line 47
- `intervalC1Bound_const` at line 52
- `IntervalC1Bound.mul` at line 57
- `intervalC1Bound_ofReal_of_deriv_nonneg` at line 97
- `intervalC1Bound_ofReal_of_deriv_nonpos` at line 129
- `IntervalC1Bound.join` at line 163

### MathCollab.Density.Stronger.Atkinson.FiniteWeightVariation

File: `lean/MathCollab/Density/Stronger/Atkinson/FiniteWeightVariation.lean`; 204 source lines; SHA-256 `851ee9d1da8c36da27c4603101fe3cb81f5c3a7e9e9d517f03d214991c99503d`.

- `FiniteVariationBound` at line 23
- `FiniteVariationBound.mono` at line 28
- `FiniteVariationBound.congr` at line 33
- `finiteVariationBound_const` at line 44
- `FiniteVariationBound.mul` at line 49
- `finiteVariationBound_of_monotone` at line 75
- `finiteVariationBound_of_antitone` at line 94
- `finiteVariationBound_of_envelope` at line 114
- `finiteVariationBound_comp_of_lipschitz` at line 126
- `norm_sum_mul_le_discrete_parts` at line 165
- `FiniteVariationBound.norm_sum_mul_le` at line 177

### MathCollab.Density.Stronger.Atkinson.AtkinsonCutoffVariation

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonCutoffVariation.lean`; 77 source lines; SHA-256 `85215c30e6850fcfe36deb2c80fb1fddfbbef3d2f6923e202da8c612605d9ad0`.

- `intervalC1Bound_zetaBandCutoff` at line 24
- `intervalC1Bound_zetaDivisorBandCutoff` at line 45
- `finiteVariationBound_zetaBandCutoff_sample` at line 51

### MathCollab.Density.Stronger.Atkinson.MainElementaryWeights

File: `lean/MathCollab/Density/Stronger/Atkinson/MainElementaryWeights.lean`; 65 source lines; SHA-256 `7afc8765396079fced2be055a22e204d6f8cb6fedfec6897722bc012b037426c`.

- `intervalC1Bound_source_sqrt` at line 22
- `mul_exp_neg_half_log_eq_sqrt` at line 32
- `intervalC1Bound_source_log` at line 43
- `sourceLogWeight_le_three_log` at line 61

### MathCollab.Density.Stronger.Atkinson.ZetaAtkinsonPhase

File: `lean/MathCollab/Density/Stronger/Atkinson/ZetaAtkinsonPhase.lean`; 59 source lines; SHA-256 `4cc7b24a548798ffcd4fcf99a0715dd4b1dfde92515f31d84eab425c35310763`.

- `zetaAtkinsonPhase` at line 27
- `hasDerivAt_zetaAtkinsonPhase` at line 30
- `hasDerivAt_zetaAtkinsonPhaseDerivative` at line 40
- `hasDerivAt_deriv_zetaAtkinsonPhase` at line 52

### MathCollab.Density.Stronger.Atkinson.AtkinsonAmplitude

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonAmplitude.lean`; 64 source lines; SHA-256 `42c13f3cd6196b261b8e951327232826fa7d3a36f50d2edf3f6f77fcfda12fcd`.

- `zetaAtkinsonAmplitude` at line 23
- `ofReal_cpow_critical_conjugate` at line 29
- `zetaAtkinsonDivisorTest_mul_carrier` at line 38
- `zetaAtkinsonDivisorTest_eq_amplitude_phase` at line 57

### MathCollab.Density.Stronger.Atkinson.IntervalSecondDerivativeBounds

File: `lean/MathCollab/Density/Stronger/Atkinson/IntervalSecondDerivativeBounds.lean`; 133 source lines; SHA-256 `bca3df74c4046d5678b4ed6ac168e5ad522e67e0c7e4f56bb8f49900f7eaf371`.

- `IntervalC2Bound` at line 24
- `intervalC2Bound_const` at line 32
- `IntervalC2Bound.mono` at line 42
- `iteratedDeriv_two_mul` at line 54
- `IntervalC2Bound.mul` at line 61
- `exists_intervalC2Bound_fixed` at line 100
- `IntervalC2Bound.norm_sub_le` at line 126

### MathCollab.Density.Stronger.Atkinson.IntervalAmplitudeRescaled

File: `lean/MathCollab/Density/Stronger/Atkinson/IntervalAmplitudeRescaled.lean`; 70 source lines; SHA-256 `a661696971a3d80061870b8d98812c0853e9767fae6474074caee65cc57ee141`.

- `exists_intervalC1Bound_rescaled` at line 22

### MathCollab.Density.Stronger.Atkinson.AtkinsonCompactProfiles

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonCompactProfiles.lean`; 75 source lines; SHA-256 `6aa5778b2a61fbf5e8eab9d8a8a827ba18bbfd85b8649bfc5d5c2ce4e0b441a7`.

- `zetaMainMellinProfile` at line 26
- `contDiffAt_zetaMainMellinProfile` at line 30
- `zetaDivisorWeight_source_eq_profile` at line 38
- `exists_intervalC1Bound_zetaMainMellinProfile` at line 47
- `atkinsonPowerProfile` at line 52
- `contDiffAt_atkinsonPowerProfile` at line 55
- `exists_intervalC2Bound_atkinsonPowerRootProfile` at line 63

### MathCollab.Density.Stronger.Atkinson.ZetaLogGaussianVariation

File: `lean/MathCollab/Density/Stronger/Atkinson/ZetaLogGaussianVariation.lean`; 88 source lines; SHA-256 `7333733bb267dcd6c8a671fcf49fc3c14ac662b5c22146d1db8e8950c6a68aad`.

- `zetaLogGaussianEnvelope` at line 33
- `zetaLogGaussianEnvelope_bounds` at line 36
- `contDiffAt_zetaLogGaussianEnvelope` at line 40
- `hasDerivAt_zetaLogGaussianEnvelope` at line 46
- `intervalC1Bound_zetaLogGaussianEnvelope` at line 56
- `atkinson_center_mem_physical` at line 79

### MathCollab.Density.Stronger.Atkinson.ZetaQuadraticLogGaussianVariation

File: `lean/MathCollab/Density/Stronger/Atkinson/ZetaQuadraticLogGaussianVariation.lean`; 109 source lines; SHA-256 `d523532782a7d7df4483afdb2fd0431de474835f34d3e886fc261e90c4c12ad0`.

- `deriv_zetaQuadraticLogGaussian` at line 35
- `norm_deriv_zetaQuadraticLogGaussian_le` at line 42
- `intervalC1Bound_zetaQuadraticLogGaussian` at line 66

### MathCollab.Density.Stronger.Atkinson.AtkinsonMainWeight

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonMainWeight.lean`; 71 source lines; SHA-256 `064b2d9a6fe24fa18ea9749f0087adc93eed285ed0a31955f936f2aabc711b84`.

- `zetaAtkinsonMainWeight` at line 24
- `zetaAtkinsonMainWeight_eq_amplitude` at line 30
- `zetaAtkinsonMainWeight_carrier` at line 39
- `exists_intervalC1Bound_zetaAtkinsonMainWeight` at line 49

### MathCollab.Density.Stronger.Atkinson.ContinuousKernelPrimitive

File: `lean/MathCollab/Density/Stronger/Atkinson/ContinuousKernelPrimitive.lean`; 73 source lines; SHA-256 `b8ad6300130dfacb947df0f84c20269ceea832594a6f32cd1d5cf35d2a750bbb`.

- `IntervalC1Bound.continuousKernel_of_primitive_bound` at line 31

### MathCollab.Density.Stronger.Atkinson.MainReflection

File: `lean/MathCollab/Density/Stronger/Atkinson/MainReflection.lean`; 69 source lines; SHA-256 `105e26da2967cb9817db1888aba9cdce79bfd017feb0a9f9f8445b30bdf67b9c`.

- `IntervalC1Bound.reflection_source` at line 21

### MathCollab.Density.Stronger.Atkinson.AtkinsonMainIntegral

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonMainIntegral.lean`; 106 source lines; SHA-256 `2c6153936eaad9429d0df4f14579a879d312df730060e2aeb98b23ed2f01217b`.

- `zetaAtkinsonMainIntegrand` at line 24
- `integrable_zetaAtkinsonMainIntegrand` at line 27
- `zetaAtkinsonVoronoiMain_eq_reflection` at line 49
- `exists_norm_zetaAtkinsonVoronoiMain_le` at line 74
- `exists_zetaAtkinsonVoronoiMain_log_bound` at line 88

### MathCollab.Density.Stronger.Atkinson.ZetaAtkinsonMinusSource

File: `lean/MathCollab/Density/Stronger/Atkinson/ZetaAtkinsonMinusSource.lean`; 67 source lines; SHA-256 `124ffd6e0b9a2e0bd54b8b863d980482c8e009589e5ee6edb1a0ddf41bde91cf`.

- `exists_zetaSquarePhysicalGaussian_atkinson_minus_approximation` at line 33
- `exists_zetaSquareLocalMean_le_atkinson_minus` at line 50

### MathCollab.Density.Stronger.Atkinson.NeumannLaplaceRemainder

File: `lean/MathCollab/Density/Stronger/Atkinson/NeumannLaplaceRemainder.lean`; 103 source lines; SHA-256 `6e3155ae753db2811cf22ed02087a9cd51332505eac703bbcf1d836e582b7179`.

- `neumannLaplaceApproximation` at line 32
- `norm_neumannLaplaceIntegrand_sub_linear_le` at line 36
- `norm_neumannLaplaceIntegral_sub_moments_le` at line 60
- `norm_neumannLaplaceIntegral_sub_approximation_le` at line 87

### MathCollab.Density.Stronger.Atkinson.NeumannTwoTermExpansion

File: `lean/MathCollab/Density/Stronger/Atkinson/NeumannTwoTermExpansion.lean`; 79 source lines; SHA-256 `00d1993debf0854c8ce19d29cfad8b91912ec6752a978b59526511413d2a605d`.

- `neumannTwoTerm` at line 32
- `neumannTwoTermErrorConstant` at line 37
- `neumannTwoTermErrorConstant_pos` at line 39
- `neumannTwoTerm_eq_ray_approximation` at line 43
- `abs_dfiBesselY0_sub_neumannTwoTerm_le` at line 51

### MathCollab.Density.Stronger.Atkinson.NeumannSourceBounds

File: `lean/MathCollab/Density/Stronger/Atkinson/NeumannSourceBounds.lean`; 113 source lines; SHA-256 `3374caefdf58484b4c9ab0ff2d6f8a03f6d651adfce9b99397cd3cd4c079c703`.

- `measurable_dfiBesselY0` at line 33
- `measurable_neumannTwoTerm` at line 54
- `neumann_source_argument_bounds` at line 58
- `abs_neumann_source_remainder_le` at line 78
- `abs_dfiBesselY0_source_le_seven` at line 98
- `neumann_source_height_absorb` at line 106

### MathCollab.Density.Stronger.Atkinson.ZetaNeumannRemainder

File: `lean/MathCollab/Density/Stronger/Atkinson/ZetaNeumannRemainder.lean`; 157 source lines; SHA-256 `dd055ed65b12330a1b42ea28bb08c11aa9f0c6a5de28c9d08e2116914c386335`.

- `zetaAtkinsonY0Integrand` at line 33
- `zetaAtkinsonTwoTermIntegrand` at line 36
- `zetaNeumannRemainderIntegrand` at line 39
- `integrable_zetaAtkinson_kernel_of_support_bound` at line 44
- `integrable_zetaAtkinsonY0Integrand` at line 70
- `integrable_zetaNeumannRemainderIntegrand` at line 79
- `zetaAtkinsonTwoTermIntegrand_eq_sub` at line 89
- `integrable_zetaAtkinsonTwoTermIntegrand` at line 96
- `norm_integral_zetaNeumannRemainder_le` at line 105
- `exists_norm_integral_zetaNeumannRemainder_le` at line 131

### MathCollab.Density.Stronger.Atkinson.NeumannRemainderSeries

File: `lean/MathCollab/Density/Stronger/Atkinson/NeumannRemainderSeries.lean`; 99 source lines; SHA-256 `85cfbc836cd105e7d515816cb8b20b7398b5277680ae59984fa0efb6f4b623a3`.

- `zetaAtkinsonY0Term` at line 24
- `zetaAtkinsonTwoTerm` at line 27
- `zetaNeumannRemainderTerm` at line 30
- `norm_divisorDirichletTerm_real` at line 33
- `exists_norm_zetaNeumannRemainderTerm_le` at line 40
- `summable_zetaNeumannRemainderTerm` at line 60
- `zetaAtkinsonTwoTerm_eq_sub` at line 68
- `exists_norm_tsum_zetaNeumannRemainderTerm_le` at line 81

### MathCollab.Density.Stronger.Atkinson.ZetaNeumannSeries

File: `lean/MathCollab/Density/Stronger/Atkinson/ZetaNeumannSeries.lean`; 75 source lines; SHA-256 `c83648a3a54710689bc0192aa5f5408ec6e7dc484a81ed5160390a71528f1439`.

- `zetaAtkinsonTwoTermSum` at line 23
- `zetaAtkinsonY0Term_eq_native` at line 25
- `summable_zetaAtkinsonY0Term` at line 38
- `summable_zetaAtkinsonTwoTerm` at line 46
- `zetaAtkinsonBesselMinus_sub_twoTerm` at line 53
- `exists_norm_zetaAtkinsonBesselMinus_sub_twoTerm_le` at line 65

### MathCollab.Density.Stronger.Atkinson.ZetaAtkinsonTwoTermSource

File: `lean/MathCollab/Density/Stronger/Atkinson/ZetaAtkinsonTwoTermSource.lean`; 94 source lines; SHA-256 `dd3bb3e4a4b2bff5df60e0bd1429740d03ad29431ddea77b6b887875ee9bc930`.

- `exists_zetaAtkinsonBesselMinus_twoTerm_log_bound` at line 33
- `exists_zetaSquarePhysicalGaussian_atkinson_twoTerm_approximation` at line 54
- `exists_zetaSquareLocalMean_le_atkinson_twoTerm` at line 75

### MathCollab.Density.Stronger.Atkinson.AtkinsonPowerWeight

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonPowerWeight.lean`; 51 source lines; SHA-256 `5c6861d65bf1cd2e6d489f151232541d5689628483503c4fbb6c00401b1b0dd2`.

- `atkinsonPowerWeight` at line 25
- `exists_intervalC1Bound_atkinsonPowerWeight` at line 30

### MathCollab.Density.Stronger.Atkinson.AtkinsonPowerAmplitude

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonPowerAmplitude.lean`; 54 source lines; SHA-256 `849ca9b349f97ec091a2449eacc5889bae821f8a65b25748f9d11749b916f318`.

- `sqrt_mul_exp_neg_half_log` at line 23
- `atkinsonPowerWeight_eq_amplitude` at line 30

### MathCollab.Density.Stronger.Atkinson.ZetaAtkinsonSaddle

File: `lean/MathCollab/Density/Stronger/Atkinson/ZetaAtkinsonSaddle.lean`; 131 source lines; SHA-256 `cc79d894eb95af73e539b7ce48d74aa0d670f062b170dc11bc0019602e60f311`.

- `atkinsonSaddleRoot` at line 31
- `zetaAtkinsonSaddle` at line 33
- `atkinsonSaddleRoot_pos` at line 35
- `atkinsonSaddleRoot_equation` at line 42
- `atkinsonSaddleRoot_sub_pos` at line 48
- `atkinson_saddle_equation_iff` at line 54
- `zetaAtkinsonSaddle_pos` at line 71
- `zetaAtkinsonPhase_deriv_factored` at line 75
- `zetaAtkinsonPhase_stationary_iff` at line 87
- `zetaAtkinsonPhase_stationary` at line 95
- `zetaAtkinsonSaddle_zero` at line 99
- `zetaAtkinsonPhase_secondDeriv_saddle` at line 105
- `zetaAtkinsonPhase_secondDeriv_saddle_neg` at line 122

### MathCollab.Density.Stronger.Atkinson.AtkinsonRootPhase

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonRootPhase.lean`; 112 source lines; SHA-256 `bf45393df7ad793bac56305045c8ad2d6f0ee6103353d585254ab45d6d00d18a`.

- `atkinsonRootPhase` at line 33
- `atkinsonRootSlope` at line 36
- `zetaAtkinsonPhase_sq` at line 39
- `contDiffAt_atkinsonRootPhase` at line 46
- `hasDerivAt_atkinsonRootPhase` at line 51
- `hasDerivAt_atkinsonRootSlope` at line 61
- `atkinsonRootSlope_strictAnti` at line 73
- `atkinsonRootSlope_factored` at line 82
- `atkinsonRootSlope_le_neg_two` at line 94
- `two_le_atkinsonRootSlope` at line 103

### WeylPort.Analytic.NonstationaryFoundation

File: `lean/WeylPort/Analytic/NonstationaryFoundation.lean`; 519 source lines; SHA-256 `b4d916a71ecdab7aade0f8e8b2e02021532b223aaaaa356127b492c13626ce47`.

- `e` at line 15
- `lemma_IBP_bound_C1` at line 18
- `lemma_IBP_bound_C1_monotone` at line 145
- `bernsteinApproximation_monotone` at line 185
- `lemma_approx_monotone_C1_I` at line 271
- `lemma_approx_monotone_C1` at line 289
- `lemma_IBP_bound_monotone` at line 323
- `lemma_IBP_bound_abs_antitone` at line 390
- `lemma_aachmonophase` at line 469
- `nonstationary_phase_integral_bound` at line 507

### MathCollab.Density.Stronger.Atkinson.AtkinsonFirstDerivative

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonFirstDerivative.lean`; 98 source lines; SHA-256 `44720d8e1c075947aa837dea8bddebe4fbb6d05f3f15b53164ec7102b4c011c1`.

- `norm_phaseIntegral_le_of_negative_slope` at line 33
- `norm_phaseIntegral_le_of_positive_slope` at line 72

### MathCollab.Density.Stronger.Atkinson.AtkinsonRootFirstDerivative

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonRootFirstDerivative.lean`; 59 source lines; SHA-256 `28ad23d2849edbc030da360e2bb0ad9920517f0f6449df8c94e33909b6e27dc3`.

- `norm_atkinsonRootPhase_integral_right` at line 23
- `norm_atkinsonRootPhase_integral_left` at line 41

### MathCollab.Density.Stronger.Atkinson.AtkinsonRootIntegral

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonRootIntegral.lean`; 108 source lines; SHA-256 `d1e38361f34c392320da5f9172fe65d9a1413e4eb285460da76d35070510da4c`.

- `atkinsonRootKernel` at line 32
- `norm_atkinsonRootKernel` at line 35
- `continuousAt_atkinsonRootKernel` at line 38
- `intervalIntegrable_atkinsonRootKernel` at line 44
- `norm_atkinsonRootKernel_integral_le_length` at line 51
- `norm_atkinsonRootKernel_integral_le_four` at line 57

### MathCollab.Density.Stronger.Atkinson.AtkinsonAmplitudeIntegral

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonAmplitudeIntegral.lean`; 124 source lines; SHA-256 `b65fbed8ee5a6adbc70791ffcf367092cd2d4560e521d04ed5d540e32ed24289`.

- `IntervalC1Bound.comp_sq` at line 34
- `IntervalC1Bound.atkinsonRoot_of_primitive_bound` at line 67
- `IntervalC1Bound.atkinsonRoot` at line 116

### MathCollab.Density.Stronger.Atkinson.AtkinsonPowerIntegral

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonPowerIntegral.lean`; 116 source lines; SHA-256 `76521a253962a1786a76daa38df86f124166c344dfb09c0e8e3f7dce150a69bb`.

- `atkinsonPowerIntegrand` at line 34
- `atkinsonPowerIntegral` at line 38
- `atkinsonPowerIntegrand_sq` at line 41
- `atkinsonPowerIntegral_eq_root` at line 60
- `exists_norm_atkinsonPowerIntegral_le` at line 97

### MathCollab.Density.Stronger.Atkinson.AtkinsonFrequencyTail

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonFrequencyTail.lean`; 107 source lines; SHA-256 `82b4079fdf5e639ccc6df3479a519bb3beaa48d8b5e41199bcbb0040337aa6c5`.

- `atkinsonRootSlope_far_positive` at line 23
- `atkinsonRootSlope_far_negative` at line 32
- `norm_atkinsonRootKernel_integral_far` at line 52
- `exists_norm_atkinsonPowerIntegral_far_le` at line 80

### MathCollab.Density.Stronger.Atkinson.AtkinsonPowerPairBound

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonPowerPairBound.lean`; 41 source lines; SHA-256 `d783dbc597452f4eef7029d0f52a346e5eb03f0cbb5c3e925d9c468a896221b1`.

- `exists_norm_atkinsonPowerPair_le` at line 22

### MathCollab.Density.Stronger.Atkinson.AtkinsonCoefficientVariation

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonCoefficientVariation.lean`; 110 source lines; SHA-256 `12393074d0f4242cad4574f62aec5a2d794e3d7ae7d6cbb84159fa335454bda3`.

- `atkinsonCommonSaddleFactor` at line 23
- `atkinsonCommonSaddleFactor_neg` at line 26
- `atkinsonCommonSaddleFactor_pos` at line 30
- `atkinsonCommonSaddleFactor_eq_rpow` at line 35
- `atkinsonFourthRootCoefficient` at line 46
- `atkinsonFourthRootCoefficient_eq` at line 49
- `atkinsonCommonSaddleFactor_le_height` at line 57
- `atkinsonFourthRootCoefficient_nonneg` at line 71
- `atkinsonFourthRootCoefficient_le_height` at line 76
- `atkinsonFourthRootCoefficient_antitone` at line 84
- `finiteVariationBound_fourthRootCoefficient` at line 96

### MathCollab.Density.Stronger.Atkinson.AtkinsonCarrierCoefficients

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonCarrierCoefficients.lean`; 39 source lines; SHA-256 `0debbad95aa275db4ec6894888fd7a06efbcd217f4efe50a0342e76b47f8cc8f`.

- `atkinsonBesselScale` at line 21
- `neumannLeadingPlus` at line 24
- `neumannLeadingMinus` at line 25
- `neumannCorrectionPlus` at line 26
- `neumannCorrectionMinus` at line 27
- `atkinsonBesselScale_quarter_normalization` at line 29

### MathCollab.Density.Stronger.Atkinson.AtkinsonLeadingFinite

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonLeadingFinite.lean`; 40 source lines; SHA-256 `503627094921e0f6c23bc5abfd0207c39cbca01cdcf0b2d73701179bd762972f`.

- `atkinsonLeadingIntegral` at line 23
- `atkinsonLeadingTerm` at line 28
- `atkinsonLeadingSum` at line 31
- `atkinsonLeadingFiniteSum` at line 33
- `atkinsonBesselScale_nonneg` at line 36

### MathCollab.Density.Stronger.Atkinson.AtkinsonCorrectionBounds

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonCorrectionBounds.lean`; 135 source lines; SHA-256 `cd9bba47e3c683f37f6bc6ba346bf0de721b2312a21c3eb8021bbbf64ae915c5`.

- `atkinsonCorrectionIntegral` at line 25
- `atkinsonCorrectionTerm` at line 30
- `exists_norm_atkinsonPowerPair_far_le` at line 33
- `atkinson_correction_height_absorb` at line 55
- `exists_norm_atkinsonCorrectionPair_le` at line 60
- `exists_norm_atkinsonCorrectionTerm_le` at line 95

### MathCollab.Density.Stronger.Atkinson.AtkinsonCarrierAlgebra

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonCarrierAlgebra.lean`; 87 source lines; SHA-256 `22d53185f0f227c0a47a4f209723e6b87e9f3a53336be27bd14bf75aa6852b5b`.

- `neumannTwoTerm_complex_exp` at line 24
- `atkinson_bessel_argument_rpow` at line 38
- `atkinsonPowerIntegrand_bessel` at line 48
- `zetaAtkinsonTwoTermIntegrand_eq_carriers` at line 65

### MathCollab.Density.Stronger.Atkinson.AtkinsonCarrierIntegrals

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonCarrierIntegrals.lean`; 111 source lines; SHA-256 `9c08954285b5bcd737a5c769ec2f4aa480d0d673d302b887d8bf975e803fe5ad`.

- `norm_atkinsonPowerIntegrand` at line 22
- `integrable_atkinsonPowerIntegrand` at line 29
- `atkinsonTwoTermCarrierIntegral` at line 62
- `integral_zetaAtkinsonTwoTermIntegrand_eq_carriers` at line 71
- `zetaAtkinsonTwoTerm_eq_carrierIntegral` at line 102

### MathCollab.Density.Stronger.Atkinson.AtkinsonCorrectionSeries

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonCorrectionSeries.lean`; 64 source lines; SHA-256 `b1c35e9728706dc31f6d2068542a2c2b6c8663c6eb09485afba0f06106662b8f`.

- `atkinsonCorrectionSum` at line 23
- `atkinsonTwoTermCarrierIntegral_eq_leading_sub_correction` at line 25
- `zetaAtkinsonTwoTerm_eq_leading_sub_correction` at line 31
- `summable_atkinsonCorrectionTerm` at line 39
- `exists_norm_atkinsonCorrectionSum_le` at line 47

### MathCollab.Density.Stronger.Atkinson.AtkinsonLeadingSeriesAlgebra

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonLeadingSeriesAlgebra.lean`; 63 source lines; SHA-256 `ad049c89c3bf09a134d8983671333a901e2f027f4709e8caa27dd4409be98007`.

- `summable_atkinsonLeadingTerm_iff_twoTerm` at line 22
- `tsum_zetaAtkinsonTwoTerm_eq_leading_sub_correction_of_summable` at line 40
- `exists_norm_tsum_zetaAtkinsonTwoTerm_sub_leading_le_of_summable` at line 52

### MathCollab.Density.Stronger.Atkinson.AtkinsonGaussianVariation

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonGaussianVariation.lean`; 165 source lines; SHA-256 `b16eb4f9e4d37a462b380e428461c18e30ee61c6d4ebe306fcd65c14992c6a84`.

- `atkinsonSaddleGaussian` at line 25
- `third_mul_le_arsinh` at line 29
- `quadraticFrequencyEnvelope` at line 47
- `quadraticFrequencyEnvelope_antitone` at line 49
- `norm_quadraticGaussian_increment_le` at line 57
- `atkinsonSaddleFrequency` at line 87
- `atkinsonSaddleFrequency_nonneg` at line 90
- `atkinsonSaddleFrequency_monotone` at line 94
- `finiteVariationBound_atkinsonSaddleGaussian` at line 103
- `quadraticFrequencyEnvelope_saddle_le_physical` at line 129
- `finiteVariationBound_atkinsonSaddleGaussian_physical` at line 158

### MathCollab.Density.Stronger.Atkinson.AtkinsonSaddleNormalization

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSaddleNormalization.lean`; 112 source lines; SHA-256 `499309c91ff9d2158fd1344a38ee741e27f60e3785d1c53fcf885da4c04c1652`.

- `atkinsonSaddleRoot_neg` at line 32
- `atkinsonSaddleRoot_mul_neg` at line 38
- `atkinsonSaddleRoot_sum_neg` at line 43
- `zetaAtkinsonSaddle_mul_neg` at line 49
- `log_atkinsonSaddleRoot_div_sqrt` at line 54
- `log_atkinsonSaddleRoot_sq_sub_log` at line 68
- `zetaAtkinsonSaddle_log_argument` at line 77
- `atkinsonDualPhase` at line 82
- `atkinsonCentralPhase` at line 86
- `atkinsonDualPhase_neg` at line 88
- `zetaAtkinsonPhase_at_saddle` at line 93

### MathCollab.Density.Stronger.Atkinson.AtkinsonIndexPhase

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonIndexPhase.lean`; 266 source lines; SHA-256 `c2e0a6f80ad200d958a77748f177f2478dc84c23d836de1dd65a70af738b89ee`.

- `atkinsonSourcePhase` at line 39
- `atkinsonIndexRealPhase` at line 45
- `atkinsonIndexRealRatio` at line 51
- `atkinsonIndexRealRoot` at line 55
- `atkinsonIndexRealNormalizedPhase` at line 59
- `atkinsonIndexRealPhase_natCast` at line 68
- `atkinsonIndexRealPhase_eq_normalized` at line 73
- `hasDerivAt_atkinsonIndexRealRatio` at line 119
- `hasDerivAt_atkinsonIndexRealRoot` at line 132
- `hasDerivAt_atkinsonIndexRealNormalizedPhase` at line 164
- `hasDerivAt_atkinsonIndexRealPhase` at line 252

### MathCollab.Density.Stronger.Atkinson.AtkinsonSaddlePhase

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSaddlePhase.lean`; 106 source lines; SHA-256 `301187d4cdf8aeb1809c2e0ab0c0063568b6a6db7100a946f44a3dc25be283d6`.

- `atkinson_sqrt_frequency_normalized` at line 35
- `atkinson_sqrt_frequency_radical` at line 45
- `atkinsonDualPhase_sqrt` at line 58
- `zetaAtkinsonPhase_saddle_sqrt` at line 64
- `zetaAtkinsonPhase_saddle_neg_sqrt` at line 71
- `exp_atkinson_natural_pi` at line 78
- `exp_zetaAtkinsonPhase_saddle_sqrt` at line 84
- `exp_zetaAtkinsonPhase_saddle_neg_sqrt` at line 95

### MathCollab.Density.Stronger.Atkinson.AtkinsonSaddleGaussianIdentities

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSaddleGaussianIdentities.lean`; 53 source lines; SHA-256 `b90ed7e341ec36734c9bc2d1bedf55fb7715b48ff98903bc9de83e861d262988`.

- `zetaGaussianQuadraticIntegral_neg` at line 22
- `zetaGaussianQuadraticIntegral_at_saddle` at line 27
- `zetaGaussianQuadraticIntegral_at_neg_saddle` at line 34
- `atkinsonSaddleGaussian_eq` at line 43

### MathCollab.Density.Stronger.Atkinson.AtkinsonSaddleTaylor

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSaddleTaylor.lean`; 123 source lines; SHA-256 `031d9d5079981cb1806d745f945624905c00224eff4367b5c02c83f61fc7ccee`.

- `abs_log_one_add_sub_quadratic_le` at line 32
- `atkinsonRootQuadratic` at line 44
- `atkinsonRootPhase_sub_quadratic` at line 48
- `abs_atkinsonRootPhase_sub_quadratic_le` at line 71
- `norm_exp_real_phase_sub_le` at line 91
- `norm_atkinsonRootKernel_sub_quadratic_le` at line 102

### MathCollab.Density.Stronger.Atkinson.FresnelDampedTails

File: `lean/MathCollab/Density/Stronger/Atkinson/FresnelDampedTails.lean`; 106 source lines; SHA-256 `3eed3062431ae59b77bf221f96d6cc619bc638bdaecb1836f797de39107e8051`.

- `fresnelDampedKernel` at line 33
- `continuous_fresnelDampedKernel` at line 36
- `fresnelDampedKernel_eq_weighted` at line 40
- `norm_fresnelDampedKernel` at line 49
- `fresnelDampedKernel_neg` at line 61
- `intervalC1Bound_gaussian_damping` at line 65
- `norm_fresnelPhase_integral_le` at line 81
- `norm_integral_fresnelDampedKernel_le` at line 96

### MathCollab.Density.Stronger.Atkinson.FresnelGaussianComparison

File: `lean/MathCollab/Density/Stronger/Atkinson/FresnelGaussianComparison.lean`; 83 source lines; SHA-256 `9a166f4a8ae86533ea320878803963918f4dac15195c7fe61279d5bb7435b376`.

- `integrable_fresnelDampedKernel` at line 33
- `integral_Ioi_fresnelDampedKernel` at line 38
- `norm_integral_Ioi_fresnelDampedKernel_le` at line 44
- `integral_symmetric_fresnelDampedKernel` at line 53
- `norm_gaussianValue_sub_fresnelDampedWindow_le` at line 66

### MathCollab.Density.Stronger.Atkinson.FresnelAbelLimit

File: `lean/MathCollab/Density/Stronger/Atkinson/FresnelAbelLimit.lean`; 102 source lines; SHA-256 `da9d5ead14329f74080d277454ca29956903c42a25391c5fbbdbec26929ab693`.

- `atkinsonQuadraticWindow` at line 35
- `fresnelGaussianValue` at line 39
- `fresnelGaussianBase` at line 42
- `continuousAt_fresnelGaussianValue_damping` at line 50
- `fresnelDampedKernel_zero` at line 71
- `continuous_fresnelDampedWindow` at line 78
- `norm_atkinsonQuadraticWindow_sub_gaussianValue_le` at line 84

### MathCollab.Density.Stronger.Atkinson.FresnelEvaluation

File: `lean/MathCollab/Density/Stronger/Atkinson/FresnelEvaluation.lean`; 91 source lines; SHA-256 `e9f8b62196377916c87f815fee6261d1ab87d422ff43368a4499d360648ab045`.

- `fresnelGaussianValue_eq_cartesian` at line 32
- `fresnelGaussianValue_eq_phase` at line 52
- `norm_fresnelGaussianValue` at line 65
- `norm_atkinsonQuadraticWindow_sub_fresnel_le` at line 70
- `tendsto_atkinsonQuadraticWindow` at line 78

### MathCollab.Density.Stronger.Atkinson.AtkinsonQuadraticKernel

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonQuadraticKernel.lean`; 115 source lines; SHA-256 `200a476aaf21db149a88f1ec36d83a0e3ba2b40eb13ff239f67edc11b03839ff`.

- `atkinsonRootQuadraticKernel` at line 29
- `norm_atkinsonRootQuadraticKernel` at line 32
- `continuous_atkinsonRootQuadraticKernel` at line 36
- `atkinsonSaddleCurvature` at line 41
- `one_lt_atkinsonSaddleCurvature` at line 44
- `atkinsonSaddleCurvature_mul_root` at line 52
- `atkinsonSaddle_squareRoot_normalization` at line 65
- `atkinsonRootQuadraticKernel_translate` at line 72
- `integral_atkinsonRootQuadraticKernel` at line 82
- `norm_integral_atkinsonRootQuadraticKernel_sub_fresnel_le` at line 102

### MathCollab.Density.Stronger.Atkinson.AtkinsonStationaryTails

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonStationaryTails.lean`; 154 source lines; SHA-256 `ebb63813b5a90dfe442d6bcbd0c488e8c48a08dce734aecccf163eab59152262`.

- `IntervalC1Bound.restrict` at line 33
- `atkinsonRootSlope_le_neg_window` at line 44
- `window_le_atkinsonRootSlope` at line 54
- `norm_atkinsonRootKernel_integral_right_window` at line 64
- `norm_atkinsonRootKernel_integral_left_window` at line 82
- `IntervalC1Bound.atkinsonRoot_right_window` at line 99
- `IntervalC1Bound.atkinsonRoot_left_window` at line 108
- `IntervalC1Bound.atkinsonRoot_sub_local` at line 118

### MathCollab.Density.Stronger.Atkinson.AtkinsonLocalQuadratic

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonLocalQuadratic.lean`; 104 source lines; SHA-256 `ee28371823cb249d48789d7c919c8b3a9e1dd38fad298003e946ea2011ed0263`.

- `IntervalC2Bound.atkinsonLocalQuadratic` at line 24
- `IntervalC2Bound.atkinsonQuadraticApproximation` at line 85

### MathCollab.Density.Stronger.Atkinson.ZetaQuadraticGaussianSecondDerivative

File: `lean/MathCollab/Density/Stronger/Atkinson/ZetaQuadraticGaussianSecondDerivative.lean`; 89 source lines; SHA-256 `7a42534402a5d96f86de05acf2c4e4cd230fd4574958a9d4c0ca80bf607b7339`.

- `hasDerivAt_deriv_zetaGaussianQuadraticIntegral` at line 33
- `norm_iteratedDeriv_two_zetaGaussianQuadraticIntegral_le` at line 52
- `norm_iteratedDeriv_two_zetaGaussianQuadraticIntegral_le_polynomial` at line 74

### MathCollab.Density.Stronger.Atkinson.SecondDerivativeComposition

File: `lean/MathCollab/Density/Stronger/Atkinson/SecondDerivativeComposition.lean`; 115 source lines; SHA-256 `f15bed1e6245540c6e052bc8859d69394d745c88741bb8d2250c0cff48d8db7e`.

- `iteratedDeriv_ofReal_fun` at line 32
- `iteratedDeriv_two_comp_real` at line 37
- `IntervalC2Bound.congr_of_eventuallyEq` at line 60
- `IntervalC2Bound.absorb_scale` at line 77
- `exists_real_profile_derivative_bound` at line 94

### MathCollab.Density.Stronger.Atkinson.ZetaGaussianNaturalDerivatives

File: `lean/MathCollab/Density/Stronger/Atkinson/ZetaGaussianNaturalDerivatives.lean`; 136 source lines; SHA-256 `5c1330c7d565db0ef896af9f440d514dc9dd9f3480363284f0e9573a268b982e`.

- `sq_mul_gaussian_eighth_le` at line 35
- `abs_mul_gaussian_eighth_le` at line 43
- `norm_deriv_zetaGaussianQuadraticIntegral_le_natural` at line 50
- `norm_iteratedDeriv_two_zetaGaussianQuadraticIntegral_le_natural` at line 63
- `exists_intervalC2Bound_quadraticGaussian_profile_natural` at line 80

### MathCollab.Density.Stronger.Atkinson.AtkinsonRootLogProfile

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonRootLogProfile.lean`; 33 source lines; SHA-256 `27630068fd21ae52c529538e30926045bb659edb2ee3fc24aa017b9fe6d1b331`.

- `atkinsonRootLogProfile` at line 19
- `zetaQuadraticLogGaussian_root_rescale` at line 21

### MathCollab.Density.Stronger.Atkinson.AtkinsonNaturalGaussianProfile

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonNaturalGaussianProfile.lean`; 72 source lines; SHA-256 `b9168fe89a7f3d2a714a69b8d9389cace644d7c1a7f46a67c8e80a7e81128db3`.

- `IntervalC2Bound.comp_div` at line 24
- `exists_intervalC2Bound_zetaQuadraticLogGaussian_root_natural` at line 54

### MathCollab.Density.Stronger.Atkinson.ZetaBandSecondDerivatives

File: `lean/MathCollab/Density/Stronger/Atkinson/ZetaBandSecondDerivatives.lean`; 140 source lines; SHA-256 `ff47b4ec62fae3ab06af367827682f99672074ae2efc8e8018bd8f25dcb59a7c`.

- `support_iteratedDeriv_smoothTransition` at line 23
- `exists_norm_iteratedDeriv_smoothTransition_le` at line 38
- `deriv_smoothTransition_quadratic` at line 59
- `iteratedDeriv_two_smoothTransition_quadratic` at line 71
- `exists_intervalC2Bound_quadraticTransition` at line 88

### MathCollab.Density.Stronger.Atkinson.ZetaBandPhysicalDerivatives

File: `lean/MathCollab/Density/Stronger/Atkinson/ZetaBandPhysicalDerivatives.lean`; 130 source lines; SHA-256 `e9ce1868606daf434c9f0859fd91f0185a8cb44badb38831282c2a3d101837f9`.

- `exp_gap_lower` at line 22
- `zetaDivisorBandEdge_normalized_gap_lower` at line 30
- `zetaDivisorBandCutoff_inverse_widths` at line 41
- `zetaBandCutoff_mul_height` at line 69
- `zetaDivisorBandCutoff_root_rescale` at line 76
- `exists_intervalC2Bound_zetaDivisorBandCutoff_root` at line 84

### MathCollab.Density.Stronger.Atkinson.AtkinsonNaturalAmplitude

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonNaturalAmplitude.lean`; 78 source lines; SHA-256 `76057498731dfe5d5962dbdf917c8022e7c1491970f768eab130218e41694d85`.

- `exists_intervalC2Bound_atkinsonPowerWeight_normalized_natural` at line 24
- `exists_intervalC2Bound_atkinsonPowerWeight_root_natural` at line 59

### MathCollab.Density.Stronger.Atkinson.AtkinsonLocalStationary

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonLocalStationary.lean`; 50 source lines; SHA-256 `dab8ca269b265d8e7ddcbfa080fce0fd3d8191b82fececa0ea993b38c9902e56`.

- `exists_atkinsonPowerIntegral_local_quadratic_approximation` at line 24

### MathCollab.Density.Stronger.Atkinson.AtkinsonPowerWeightRoot

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonPowerWeightRoot.lean`; 40 source lines; SHA-256 `2c8734e5df59ca3adbac01ee76fb02ad820889a420b130f9fac1c36e9bd890e0`.

- `exists_intervalC1Bound_atkinsonPowerWeight_root` at line 23

### MathCollab.Density.Stronger.Atkinson.AtkinsonStationaryReduction

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonStationaryReduction.lean`; 55 source lines; SHA-256 `a5152c75e4c82237557b3dcf1de2c8f88e7fec38fed436997e91f91407ee07ab`.

- `exists_atkinsonPowerIntegral_quadratic_approximation` at line 23

### MathCollab.Density.Stronger.Atkinson.AtkinsonFiniteStationaryMain

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonFiniteStationaryMain.lean`; 49 source lines; SHA-256 `8b322edb5e10a800834b0222856d472e651a5cceca5f6d16ce8e5de269160368`.

- `atkinsonFiniteStationaryMain` at line 22
- `atkinsonFiniteStationaryMain_eq_quadratic` at line 27
- `exists_atkinsonPowerIntegral_finite_stationary_approximation` at line 36

### MathCollab.Density.Stronger.Atkinson.AtkinsonStationaryMain

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonStationaryMain.lean`; 96 source lines; SHA-256 `a4f0d51d693f629353b65207e73e889c928d60485c9970fcddad4f30c47d850f`.

- `atkinsonStationaryMain` at line 31
- `atkinsonStationaryMain_eq_phase` at line 36
- `exists_norm_atkinsonFiniteStationaryMain_sub_main_le` at line 45
- `exists_atkinsonPowerIntegral_stationary_approximation` at line 67

### MathCollab.Density.Stronger.Atkinson.AtkinsonIndexCurvature

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonIndexCurvature.lean`; 122 source lines; SHA-256 `2fe54fb98e8cd9f0cf7f9514cbe07c7e89fa16e31ecad5ccec377201bd7980f1`.

- `atkinsonIndexRealSlope` at line 35
- `atkinsonIndexRealCurvature` at line 39
- `atkinsonIndexRealSlope_pos` at line 43
- `hasDerivAt_atkinsonIndexRealSlope` at line 52
- `hasDerivAt_deriv_atkinsonIndexRealPhase` at line 75
- `atkinsonIndexPhaseDifference` at line 88
- `hasDerivAt_atkinsonIndexPhaseDifference` at line 92
- `hasDerivAt_atkinsonIndexPhaseDifferenceSlope` at line 102
- `atkinsonIndexRealCurvature_neg` at line 112

### MathCollab.Density.Stronger.Atkinson.AtkinsonIndexHeight

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonIndexHeight.lean`; 189 source lines; SHA-256 `66bcaeab992144340a1e64fa0fe07b03178b37c22edffbc8195d3adf2ee40fea`.

- `atkinsonIndexCurvatureMagnitude` at line 38
- `atkinsonIndexCurvatureMagnitude_eq_neg` at line 42
- `atkinsonIndexCurvatureMagnitude_pos` at line 50
- `hasDerivAt_atkinsonIndexRealSlope_height` at line 58
- `hasDerivAt_atkinsonIndexCurvatureMagnitude` at line 76
- `atkinsonIndexCurvatureMagnitude_deriv_pos` at line 116
- `strictMonoOn_atkinsonIndexCurvatureMagnitude` at line 130
- `atkinsonIndexCurvatureDifference_neg` at line 144
- `exists_atkinsonIndexCurvatureDifference_eq` at line 156

### MathCollab.Density.Stronger.Atkinson.AtkinsonIndexScales

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonIndexScales.lean`; 304 source lines; SHA-256 `a5a5104de07c1a3efd100e103218c9e7356917e209b90850b2ab50a10f7e5822`.

- `atkinsonIndexSlopeLower` at line 35
- `atkinsonIndexSlopeUpper` at line 39
- `atkinsonIndexCurvatureDerivativeLower` at line 43
- `atkinsonIndexCurvatureDerivativeUpper` at line 48
- `atkinsonIndexBoxCurvatureLower` at line 53
- `atkinsonIndexBoxCurvatureUpper` at line 57
- `atkinsonIndexSlopeLower_pos` at line 60
- `atkinsonIndexSlopeUpper_pos` at line 66
- `atkinsonIndexSlopeLower_le` at line 76
- `atkinsonIndexSlope_le_upper` at line 89
- `atkinsonIndexCurvatureDerivativeLower_pos` at line 104
- `atkinsonIndexCurvatureDerivativeUpper_pos` at line 112
- `atkinsonIndexSlopeUpper_anti` at line 120
- `atkinsonIndexSlopeLower_anti` at line 130
- `atkinsonIndexCurvatureDerivative_box_bounds` at line 140
- `atkinsonIndexCurvatureDerivative_bounds` at line 181
- `atkinsonIndexCurvatureDifference_bounds` at line 284

### GuthMaynard.VanDerCorput

File: `lean/GuthMaynard/VanDerCorput.lean`; 656 source lines; SHA-256 `164bc76bf2f027a86cb42181855c6d3863afabddd45e8b49fc4148a77881f563`.

- `unitaryPhase` at line 29
- `phaseResolvent` at line 32
- `unitaryPhase_add` at line 37
- `unitaryPhase_sub` at line 41
- `phaseSum` at line 50
- `logarithmicPhase` at line 54
- `logarithmicSum` at line 57
- `unitaryPhase_logarithmicPhase_eq_cpow` at line 60
- `logarithmicSum_eq_cpow` at line 68
- `norm_phaseSum_le_card` at line 75
- `norm_logarithmicSum_le_length` at line 81
- `hasDerivAt_logarithmicPhase` at line 86
- `hasDerivAt_logarithmicPhase_deriv` at line 92
- `hasDerivAt_logarithmicPhase_secondDeriv` at line 105
- `phaseResolvent_eq` at line 125
- `hasDerivAt_real_cot` at line 150
- `strictAntiOn_real_cot` at line 161
- `sin_half_lower` at line 174
- `norm_phaseResolvent_le` at line 199
- `norm_phaseResolvent_sub_eq` at line 217
- `phaseResolvent_variation` at line 241
- `abs_cot_half_le_norm_phaseResolvent` at line 263
- `unitaryPhase_resolvent_step` at line 281
- `finite_resolvent_telescoping` at line 301
- `norm_sum_le_resolvent_variation` at line 324
- `kusminLandau_one_period` at line 350
- `unitaryPhase_int_mul_two_pi` at line 398
- `unitaryPhase_sub_int_mul_two_pi` at line 406
- `kusminLandau_one_period_decreasing` at line 412
- `kusminLandau_interval` at line 447
- `norm_sum_sq_le_card_mul_sum_norm_sq` at line 484
- `finite_weyl_differencing` at line 500
- `paddedShift` at line 569
- `sum_paddedShift_eq` at line 574
- `sum_norm_sq_paddedShift_eq` at line 600
- `interval_weyl_differencing` at line 626

### GuthMaynard.SecondDerivative

File: `lean/GuthMaynard/SecondDerivative.lean`; 418 source lines; SHA-256 `86e0903ddc9f28227977811b18a892671efe9f261567bf972f949c2dacd189cd`.

- `discrete_growth_lower` at line 22
- `monotone_of_step` at line 37
- `filter_card_bound` at line 48
- `sum_Icc_eq_shifted_range` at line 92
- `kusminLandau_good_fiber` at line 113
- `periodIndex` at line 171
- `periodIndex_bounds` at line 174
- `periodIndex_mono` at line 186
- `period_count_bound` at line 191
- `discrete_growth_upper` at line 215
- `norm_phase_sum_finset_le_card` at line 230
- `vanDerCorput_second_derivative` at line 237
- `vanDerCorput_B_process` at line 404

### GuthMaynard.SecondOrderMeanValue

File: `lean/GuthMaynard/SecondOrderMeanValue.lean`; 72 source lines; SHA-256 `17bdb1eb7c5491b385b0ae7b0977c954ab864ce12bcb24eeb6ba0cbf4c8bb23a`.

- `twice` at line 15
- `second_order_mean_value` at line 16

### MathCollab.Density.Stronger.Atkinson.AtkinsonIndexBProcess

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonIndexBProcess.lean`; 237 source lines; SHA-256 `06512fa887fc938666ccb65ab553f15f04f6990f3e37f49c9dc32b50c9b4d22e`.

- `atkinsonIndexPositiveDifference` at line 40
- `hasDerivAt_atkinsonIndexPositiveDifference` at line 43
- `hasDerivAt_atkinsonIndexPositiveDifferenceSlope` at line 52
- `exists_atkinsonIndexPositiveDifference_secondDifference` at line 64
- `atkinsonIndexPositiveDifferenceNat` at line 97
- `atkinsonIndexPositiveDifference_natCast` at line 104
- `atkinsonIndexBProcessLambda` at line 114
- `atkinsonIndexBProcessLambdaUpper` at line 119
- `atkinsonIndexBProcessLambda_pos` at line 123
- `atkinsonIndexPositiveDifferenceNat_secondDifference_bounds` at line 137
- `atkinsonIndexPositiveDifference_B_process` at line 212

### MathCollab.Density.Stronger.Atkinson.AtkinsonIndexFirstDerivative

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonIndexFirstDerivative.lean`; 324 source lines; SHA-256 `6cb4ee8f8114855cf08a91540ed3ceff7dd4c846236034987d6bff28c5f0f44e`.

- `atkinsonIndexFirstDerivativeLower` at line 38
- `atkinsonIndexFirstDerivativeUpper` at line 44
- `atkinsonIndexRealSlope_sub_eq` at line 50
- `atkinsonIndexRealSlopeDifference_box_bounds` at line 82
- `atkinsonIndexIncreasingDifferenceNat` at line 176
- `exists_atkinsonIndexIncreasingDifferenceNat_increment` at line 183
- `atkinsonIndexIncreasingDifferenceNat_increment_bounds` at line 226
- `atkinsonIndexIncreasingDifferenceNat_increment_anti` at line 261
- `atkinsonIndexIncreasingDifference_KL` at line 284

### MathCollab.Density.Stronger.Atkinson.AtkinsonPrefixVectors

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonPrefixVectors.lean`; 130 source lines; SHA-256 `1fff55cd9fcebf95568cb864e17aaf03721595a062886dc1d467fc702f20db78`.

- `sum_range_prefix_mask` at line 35
- `atkinsonPositivePhaseTerm` at line 47
- `atkinsonPhaseBlockSum` at line 50
- `atkinsonAlternatingCoefficient` at line 54
- `atkinsonPhaseVector` at line 56
- `atkinsonMaskedPhaseVector` at line 58
- `atkinsonPrefixGram` at line 61
- `atkinsonBlockCoefficientEnergy` at line 64
- `norm_atkinsonAlternatingCoefficient` at line 67
- `atkinsonPhaseTerm_eq_coefficient_vector` at line 71
- `atkinsonPhaseBlockSum_eq_masked` at line 76
- `atkinsonPrefixGram_eq_vector` at line 84
- `atkinsonMaskedPhaseVector_gram` at line 93
- `atkinsonPrefixGram_self` at line 107
- `norm_atkinsonPrefixGram_self` at line 111
- `atkinsonPrefixGram_swap` at line 115
- `atkinsonBlockCoefficientEnergy_nonneg` at line 124

### MathCollab.Density.Stronger.Atkinson.AtkinsonPrefixMax

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonPrefixMax.lean`; 51 source lines; SHA-256 `ebdefd922d126e693f4b6dd94679cc7d831faacd61414128402aeb1016e6c8ec`.

- `atkinsonPrefixGramMax` at line 20
- `norm_atkinsonPrefixGram_le_max` at line 23
- `atkinsonPrefixGramMax_nonneg` at line 29
- `atkinsonPrefixGramMax_self` at line 34
- `atkinsonPrefixGramMax_swap` at line 45

### MathCollab.Density.Stronger.Atkinson.AtkinsonPrefixCancellation

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonPrefixCancellation.lean`; 155 source lines; SHA-256 `cdf6692e30d726955f7df558fe5eae8c3caf4d027e2fe41d1fb0214386738739`.

- `atkinsonPrefixBProcessMajorant` at line 34
- `atkinsonIndexBProcessLambdaUpper_pos` at line 40
- `atkinsonPrefixBProcessMajorant_nonneg` at line 50
- `norm_atkinsonPrefixGram_le_bProcess` at line 58
- `atkinsonPrefixGramMax_le_bProcess` at line 81
- `atkinsonPrefixFirstDerivativeMajorant` at line 91
- `atkinsonPrefixFirstDerivativeMajorant_pos` at line 94
- `norm_atkinsonPrefixGram_le_firstDerivative` at line 103
- `atkinsonPrefixGramMax_le_firstDerivative` at line 135
- `atkinsonPrefixFirstDerivativeMajorant_eq_gap` at line 146

### MathCollab.Density.Stronger.Atkinson.AtkinsonPrefixGapBound

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonPrefixGapBound.lean`; 110 source lines; SHA-256 `3343c308e3c0469e6e85108975bb3718af38843c58a41996a90c416ee82fcb05`.

- `norm_atkinsonPrefixGram_le_length` at line 32
- `atkinsonPrefixGramMax_le_length` at line 41
- `atkinsonOrderedPrefixGapMajorant` at line 49
- `atkinsonPrefixGapMajorant` at line 56
- `atkinsonPrefixGramMax_le_orderedGap` at line 60
- `atkinsonPrefixGapMajorant_self` at line 72
- `atkinsonPrefixGapMajorant_swap` at line 76
- `atkinsonPrefixGramMax_le_gap` at line 80
- `atkinsonPrefixGapMajorant_nonneg` at line 96
- `norm_atkinsonPrefixGram_le_gap` at line 103

### WeylPort.GrowthAlgebra

File: `lean/WeylPort/GrowthAlgebra.lean`; 139 source lines; SHA-256 `1c9d76ac39ce51f8570f00259d9b6892278571be3edc4c14c29cb14f7db39c2b`.

- `eventually_const_log_pow_le_rpow` at line 21
- `eventually_const_height_log_pow_mul_rpow_le_rpow` at line 30
- `pointValue_sixth_power_count_identity` at line 53
- `eventually_pointValue_sixth_power_count_lt_one` at line 74
- `eventually_pointValue_sixth_power_source_range` at line 92

### MathCollab.Density.Stronger.Atkinson.AtkinsonPhysicalCutoff

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonPhysicalCutoff.lean`; 138 source lines; SHA-256 `6e23c5a3a04578dbbd9586df48a11fad85cccf2b967e09a6e3798b440a20f718`.

- `atkinsonSourceCutoff` at line 23
- `atkinsonSourceCutoff_lower` at line 25
- `atkinsonSourceCutoff_pos` at line 29
- `atkinsonSourceCutoff_le_small` at line 35
- `eventually_atkinsonSourceCutoff_small` at line 49
- `atkinsonPacketCutoff` at line 60
- `atkinsonSourceCutoff_le_packet` at line 63
- `atkinsonSourceCutoff_log_mono_height` at line 69
- `atkinsonPacketCutoff_le_height` at line 81
- `atkinson_doubled_height_half_power` at line 90
- `exists_atkinsonPhysicalCutoff_prefix_geometry` at line 100
- `atkinson_dyadic_prefix_geometry` at line 113
- `exists_atkinsonPhysicalPrefixGramMax_le_gap` at line 123

### MathCollab.Density.Stronger.Atkinson.AtkinsonSaddleSupport

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSaddleSupport.lean`; 128 source lines; SHA-256 `6ef148761f166f8a16036cba451cef09e754d76409f2435e0fe0aeb56c443f68`.

- `log_zetaDivisorBandEdge` at line 23
- `zetaDivisorBand_log_bound` at line 27
- `zetaDivisorBandCutoff_log_bound` at line 38
- `arsinh_abs` at line 44
- `abs_le_three_mul_of_arsinh_bound` at line 50
- `abs_frequency_le_of_saddle_log_bound` at line 62
- `abs_frequency_le_of_saddle_cutoff` at line 85
- `atkinsonStationaryMain_eq_zero_of_frequency` at line 92
- `atkinsonStationaryMain_pair_eq_zero_of_index` at line 102
- `atkinsonStationaryMain_pair_eq_zero_after_cutoff` at line 117

### MathCollab.Density.Stronger.Atkinson.AtkinsonRootBand

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonRootBand.lean`; 138 source lines; SHA-256 `d028b172e29fdd3942b75eda2cea617544272752522b7002ee0149747f1a37bb`.

- `atkinsonRootBandLower` at line 31
- `atkinsonRootBandUpper` at line 34
- `atkinsonRootBandLower_pos` at line 37
- `atkinsonRootBand_order` at line 41
- `atkinsonRootBand_square_mem` at line 46
- `atkinsonRootBand_physical` at line 57
- `zetaAtkinsonSaddle_inverse_root` at line 72
- `abs_atkinsonRootSlope_zero_le_band` at line 81
- `atkinsonPowerIntegral_eq_root_band` at line 95

### MathCollab.Density.Stronger.Atkinson.AtkinsonBandCancellation

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonBandCancellation.lean`; 119 source lines; SHA-256 `1c3603a72a6b19d631335d04a99b371e1610018d19de4412bd9a4c19e51dc948`.

- `atkinsonRootSlope_outside_band` at line 30
- `norm_atkinsonRootKernel_integral_outside_band` at line 45
- `exists_intervalC1Bound_atkinsonPowerWeight_root_band` at line 80
- `exists_norm_atkinsonPowerIntegral_outside_band_le` at line 96

### MathCollab.Density.Stronger.Atkinson.ReciprocalSecondDerivativeBounds

File: `lean/MathCollab/Density/Stronger/Atkinson/ReciprocalSecondDerivativeBounds.lean`; 115 source lines; SHA-256 `b9bffaa12b72f0d711a5119e223a2842506b0981eaf042a55d1ef58646160134`.

- `iteratedDeriv_two_real_inv` at line 31
- `intervalC2Bound_real_reciprocal` at line 48
- `IntervalC2Bound.deriv_c1` at line 91

### MathCollab.Density.Stronger.Atkinson.AtkinsonSecondOrderIntegration

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSecondOrderIntegration.lean`; 105 source lines; SHA-256 `812b991cf7abc63908a3bc9de2c4035de51dc1f68566b5a60c1cb1d4b844eef8`.

- `hasDerivAt_atkinsonRootKernel` at line 30
- `IntervalC2Bound.atkinsonRoot_secondOrder` at line 43

### MathCollab.Density.Stronger.Atkinson.AtkinsonSlopeDerivativeBounds

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSlopeDerivativeBounds.lean`; 130 source lines; SHA-256 `c5e3376fb12d89d94029136ae0c0b7ac541db871f1e149e31fcb64d005647ef3`.

- `IntervalC2Bound.restrict` at line 31
- `hasDerivAt_atkinsonRootSlopeFirst` at line 40
- `iteratedDeriv_two_atkinsonRootSlope` at line 52
- `atkinsonRootSlope_derivative_bounds` at line 61
- `intervalC2Bound_atkinsonSlope_reciprocal_band` at line 88

### MathCollab.Density.Stronger.Atkinson.AtkinsonBandAmplitude

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonBandAmplitude.lean`; 121 source lines; SHA-256 `42e14a7554f304a18f85635fe148d9256f328336860838d727fd829b97e67142`.

- `sqrt_exp_half` at line 30
- `sqrt_zetaDivisorBandEdge` at line 37
- `atkinsonRootBand_length_le` at line 42
- `zetaDivisorBandCutoff_endpoints` at line 64
- `atkinsonPowerWeight_rootBand_endpoints` at line 72
- `exists_intervalC2Bound_atkinsonPowerWeight_root_band` at line 84
- `exists_intervalC2Bound_atkinsonSlopeQuotient_band` at line 101

### MathCollab.Density.Stronger.Atkinson.AtkinsonBandSecondOrder

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonBandSecondOrder.lean`; 136 source lines; SHA-256 `f1ee7928891f88c68854892fa3c43396593b0b5732e61dabca47324a6ea6fa7e`.

- `atkinsonRootBand_derivative_bracket` at line 30
- `exists_norm_atkinsonPowerIntegral_band_secondOrder_le` at line 46
- `exists_norm_atkinsonPowerIntegral_index_band_secondOrder_le` at line 96
- `exists_norm_atkinsonPowerPair_band_secondOrder_le` at line 116

### MathCollab.Density.Stronger.Atkinson.AtkinsonSharpTruncation

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSharpTruncation.lean`; 152 source lines; SHA-256 `d521c0ff0b15bdba3ee7915e6d7f0dfc5a4f61c14ddf7b76bfdffbe8a55bb8c3`.

- `exists_norm_atkinsonLeadingTerm_band_le` at line 33
- `summable_atkinsonLeadingTerm_of_band` at line 82
- `exists_norm_atkinsonLeadingSum_sub_band_finite_le` at line 96
- `atkinsonBand_tail_scale_le` at line 135

### MathCollab.Density.Stronger.Atkinson.AtkinsonLeadingSeriesConvergence

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonLeadingSeriesConvergence.lean`; 51 source lines; SHA-256 `6fd756f9c063548b78c77796abcf31d58c82b27046f60f3a53888a39bc6ec189`.

- `summable_zetaAtkinsonTwoTerm_of_band` at line 23
- `tsum_zetaAtkinsonTwoTerm_eq_leading_sub_correction` at line 31
- `exists_norm_tsum_zetaAtkinsonTwoTerm_sub_leading_le` at line 40

### MathCollab.Density.Stronger.Atkinson.AtkinsonSourceBand

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSourceBand.lean`; 62 source lines; SHA-256 `ab74a7b51a9b1a1ef61a4b49b48898e440f1d7f8d9595b0b66815a9037ec44a1`.

- `exists_atkinsonLeading_source_band_bound` at line 32

### MathCollab.Density.Stronger.Atkinson.AtkinsonSourceCutoffBound

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSourceCutoffBound.lean`; 34 source lines; SHA-256 `cf4dde4b424ffbe8bac9a57fccde52a64e053a577493cb3c3d4d16e78f628eb6`.

- `atkinsonSourceCutoff_le_natural` at line 18

### MathCollab.Density.Stronger.Atkinson.AtkinsonStationarySeries

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonStationarySeries.lean`; 65 source lines; SHA-256 `46f666e0a356a9e25220a03e983d89ec3980d6827ed1ab720ce6b0edbbd29075`.

- `atkinsonStationaryLeadingIntegral` at line 24
- `atkinsonStationaryLeadingTerm` at line 29
- `atkinsonStationaryLeadingFiniteSum` at line 32
- `atkinsonStationaryLeadingSum` at line 35
- `atkinsonStationaryLeadingTerm_zero` at line 38
- `atkinsonStationaryLeadingTerm_eq_zero_after_cutoff` at line 42
- `hasSum_atkinsonStationaryLeadingTerm` at line 50
- `atkinsonStationaryLeadingSum_eq_finite` at line 59

### MathCollab.Density.Stronger.Atkinson.StationaryOddRemainder

File: `lean/MathCollab/Density/Stronger/Atkinson/StationaryOddRemainder.lean`; 195 source lines; SHA-256 `53cc56a82f697a27fe7f030e904287f20c9188612ed40de57ab98bdc09c133c5`.

- `IntervalC2Bound.norm_deriv_sub_le` at line 33
- `IntervalC2Bound.norm_sub_linear_le` at line 43
- `norm_exp_real_phase_sub_linear_le` at line 76
- `abs_log_one_add_sub_cubic_le` at line 91
- `atkinsonRootCubicCorrection` at line 104
- `abs_atkinsonRootPhase_sub_cubic_le` at line 108
- `norm_atkinsonRootKernel_sub_cubic_le` at line 137

### MathCollab.Density.Stronger.Atkinson.AtkinsonSymmetricStationary

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSymmetricStationary.lean`; 175 source lines; SHA-256 `0bd87a968eb2543f0c7c19c6d9dc2013fc6664d78796c4689ee209e1f20c15ec`.

- `atkinsonRootQuadraticKernel_reflect` at line 32
- `integral_atkinsonRootQuadratic_odd` at line 40
- `abs_atkinsonRootCubicCorrection_le` at line 60
- `IntervalC2Bound.atkinsonLocalSymmetric` at line 74

### MathCollab.Density.Stronger.Atkinson.AtkinsonSymmetricReduction

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSymmetricReduction.lean`; 115 source lines; SHA-256 `8b3b112e4e42cd16fe6206a5ce22baa5d505f0ffc092ed9abdd69d6a2922d881`.

- `atkinsonSymmetricError` at line 33
- `atkinsonSymmetricError_tail_le` at line 38
- `IntervalC2Bound.atkinsonSymmetricApproximation` at line 49
- `exists_atkinsonPowerIntegral_finite_symmetric_approximation` at line 67
- `exists_atkinsonPowerIntegral_symmetric_approximation` at line 93

### MathCollab.Density.Stronger.Atkinson.AtkinsonSampleGeometry

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSampleGeometry.lean`; 136 source lines; SHA-256 `270151c3b9640017a6978ce3a3d122c66558a28abca19b1d4e649715006e9da8`.

- `atkinsonSaddleRoot_small_frequency` at line 23
- `atkinsonSaddleRoot_small_frequency_window` at line 51
- `sqrt_nat_small_frequency` at line 61
- `atkinsonSaddleRoot_inverse_identity` at line 68
- `atkinsonSaddleRoot_monotone` at line 75
- `zetaAtkinsonSaddle_monotone` at line 85
- `atkinsonPositiveRootSample` at line 91
- `atkinsonNegativeRootSample` at line 94
- `atkinsonPositiveRootSample_monotone` at line 97
- `atkinsonNegativeRootSample_antitone` at line 104
- `atkinsonRootSample_mem` at line 112

### MathCollab.Density.Stronger.Atkinson.AtkinsonSymmetricBalance

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSymmetricBalance.lean`; 129 source lines; SHA-256 `24ddd58f60750327c4e9940516624ecac6f3d1f4d94844dabde7030b52ea364e`.

- `atkinsonSymmetricError_le_physical` at line 33
- `atkinsonSymmetric_error_le_of_power_balance` at line 74
- `exists_atkinsonPowerIntegral_symmetric_balance` at line 105

### MathCollab.Density.Stronger.Atkinson.AtkinsonFourthRootRadius

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonFourthRootRadius.lean`; 119 source lines; SHA-256 `8bf8cc081f27cd6858604f9b14bc20cce0672c6edbc08934cb7f2083608e9884`.

- `atkinsonSymmetricRadiusScale` at line 32
- `atkinsonSymmetricRadiusScale_pos` at line 35
- `atkinsonSymmetricRadiusScale_sq` at line 40
- `atkinsonSymmetricRadiusScale_fourth` at line 47
- `atkinsonSymmetricRadiusScale_balance` at line 53
- `exists_atkinsonPowerIntegral_fourthRoot_width` at line 81
- `exists_atkinsonPowerIntegral_fourthRoot_pair` at line 102

### MathCollab.Density.Stronger.Atkinson.DivisorQuarterPrefix

File: `lean/MathCollab/Density/Stronger/Atkinson/DivisorQuarterPrefix.lean`; 66 source lines; SHA-256 `5a26df21912693b727d74c3d6aee60840d1f3ab37360181b505115b87f93830b`.

- `norm_divisorDirichletTerm_quarter_le_prefix` at line 21
- `exists_sum_norm_divisorDirichletTerm_quarter_le` at line 44

### MathCollab.Density.Stronger.Atkinson.AtkinsonFiniteStationaryError

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonFiniteStationaryError.lean`; 115 source lines; SHA-256 `ba6c4ee52293b0fa8963c405d4f116e33aac8abd8904f41ed21872c20f38f5e4`.

- `exists_norm_atkinsonLeadingTerm_sub_stationary_le` at line 24
- `exists_norm_atkinsonLeadingFiniteSum_sub_stationary_mass_le` at line 79
- `exists_norm_atkinsonLeadingFiniteSum_sub_stationary_le` at line 99

### MathCollab.Density.Stronger.Atkinson.AtkinsonStationarySumScale

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonStationarySumScale.lean`; 69 source lines; SHA-256 `1046e8d0e14f2cb24114d817d0e09589729273f45cb74efe07dc789120ad17d6`.

- `atkinsonStationary_scale_identity` at line 23
- `atkinsonStationary_cutoff_scale_le` at line 42

### MathCollab.Density.Stronger.Atkinson.AtkinsonFiniteSourceError

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonFiniteSourceError.lean`; 86 source lines; SHA-256 `e392e39e6320fd214c801976cf0799457d953a35c4625b6a3fe1d86e1a5b07c8`.

- `exists_atkinsonStationary_finite_log_error` at line 22
- `exists_atkinsonStationary_finite_power_error` at line 59

### MathCollab.Density.Stronger.Atkinson.AtkinsonStationarySumError

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonStationarySumError.lean`; 55 source lines; SHA-256 `653c4f84fbb355e5603c982803adf0f5c3737ce90e15522a94f4770ccb116df5`.

- `exists_atkinsonLeadingSum_sub_stationary_bound` at line 22
- `exists_atkinsonLeadingSum_sub_stationary_above_fourthRoot` at line 40

### MathCollab.Density.Stronger.Atkinson.AtkinsonTwoTermStationary

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonTwoTermStationary.lean`; 67 source lines; SHA-256 `6820f610c50d66e687574ff97d85bad4eea304d2afb57ac058e0fbc8b9060572`.

- `exists_tsum_zetaAtkinsonTwoTerm_sub_leading_bound` at line 25
- `exists_tsum_zetaAtkinsonTwoTerm_sub_stationary_above_fourthRoot` at line 49

### MathCollab.Density.Stronger.Atkinson.AtkinsonSignedSaddleProfile

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSignedSaddleProfile.lean`; 51 source lines; SHA-256 `e5b093ff1f1e1725daa6155194b1668edd04dd524c90d8ae6590df342b39d732`.

- `atkinsonSaddleProfile` at line 23
- `atkinsonRootKernel_at_saddle` at line 29
- `atkinsonPowerWeight_at_saddle` at line 38
- `atkinsonPowerWeight_at_neg_saddle` at line 44

### MathCollab.Density.Stronger.Atkinson.AtkinsonEvaluatedPhases

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonEvaluatedPhases.lean`; 79 source lines; SHA-256 `246839e1e046477a5228553dae0e5c3b0bfacd25b63459c9a51aa70379cc0252`.

- `exp_positive_saddle_mul_fresnel` at line 22
- `exp_negative_saddle_mul_fresnel` at line 30
- `atkinsonStationaryMain_sqrt` at line 41
- `atkinsonStationaryMain_neg_sqrt` at line 60

### MathCollab.Density.Stronger.Atkinson.AtkinsonResidualVariation

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonResidualVariation.lean`; 100 source lines; SHA-256 `7beb5de97ed2742a55ff7acdd23bc9f3dba183cab3455f6bb1cbfb68cb638f7f`.

- `atkinsonSaddleResidual` at line 24
- `zetaMainMellinProfile_saddle_eq_root` at line 28
- `exists_finiteVariationBound_saddleMellin` at line 35
- `finiteVariationBound_saddleCutoff` at line 61
- `exists_finiteVariationBound_saddleResidual` at line 82

### MathCollab.Density.Stronger.Atkinson.AtkinsonSaddleProfileNormalization

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSaddleProfileNormalization.lean`; 67 source lines; SHA-256 `19267415190190d68b8dd4c4b66f77dcd50ff390ae9fcc413989adffdb80496a`.

- `atkinsonSaddle_quarter_power_curvature` at line 24
- `atkinsonSaddleProfile_div_curvature` at line 47

### MathCollab.Density.Stronger.Atkinson.AtkinsonMainNormalization

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonMainNormalization.lean`; 54 source lines; SHA-256 `4fd977885b54e647b18f2137210139c7f0e3a74f21f8a178c5039e6629a1b1f3`.

- `atkinsonStationaryMain_sqrt_normalized` at line 22
- `atkinsonStationaryMain_neg_sqrt_normalized` at line 37

### MathCollab.Density.Stronger.Atkinson.AtkinsonMainVariation

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonMainVariation.lean`; 61 source lines; SHA-256 `3269618492df0e0ef88981d9a0d624d02597506f915b2f163ca2101cfb1c231d`.

- `atkinsonPositiveMainWeight` at line 24
- `atkinsonNegativeMainWeight` at line 28
- `exists_finiteVariationBound_atkinsonMainWeights` at line 32

### MathCollab.Density.Stronger.Atkinson.AtkinsonSignedPhaseSeries

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSignedPhaseSeries.lean`; 101 source lines; SHA-256 `d20cfe805ab8f74506f3e7b1529df3c907b39dfa204cf1c251c95445191a4451`.

- `atkinsonNegativePhaseTerm` at line 25
- `atkinsonPositiveMainSum` at line 28
- `atkinsonNegativeMainSum` at line 31
- `atkinsonCommonMainPhase` at line 34
- `atkinsonStationaryLeadingTerm_eq_signed` at line 37
- `atkinsonStationaryLeadingFiniteSum_eq_signed` at line 58
- `atkinsonStationaryLeadingSum_eq_signed` at line 67
- `norm_atkinsonCommonMainPhase_le` at line 76
- `norm_atkinsonStationaryLeadingSum_le_signed` at line 84
- `atkinsonNegativePhaseTerm_eq_conj` at line 93

### MathCollab.Density.Stronger.Atkinson.TruncatedDyadicPartition

File: `lean/MathCollab/Density/Stronger/Atkinson/TruncatedDyadicPartition.lean`; 85 source lines; SHA-256 `8633144cca7e8e266047cf53d81d3b5caf639588c56acad76e1afa7287e0388c`.

- `truncatedDyadicLength` at line 23
- `truncatedDyadicLength_le_width` at line 25
- `truncatedDyadic_start_lt` at line 28
- `truncatedDyadic_endpoint_le` at line 31
- `truncatedDyadicLength_pos` at line 37
- `truncatedDyadicLength_eq_width` at line 44
- `sum_range_min_pow_eq_truncatedDyadic` at line 50
- `sum_range_eq_truncatedDyadic` at line 74

### MathCollab.Density.Stronger.Atkinson.FiniteWeightedGram

File: `lean/MathCollab/Density/Stronger/Atkinson/FiniteWeightedGram.lean`; 168 source lines; SHA-256 `041a2871284ab4c38dc5993bb2942c1d682b0145f6f0cdd7482216f0b17e6349`.

- `phaseAlign` at line 24
- `norm_conj_eq` at line 26
- `norm_phaseAlign_le_one` at line 30
- `phaseAlign_mul` at line 38
- `norm_sum_mul_sq_le` at line 52
- `sum_norm_sq_sum_le_gram` at line 64
- `sum_norm_coefficient_vector_sq_le_gram` at line 127
- `card_mul_lower_sq_le_coefficient_gram` at line 155

### MathCollab.Density.Stronger.Atkinson.AtkinsonWeightedGram

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonWeightedGram.lean`; 102 source lines; SHA-256 `6860188785925a3bbbfea1c3dcf82194303c36157e0c04a2d3fb0039864c8071`.

- `atkinsonPhaseBlockMax` at line 25
- `norm_atkinsonPhaseBlockSum_le_max` at line 28
- `atkinsonPhaseBlockMax_nonneg` at line 34
- `exists_atkinsonPhaseBlockMax_prefix` at line 40
- `atkinsonMaximizingPrefix` at line 46
- `atkinsonMaximizingPrefix_le` at line 49
- `atkinsonMaximizingPrefix_spec` at line 53
- `sum_atkinsonPhaseBlockMax_sq_le_selectedGram` at line 58
- `sum_atkinsonPhaseBlockMax_sq_le_gramMax` at line 80
- `card_mul_atkinsonPhaseBlockMax_lower_sq_le_gramMax` at line 93

### MathCollab.Density.Stronger.Atkinson.AtkinsonCoefficientEnergy

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonCoefficientEnergy.lean`; 69 source lines; SHA-256 `5079ec1dad6f05251cc801241d24a5b118028a0842de9ba607f162d7d61149a1`.

- `exists_atkinsonBlockCoefficientEnergy_le` at line 24
- `exists_sum_atkinsonPhaseBlockMax_sq_le_arithmeticGram` at line 58

### MathCollab.Density.Stronger.Atkinson.AtkinsonDyadicGramBudget

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonDyadicGramBudget.lean`; 78 source lines; SHA-256 `50cbc169c631735ac43336f25aa2a6b4730b81a15f91a6afc6cc1b50ac352437`.

- `atkinsonUndampedDyadicPhaseBound` at line 25
- `atkinsonUndampedDyadicPhaseBound_nonneg` at line 29
- `atkinsonUndampedDyadicPhaseBound_mono` at line 34
- `atkinsonDyadicGramBudget` at line 40
- `atkinsonDyadicGramBudget_nonneg` at line 45
- `sum_atkinsonUndampedDyadicPhaseBound_sq_le_budget` at line 54

### MathCollab.Density.Stronger.Atkinson.AtkinsonDampedDyadic

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonDampedDyadic.lean`; 78 source lines; SHA-256 `74045354e21ae8204ef1e5a3243e29bf6961ed2ad3dee007c9d736a16c07d17f`.

- `atkinsonDyadicPhaseBound` at line 22
- `atkinsonDyadicPhaseBound_nonneg` at line 27
- `atkinsonPhaseBlockMax_mono` at line 34
- `atkinsonFullDyadicPhaseBound` at line 44
- `atkinsonFullDyadicPhaseBound_nonneg` at line 49
- `atkinsonDyadicPhaseBound_le_full` at line 56
- `atkinsonFullDyadicPhaseBound_le_undamped` at line 64

### MathCollab.Density.Stronger.Atkinson.AtkinsonStationaryBlockBound

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonStationaryBlockBound.lean`; 87 source lines; SHA-256 `7cd00f1790627c20d62517fb022b749cc9dc7cde6b7a47e6dfc8ecdf07bcfc63`.

- `atkinsonStationaryBlock` at line 23
- `norm_atkinsonNegativePhaseBlockSum` at line 26
- `atkinsonStationaryBlock_eq_signed` at line 32
- `exists_norm_atkinsonStationaryBlock_le` at line 41
- `exists_atkinsonSourceCutoff_block_bound` at line 61

### MathCollab.Density.Stronger.Atkinson.AtkinsonStationaryDyadic

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonStationaryDyadic.lean`; 110 source lines; SHA-256 `4dc97e320694879fe12e8b37d41092808dd9ff749c9f8f3535a66616ab8aae21`.

- `atkinsonStationaryLeadingFiniteSum_eq_dyadic` at line 24
- `norm_atkinsonStationaryLeadingFiniteSum_le_blocks` at line 31
- `exists_norm_atkinsonStationaryFiniteSum_le_dyadic` at line 38
- `exists_norm_atkinsonStationarySum_le_dyadic` at line 57
- `exists_norm_atkinsonStationarySum_le_fullDyadic` at line 81
- `exists_norm_atkinsonStationarySum_le_undamped` at line 96

### MathCollab.Density.Stronger.Atkinson.AtkinsonNearGap

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonNearGap.lean`; 119 source lines; SHA-256 `ba8a27bb68e9596f3ed291ff23eb62a7bc442fa054634a6976e19b472a1b420a`.

- `atkinson_mul_sqrt_div` at line 30
- `atkinson_near_slope_lower` at line 37
- `atkinson_near_slope_upper` at line 52
- `atkinson_near_half_period` at line 66
- `atkinsonOrderedPrefixGapMajorant_le_near` at line 81
- `atkinsonPrefixGapMajorant_le_near` at line 104

### MathCollab.Density.Stronger.Atkinson.SeparatedReciprocal

File: `lean/MathCollab/Density/Stronger/Atkinson/SeparatedReciprocal.lean`; 149 source lines; SHA-256 `97c5e704e0f9fc64c4de5f84672f3d09dadbf34c94cc9c9a6471196f4443196a`.

- `IsSeparated` at line 25
- `separated_subset_card_le_one_of_diameter` at line 28
- `separated_annulus_card_le_two` at line 40
- `sum_inv_distance_near_le_harmonic` at line 79

### MathCollab.Density.Stronger.Atkinson.AtkinsonSeparatedReciprocal

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSeparatedReciprocal.lean`; 82 source lines; SHA-256 `3fd90f58616b2e7e2445a5f95f79a3a83d17c1dfa748274dea4800bc27fe6e2f`.

- `atkinson_isSeparated_div` at line 24
- `atkinson_sum_inv_gap_le_harmonic` at line 37
- `atkinson_sum_inv_gap_le_harmonic_ceil` at line 71

### MathCollab.Density.Stronger.Atkinson.AtkinsonGapBudget

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonGapBudget.lean`; 72 source lines; SHA-256 `8e976165602bcaedcbf5d0fd7fbed68e8662793df6915fdc65bc813e1c358bf7`.

- `atkinsonDyadicGapBudget` at line 24
- `atkinsonDyadicGramBudget_le_gapBudget` at line 29
- `atkinsonDyadicGapBudget_empty` at line 45
- `atkinsonDyadicGapBudget_zero` at line 49
- `exists_atkinsonPhysicalGramBudget_le_gapBudget` at line 53

### MathCollab.Density.Stronger.Atkinson.AtkinsonGapArithmetic

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonGapArithmetic.lean`; 100 source lines; SHA-256 `c4ccb26376d4a7d926de0f3d3e16e54fccd61f63333b6bbbb00ea3a9aecc5cc6`.

- `atkinsonArithmeticGapBudget` at line 24
- `atkinsonArithmeticGapBudget_empty` at line 29
- `atkinsonArithmeticGapBudget_zero` at line 33
- `atkinson_quarter_energy_power` at line 37
- `exists_atkinsonGapBudget_le_arithmetic` at line 43
- `exists_atkinsonPhysicalGapBudget_le_arithmetic` at line 78

### MathCollab.Density.Stronger.Atkinson.AtkinsonNearGapBudget

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonNearGapBudget.lean`; 121 source lines; SHA-256 `0832ccccd6dc4964378a4829ae63f254e41ca28f2605ab397725a76f02db5ba7`.

- `atkinsonFarGapRow` at line 25
- `atkinsonNearRowBound` at line 29
- `atkinson_near_gap_row_le` at line 33
- `atkinson_gap_row_le_near_add_far` at line 59
- `atkinson_gap_double_sum_le_near_add_far` at line 90
- `atkinsonSeparatedGapBudget` at line 100
- `atkinsonSeparatedGapBudget_empty` at line 106
- `atkinsonArithmeticGapBudget_le_separated` at line 110

### MathCollab.Density.Stronger.Atkinson.AtkinsonFarCurvature

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonFarCurvature.lean`; 92 source lines; SHA-256 `168666370ef3c5b103a07567f8a6809bec6d235ad7de2787a845906e20da30de`.

- `atkinson_far_slope_lower` at line 28
- `atkinson_far_box_curvature_bounds` at line 40
- `atkinson_far_lambda_bounds` at line 76

### MathCollab.Density.Stronger.Atkinson.AtkinsonFarRadical

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonFarRadical.lean`; 97 source lines; SHA-256 `a368cfedbdb127161e14661ee14840165f6950ecf9d9d3169f3c7e315cc17867`.

- `atkinson_far_inverse_sqrt` at line 29
- `atkinson_far_second_factor` at line 42
- `atkinson_far_radical_identity` at line 56
- `atkinson_far_min_bProcess` at line 64

### MathCollab.Density.Stronger.Atkinson.AtkinsonFarGap

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonFarGap.lean`; 71 source lines; SHA-256 `8a7df99c6d69b38cc49030bfa88e32af1856ddc91f9596a5498d1cc27cc738ee`.

- `atkinsonOrderedPrefixGapMajorant_le_min_bProcess` at line 29
- `atkinsonOrderedPrefixGapMajorant_le_far` at line 36
- `atkinsonPrefixGapMajorant_le_far` at line 48

### MathCollab.Density.Stronger.Atkinson.AtkinsonLocalizedGapBudget

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonLocalizedGapBudget.lean`; 95 source lines; SHA-256 `e11aea2a66ccbc136147993d53becfe02c6b26f7273a66a19ff75ade57d6bc3c`.

- `atkinson_far_gap_row_le` at line 25
- `atkinson_far_gap_double_sum_le` at line 55
- `atkinsonLocalizedGapBudget` at line 66
- `atkinsonLocalizedGapBudget_zero_card` at line 72
- `atkinsonSeparatedGapBudget_le_localized` at line 76
- `atkinson_height_interval_diameter` at line 89

### MathCollab.Density.Stronger.Atkinson.AtkinsonLocalizedPowers

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonLocalizedPowers.lean`; 64 source lines; SHA-256 `85b49f264cffb265124ab15b5bf4954836a56ff42ec9fa6c72971dd04d638640`.

- `atkinson_far_radical_eq_rpow` at line 24
- `atkinson_weighted_diagonal_power` at line 44
- `atkinson_weighted_near_power` at line 50
- `atkinson_weighted_far_power` at line 57

### MathCollab.Density.Stronger.Atkinson.AtkinsonPowerGapBudget

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonPowerGapBudget.lean`; 99 source lines; SHA-256 `b3c2bf0913bac3eeb58040bb1c1f16015b67d6cf4f19b844ceb1a98a8c433b05`.

- `atkinson_harmonic_mono` at line 24
- `atkinsonPowerGapTerm` at line 31
- `atkinsonPowerGapBudget` at line 37
- `atkinson_localized_gap_term_eq` at line 40
- `atkinsonPowerGapTerm_mono_index` at line 57
- `atkinsonLocalizedGapBudget_le_power` at line 80
- `atkinsonPowerGapBudget_zero_card` at line 96

### MathCollab.Density.Stronger.Atkinson.AtkinsonLocalizedGram

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonLocalizedGram.lean`; 80 source lines; SHA-256 `89f5858e402e87dc861bc490f3f828a6b9cf1145e525e2b2ede0c476c17c348a`.

- `exists_atkinsonPhysicalGramBudget_le_power` at line 24
- `exists_sum_atkinsonUndampedDyadicPhaseBound_sq_le_power` at line 64

### MathCollab.Density.Stronger.Atkinson.AtkinsonPhysicalBudget

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonPhysicalBudget.lean`; 319 source lines; SHA-256 `d206437cdf3a17e5a47b53a222e2547725d016f397ebf8dc53a35686b5ce44a3`.

- `atkinson_clog_le_height_log` at line 28
- `atkinson_harmonic_le_height_log` at line 49
- `eventually_atkinson_height_log_pow_le_rpow` at line 69
- `atkinsonPhysicalCutoff_le_natural` at line 84
- `atkinsonPhysical_cutoff_scale_identity` at line 92
- `atkinsonPhysical_diagonal_scale` at line 107
- `atkinsonPhysical_near_scale` at line 123
- `atkinsonPhysical_far_scale` at line 136
- `atkinsonPowerGapTerm_epsilon_factor` at line 165
- `atkinsonPhysical_gap_term_zero_le` at line 174
- `atkinsonPhysical_gap_budget_log_le` at line 233
- `exists_atkinsonPhysicalGapBudget_le_twoTerm` at line 271

### MathCollab.Density.Packing

File: `lean/MathCollab/Density/Packing.lean`; 157 source lines; SHA-256 `ca2606c1c44570bc917e81ac34b3d32ea523a67924401b603f798ee7077dfa4a`.

- `intervalSpan_nonneg` at line 18
- `localDiameter_ge_one` at line 24
- `abs_sub_le_intervalSpan` at line 29
- `intervalSpan_le_of_forall` at line 39
- `separated_floor_shift_injOn` at line 46
- `separated_card_le_localDiameter` at line 61
- `separationMass` at line 96
- `summable_separation_majorant` at line 98
- `separationMass_nonneg` at line 110
- `decay_le_floor_majorant` at line 113
- `separated_decay_row` at line 127
- `separated_decay_pairs` at line 139
- `LargeValueData.local_card_le` at line 145

### MathCollab.Density.Stronger.MomentPower

File: `lean/MathCollab/Density/Stronger/MomentPower.lean`; 72 source lines; SHA-256 `dfdd486b0edcfd58152538d709840fab7dcce6d77a1c143a82a1b0a33d51848e`.

- `twelfth_tangent_bound` at line 25
- `integral_weighted_twelfth` at line 45

### MathCollab.Density.Stronger.SeparatedMoment

File: `lean/MathCollab/Density/Stronger/SeparatedMoment.lean`; 123 source lines; SHA-256 `b6ea2c9ff4b93490b0751fc43c913a851459db36f751359bbba658e137cea912`.

- `momentDecay` at line 18
- `momentDecay_pos` at line 20
- `momentDecay_le_one` at line 24
- `momentDecay_antitone` at line 29
- `momentDecay_continuous` at line 35
- `momentDecay_le_inv_one_add_sq` at line 41
- `integrable_momentDecay` at line 49
- `momentDecay_mass_bounds` at line 56
- `momentDecay_holder_twelfth` at line 74
- `separated_momentDecay_row` at line 87
- `integrable_momentDecay_mul` at line 95
- `separated_momentDecay_integral_le` at line 109

### MathCollab.Density.Stronger.SmoothPartition

File: `lean/MathCollab/Density/Stronger/SmoothPartition.lean`; 201 source lines; SHA-256 `f2d75db09814766c6a640313025d8e28b1cf558df31e5ed25d7fb2bc0ee218cb`.

- `dyadicStep` at line 22
- `dyadicStep_contDiff` at line 24
- `dyadicStep_bounds` at line 28
- `dyadicStep_antitone` at line 34
- `dyadicStep_one` at line 40
- `dyadicStep_zero` at line 44
- `smoothDyadicWeight` at line 50
- `smoothDyadicWeight_contDiff` at line 52
- `smoothDyadicWeight_zero_of_le` at line 56
- `smoothDyadicWeight_zero_of_ge` at line 61
- `smoothDyadicWeight_bounds` at line 66
- `smoothDyadicWeight_tsupport` at line 77
- `smoothDyadicWeight_support_open` at line 88
- `smoothDyadicWeight_hasCompactSupport` at line 94
- `smoothDyadicWeight_div_pow_succ` at line 97
- `dyadicStep_div_pow_tendsto` at line 105
- `hasSum_smoothDyadicWeight_nonneg_scales` at line 114
- `dyadicStep_mul_pow_tendsto` at line 128
- `hasSum_smoothDyadicWeight_neg_scales` at line 137
- `hasSum_smoothDyadicWeight` at line 151
- `tsum_smoothDyadicWeight` at line 163
- `smoothDyadicWeight_index_bounds` at line 169
- `smoothDyadicWeight_pointwise_finite` at line 193

### MathCollab.Density.Stronger.SmoothExpansion

File: `lean/MathCollab/Density/Stronger/SmoothExpansion.lean`; 178 source lines; SHA-256 `4b3298d22c0d123357c9d613a1c341331a33a34808c6c53b69548a7f9ae5ec88`.

- `smoothDyadicTerm` at line 21
- `smoothDyadicBlock` at line 24
- `norm_smoothDyadicTerm` at line 26
- `hasSum_norm_smoothDyadicTerm` at line 32
- `hasSum_smoothDyadicTerm` at line 37
- `summable_norm_smoothDyadicTerm` at line 46
- `summable_smoothDyadicTerm` at line 53
- `summable_smoothDyadicBlock` at line 58
- `summable_norm_smoothDyadicBlock` at line 62
- `tsum_smoothDyadicBlock` at line 71
- `tsum_norm_smoothDyadicBlock_le` at line 78
- `smoothDyadicTerm_zero_of_nonpos` at line 90
- `smoothDyadicBlock_zero_of_nonpos` at line 99
- `smoothDyadicTerm_zero_of_large_index` at line 105
- `smoothDyadicTerm_hasFiniteSupport` at line 116
- `smoothDyadicBlock_eq_sum_range` at line 124
- `smoothDyadicBlock_scale_tail_le` at line 133

### MathCollab.Density.ZetaCounting

File: `lean/MathCollab/Density/ZetaCounting.lean`; 113 source lines; SHA-256 `42056c6abc53d7ad4d5d8d0450c390c72fc4e0bbe0d79bda2ac225003fdad4f9`.

- `IsNontrivialZetaZero` at line 19
- `zetaMultiplicity` at line 24
- `zeta_analyticOrder_ne_top` at line 26
- `nontrivialZetaZero_ne_one` at line 34
- `zetaMultiplicity_cast` at line 39
- `zetaMultiplicity_pos` at line 43
- `zetaMultiplicity_local_factorization` at line 49
- `zetaZeroRegion` at line 56
- `zetaZeroRegion_finite` at line 59
- `zetaZeroFinset` at line 75
- `mem_zetaZeroFinset` at line 77
- `zetaSlabCount` at line 83
- `zetaDensityCount` at line 87
- `mem_zetaDensityFinset` at line 89
- `zetaZeroFinset_card_le_count` at line 94
- `zetaSlabCount_mono` at line 101
- `zetaDensityCount_mono` at line 109

### MathCollab.Density.ZeroSeparation

File: `lean/MathCollab/Density/ZeroSeparation.lean`; 130 source lines; SHA-256 `24dd746d6dd4725fd6cc3a4285726d8d4490885fa94a525f6b186dc53fd3dc62`.

- `ordinateBin` at line 19
- `ordinateBin_eq_iff` at line 21
- `occupied_bins_parity` at line 26
- `same_parity_bins_separated` at line 43
- `weighted_separated_extraction` at line 61
- `zetaSlab_separated_representatives` at line 119

### MathCollab.Density.ReflectionApplication

File: `lean/MathCollab/Density/ReflectionApplication.lean`; 118 source lines; SHA-256 `a3d0cdc595a86b80977c8c3c5af65268c480c7dc18e75412babff6c5f538a3b8`.

- `localSet_localDiameter_le` at line 17
- `reflection_recursive_scale` at line 27
- `reflection_scale_error_power` at line 45
- `reflection_error_specialization` at line 55
- `uniform_reflection_application` at line 83

### MathCollab.Density.BootstrapDomain

File: `lean/MathCollab/Density/BootstrapDomain.lean`; 72 source lines; SHA-256 `c19c7596a01c5734962db517075a1d6b654add1f481b0cd6c65b4634dfcd3fd5`.

- `LargeValueData.scalar_lower` at line 18
- `LargeValueData.scalar_pos` at line 31
- `bootstrapFamily` at line 36
- `mem_bootstrapFamily` at line 38
- `bootstrapFamily_nonempty` at line 42
- `localSet_subset_original` at line 45
- `bootstrapFamily_local_closed` at line 48
- `LargeValueData.normalization_lower` at line 54

### MathCollab.Density.ComparisonAlgebra

File: `lean/MathCollab/Density/ComparisonAlgebra.lean`; 98 source lines; SHA-256 `bb092693917f9167eefffc8e1e069478e3bb567fcfa635ecd579d85b93a2ce75`.

- `completePairEnergy_gram` at line 19
- `completePairEnergy_diagonal_lower` at line 30
- `norm_sum_mul_sq_le` at line 49
- `detecting_insertion_bound` at line 63
- `normalized_product_phase` at line 89

### MathCollab.Density.ComparisonExpansion

File: `lean/MathCollab/Density/ComparisonExpansion.lean`; 89 source lines; SHA-256 `39b785be5efa28f6d2bb9d3aa640e5b6da8d3d42fce7d93eeb1497e38446dc95`.

- `weighted_mode_expansion` at line 17
- `cutoff_finite_sum` at line 42
- `comparisonExtension` at line 57
- `comparisonExtension_nonneg` at line 63
- `comparisonExtension_identity` at line 67

### MathCollab.Density.BootstrapSupremum

File: `lean/MathCollab/Density/BootstrapSupremum.lean`; 116 source lines; SHA-256 `da85ffd7d1f378e69cef75a0cffd96c962b9ec4cc3c61859e84fbd542c8d7f1b`.

- `crude_kernel_bound` at line 19
- `bootstrapValues` at line 54
- `bootstrapBound` at line 59
- `bootstrapValues_nonempty` at line 62
- `bootstrapValues_bddAbove` at line 67
- `bootstrapBound_nonneg` at line 92
- `kernelEnergy_le_bootstrapBound` at line 102

### MathCollab.Density.Comparison

File: `lean/MathCollab/Density/Comparison.lean`; 207 source lines; SHA-256 `26a8e31f4e39821badb7397e2da1cea9ec5e7950fe789330e00f368e533fd17c`.

- `comparison_extension_bound` at line 18
- `dyadicPolynomial_norm_le` at line 57
- `detecting_pair_division_bound` at line 63
- `bootstrapScalar_nonneg` at line 78
- `comparison_continuous_bound` at line 83
- `comparison_remainder_bound` at line 132
- `uniform_comparison` at line 173

### MathCollab.Density.BootstrapShell

File: `lean/MathCollab/Density/BootstrapShell.lean`; 157 source lines; SHA-256 `3b2105ba854d49c54718b7bbf1ec407e61a85beeb8d0d5f1ec04ea8871703675`.

- `comparisonConstant` at line 18
- `comparisonConstant_nonneg` at line 20
- `local_comparison_from_supremum` at line 23
- `reflectionBlock_scaled_square` at line 62
- `localReflectionEnergy_from_supremum` at line 74
- `bootstrap_one_shell` at line 121

### MathCollab.Density.BootstrapShells

File: `lean/MathCollab/Density/BootstrapShells.lean`; 135 source lines; SHA-256 `f18090e9b66f7839f564bea1112bf663b674899543e4e64cb79152c4a32bcaac`.

- `shellIndices` at line 17
- `shellIndex_bounds` at line 20
- `exists_shellIndex` at line 24
- `shellIndices_sum_le` at line 40
- `shellIndices_card_le_log` at line 58
- `shellIndices_card_le_diameter` at line 82
- `shellEnergy_nonneg` at line 92
- `kernelEnergy_le_dyadic_shells` at line 101

### MathCollab.Density.BootstrapAbsorption

File: `lean/MathCollab/Density/BootstrapAbsorption.lean`; 149 source lines; SHA-256 `0377257f975b5862480e0bed47f4c83828702d2b15a83ce583c42fd11d3bed2d`.

- `bootstrap_preabsorption` at line 18
- `bootstrap_absorption_inequality` at line 84
- `bootstrap_absorbed` at line 137

### MathCollab.Density.UniformThreshold

File: `lean/MathCollab/Density/UniformThreshold.lean`; 128 source lines; SHA-256 `7490058189b43e567c37205c8a4b3f7a4d40fd342b1b168bf93b900f1e741902`.

- `LargeValueData.scalar_square_le` at line 18
- `uniform_scalar_decay` at line 40
- `tendsto_power_log_two_mul` at line 67
- `uniform_absorption_threshold` at line 79
- `uniform_absorbed_kernel` at line 102

### MathCollab.Density.LargeValuesOptimization

File: `lean/MathCollab/Density/LargeValuesOptimization.lean`; 133 source lines; SHA-256 `3035b727187f06c47a7372db364b074c6629e9383092a13557972a18ad4c4cc1`.

- `cardinality_at_length` at line 17
- `optimal_integer_scale` at line 53
- `large_values_with_divisors` at line 100

### MathCollab.Density.LargeValues

File: `lean/MathCollab/Density/LargeValues.lean`; 99 source lines; SHA-256 `147fd08f423325b76d854a5d0173245a6df43a9173fddae87e35e905d344cd16`.

- `large_values_data` at line 17
- `large_values` at line 81

### MathCollab.Density.ZeroLargeValues

File: `lean/MathCollab/Density/ZeroLargeValues.lean`; 75 source lines; SHA-256 `eb5248569ee5a8c97ac9aa43a002d501adfe797ca7a57717b981ce703d2925e0`.

- `zetaSlab_large_values_cover` at line 22

### MathCollab.Density.MollifierCoefficients

File: `lean/MathCollab/Density/MollifierCoefficients.lean`; 64 source lines; SHA-256 `38803f4c61b1c904147958ad392abc585bff480fe2364281d43d3d1c956d18e0`.

- `zetaMollifier` at line 20
- `mollifierCoefficient` at line 24
- `mollifierCoefficient_eq_full` at line 27
- `mollifierCoefficient_one` at line 34
- `mollifierCoefficient_vanishes` at line 39
- `mollifierCoefficient_abs_le` at line 47
- `mollifierCoefficient_norm_le` at line 58

### MathCollab.Density.DetectorParameters

File: `lean/MathCollab/Density/DetectorParameters.lean`; 63 source lines; SHA-256 `d9c44ed3d03bcb41fbb9a60bd015c1856378c871c9459c172a90676722361866`.

- `firstDetectorX` at line 19
- `firstDetectorY` at line 21
- `first_detector_error_scale` at line 24
- `first_detector_majorant_tendsto_zero` at line 45
- `density_margin_choice` at line 52

### MathCollab.Density.Stronger.Parameters

File: `lean/MathCollab/Density/Stronger/Parameters.lean`; 111 source lines; SHA-256 `81de67c3a666fd9c3d36a805e10400fa517dda17d8f5cdd1a40cc438465a5c9e`.

- `lowerExponent` at line 17
- `smoothingExponent` at line 20
- `densityExponent` at line 23
- `detectorX` at line 25
- `detectorY` at line 27
- `smoothingExponent_pos` at line 29
- `smoothingExponent_lt_one` at line 35
- `smoothingExponent_eq` at line 41
- `densityExponent_pos` at line 46
- `densityExponent_lt_density_hypothesis` at line 52
- `exists_detector_exponent` at line 60
- `short_exponent_identities` at line 70
- `long_exponent_identity` at line 77
- `long_exponent_saving` at line 84
- `detector_error_scale` at line 92

### MathCollab.Density.MollifierDirichlet

File: `lean/MathCollab/Density/MollifierDirichlet.lean`; 164 source lines; SHA-256 `0a6d30240292d997c2f125052bc7b9e85d07d486a20c96197f237ecdd3206445`.

- `mollifierDirichletCoeff` at line 23
- `truncatedMoebius` at line 26
- `truncatedMoebius_apply` at line 32
- `truncatedMoebius_hasFiniteSupport` at line 36
- `truncatedMoebius_LSeriesSummable` at line 45
- `zetaMollifier_eq_LSeries` at line 58
- `zeta_mul_truncatedMoebius_apply` at line 70
- `riemannZeta_mul_zetaMollifier_eq_LSeries` at line 89
- `mollifierDirichletCoeff_LSeriesSummable` at line 117
- `mollifierDirichletCoeff_zero` at line 129
- `norm_mollifierDirichletCoeff_le_cutoff` at line 133
- `differentiableAt_zetaMollifier` at line 154

### MathCollab.Density.DetectorMellin

File: `lean/MathCollab/Density/DetectorMellin.lean`; 474 source lines; SHA-256 `86c6af9f240df18f248348e36f2f386b14e8eb348667d195e790f41dc31f0fc9`.

- `integrable_tsum_of_summable_integral_norm` at line 22
- `smoothedDetector` at line 61
- `norm_mollifier_LSeries_term_le_cutoff` at line 65
- `summable_smoothedDetector` at line 81
- `hasSum_smoothedDetector` at line 105
- `norm_LSeries_term_div_rpow_eq_add` at line 113
- `Gamma_mul_term_div_cpow_eq_add` at line 124
- `mellin_smoothedDetector_eq` at line 137
- `detectorPSeries` at line 178
- `summable_detectorPSeries` at line 181
- `detectorPSeries_nonneg` at line 185
- `norm_mollifier_LSeries_le_cutoff_pSeries` at line 188
- `verticalIntegrable_mellin_smoothedDetector` at line 230
- `continuousAt_smoothedDetector` at line 300
- `mellinConvergent_smoothedDetector` at line 355
- `smoothedDetector_eq_mellinInv` at line 433
- `detectorKernel` at line 449
- `smoothedDetector_eq_rightContour` at line 454

### MathCollab.Density.DetectorGamma

File: `lean/MathCollab/Density/DetectorGamma.lean`; 175 source lines; SHA-256 `6f4667dfd26c4ce48a8152997d1b1071934eedd88f97f36d15c4678414e0e418`.

- `norm_Gamma_detector_strip` at line 20
- `continuous_Gamma_detector_strip` at line 46
- `norm_Gamma_contour_strip` at line 65
- `norm_Gamma_one_sub_zero_le` at line 107
- `detectorGammaMajorant` at line 117
- `integrable_detectorGammaMajorant` at line 119
- `uniform_detector_gamma_mass` at line 145

### MathCollab.Density.DetectorContour

File: `lean/MathCollab/Density/DetectorContour.lean`; 292 source lines; SHA-256 `db2dd23d8919b64d312773ec0b9e475beaf01f56bba9afc7e7bc868fd28fff7e`.

- `shiftedRegularizedZeta` at line 25
- `zetaZeroQuotient` at line 30
- `detectorContourNumerator` at line 36
- `detectorResidue` at line 41
- `shiftedRegularizedZeta_zero` at line 45
- `shiftedRegularizedZeta_eq` at line 51
- `detectorContourNumerator_div_eq_integrand` at line 61
- `detectorContourNumerator_at_pole` at line 94
- `differentiableAt_shiftedRegularizedZeta` at line 122
- `differentiableAt_zetaZeroQuotient` at line 128
- `differentiableOn_detectorContourNumerator` at line 141
- `detector_finite_rectangle_residue` at line 169
- `detector_finite_rectangle_kernel` at line 235

### MathCollab.Density.DetectorEstimates

File: `lean/MathCollab/Density/DetectorEstimates.lean`; 223 source lines; SHA-256 `78e0dcee51b0b61e52795b9115f2095082744ee9348b3c3d06b91d531d891235`.

- `norm_zetaMollifier_le_cutoff` at line 19
- `norm_riemannZeta_critical_le_linear` at line 38
- `integrable_detectorKernel_right` at line 65
- `integrable_detectorKernel_left` at line 93
- `norm_detectorKernel_horizontal` at line 144
- `tendsto_detector_horizontal_majorant` at line 184
- `tendsto_detector_horizontal_integral` at line 197

### MathCollab.Density.DetectorIdentity

File: `lean/MathCollab/Density/DetectorIdentity.lean`; 109 source lines; SHA-256 `8bc3a69bc154f34a7abf2298b86b75e99eb46eac4ecd0bf4e48ce7322ec15200`.

- `smoothedDetector_contour_identity` at line 19
- `smoothedDetector_term_eq` at line 63
- `summable_zeta_detector_series` at line 70
- `zeta_detector_identity` at line 79

### MathCollab.Density.MollifierBound

File: `lean/MathCollab/Density/MollifierBound.lean`; 56 source lines; SHA-256 `67469523d9bb071560c356e44e03911486dd38a3480b947136b3eca78c822014`.

- `sum_inv_sqrt_le` at line 16
- `norm_zetaMollifier_le_two_sqrt` at line 34

### MathCollab.Density.DetectorError

File: `lean/MathCollab/Density/DetectorError.lean`; 173 source lines; SHA-256 `88ad8aead12cf1b4d6da728d981a7e4ab7348ec60cdd955735cd36336a51ccae`.

- `detectorIntegral` at line 18
- `detector_shifted_rpow_le` at line 23
- `uniform_detector_integral_bound` at line 40
- `norm_detectorResidue_le` at line 91
- `norm_firstDetector_residue_le` at line 106
- `firstDetector_residue_eventually_small` at line 132
- `firstDetector_eventually_small_of_zeta_bound` at line 146

### MathCollab.Density.DetectorTruncation

File: `lean/MathCollab/Density/DetectorTruncation.lean`; 115 source lines; SHA-256 `cb55adb78528ad678d4fc90d46e46f7c44fe84890ba7531090382c0151dbfe8f`.

- `detectorTerm` at line 16
- `norm_detectorTerm_le` at line 19
- `norm_detector_tail_le` at line 31
- `detector_geometric_factor_le` at line 54
- `firstDetectorCutoff` at line 72
- `norm_firstDetector_tail_le` at line 75
- `firstDetector_tail_eventually_small` at line 105

### WeylPort.Analytic.DigammaSeries

File: `lean/WeylPort/Analytic/DigammaSeries.lean`; 587 source lines; SHA-256 `b11016cfb3324032e1ad39fc901dd10baad0dfd71c486900f6570698e4bc34c5`.

- `norm_natCast_add_one` at line 68
- `sum_inv_natCast_add_one` at line 74
- `sum_inv_natCast_add_one_real` at line 81
- `inv_add_one_sub_inv_eq` at line 88
- `norm_inv_add_one_sub_inv_le` at line 96
- `norm_inv_add_one_sub_inv_le'` at line 119
- `summable_one_div_natCast_add_one_sq` at line 142
- `hasSum_sub_succ_of_tendsto_zero` at line 148
- `tsum_one_div_natCast_add_add_one_sq_le` at line 161
- `logGammaSeq` at line 221
- `logGammaSeq_succ_sub` at line 225
- `cauchySeq_logGammaSeq` at line 261
- `exp_logGammaSeq` at line 341
- `hasSum_digamma_of_re_pos` at line 361
- `hasSum_digamma` at line 496
- `digamma_eq_tsum` at line 580

### WeylPort.AFE.HarmonicDigamma

File: `lean/WeylPort/AFE/HarmonicDigamma.lean`; 541 source lines; SHA-256 `35072a8f09c6130f7d46f2fde753542a47d6fe55c6d392733758d45a591fcc28`.

- `hasSum_real_digamma` at line 30
- `hasSum_digamma_difference` at line 48
- `tendsto_log_sub_reciprocal_sum` at line 55
- `hasSum_harmonic_tail` at line 71
- `reciprocal_le_chord` at line 89
- `log_succ_sub_le` at line 99
- `le_log_succ_sub` at line 135
- `log_sub_reciprocal_sum_bounds` at line 144
- `real_digamma_bounds` at line 161
- `harmonic_tail_bounds` at line 184
- `hasSum_harmonic_plus` at line 208
- `harmonic_plus_bound` at line 221
- `sum_bounds_from_differences` at line 230
- `reciprocal_square_series_bounds` at line 248
- `reciprocal_cube_series_bounds` at line 275
- `reciprocal_square_series_sharp` at line 308
- `reciprocal_cube_series_sharp` at line 321
- `hasSum_harmonic_tail_square` at line 334
- `hasSum_harmonic_tail_cube` at line 354
- `harmonic_tail_square_bound` at line 376
- `harmonic_tail_cube_bound` at line 393
- `hasSum_harmonic_plus_square` at line 413
- `hasSum_harmonic_plus_cube` at line 429
- `harmonic_plus_square_bound` at line 448
- `harmonic_plus_cube_bound` at line 462
- `tsum_nat_tail_eq` at line 479
- `source_harmonic_tail_identity` at line 497
- `source_harmonic_tail_power_eq` at line 508
- `source_harmonic_plus_power_eq` at line 525

### WeylPort.AFE.AlternatingHarmonic

File: `lean/WeylPort/AFE/AlternatingHarmonic.lean`; 403 source lines; SHA-256 `54d13860b8c78420110ece36d80dacd27fe69d36f329233b69d98cbae040d879`.

- `ne_pole_of_re_pos` at line 29
- `digamma_two_mul` at line 37
- `real_digamma_two_mul` at line 85
- `hasSum_paired_reciprocal` at line 92
- `reciprocal_sub_succ` at line 107
- `hasSum_reciprocal_unit_difference` at line 113
- `paired_reciprocal_bounds` at line 129
- `paired_reciprocal_source_eq` at line 155
- `tsum_pair_nat` at line 165
- `alternating_reciprocal_difference` at line 176
- `hasSum_alternating_harmonic_tail` at line 192
- `alternating_harmonic_tail_bound` at line 218
- `abs_tsum_alternating_shift` at line 254
- `hasSum_alternating_harmonic_plus` at line 267
- `alternating_harmonic_plus_identity` at line 289
- `alternating_harmonic_plus_bound` at line 301
- `real_digamma_one` at line 319
- `real_digamma_half` at line 323
- `real_digamma_add_one` at line 329
- `real_digamma_eq_deriv_Gamma_div` at line 335
- `source_alternating_harmonic_tail_bound` at line 344
- `source_alternating_harmonic_plus_bound` at line 369
- `source_alternating_harmonic_plus_identity` at line 380
- `not_printed_alternating_plus_identity` at line 392

### WeylPort.AFE.FiniteExponentialSums

File: `lean/WeylPort/AFE/FiniteExponentialSums.lean`; 353 source lines; SHA-256 `1198f50febe40945b67b58f350359db4bea1bb0c9b59e01bc960b1f0c59b6506`.

- `expMode` at line 23
- `finiteS0` at line 27
- `finiteS1` at line 31
- `tildeS1` at line 35
- `sum_Icc_one_eq_sum_range` at line 39
- `norm_expMode` at line 45
- `expMode_eq_pow` at line 49
- `norm_expMode_sub_one` at line 57
- `expMode_one_ne_one` at line 66
- `norm_finite_mode_sum` at line 75
- `norm_finiteS0` at line 93
- `norm_finiteS0_le` at line 98
- `norm_weighted_sum_le` at line 104
- `norm_finiteS1_le` at line 136
- `norm_finiteS1_le_source` at line 157
- `finite_sums_eq_zero` at line 165
- `sin_pi_mul_ne_zero_of_noninteger` at line 169
- `expMode_integer` at line 177
- `expMode_half_integer` at line 187
- `finiteS0_integer` at line 200
- `finiteS1_integer` at line 204
- `antitone_reciprocal_succ` at line 209
- `sum_range_even_pairs` at line 214
- `tendsto_alternating_harmonic_prefix` at line 224
- `alternating_harmonic_prefix_error` at line 256
- `finiteS1_half_integer` at line 283
- `norm_finiteS1_half_integer` at line 295
- `finiteS1_half_integer_error` at line 301
- `norm_finiteS1_half_integer_le` at line 315
- `norm_finiteS0_source_floor` at line 321
- `norm_finiteS0_le_source` at line 327
- `norm_finiteS1_le_tildeS1` at line 334
- `not_prose_log_bound` at line 342

### WeylPort.AFE.ExponentialTails

File: `lean/WeylPort/AFE/ExponentialTails.lean`; 373 source lines; SHA-256 `76182680d84b980b68f440bb0bf0cb95db977b67559a36fa84fd789990866308`.

- `expMode_add` at line 22
- `norm_shifted_mode_prefix_le` at line 31
- `summable_weighted_modes` at line 42
- `norm_tsum_weighted_modes_le` at line 51
- `antitone_negative_tail_weight` at line 60
- `antitone_positive_tail_weight` at line 69
- `norm_negative_tail_le` at line 77
- `norm_positive_tail_le` at line 90
- `tsum_complex_nat_tail_eq` at line 99
- `negativeTail` at line 117
- `positiveTail` at line 121
- `summable_negative_tail_shift` at line 125
- `negativeTail_eq_shift` at line 137
- `summable_positive_tail_shift` at line 150
- `positiveTail_eq_shift` at line 158
- `norm_negativeTail_le_source` at line 171
- `norm_positiveTail_le_source` at line 192
- `real_digamma_one_sub` at line 209
- `paired_reciprocal_half` at line 242
- `paired_reciprocal_antitone` at line 257
- `digamma_half_integer_tail_bound` at line 276
- `summable_negativeTail` at line 298
- `summable_positiveTail` at line 310
- `negativeTail_half_integer` at line 320
- `positiveTail_half_integer` at line 333
- `norm_negativeTail_half_integer_le` at line 346
- `norm_negativeTail_half_integer_le_pi` at line 356
- `norm_positiveTail_half_integer_le` at line 368

### WeylPort.AFE.NonstationaryPhase

File: `lean/WeylPort/AFE/NonstationaryPhase.lean`; 299 source lines; SHA-256 `5479c6dc7e79c2085519e0d5517aa53d5e8e8838c9636b7437bbd707453e2c50`.

- `nonstationary_interval_bound` at line 28
- `deriv_frequency_shift` at line 40
- `frequency_shift_deriv_neg` at line 46
- `negative_frequency_quotient_antitone` at line 56
- `negative_frequency_integral_bound` at line 74
- `positive_frequency_quotient_antitone` at line 105
- `weighted_slope_quotient_antitone` at line 126
- `weighted_slope_abs_antitone` at line 143
- `positive_frequency_integral_bound` at line 154
- `contDiffOn_one_of_continuous_deriv` at line 195
- `weighted_wave_hasDerivAt` at line 204
- `norm_integral_two_amplitudes_le` at line 214
- `intervalIntegrable_amplitude_phase` at line 224
- `negative_derivative_amplitude_integral_bound` at line 234
- `positive_derivative_amplitude_integral_bound` at line 267

### WeylPort.AFE.FirstDerivativeTest

File: `lean/WeylPort/AFE/FirstDerivativeTest.lean`; 142 source lines; SHA-256 `cb8127b320a7f0f2ea5fee9d672823b635316e0dd6f2d42505e2d1177b0da263`.

- `contDiffOn_one_of_continuous_derivative` at line 26
- `first_derivative_test_antitone` at line 37
- `first_derivative_test_monotone` at line 73
- `first_derivative_test` at line 101
- `quotient_max_isGreatest` at line 118
- `first_derivative_test_sup` at line 131

### WeylPort.AFE.OscillatoryParts

File: `lean/WeylPort/AFE/OscillatoryParts.lean`; 240 source lines; SHA-256 `9f352575f72329e4ac5b4501c46b4b9cf8579bc4ec4cd41623b81b701f7ac02b`.

- `oscillatory_integral_parts` at line 26
- `norm_oscillatory_integral_sub_boundary_le` at line 71
- `norm_expMode_integral_sub_boundary_le` at line 122
- `negative_second_quotients_antitone` at line 184
- `norm_negative_exp_integral_sub_boundary_le` at line 211

### WeylPort.AFE.SecondModeTails

File: `lean/WeylPort/AFE/SecondModeTails.lean`; 212 source lines; SHA-256 `072de2ae359768fcda9ae4c10dba422daf7bdc58a64abf0039232d5d54539494`.

- `secondModeTerm` at line 27
- `secondModeEndpoint` at line 32
- `secondModeEndpoint_eq` at line 38
- `summable_secondModeEndpoint` at line 54
- `tsum_secondModeEndpoint` at line 61
- `norm_tsum_secondModeEndpoint` at line 73
- `secondModeTerm_remainder_bound` at line 84
- `secondModeTail_bound` at line 136
- `secondModeTail_source_bound` at line 187

### WeylPort.AFE.UpperModeTails

File: `lean/WeylPort/AFE/UpperModeTails.lean`; 210 source lines; SHA-256 `44dc5baeadb39999e1018cc5c5726cca8355ea92ee404eeffa98765cd1de355c`.

- `upperModeTerm` at line 21
- `upperModeEndpoint` at line 26
- `upperModeEndpoint_eq` at line 32
- `summable_upperModeEndpoint` at line 50
- `tsum_upperModeEndpoint` at line 58
- `norm_tsum_upperModeEndpoint` at line 71
- `upperModeTerm_remainder_bound` at line 83
- `upperModeTail_bound` at line 124
- `upperModeTail_source_bound` at line 179

### WeylPort.AFE.PowerWeights

File: `lean/WeylPort/AFE/PowerWeights.lean`; 100 source lines; SHA-256 `4a611ac8ef91444644ce549977b6d2ef52369172b2c8bd37153318c514a6fc1a`.

- `afeWeight` at line 27
- `afePhase` at line 30
- `afeWeight_hasDerivAt` at line 33
- `afePhase_hasDerivAt` at line 38
- `afeWeight_pos` at line 45
- `afeWeight_antitone` at line 49
- `abs_deriv_afeWeight` at line 55
- `abs_deriv_afeWeight_antitone` at line 61
- `afe_derivative_quotient` at line 70
- `afe_derivative_quotient_antitone` at line 80
- `afe_weights_satisfy_accepted_partI_hypotheses` at line 93

### WeylPort.AFE.AFESecondWeights

File: `lean/WeylPort/AFE/AFESecondWeights.lean`; 256 source lines; SHA-256 `12f7771142aab29c358d49842f1ce1670e308b904351b9151782865aaead35dd`.

- `afeWeight_deriv_hasDerivAt` at line 25
- `afePhase_deriv_hasDerivAt` at line 37
- `afe_power_quotient_normalize` at line 47
- `afe_power_quotient_antitone` at line 57
- `afeWeight_phaseProduct_hasDerivAt` at line 68
- `afe_second_derivative_quotient` at line 79
- `afe_derivative_curvature_quotient` at line 88
- `afe_product_derivative_quotient` at line 102
- `afe_product_curvature_quotient` at line 116
- `afe_second_quotients_antitone` at line 132
- `afe_second_derivatives_antitone` at line 164
- `afe_second_derivatives_pos` at line 193
- `afe_second_amplitude_regular` at line 208
- `afe_second_amplitudes_antitone` at line 226

### WeylPort.AFE.AFESecondModes

File: `lean/WeylPort/AFE/AFESecondModes.lean`; 183 source lines; SHA-256 `f5546e14b27f755be18e7eaa8a56a499914d4d46c15301bcc4d8896ae30344dd`.

- `afe_positive_second_integral_bound` at line 27
- `afe_positive_second_tail_bound` at line 78
- `afe_upper_second_tail_bound` at line 129

### WeylPort.AFE.AbelSawtooth

File: `lean/WeylPort/AFE/AbelSawtooth.lean`; 335 source lines; SHA-256 `ce407569d1e37d37ae67a1e4f87aa0822fdab3e58e4f34092426baf95e4d8418`.

- `positivePhase` at line 34
- `abelSawtooth` at line 38
- `norm_positivePhase` at line 42
- `positivePhase_eq_expMode` at line 46
- `positivePhase_ne_one` at line 53
- `positivePhase_add_int` at line 63
- `positivePhase_fract` at line 70
- `one_sub_positivePhase_mem_slitPlane` at line 74
- `one_sub_positivePhase_factor` at line 86
- `arg_one_sub_positivePhase` at line 101
- `abelSawtooth_one` at line 112
- `abs_abelSawtooth_le` at line 126
- `tendsto_abelSawtooth` at line 132
- `continuous_positivePhase` at line 144
- `radial_phase_mem_slitPlane` at line 149
- `continuous_abelSawtooth` at line 160
- `hasSum_abelSawtooth` at line 168
- `ae_noninteger` at line 179
- `tendsto_integral_mul_abelSawtooth` at line 184
- `sawtoothMode` at line 203
- `conj_expMode` at line 207
- `abelSawtooth_term_eq` at line 217
- `hasSum_abelSawtooth_modes` at line 228
- `continuous_sawtoothMode` at line 233
- `norm_sawtoothMode_le` at line 238
- `integrable_mul_sawtoothMode` at line 258
- `hasSum_integral_abelSawtooth` at line 264
- `tendsto_tsum_abel` at line 301
- `integral_mul_sawtooth_eq_tsum` at line 314

### WeylPort.AFE.PoissonFourier

File: `lean/WeylPort/AFE/PoissonFourier.lean`; 312 source lines; SHA-256 `a03f8323524523f9ddfd1949e7307386d0c4439f39ae59e34c162424302eda4b`.

- `PartIRegularity` at line 29
- `weightedWave` at line 43
- `waveDerivative` at line 47
- `derivativeMode` at line 52
- `negativeCoefficient` at line 58
- `positiveCoefficient` at line 62
- `partICoefficient` at line 66
- `waveDerivative_eq_deriv` at line 70
- `PartIRegularity.g_continuous` at line 78
- `PartIRegularity.f_continuous` at line 83
- `PartIRegularity.coefficient_nonneg` at line 88
- `negativeCoefficient_bound` at line 97
- `positiveCoefficient_bound` at line 113
- `summable_negativeCoefficient_tail` at line 138
- `summable_negativeCoefficient` at line 150
- `summable_positiveCoefficient` at line 157
- `PartIRegularity.waveDerivative_continuous` at line 166
- `waveDerivative_mul_phase` at line 175
- `integral_waveDerivative_expMode` at line 186
- `integral_waveDerivative_expMode_neg` at line 201
- `integral_waveDerivative_sawtoothMode` at line 216
- `integral_waveDerivative_sawtooth` at line 233
- `norm_negativeCoefficient_tail_le_digamma` at line 249
- `norm_positiveCoefficient_sum_le_digamma` at line 264
- `norm_negativeCoefficient_tail_le_source` at line 278
- `norm_positiveCoefficient_sum_le_source` at line 294

### WeylPort.Analytic.EulerMaclaurin

File: `lean/WeylPort/Analytic/EulerMaclaurin.lean`; 91 source lines; SHA-256 `5bb54538c2032c46f2b1f73fd626f26424ce3f2044a0b035da6e870d9b3d7118`.

- `B1` at line 25
- `aestronglyMeasurable_B1` at line 28
- `abs_B1_le_half` at line 32
- `integral_deriv_mul_add_const` at line 38
- `intervalIntegrable_deriv_mul_B1` at line 53
- `integral_deriv_mul_floor_add_one` at line 63
- `sum_eq_integral_add_integral_deriv` at line 79

### WeylPort.AFE.EulerMaclaurin

File: `lean/WeylPort/AFE/EulerMaclaurin.lean`; 185 source lines; SHA-256 `d1552427b16d737f922a8444c59dc9d039941b9f55bb282c5baa7accef42970e`.

- `B1_eq_fract` at line 28
- `sum_shift_nat_floor` at line 33
- `euler_maclaurin_int` at line 71
- `poissonBoundary` at line 120
- `weighted_sum_eq_fourier` at line 125
- `norm_weightedWave` at line 150
- `abs_fract_sub_half_le` at line 160
- `norm_poissonBoundary_le` at line 165
- `poissonBoundary_half_integer` at line 177

### WeylPort.AFE.PoissonPartI

File: `lean/WeylPort/AFE/PoissonPartI.lean`; 303 source lines; SHA-256 `66732826b8bb0507baa6d2445cfec6eec35e8b1d3d13858f44341f2dec8f75a5`.

- `poissonHeadBoundary` at line 22
- `poissonMain` at line 26
- `hasDerivAt_expMode` at line 30
- `PartIRegularity.wave_hasDerivAt` at line 49
- `negativeCoefficient_eq_boundary_add_integral` at line 58
- `poissonHeadBoundary_eq_sum` at line 88
- `sum_negativeCoefficient_head` at line 99
- `poissonMain_eq_zero_add_head` at line 114
- `negativeCoefficient_sum_eq_head_add_tail` at line 127
- `weighted_sum_eq_poissonMain_add_remainder` at line 138
- `poissonEndpointMajorant` at line 149
- `norm_finiteS1_le_poissonEndpointMajorant` at line 154
- `norm_poissonHeadBoundary` at line 167
- `norm_poissonHeadBoundary_le` at line 174
- `partIAnalyticError` at line 183
- `partIZeroError` at line 190
- `corrected_poisson_partI_zero` at line 196
- `poissonMain_eq_source` at line 219
- `poissonEndpointMajorant_eq_tildeS1` at line 236
- `norm_finiteS1_half_integer_le_of_pos` at line 242
- `norm_poissonHeadBoundary_half_integer_le` at line 251
- `corrected_poisson_partI_zero_half_integer` at line 263
- `corrected_poisson_partI_zero_noninteger` at line 292

### WeylPort.AFE.PoissonShift

File: `lean/WeylPort/AFE/PoissonShift.lean`; 231 source lines; SHA-256 `34ab0213f4aa3d4fd22e1b21cde03f169ec62f17f9fb9f4a58d7a7efec78e53e`.

- `phaseShift` at line 22
- `PartIRegularityAt` at line 25
- `deriv_phaseShift` at line 39
- `PartIRegularityAt.deriv_gt` at line 44
- `PartIRegularityAt.shift` at line 51
- `weightedWave_phaseShift_int` at line 71
- `weighted_sum_phaseShift` at line 82
- `poissonMain_phaseShift` at line 90
- `phaseShift_delta` at line 120
- `partIShiftAnalyticError` at line 126
- `partIError` at line 135
- `shifted_floor_delta` at line 142
- `partIAnalyticError_phaseShift_eq` at line 150
- `partIZeroError_phaseShift_eq` at line 160
- `corrected_poisson_partI` at line 167
- `corrected_poisson_partI_half_integer` at line 181
- `corrected_poisson_partI_noninteger` at line 198
- `mem_source_sample_interval` at line 214
- `partIRegularityAt_of_source_hypotheses` at line 219

### WeylPort.AFE.PoissonApplications

File: `lean/WeylPort/AFE/PoissonApplications.lean`; 208 source lines; SHA-256 `72a8affa0a4509896787a05ea59e32d9329325454ad2d8da3e6cf10df5acef8c`.

- `constant_weight_partIRegularity` at line 23
- `corollary_poisson_partI` at line 46
- `afe_partIRegularity` at line 72
- `afe_finite_poisson_partI` at line 105
- `poissonEndpointMajorant_eq_zero` at line 119
- `afePartIFactor` at line 125
- `afe_partIAnalyticError_eq` at line 130
- `afe_partIZeroError_eq` at line 144
- `norm_poissonBoundary_left_half_integer_le` at line 156
- `afe_finite_sum_sub_integral_bound` at line 169
- `afePartIFactor_nonneg` at line 187

### WeylPort.AFE.SecondCoefficients

File: `lean/WeylPort/AFE/SecondCoefficients.lean`; 137 source lines; SHA-256 `a33ed92a835fd82bd0721290f3af6a6224f4a8089c8a8d0130d50d30cb793bb3`.

- `derivativeMode_eq_amplitude_integrals` at line 24
- `amplitude_coefficient_normalize` at line 46
- `positiveCoefficient_eq_secondModes` at line 56
- `negativeCoefficient_eq_upperModes` at line 66
- `tsum_positiveCoefficient_eq_secondModes` at line 76
- `tsum_negativeCoefficient_eq_upperModes` at line 90
- `weighted_sum_eq_second_mode_series` at line 101
- `afe_second_poisson_identity` at line 119

### WeylPort.AFE.PartIISignReview

File: `lean/WeylPort/AFE/PartIISignReview.lean`; 107 source lines; SHA-256 `158a03b923f0b0f002c3fc61ae4d6dd9e7121b47edef9a8dc178f8b96b765a39`.

- `printedPartIIE1` at line 25
- `printedPartIIE1_one` at line 33
- `printedPartIIE1_one_lt_one` at line 39
- `partII_square_tails_at_one` at line 47
- `printedPartIIE1_not_square_tail_bound` at line 64
- `partIISquareTailEnvelope` at line 73
- `partIISquareTailEnvelope_sub_printed` at line 81
- `partII_square_tail_envelope_bound` at line 89
- `partIISquareTailEnvelope_one` at line 103

### WeylPort.AFE.SecondCoeffBounds

File: `lean/WeylPort/AFE/SecondCoeffBounds.lean`; 327 source lines; SHA-256 `5b00f0271c50cf30cd9caf06a808dcb83f73a1fd060b778f2d79966598d00839`.

- `plusSquareBound` at line 26
- `plusCubeBound` at line 31
- `positiveModeError` at line 36
- `secondH` at line 43
- `secondH1` at line 47
- `plusSquareBound_nonneg` at line 52
- `plusCubeBound_nonneg` at line 57
- `positiveModeError_pair_le` at line 62
- `norm_positiveCoefficient_le_mode_errors` at line 86
- `afe_positiveCoefficient_bound` at line 111
- `minusSquareBound` at line 142
- `minusCubeBound` at line 148
- `negativeModeError` at line 155
- `minusSquareBound_nonneg` at line 162
- `minusCubeBound_nonneg` at line 168
- `negativeModeError_pair_le` at line 176
- `norm_negativeCoefficient_le_mode_errors` at line 200
- `afe_negativeCoefficient_bound` at line 226
- `afe_finite_poisson_second_bound` at line 259
- `squareBounds_eq_proposed_envelope` at line 290
- `partIICubeCoefficient` at line 301
- `cubeBounds_eq_source_coefficient` at line 310
- `partII_cube_coefficient_bound` at line 321

### WeylPort.AFE.SecondEndpoints

File: `lean/WeylPort/AFE/SecondEndpoints.lean`; 138 source lines; SHA-256 `41978834c51190d9706a57fb5b63a65138a127440e34863fd4678e2c68b229dc`.

- `conj_positiveTail` at line 21
- `norm_positiveTail_neg` at line 31
- `secondH_nonneg` at line 35
- `secondH1_nonneg` at line 40
- `halfSecondEndpointBound` at line 45
- `second_endpoint_half_integer_bound` at line 49
- `afe_finite_poisson_second_half` at line 64
- `norm_positiveTail_le_two` at line 102
- `norm_negativeTail_le_four` at line 116

### WeylPort.AFE.SecondTailSharp

File: `lean/WeylPort/AFE/SecondTailSharp.lean`; 104 source lines; SHA-256 `e16a1c536260ee259b77e9ea70aced14b494fd48a76e19e0608504a826c412c1`.

- `alternating_harmonic_tail_bound_sharp` at line 20
- `norm_negativeTail_half_integer_sharp` at line 47
- `alternating_harmonic_plus_bound_sharp` at line 68
- `norm_positiveTail_half_integer_sharp` at line 84
- `second_endpoint_half_integer_sharp` at line 95

### WeylPort.Analytic.ZetaContinuation

File: `lean/WeylPort/Analytic/ZetaContinuation.lean`; 659 source lines; SHA-256 `b8ebff2272fa0096c8366dce7510a6bd63e86654f55f7ef7a3e2c5af10ec8852`.

- `div_cpow_eq_cpow_neg` at line 16
- `div_rpow_eq_rpow_neg` at line 19
- `one_div_cpow_eq_cpow_neg` at line 22
- `riemannZeta0` at line 26
- `riemannZeta0_apply` at line 35
- `Real.differentiableAt_cpow_const_of_ne` at line 42
- `Complex.one_div_cpow_eq` at line 48
- `sum_eq_int_deriv` at line 54
- `xpos_of_uIcc` at line 76
- `ZetaSum_aux1₁` at line 81
- `ZetaSum_aux1φDiff` at line 91
- `ZetaSum_aux1φderiv` at line 97
- `ZetaSum_aux1derivφCont` at line 115
- `ZetaSum_aux1` at line 124
- `ZetaSum_aux1_1'` at line 146
- `ZetaSum_aux1_1` at line 149
- `ZetaSum_aux1_2` at line 152
- `ZetaSum_aux1_3` at line 164
- `ZetaSum_aux1_4'` at line 167
- `ZetaSum_aux1_4` at line 173
- `ZetaSum_aux1_5a` at line 179
- `ZetaSum_aux1_5b` at line 185
- `measurable_floor_add_half_sub` at line 192
- `ZetaSum_aux1_5c` at line 197
- `ZetaSum_aux1_5d` at line 205
- `ZetaSum_aux1_5` at line 215
- `ZetaBnd_aux1a` at line 224
- `Finset.Ioc_eq_Ico` at line 234
- `Finset.Ioc_eq_Icc` at line 237
- `Finset.Icc_eq_Ico` at line 240
- `finsetSum_tendsto_tsum` at line 243
- `Complex.cpow_tendsto` at line 255
- `Complex.cpow_inv_tendsto` at line 263
- `ZetaSum_aux2a` at line 270
- `ZetaSum_aux3` at line 273
- `integrableOn_of_Zeta0_fun` at line 285
- `ZetaSum_aux2` at line 297
- `ZetaBnd_aux1b` at line 328
- `isOpen_aux` at line 354
- `integrable_log_over_pow` at line 359
- `integrableOn_of_Zeta0_fun_log` at line 395
- `hasDerivAt_Zeta0Integral` at line 426
- `ζ₀'` at line 516
- `HasDerivAt_neg_cpow_over2` at line 523
- `HasDerivAt_cpow_over_var` at line 528
- `HasDerivAtZeta0` at line 544
- `HolomorphicOn_riemannZeta0` at line 563
- `HolomorphicOn_riemannZeta` at line 568
- `isPathConnected_aux` at line 575
- `Zeta0EqZeta` at line 631

### WeylPort.AFE.Objects

File: `lean/WeylPort/AFE/Objects.lean`; 48 source lines; SHA-256 `27f0878bb3bc9287aa6231b695085be91a97a61d63410bf88be441136577b659`.

- `zetaTerm` at line 29
- `sharpZetaSum` at line 32
- `printedAFE1Sum` at line 36
- `chi` at line 40
- `afeRemainder` at line 45

### WeylPort.AFE.ZetaTruncation

File: `lean/WeylPort/AFE/ZetaTruncation.lean`; 266 source lines; SHA-256 `cbbf42a12bd646b3fae45adabc2ba3d331fc6d331e713462a7650589ba558385`.

- `norm_zeta_sub_regularized_sum_le` at line 29
- `tendsto_regularized_sum` at line 60
- `weightedWave_afe_eq_cpow` at line 73
- `conj_weightedWave_afe` at line 84
- `integral_cpow_neg` at line 96
- `sum_int_Ioc_eq_nat_Ioc` at line 115
- `conj_intervalIntegral` at line 136
- `afe_finite_cpow_bound` at line 141
- `sum_range_reciprocal_eq_sharpZetaSum` at line 174
- `sum_cpow_Ioc_eq_sharp_sub` at line 183
- `tendsto_cpow_tail_sub_integral` at line 206
- `afe_zeta_sub_sum_sub_pole_bound` at line 224
- `norm_afe_pole_le` at line 250

### WeylPort.AFE.WeightedIntegralSums

File: `lean/WeylPort/AFE/WeightedIntegralSums.lean`; 153 source lines; SHA-256 `0e8b6e903230ac251e45c5e321ec91da5fd84923fa76472a0cc6ffa45ba96786`.

- `real_digamma_add_nat` at line 26
- `sum_Icc_one_eq_sum_range_real` at line 39
- `sum_Icc_natCast_real` at line 45
- `half_integer_reciprocal_sum` at line 56
- `half_integer_quadratic_sum_eq` at line 76
- `half_integer_quadratic_sum_le` at line 97
- `alternating_linear_sum_eq` at line 112
- `abs_alternating_linear_sum_le` at line 124
- `norm_alternating_linear_sum_le` at line 134
- `norm_alternating_sum_le_one` at line 142

### WeylPort.AFE.WeightedIntegrals

File: `lean/WeylPort/AFE/WeightedIntegrals.lean`; 162 source lines; SHA-256 `9a7dd0160fe9f7471932867adc414fcdb82a46b82e5597d550b86b2109de4aea`.

- `weightedIntegral` at line 29
- `continuous_linear_wave` at line 33
- `linear_wave_hasDerivAt` at line 38
- `intervalIntegrable_weighted_integrand` at line 46
- `integral_cpow_linear_wave_parts` at line 53
- `weightedIntegral_parts` at line 92
- `weightedIntegral_parts_twice` at line 100
- `linear_wave_half_integer` at line 137
- `weightedIntegral_parts_twice_half_integer` at line 149

### WeylPort.AFE.WeightedIntegralPhase

File: `lean/WeylPort/AFE/WeightedIntegralPhase.lean`; 204 source lines; SHA-256 `29475a9525aec4174220a439892eff77d320a7d80b88bd31c888d3fa47ba3cda`.

- `weightedIntegralPhase` at line 27
- `weightedIntegralPhase_hasDerivAt` at line 31
- `weightedIntegralPhase_deriv_ne_zero` at line 38
- `abs_weightedIntegralPhase_deriv_antitone` at line 48
- `weightedIntegralPhase_quotient_monotone` at line 74
- `norm_integral_power_log_phase_le` at line 91
- `norm_integral_power_log_phase_distance_le` at line 109
- `cpow_linear_wave_eq_power_log_phase` at line 133
- `norm_weightedIntegral_shift_two_le` at line 146
- `continuous_weightedIntegral_left` at line 165
- `norm_weightedIntegral_shift_two_zero_le` at line 172
- `norm_weightedIntegral_shift_two_source` at line 188

### WeylPort.AFE.MonotoneAmplitude

File: `lean/WeylPort/AFE/MonotoneAmplitude.lean`; 64 source lines; SHA-256 `3504e96e2d6cac75629870d79b8b67de25c3035f59ddc4f0cc3224a33b41de65`.

- `norm_integral_mul_le_of_primitive_bound` at line 27

### WeylPort.AFE.UpperIntegralEstimate

File: `lean/WeylPort/AFE/UpperIntegralEstimate.lean`; 236 source lines; SHA-256 `25cd2c0d91d4627deb9a456837fce2dace99be874101bacf171f9508851b3d19`.

- `upper_phase_derivative_lower` at line 30
- `upper_phase_reciprocal_monotone` at line 40
- `norm_integral_upper_phase_le` at line 64
- `continuousOn_upper_phase` at line 89
- `upper_phase_primitive_hasDerivAt` at line 98
- `norm_weightedIntegral_upper_le` at line 113
- `weightedIntegral_sub` at line 149
- `weightedIntegral_cauchy_atTop` at line 156
- `weightedIntegralTail` at line 176
- `weightedIntegral_tendsto_tail` at line 180
- `norm_weightedIntegralTail_le` at line 187
- `sum_reciprocals_floor_le` at line 197
- `norm_sum_weightedIntegralTail_le` at line 204
- `norm_sum_weightedIntegralTail_source` at line 223

### GuthMaynard.Weyl

File: `lean/GuthMaynard/Weyl.lean`; 616 source lines; SHA-256 `8704920baecba9cd6ee159672f44ec7cf72b33d80a5ce9c4fd89eb1e22b87923`.

- `interval_weyl_differencing_complex` at line 23
- `logarithmicDifferencePhase` at line 48
- `hasDerivAt_logarithmicDifferencePhase` at line 52
- `hasDerivAt_logarithmicDifferencePhase_deriv` at line 68
- `logarithmicDifferencePhase_secondDifference` at line 96
- `logarithmicDifferenceCurvature_bounds` at line 124
- `logarithmicDifference_secondDifference_bounds` at line 179
- `logarithmicDifference_B_process` at line 232
- `integerLogarithmicTerm` at line 263
- `padded_logarithmic_correlation_eq` at line 270
- `logarithmicCorrelationBound` at line 392
- `logarithmicCorrelationBound_nonneg` at line 400
- `padded_logarithmic_correlation_norm_le_of_lt` at line 406
- `shiftDistance` at line 432
- `padded_logarithmic_correlation_norm_le` at line 434
- `logarithmic_weyl_AB_process` at line 479
- `weylShiftLength` at line 516
- `weylShiftLength_le` at line 519
- `logarithmicWeylMajorant` at line 524
- `logarithmicWeylBound` at line 531
- `integerLogarithmicSum_eq` at line 534
- `logarithmic_weyl_optimized` at line 581
- `norm_logarithmicSum_le_weylBound` at line 594

### GuthMaynard.WeylExplicit

File: `lean/GuthMaynard/WeylExplicit.lean`; 715 source lines; SHA-256 `0b1dffb04e2e1afa6f4e6f8d52a159dc59068f8e01aaa3dc04a9ae1f2983ecba`.

- `vdc_product_bound` at line 24
- `logarithmicCorrelationBound_le_simple` at line 95
- `simpleLogarithmicCorrelationBound` at line 128
- `logarithmicCorrelationBound_le_uniform` at line 133
- `logarithmic_weyl_AB_process_simple` at line 169
- `simpleLogarithmicCorrelationBound_le_four_hundred` at line 202
- `simpleLogarithmicCorrelationBound_le_four_hundred_mul` at line 268
- `logarithmic_weyl_exponent_pair_with_shift` at line 346
- `classicalWeylShiftLength` at line 416
- `classicalWeylShiftLength_spec` at line 419
- `logarithmic_weyl_exponent_pair` at line 465
- `logarithmic_weyl_exponent_pair_prefix` at line 476
- `logarithmic_weyl_exponent_pair_prefix_with_slack` at line 589

### GuthMaynard.WeylZeta

File: `lean/GuthMaynard/WeylZeta.lean`; 211 source lines; SHA-256 `2873ef0874b4d9782223e26b4414ef24037952f469001fde1c0a932a98c04db5`.

- `norm_weighted_sum_le_of_antitone` at line 22
- `logarithmicSum_eq_sum_range` at line 76
- `criticalLineWeylBlock` at line 84
- `criticalLineTerm_eq_cpow` at line 89
- `criticalLineWeylBlock_eq_cpow` at line 103
- `norm_criticalLineWeylBlock_le` at line 115
- `weightedWeylBlock` at line 152
- `weightedWeylBlock_eq_cpow` at line 158
- `norm_weightedWeylBlock_le` at line 183

### WeylPort.Block

File: `lean/WeylPort/Block.lean`; 51 source lines; SHA-256 `8a0fe58d30d523db118167f70efaf00b32a7e1976eea09c4be1aa563bad73d3a`.

- `norm_criticalLine_cpow_block_le` at line 25

### WeylPort.ShortSum

File: `lean/WeylPort/ShortSum.lean`; 168 source lines; SHA-256 `9b54ae817c756d581b730f44b3391dd4dee26c3a9b270a0059a8aee9f4bfa3eb`.

- `criticalTerm` at line 16
- `norm_criticalTerm` at line 19
- `norm_critical_block_small` at line 27
- `norm_critical_block_le` at line 51
- `norm_critical_sum_le_dyadic` at line 63
- `norm_critical_sum_le_log` at line 103
- `eventually_mul_norm_critical_sum_le_rpow` at line 136
- `exists_critical_sum_le_sixth_power` at line 159

### WeylPort.Reflection

File: `lean/WeylPort/Reflection.lean`; 133 source lines; SHA-256 `79df73d206af81fdaf7c70e603f76608dfa46f7cc031e6be7afb708658402102`.

- `criticalPoint` at line 15
- `one_sub_criticalPoint` at line 17
- `criticalPoint_neg` at line 21
- `criticalTerm_neg` at line 25
- `norm_critical_sum_neg` at line 33
- `norm_dual_critical_sum` at line 40
- `norm_critical_sum_le_log_abs` at line 50
- `gammaReal_conj` at line 61
- `criticalGammaRatio` at line 70
- `norm_criticalGammaRatio` at line 73
- `riemannZeta_critical_functional_equation` at line 80
- `critical_chi_product_eq_ratio` at line 99
- `norm_critical_chi_product` at line 128

### WeylPort.AFE.ChiReflection

File: `lean/WeylPort/AFE/ChiReflection.lean`; 81 source lines; SHA-256 `6f0a53bf5979c838f78fe93fd516cc91adb50871e0e50891fa586735f513264e`.

- `chi_eq_two_mul` at line 30
- `zeta_eq_chi_mul_zeta_one_sub` at line 45
- `conj_nonneg_cpow` at line 65
- `chi_conj` at line 73

### WeylPort.AFE.ChiGammaFactor

File: `lean/WeylPort/AFE/ChiGammaFactor.lean`; 169 source lines; SHA-256 `99d15ca234b39702269db0a87ada1d0094b942e9817e36f69e3003b678c6b716`.

- `cpow_two_pi_div_I` at line 27
- `gamma_factor_mul_one_sub_exp` at line 46
- `norm_exp_pi_mul_I` at line 63
- `one_sub_exp_neg_abs_le_norm` at line 72
- `gammaChiError` at line 87
- `gammaChi_denominator_bound` at line 91
- `norm_gammaChiError_le` at line 105
- `gamma_factor_eq_chi_mul_one_add` at line 114
- `gamma_factor_lemma_seven` at line 134
- `gamma_factor_conjugate_branch` at line 143

### WeylPort.Analytic.RealLaplace

File: `lean/WeylPort/Analytic/RealLaplace.lean`; 50 source lines; SHA-256 `c85ffd8e17452ace9d05753db57d8e01c45ee2b862d7458da9887c2fc21c117f`.

- `integral_cpow_mul_exp_neg_mul_Ioi_eq` at line 17
- `integrableOn_cpow_mul_exp_neg_mul_Ioi` at line 28

### WeylPort.Analytic.ComplexLaplace

File: `lean/WeylPort/Analytic/ComplexLaplace.lean`; 201 source lines; SHA-256 `9927378de6bbec8d399bdd6e343b3d2e1bf880242819731f55b0f74465945736`.

- `integrableOn_cpow_mul_cexp_neg_complex_mul_Ioi` at line 30
- `dfiComplexLaplace` at line 49
- `hasDerivAt_dfiComplexLaplace` at line 52
- `analyticOnNhd_dfiComplexLaplace` at line 132
- `dfiComplexLaplace_ofReal` at line 141
- `dfiComplexLaplace_eq` at line 161

### WeylPort.AFE.DampedWeightedKernel

File: `lean/WeylPort/AFE/DampedWeightedKernel.lean`; 326 source lines; SHA-256 `750aa1a6777a3743800e2f1b57283cde6f80c0c75eba33059eaca024c039216f`.

- `dampedWeightedKernel` at line 32
- `continuous_dampedWeightedKernel_parameter` at line 37
- `intervalIntegrable_dampedWeightedKernel` at line 43
- `dampedWeightedKernel_eq_laplace` at line 48
- `integrableOn_dampedWeightedKernel` at line 59
- `integral_dampedWeightedKernel_Ioi` at line 68
- `continuousAt_dampedGamma_factor` at line 78
- `dampedWeightedKernel_zero` at line 93
- `norm_dampedWeightedKernel_le` at line 99
- `dampedWeightedKernel_finite_abel_limit` at line 109
- `norm_integral_dampedWeightedKernel_le` at line 132
- `norm_integral_Ioi_dampedWeightedKernel_le` at line 195
- `norm_dampedGamma_sub_finite_integral_le` at line 209
- `norm_gamma_sub_weightedIntegral_le` at line 229
- `weightedIntegralTail_zero_eq_gamma` at line 244
- `cpow_negative_imaginary_frequency` at line 270
- `weightedIntegralTail_zero_eq_gamma_product` at line 284
- `weightedIntegralTail_zero_eq_chi` at line 294
- `weightedIntegralTail_eq_sub` at line 304
- `weightedIntegral_eq_tail_sub_lower_sub_upper` at line 316

### WeylPort.AFE.LowerIntegralEstimate

File: `lean/WeylPort/AFE/LowerIntegralEstimate.lean`; 216 source lines; SHA-256 `f1d23220e3d7f1ed800dd0b0446227d433fb01ff5bbfd0525c6fcc41a317ffcc`.

- `abs_height_le_norm_real_sub` at line 27
- `height_sq_le_norm_boundary_denominator` at line 34
- `sum_weightedIntegral_parts_twice` at line 42
- `norm_lower_boundary_one_le` at line 58
- `norm_lower_boundary_two_le` at line 68
- `norm_lower_remainder_coefficient_le` at line 80
- `norm_lower_remainder_sum_le` at line 90
- `norm_sum_lower_integral_le_arithmetic` at line 123
- `norm_sum_lower_integral_half_integer` at line 148
- `half_integer_eq_nat_floor_add_half` at line 191
- `norm_sum_lower_integral_source` at line 203

### WeylPort.AFE.WeightedIntegralAssembly

File: `lean/WeylPort/AFE/WeightedIntegralAssembly.lean`; 150 source lines; SHA-256 `2ad56cd39fa7043c49a432d24f720fbe68b1695d2003e4f4c054e92476350d74`.

- `norm_sum_dual_powers_le` at line 27
- `sum_weightedIntegralTail_zero_eq_chi` at line 65
- `norm_sum_weightedIntegralTail_sub_chi_le` at line 77
- `sum_weightedIntegral_eq_three_terms` at line 102
- `norm_sum_weightedIntegral_sub_chi_le` at line 115

### WeylPort.AFE.AFESecondLimits

File: `lean/WeylPort/AFE/AFESecondLimits.lean`; 321 source lines; SHA-256 `10a063d7a9200956a597a20fffac7924f356c2ee4f5b045c6fc9d5ff644176a2`.

- `secondH_afe` at line 30
- `secondH1_afe` at line 40
- `tendsto_secondH_afe` at line 63
- `norm_poissonHeadBoundary_nat` at line 74
- `afeSecondUpperError` at line 86
- `tendsto_afeSecondUpperError` at line 91
- `afeSecondLeftError` at line 101
- `afe_finite_poisson_second_left_half` at line 112
- `conj_poissonMain_afe` at line 140
- `sum_weightedIntegral_eq_zero_add` at line 161
- `afe_second_finite_cpow_bound` at line 174
- `afe_zeta_sub_sum_pole_integrals_bound` at line 205
- `norm_sum_weightedIntegralTail_from_x_sub_chi_le` at line 246
- `afe_strict_strip_bound` at line 273

### WeylPort.AFE.UniformElementary

File: `lean/WeylPort/AFE/UniformElementary.lean`; 54 source lines; SHA-256 `101cbd5b32b157590174207731aae3bf1f97f84d91716b455c674eb675470722`.

- `digamma_gap_bounds` at line 17
- `weighted_log_cutoff_le` at line 28
- `eventually_gamma_envelope_le_one` at line 42

### WeylPort.AFE.UniformCoefficients

File: `lean/WeylPort/AFE/UniformCoefficients.lean`; 94 source lines; SHA-256 `5874063c0ebc81632602046f17772319568a8c4cc0de8e489142eb4f773e0528`.

- `plus_coefficients_uniform` at line 14
- `minus_coefficients_uniform` at line 40

### WeylPort.GapSum

File: `lean/WeylPort/GapSum.lean`; 72 source lines; SHA-256 `2548c6e1b92e08882691baf512dec041f4086c1edbb81a3f583c808c0cbd3f46`.

- `quadratic_gap_sum_le` at line 18

### WeylPort.CutoffSelection

File: `lean/WeylPort/CutoffSelection.lean`; 134 source lines; SHA-256 `0f0d2db3da5a4b029ef0cd903cebaa3bd6d07ff3705b2a59e10ee13bfdeaa72a`.

- `exists_balanced_half_cutoff` at line 16
- `exists_afe_cutoffs_all_heights` at line 87

### WeylPort.AFE.UniformError

File: `lean/WeylPort/AFE/UniformError.lean`; 279 source lines; SHA-256 `779c990a957fd42f905ef3423d9406d24135f36f53c246a6407706fb09d54e80`.

- `criticalPoissonConstant` at line 18
- `criticalPoissonConstant_pos` at line 24
- `afeSecondLeftError_critical_uniform` at line 30
- `critical_boundary_factors` at line 114
- `norm_critical_lower_integrals_uniform` at line 149
- `criticalAFEConstant` at line 173
- `criticalAFEConstant_pos` at line 176
- `norm_chi_criticalPoint` at line 182
- `norm_critical_afe_uniform` at line 186
- `eventually_actual_zeta_short_afe` at line 265

### WeylPort.ActualZeta

File: `lean/WeylPort/ActualZeta.lean`; 145 source lines; SHA-256 `2efce51ac5b7d7941e538a6e2513a77b9c9bc8328542f2ae1f5636cf73fd129b`.

- `norm_sharpZetaSum_critical` at line 17
- `norm_sharpZetaSum_dual` at line 23
- `eventually_norm_riemannZeta_critical_lt_rpow` at line 31
- `exists_riemannZeta_critical_lt_sixth_power` at line 63
- `norm_riemannZeta_critical_neg` at line 70
- `continuous_riemannZeta_critical` at line 76
- `exists_riemannZeta_critical_weyl_all_heights` at line 88
- `exists_riemannZeta_critical_weyl` at line 115
- `exists_riemannZeta_critical_dyadic_weyl` at line 124

### MathCollab.Density.WeylInput

File: `lean/MathCollab/Density/WeylInput.lean`; 26 source lines; SHA-256 `3c72677fff948f376700b60bc8583c05b9775bc55b549d64c82c6349bbb814f7`.

- `actual_zeta_weyl_input` at line 16

### MathCollab.Density.Stronger.InitialDetector

File: `lean/MathCollab/Density/Stronger/InitialDetector.lean`; 144 source lines; SHA-256 `cde37429dd2d3929aba1db767e46fc2a456e677b0e0a6d629f768d349674f4df`.

- `norm_residue_le` at line 19
- `detector_eventually_small` at line 46
- `detectorTail` at line 91
- `detectorTail_decomposition` at line 94
- `detectorTail_eventually_large` at line 112

### MathCollab.Density.Stronger.DampedCutoff

File: `lean/MathCollab/Density/Stronger/DampedCutoff.lean`; 110 source lines; SHA-256 `79fea87b7c4b9d2888e99ab9c3545d4047574f94666d3fc8fe6c0f17ce91bcdf`.

- `dampedCutoff` at line 20
- `dampedCutoff_contDiff` at line 22
- `dampedCutoff_tsupport` at line 27
- `damping_power_bound` at line 31
- `norm_iteratedDeriv_damping_le` at line 49
- `tsupport_iteratedDeriv_subset` at line 58
- `dampedCutoff_uniform_derivatives` at line 68

### MathCollab.Density.Stronger.UniformMellin

File: `lean/MathCollab/Density/Stronger/UniformMellin.lean`; 355 source lines; SHA-256 `ea1f5e2eae015b1e4ab2326c4a4f7d66c9aecf85fe9a3196e73e8fd51153a1f0`.

- `uniform_derivatives_comp_on_compact` at line 27
- `uniform_derivatives_mul_on_compact` at line 52
- `dampedMellinLift` at line 77
- `dampedMellinLift_contDiff` at line 80
- `dampedMellinLift_tsupport` at line 85
- `dampedMellinLift_uniform_derivatives` at line 106
- `tsupport_iteratedDeriv_complex_subset` at line 144
- `uniform_fourier_power_bound` at line 153
- `norm_iteratedDeriv_ofReal` at line 185
- `dampedCutoff_mellin_eq_fourier` at line 191
- `dampedCutoff_uniform_mellin_power_bound` at line 203
- `dampedCutoff_uniform_mellin_decay` at line 233
- `dampedCutoff_mellinConvergent` at line 263
- `dampedCutoff_integrable_mellin_line` at line 288
- `dampedCutoff_mellin_inversion` at line 305
- `dampedCutoff_uniform_mellin_weighted_L1` at line 320

### MathCollab.Density.Stronger.SmoothMellinIdentity

File: `lean/MathCollab/Density/Stronger/SmoothMellinIdentity.lean`; 195 source lines; SHA-256 `1e5e6946ca4133b395dfdd221b24b377a9abd56488f8ce5b33eb6fb6dbcf7715`.

- `LSeries_term_mul_scaled_cpow` at line 16
- `norm_LSeries_term_vertical` at line 32
- `continuous_LSeries_term_vertical` at line 37
- `integrable_scaled_mellin_line` at line 47
- `smoothMellin_absolute_exchange` at line 64
- `integrable_smoothLSeries_contour` at line 93
- `smoothLSeries_eq_mellinContour` at line 107
- `smoothMollifierBlock` at line 153
- `smoothMollifierBlock_eq_rightContour` at line 159
- `integrable_smoothMollifierBlock_rightContour` at line 179

### MathCollab.Density.Stronger.SmoothDetector

File: `lean/MathCollab/Density/Stronger/SmoothDetector.lean`; 394 source lines; SHA-256 `10ea1277dcbd4bbd7ba2c04a8660aa2ee89d3dc6ecd80edadc13f146616fdf77`.

- `smoothDetectorBlock` at line 21
- `summable_norm_detectorTerm` at line 24
- `summable_norm_detectorTerm_tail` at line 29
- `summable_norm_smoothDetectorBlock` at line 34
- `tsum_smoothDetectorBlock` at line 41
- `smoothDetectorBlock_zero_of_nonpos` at line 46
- `smoothDetectorBlock_zero_of_small` at line 51
- `tsum_norm_detector_tail_le` at line 67
- `shifted_indicator_tail_le` at line 88
- `smoothDetectorBlock_scale_tail_bound` at line 111
- `smoothDetectorBlock_scale_tail_le_two_rpow` at line 122
- `smoothScaleIndices` at line 165
- `mem_smoothScaleIndices` at line 168
- `smoothScaleIndices_nonempty` at line 184
- `smoothScaleIndices_card_le` at line 189
- `smoothDetectorBlock_norm_partition` at line 210
- `exists_smoothDetectorBlock` at line 248
- `smoothScaleIndices_card_le_log` at line 277
- `log_sq_eventually_le_height` at line 291
- `smoothDetector_eventually_large` at line 302
- `smoothDetectorBlock_eq_smoothMollifierBlock` at line 358

### MathCollab.Density.Stronger.MellinEntire

File: `lean/MathCollab/Density/Stronger/MellinEntire.lean`; 62 source lines; SHA-256 `601eeebd2ebf45572a0ef257c4e6d7307ac7418d839b9ba6685bf2ef339fdfa7`.

- `positive_compact_cutoff_isBigO_atTop` at line 19
- `positive_compact_cutoff_isBigO_zero` at line 29
- `positive_compact_cutoff_mellin_hasDerivAt` at line 40
- `positive_compact_cutoff_mellin_differentiable` at line 48
- `dampedCutoff_mellin_entire` at line 53

### MathCollab.Density.Stronger.SmoothContour

File: `lean/MathCollab/Density/Stronger/SmoothContour.lean`; 116 source lines; SHA-256 `d970ae3d5181de711a8f41600fb4421f4006e81c24c8ba4f62d873828faf686f`.

- `smoothDetectorKernel` at line 23
- `smoothContourNumerator` at line 27
- `smoothDetectorResidue` at line 31
- `smoothContourNumerator_div_eq_kernel` at line 35
- `smoothContourNumerator_at_pole` at line 44
- `smoothContourNumerator_differentiable` at line 50
- `entire_div_sub_rectangle` at line 66
- `smoothDetector_finite_rectangle_residue` at line 80

### MathCollab.Density.Stronger.SmoothContourEstimates

File: `lean/MathCollab/Density/Stronger/SmoothContourEstimates.lean`; 208 source lines; SHA-256 `a40f79273afc08d4fc3b3572063067893e3b0214a50d741540c041dc172066c7`.

- `norm_riemannZeta_le_eight_mul_norm` at line 19
- `continuous_smoothDetectorKernel_line` at line 37
- `integrable_smoothDetectorKernel_line` at line 70
- `integrable_smoothDetectorKernel_left` at line 110
- `integrable_smoothDetectorKernel_right` at line 120
- `smoothDetectorKernel_horizontal_bound` at line 131
- `tendsto_smoothDetector_horizontal_integral` at line 180

### MathCollab.Density.Stronger.SmoothContourIdentity

File: `lean/MathCollab/Density/Stronger/SmoothContourIdentity.lean`; 62 source lines; SHA-256 `7f0547a1a33b49ebc68c4e9f6d3e68188f4cdab652c5bbb4933f72e99a0cf77f`.

- `smoothDetector_contour_identity` at line 18

### MathCollab.Density.Stronger.SmoothBlockContour

File: `lean/MathCollab/Density/Stronger/SmoothBlockContour.lean`; 101 source lines; SHA-256 `1855f5096f5e51bc674c7e6916e92eef7c9c6eebe1c2385c017bf3fbfd7f57c7`.

- `smoothMollifierBlock_contour_identity` at line 19
- `smoothDetectorBlock_contour_identity` at line 31
- `uniform_smoothDetectorResidue_bound` at line 46
- `uniform_smoothDetectorKernel_critical_bound` at line 72

### MathCollab.Density.Stronger.WeightedCriticalMean

File: `lean/MathCollab/Density/Stronger/WeightedCriticalMean.lean`; 98 source lines; SHA-256 `a09edc80889647f6e210a58e8ae1ab8543a14c6f11bd135714746e4073f1d6bf`.

- `weightedCriticalMean` at line 15
- `integrable_weightedCriticalMean` at line 18
- `weightedCriticalMean_nonneg` at line 52
- `uniform_smoothDetector_critical_integral_bound` at line 57
- `uniform_smoothMollifierBlock_mean_bound` at line 80

### MathCollab.Density.Stronger.WeightedTwelfth

File: `lean/MathCollab/Density/Stronger/WeightedTwelfth.lean`; 88 source lines; SHA-256 `ca8ee58c3a86a2d6ca952219866e9e985bda0e5bf266ba4c19e5268333e9fbe7`.

- `zetaMomentCriticalNorm_nonneg` at line 17
- `zetaMomentCriticalNorm_le_linear` at line 19
- `weightedCriticalTwelfth` at line 24
- `integrable_weightedCriticalTwelfth` at line 28
- `weightedCriticalMean_twelfth_le` at line 60
- `weightedCriticalTwelfth_eq_translated` at line 71
- `separated_critical_twelfth_on_interval` at line 80

### MathCollab.Density.Stronger.MomentGrowth

File: `lean/MathCollab/Density/Stronger/MomentGrowth.lean`; 55 source lines; SHA-256 `cd1220457357b0ee0d6dd461478b287d2a1f04c7bf3c33c3b12a747615ca6868`.

- `zetaMomentCriticalNorm_eventually_lt_slab_power` at line 19
- `zetaMomentCriticalNorm_twelfth_eventually_le_cube` at line 41

### MathCollab.Density.Stronger.AtkinsonCardinalityAbsorption

File: `lean/MathCollab/Density/Stronger/AtkinsonCardinalityAbsorption.lean`; 104 source lines; SHA-256 `467f02f7e073a82e9c903ea2ea33f941784613a9a74d5076f50a6a422c0de082`.

- `atkinsonAbsorptionLength` at line 33
- `atkinsonAbsorptionLength_pos` at line 36
- `atkinsonAbsorptionLength_radical` at line 42
- `atkinsonAbsorptionLength_absorbs` at line 50
- `atkinson_card_le_of_packet` at line 58
- `atkinson_covered_card_budget` at line 85

### MathCollab.Density.Stronger.AtkinsonHeightCover

File: `lean/MathCollab/Density/Stronger/AtkinsonHeightCover.lean`; 85 source lines; SHA-256 `a13a406a23e299683f4ec82a922b895d9e667704f9e076167dbb95ac59404b83`.

- `atkinsonHeightBin` at line 30
- `atkinsonHeightFiber` at line 33
- `atkinsonHeightFiber_subset` at line 36
- `atkinsonHeightBin_mem_range` at line 40
- `atkinsonHeightFiber_interval` at line 49
- `atkinsonHeightFiber_card_partition` at line 65
- `atkinson_card_le_of_height_fibers` at line 72

### MathCollab.Density.Stronger.AtkinsonGlobalCardinality

File: `lean/MathCollab/Density/Stronger/AtkinsonGlobalCardinality.lean`; 78 source lines; SHA-256 `e0567797b1f5278d4fd12cf66cf144728a4a8e1d0474e08a54de0ba4c3f641f4`.

- `atkinson_card_le_of_local_packets` at line 32
- `atkinson_count_exponent_budget` at line 56

### MathCollab.Density.Stronger.Peaks.Inputs

File: `lean/MathCollab/Density/Stronger/Peaks/Inputs.lean`; 63 source lines; SHA-256 `52b470fdfcfae0af3aa2bea9ac13cbbeaf01d9c408865b89758d5e61b6278153`.

- `separatedAt` at line 30
- `atkinsonLocalMeanExcess` at line 33
- `PointMeanInput` at line 37
- `LocalMeanPacketInput` at line 54

### MathCollab.Density.Stronger.Atkinson.AtkinsonSourceAssembly

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonSourceAssembly.lean`; 121 source lines; SHA-256 `e4397b75075f42656ea81456dd82f55af6eab462ad1d4362008556667452f6ec`.

- `LocalMeanSourceToPrefix` at line 28
- `packet_width_scales` at line 37
- `localMeanPacketInput_of_sourceToPrefix` at line 53

### MathCollab.Density.Stronger.Atkinson.AtkinsonStationarySourceAssembly

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonStationarySourceAssembly.lean`; 72 source lines; SHA-256 `3b8e1f2eb9545e8db5a832496ac60ead97a9e0a8d31df3fbac69d707bf62f574`.

- `LocalMeanStationaryInput` at line 26
- `localMeanSourceToPrefix_of_stationary` at line 36
- `localMeanPacketInput_of_stationary` at line 68

### MathCollab.Density.Stronger.Atkinson.AtkinsonNativeLocalMean

File: `lean/MathCollab/Density/Stronger/Atkinson/AtkinsonNativeLocalMean.lean`; 68 source lines; SHA-256 `d3bc695e563ea5161ec1cfb08757d28f3df88edd029ed32c4b48c166c19ac9e3`.

- `exists_zetaSquareLocalMean_le_atkinson_stationary` at line 24
- `localMeanStationaryInput_native` at line 64

### MathCollab.Density.Stronger.PointMean.GammaDisplacement

File: `lean/MathCollab/Density/Stronger/PointMean/GammaDisplacement.lean`; 152 source lines; SHA-256 `9eb5859ed75cbec36c8ab337a9a3907067fd2858b40c301a8da5afb3230ce7aa`.

- `re_digamma_le_log_height_add_four` at line 24
- `real_inner_self_mul` at line 40
- `exists_norm_Gamma_sq_right_displacement_le` at line 52
- `exists_norm_Gamma_right_displacement_le` at line 127

### MathCollab.Density.Stronger.PointMean.MellinBounds

File: `lean/MathCollab/Density/Stronger/PointMean/MellinBounds.lean`; 221 source lines; SHA-256 `ee1dbcf4c1a10c8d1365fa9c75d9abd39699b7422a00591044edf3a2037feb0a`.

- `heathBrownSmoothedDivisorMajorant` at line 29
- `summable_heathBrownSmoothedDivisorMajorant` at line 32
- `heathBrownSmoothedDivisorMajorant_nonneg` at line 37
- `norm_heathBrownSmoothedDivisorTerm_le` at line 42
- `summable_norm_heathBrownSmoothedDivisorTerm` at line 73
- `norm_heathBrownSmoothedDivisorSeries_le` at line 79
- `exists_norm_Gamma_heathBrown_residue_strip_le` at line 93
- `exists_norm_Gamma_heathBrown_movingPole_le` at line 104
- `norm_digamma_small_strip_le_linear` at line 146
- `exists_norm_heathBrownMovingPoleResidue_le` at line 172

### MathCollab.Density.Stronger.PointMean.ExponentialMoments

File: `lean/MathCollab/Density/Stronger/PointMean/ExponentialMoments.lean`; 291 source lines; SHA-256 `861c04adf711f1e7e607ca4ccc1b55082cde6c796a4464972b4b726eee27f2ba`.

- `heathBrownMellinCriticalMoment` at line 25
- `heathBrownFullCriticalMoment` at line 31
- `heathBrownMellinCriticalMoment_integrand_nonneg` at line 35
- `integrable_heathBrownMellinCriticalMoment` at line 42
- `integrable_heathBrownFullCriticalMoment` at line 151
- `heathBrownMellinCriticalMoment_le_full` at line 243
- `heathBrownMellinCriticalMoment_nonneg` at line 278
- `heathBrownFullCriticalMoment_nonneg` at line 285

### MathCollab.Density.Stronger.PointMean.OffCriticalPositive

File: `lean/MathCollab/Density/Stronger/PointMean/OffCriticalPositive.lean`; 220 source lines; SHA-256 `52198fc49535a8fd0d30e4661955dc0aabcac08c1ab0cf1602d6deb04d0715ff`.

- `exists_heathBrown_Gamma_shift_kernel_strong_bound` at line 24
- `heathBrownStrongMellinCriticalMoment` at line 35
- `integrable_heathBrownStrongMellinCriticalMoment` at line 40
- `heathBrownStrongMellinCriticalMoment_nonneg` at line 68
- `exists_norm_heathBrown_leftMellinIntegrand_strong_le` at line 74
- `exists_norm_heathBrown_leftVertical_strong_le` at line 108
- `exists_heathBrown_offCritical_plus_strong_le` at line 170

### MathCollab.Density.Stronger.PointMean.Reflection

File: `lean/MathCollab/Density/Stronger/PointMean/Reflection.lean`; 220 source lines; SHA-256 `cd4db72b9c7c01ad730751c5f3990315463dc90f9775f74d3cb62274cfad1c2c`.

- `norm_GammaR_real_im` at line 25
- `norm_GammaR_real_neg_im_eq` at line 40
- `heathBrown_zeta_displaced_reflection` at line 56
- `exists_norm_GammaR_heathBrown_reflection_ratio_le` at line 90
- `exists_heathBrown_offCritical_minus_strong_le` at line 173

### MathCollab.Density.Stronger.PointMean.GammaConvolution

File: `lean/MathCollab/Density/Stronger/PointMean/GammaConvolution.lean`; 269 source lines; SHA-256 `dbbfd908a6e593a0136c7ab573882ca4e9d9d2a5423614de62489779cd726b59`.

- `heathBrownGammaReserveKernel` at line 25
- `integrable_inv_delta_sq_add_sq` at line 28
- `integral_inv_delta_sq_add_sq` at line 37
- `heathBrownGammaReserveKernel_sq_le` at line 58
- `integrable_heathBrownGammaReserveKernel_sq` at line 82
- `integral_heathBrownGammaReserveKernel_sq_le` at line 101
- `heathBrownStrongGammaConvolutionIntegrand` at line 112
- `heathBrownStrongGammaConvolutionIntegrand_nonneg` at line 117
- `heathBrown_strong_exponential_reserve` at line 123
- `heathBrownStrongGammaConvolutionIntegrand_le` at line 135
- `integrable_heathBrownGammaReserveKernel_sq_sub` at line 180
- `integral_heathBrownGammaReserveKernel_sq_sub` at line 190
- `integrable_heathBrownStrongGammaConvolutionIntegrand` at line 205
- `integral_heathBrownStrongGammaConvolutionIntegrand_le` at line 238

### MathCollab.Density.Stronger.PointMean.DoubleConvolution

File: `lean/MathCollab/Density/Stronger/PointMean/DoubleConvolution.lean`; 360 source lines; SHA-256 `28485f75b5a0a4ca9c5a5cbe4bcd2bc34953f0a90fbd380ff65ef822883eda7e`.

- `heathBrownStrongSingularKernel` at line 21
- `heathBrownCriticalWeighted` at line 24
- `integrable_heathBrownCriticalWeighted` at line 27
- `heathBrownCriticalWeighted_nonneg` at line 32
- `integrable_heathBrown_reserve_sq_mul_critical_add` at line 37
- `integral_heathBrown_reserve_sq_mul_critical_add` at line 101
- `integrable_heathBrown_reserve_sq_snd_mul_critical_add` at line 135
- `integral_heathBrown_reserve_sq_snd_mul_critical_add` at line 149
- `heathBrownStrongDoubleIntegrand` at line 176
- `heathBrownStrongDoubleMajorant` at line 182
- `heathBrownStrongDoubleIntegrand_nonneg` at line 189
- `heathBrownStrongDoubleIntegrand_le` at line 195
- `integrable_heathBrownStrongDoubleMajorant` at line 231
- `integrable_heathBrownStrongDoubleIntegrand` at line 244
- `integral_heathBrownStrongDoubleIntegrand_le` at line 269
- `integral_strongKernel_mul_strongMoment_eq_double` at line 317
- `integrable_strongKernel_mul_strongMoment` at line 334
- `integral_strongKernel_mul_strongMoment_le` at line 352

### MathCollab.Density.Stronger.PointMean.HorizontalEdges

File: `lean/MathCollab/Density/Stronger/PointMean/HorizontalEdges.lean`; 329 source lines; SHA-256 `b3628951d3074de79d96c1ff88e54abc6acca7b060ed0ff5b0423ec98be2ba3f`.

- `eventually_log_sq_le_rpow` at line 28
- `eventually_const_mul_rpow_le_rpow` at line 40
- `eventually_heathBrownLemmaThreeRadius_le_half_identity` at line 59
- `exists_norm_Gamma_heathBrown_small_horizontal_strong_le` at line 71
- `exists_norm_heathBrownLemmaThree_horizontal_integrand_le` at line 113
- `exists_norm_heathBrownLemmaThree_horizontalEdge_le` at line 159
- `heathBrown_logSquare_exponential_absorption` at line 206
- `eventually_norm_heathBrownLemmaThree_horizontalEdges_le_one` at line 234

### MathCollab.Density.Stronger.PointMean.VerticalEdges

File: `lean/MathCollab/Density/Stronger/PointMean/VerticalEdges.lean`; 529 source lines; SHA-256 `7aa60e5859be370a399512abfcffb3edf002b316a6048da2fb9cad8202f63b0f`.

- `integral_exp_neg_abs_heathBrown` at line 26
- `integrable_exp_neg_abs_heathBrown` at line 32
- `heathBrownStrongSingularKernel_le_exp` at line 51
- `integrable_heathBrownStrongSingularKernel` at line 68
- `integral_heathBrownStrongSingularKernel_le` at line 86
- `intervalIntegral_heathBrownStrongSingularKernel_le` at line 100
- `norm_VIntegral'_le_intervalIntegral_norm` at line 114
- `exists_norm_heathBrownLemmaThree_plusEdge_integrand_le` at line 140
- `integrable_heathBrownStrongLongEdgeMajorant` at line 180
- `integral_heathBrownStrongLongEdgeMajorant_le` at line 190
- `exists_norm_heathBrownLemmaThree_plusEdge_le` at line 221
- `exists_norm_heathBrownLemmaThree_minusEdge_integrand_le` at line 277
- `exists_norm_heathBrownLemmaThree_minusEdge_le` at line 326
- `heathBrownLemmaThree_minus_factor_le_exp_four` at line 399
- `eventually_heathBrownLemmaThree_minus_factor` at line 421
- `exists_eventually_heathBrownLemmaThree_fullMoment` at line 433

### MathCollab.Density.Stronger.PointMean.Statement

File: `lean/MathCollab/Density/Stronger/PointMean/Statement.lean`; 84 source lines; SHA-256 `5757bcfb3c2e82a8e739c87f1911978e1cd6a073d951064e0988cb4de2b7193a`.

- `statement_intervalIntegrable_exp_neg_abs_sub_mul` at line 22
- `heathBrownLemmaThreeMoment` at line 29
- `HeathBrownLemmaThree` at line 34
- `heathBrownLemmaThreeMoment_eq_centered` at line 44
- `heathBrownLemmaThreeMoment_le_centered` at line 68

### MathCollab.Density.Stronger.PointMean.Native

File: `lean/MathCollab/Density/Stronger/PointMean/Native.lean`; 312 source lines; SHA-256 `13a3cb3960b845c3d007114e719ea61b96e48b31a4b2fae38e223d437b8cf129`.

- `exists_zetaMomentCriticalNorm_sq_le_quadratic` at line 28
- `integral_exp_neg_half_abs_heathBrown` at line 82
- `integrable_exp_neg_half_abs_heathBrown` at line 96
- `heathBrown_fullMoment_tail_pointwise` at line 108
- `exists_heathBrownFullCriticalMoment_le_truncated` at line 164
- `heathBrownLemmaThreeMoment_nonneg` at line 219
- `exists_eventually_heathBrownLemmaThree_truncated` at line 227
- `heathBrownLemmaThree_native` at line 264

### MathCollab.Density.Stronger.PointMean.ExponentialOverlap

File: `lean/MathCollab/Density/Stronger/PointMean/ExponentialOverlap.lean`; 157 source lines; SHA-256 `75c6439286bb5e3bf48439d4035d2b89a08d4b41ddf213425546fe34a3bfa53d`.

- `exp_neg_abs_le_half_pow_floor` at line 27
- `separated_distance_shell_card_le_two` at line 50
- `sum_exp_neg_abs_sub_le_four` at line 116

### MathCollab.Density.Stronger.PointMean.IntegralOverlap

File: `lean/MathCollab/Density/Stronger/PointMean/IntegralOverlap.lean`; 150 source lines; SHA-256 `e17718bcdd3221885f88fb82ec6f95f912529d33cd0d8c5d4a06de6b6e0996f9`.

- `intervalIntegrable_exp_neg_abs_sub_mul` at line 22
- `sum_intervalIntegral_exp_neg_abs_sub_mul_eq` at line 30
- `sum_intervalIntegral_exp_neg_abs_sub_mul_le_four` at line 40
- `sum_intervalIntegral_exp_kernel_zeta_sq_le_four` at line 65
- `sum_truncated_exp_kernel_zeta_sq_le_four` at line 78
- `sum_truncated_exp_kernel_zeta_sq_le_localSecondMoment` at line 116

### MathCollab.Density.Stronger.PointMean.Equation44

File: `lean/MathCollab/Density/Stronger/PointMean/Equation44.lean`; 119 source lines; SHA-256 `dbd9ad81fde3ac902d88410c7de379441af40becdebcaa0f554a7603f2a463d9`.

- `heathBrown_equation44_of_lemmaThree` at line 25
- `heathBrown_equation44_native` at line 104

### MathCollab.Density.Stronger.PointMean.PeaksInput

File: `lean/MathCollab/Density/Stronger/PointMean/PeaksInput.lean`; 20 source lines; SHA-256 `ed9b1d671877aa2858dfc852c94fbdfe52f74a3402445a12591fd4df21ec1f58`.

- `pointMeanInput_native` at line 17

### MathCollab.Density.Stronger.Peaks.Clusters

File: `lean/MathCollab/Density/Stronger/Peaks/Clusters.lean`; 133 source lines; SHA-256 `b3463c9dfcbd697cc14ee6d40c3fcf87901110e57c9cfefacd1b720737182105`.

- `pointClusterBins` at line 30
- `pointCluster` at line 33
- `pointClusterCenter` at line 36
- `pointClusterCenters` at line 39
- `pointCluster_subset` at line 42
- `mem_pointClusterBins_iff` at line 46
- `pointCluster_card_partition` at line 51
- `pointCluster_interval` at line 55
- `pointCluster_symmetric_interval` at line 62
- `pointClusterCenter_range` at line 71
- `pointClusterCenter_injective` at line 83
- `pointClusterCenters_card` at line 92
- `pointClusterCenter_gap_of_same_parity` at line 96
- `pointClusterCenters_separated` at line 105
- `card_eq_sum_parity_cards` at line 119

### MathCollab.Density.Stronger.FiniteOccupancy

File: `lean/MathCollab/Density/Stronger/FiniteOccupancy.lean`; 85 source lines; SHA-256 `d73c2b08d3333803b9d4d9dcbc2a6664348bd8bdb71baedd3e014582cfe75cc7`.

- `sum_nat_occupancy_eq_sum_superlevel` at line 33
- `sum_pos_nat_inv_sq_le_two` at line 52
- `sum_nat_occupancy_le_of_superlevels` at line 61

### MathCollab.Density.Stronger.Peaks.ClusterCount

File: `lean/MathCollab/Density/Stronger/Peaks/ClusterCount.lean`; 291 source lines; SHA-256 `0261314b7c43db12d55c431e8efc8e36b41500cf0405ece85c96c3fd37527ec3`.

- `atkinsonLocalMeanExcess_threshold_iff` at line 28
- `exists_atkinsonLocalMeanExcess_card_le_above_fourthRoot` at line 40
- `exists_pointCluster_localMean_bound` at line 71
- `localMean_lower_bound_of_peak_mass` at line 107
- `exists_pointCluster_superlevel_entry` at line 119
- `pointClusterSuperlevel` at line 150
- `exists_pointCluster_superlevel_count` at line 153
- `occupancy_inverse_power_budget` at line 226
- `exists_pointValue_card_le_with_width` at line 241

### MathCollab.Density.Stronger.Peaks.WidthRanges

File: `lean/MathCollab/Density/Stronger/Peaks/WidthRanges.lean`; 313 source lines; SHA-256 `1598095cb8a21b93ede1510e0984e8213cc53fe54373001f7f576698fba83220`.

- `eventually_pointValue_log_scales` at line 29
- `pointValueWidth_error_absorption` at line 53
- `pointValueWidth_count_identity` at line 64
- `exists_pointValue_card_le_source_range` at line 71
- `eventually_pointValue_source_lower_range` at line 167
- `pointValue_count_mul_twelfth_identity` at line 184
- `pointValue_count_mul_twelfth_le_growth` at line 190
- `eventually_pointValue_high_budget` at line 224
- `exists_pointValue_twelfth_weighted_card_le_of_inputs` at line 238
- `pointValue_peak_card_of_inputs` at line 298

### MathCollab.Density.Stronger.DyadicMoment

File: `lean/MathCollab/Density/Stronger/DyadicMoment.lean`; 125 source lines; SHA-256 `5ceea6edb20deff8e12a191a2c3027a6b05037b4369c59ae35d09174addc2f9e`.

- `exists_dyadic_cutoff` at line 23
- `exists_dyadic_count_sq_le_rpow` at line 30
- `integral_zero_le_of_dyadic` at line 63

### MathCollab.Density.Stronger.ConditionalMoment

File: `lean/MathCollab/Density/Stronger/ConditionalMoment.lean`; 169 source lines; SHA-256 `cb9d312b51112d07b6dc52c47fb7d636ccf6f23a3502046d6f95feba6378350b`.

- `log_height_cube_div_le` at line 22
- `eventually_zeta_high_log_budget` at line 31
- `zeta_twelfth_high_eventually_of_tail` at line 47
- `zeta_twelfth_dyadic_of_fourth_and_tail` at line 97
- `zeta_twelfth_physical_of_dyadic` at line 134
- `zeta_twelfth_physical_of_fourth_and_tail` at line 157

### MathCollab.Density.Stronger.SeparatedVolume

File: `lean/MathCollab/Density/Stronger/SeparatedVolume.lean`; 97 source lines; SHA-256 `e55095780a4d57d50497e9d95fb12f9c0b80eaaff58aef42b9050bbcbae779de`.

- `exists_unitSeparated_closedBall_cover_of_card_bound` at line 24
- `volume_le_two_mul_of_separated_card_bound` at line 74

### MathCollab.Density.Stronger.Fourth.SquareKernel

File: `lean/MathCollab/Density/Stronger/Fourth/SquareKernel.lean`; 173 source lines; SHA-256 `06d83e889f1e3788db05b8a9fa74f8e5b1862d4378cb0590dd805f0e832adef6`.

- `zetaGammaShiftError_le_quadratic` at line 24
- `exp_zetaGammaLeadingLog_vertical_le` at line 37
- `exists_norm_zetaFourthKernel_near_le` at line 58
- `exists_norm_zetaFourthKernel_le` at line 125
- `integrable_zetaFourthKernel_vertical` at line 147
- `exists_integral_norm_zetaFourthKernel_le` at line 156

### MathCollab.Density.Stronger.Fourth.SquareTerm

File: `lean/MathCollab/Density/Stronger/Fourth/SquareTerm.lean`; 251 source lines; SHA-256 `8af4901eaf03338d0f5c79ab6e3f8d1b1986607147f740150561fdb6f58423ba`.

- `zetaFourthTerm` at line 24
- `zetaFourthTerm_zero` at line 27
- `differentiableAt_zetaFourthKernel` at line 30
- `differentiableAt_zetaFourthTerm` at line 45
- `norm_zetaFourthTerm_vertical` at line 60
- `norm_fourth_divisorTerm_le_card` at line 66
- `zetaFourthTerm_one` at line 77
- `zetaFourthTerm_boundaryRect_zero` at line 83
- `exists_norm_zetaFourthKernel_strip_le` at line 102
- `continuous_zetaFourthTerm_vertical` at line 187
- `exists_norm_zetaFourthTerm_strip_le` at line 197
- `integrable_zetaFourthTerm_vertical` at line 212
- `tendsto_zetaFourthTerm_horizontal_of_sq_eq` at line 221

### MathCollab.Density.Stronger.Fourth.SquareLineShift

File: `lean/MathCollab/Density/Stronger/Fourth/SquareLineShift.lean`; 91 source lines; SHA-256 `99c975837e08fa2088c2e43984ae6fdb7a0a0ef6a82d3e1ce0177f9733fa4894`.

- `integral_zetaFourthTerm_vertical_eq_of_le` at line 22
- `integral_zetaFourthTerm_vertical_eq` at line 48
- `zetaFourthContribution` at line 56
- `zetaFourthContribution_one` at line 60
- `zetaFourthContribution_line_eq` at line 67
- `hasSum_zetaFourthContribution` at line 73
- `zetaFourthRightPiece_eq_tsum` at line 85

### MathCollab.Density.Stronger.Fourth.SquareTruncation

File: `lean/MathCollab/Density/Stronger/Fourth/SquareTruncation.lean`; 179 source lines; SHA-256 `9d7f25b79b3c3b203862120b0ee9f4b88d22f666b42e750e745d29a80970178d`.

- `integral_norm_zetaFourthTerm_vertical` at line 25
- `exists_norm_zetaFourthContribution_le` at line 32
- `summable_fourth_divisorWeight` at line 58
- `zetaFourthPrefix` at line 80
- `zetaFourthTail` at line 83
- `zetaFourthPrefix_eq_integral` at line 86
- `zetaFourthPrefix_line_eq` at line 100
- `zetaFourthRightPiece_eq_prefix_add_tail` at line 107
- `summable_norm_zetaFourthTail` at line 114
- `exists_norm_zetaFourthTail_le` at line 119
- `exists_norm_fourthRightPiece_sub_prefix_le` at line 140
- `zeta_fourth_le_prefix_add_tail` at line 153
- `exists_zeta_fourth_le_prefix_add_weightTail` at line 163

### MathCollab.Density.Stronger.Fourth.SquareTail

File: `lean/MathCollab/Density/Stronger/Fourth/SquareTail.lean`; 168 source lines; SHA-256 `a42e66c6cbbb20b560effcd4dd1e9d157368471e4b9ec894e56e5f732481df9a`.

- `tsum_nat_rpow_tail_le` at line 26
- `fourth_divisorWeight_le_rpow` at line 50
- `tsum_fourth_divisorWeight_tail_le` at line 64
- `exists_norm_zetaFourthTail_cutoff_le` at line 87
- `fourth_tail_scale_le` at line 107
- `exists_norm_fourthRightPiece_sub_cutoff_le` at line 129

### MathCollab.Density.Stronger.Fourth.MeanValueCore

File: `lean/MathCollab/Density/Stronger/Fourth/MeanValueCore.lean`; 967 source lines; SHA-256 `225d06b639d2fab6bb1323ebfc36c6ae588f6b1577d439dd39bc3c1ded963e6d`.

- `sum_sq_le_card_mul_sum_sq` at line 26
- `complex_sum_sq_le_card_mul_sum_sq` at line 39
- `trigPoly` at line 51
- `integral_cexp_int` at line 54
- `integral_conj_fourier_term_mul_fourier_term` at line 73
- `integral_conj_trigPoly_mul_trigPoly` at line 110
- `integral_norm_sq_trigPoly` at line 142
- `continuous_trigPoly` at line 161
- `integral_sawtooth_cexp` at line 167
- `integral_sawtooth_cexp_all` at line 242
- `hilbertForm` at line 260
- `integral_sawtooth_conj_fourier_mul_fourier` at line 264
- `integral_sawtooth_conj_trigPoly_mul_trigPoly` at line 310
- `norm_sawtooth_conj_trigPoly_mul_trigPoly_le` at line 347
- `hilbertForm_norm_le` at line 368
- `nat_hilbertForm_norm_le` at line 429
- `abs_inv_log_sub_sub_div_le_one` at line 439
- `norm_complex_log_kernel_error_le_one` at line 520
- `logHilbertQuad` at line 534
- `natMainQuad` at line 540
- `logKernelErrorQuad` at line 547
- `logHilbertQuad_eq_main_add_error` at line 553
- `logKernelErrorQuad_norm_le` at line 567
- `natScaledCoeff` at line 604
- `natMainQuad_eq_scaled_hilbert` at line 607
- `natScaledCoeff_l2_le` at line 623
- `natMainQuad_norm_le` at line 645
- `logHilbertQuad_norm_le` at line 676
- `dirichletTime` at line 692
- `endpointTwist` at line 697
- `norm_endpointTwist` at line 700
- `integral_conj_dirichlet_term_mul_dirichlet_term` at line 709
- `integral_conj_dirichletTime_mul_dirichletTime` at line 802
- `continuous_dirichletTime` at line 893
- `ofReal_integral_norm_sq_dirichletTime` at line 899
- `integral_norm_sq_dirichletTime_le` at line 911

### MathCollab.Density.Stronger.Fourth.PrefixMean

File: `lean/MathCollab/Density/Stronger/Fourth/PrefixMean.lean`; 278 source lines; SHA-256 `0ac6d05a2f02d536c25268a827fd53e3dab9bb3e7ddca4f0c652c7e2e4007de5`.

- `norm_sum_mul_sq_le` at line 24
- `dirichletTime_shift` at line 36
- `integral_norm_sq_dirichletTime_interval_le` at line 47
- `integral_norm_sq_dirichletTime_reflected_le` at line 63
- `dirichletPrefix` at line 76
- `continuous_dirichletPrefix` at line 79
- `dirichletPrefix_one` at line 84
- `dirichletPrefix_double` at line 88
- `dirichletPrefix_pow_two` at line 94
- `norm_dirichletPrefix_pow_two_sq_le` at line 103
- `integral_norm_sq_dirichletPrefix_le_blocks` at line 119
- `integral_norm_sq_dirichletPrefix_le` at line 149
- `integral_norm_sq_dirichletPrefix_reflected_le` at line 190
- `fourth_divisorTerm_eq_coeff_phase` at line 205
- `sum_fourth_divisorTerm_eq_prefix` at line 223
- `norm_dirichletPrefix_le` at line 245
- `continuous_dirichletPrefix_reflected` at line 257
- `integrable_gaussian_dirichletPrefix_norm_pow` at line 261

### MathCollab.Density.Stronger.Fourth.GaussianProducer

File: `lean/MathCollab/Density/Stronger/Fourth/GaussianProducer.lean`; 227 source lines; SHA-256 `7a3c0c04d23b0d73214eac46a3f47b49ab1fc617b18113d7f6caf7347e889731`.

- `exists_integral_sq_fourthPolynomial_le` at line 24
- `exists_integral_sq_fourthDivisorSum_le` at line 56
- `integrable_gaussian_dirichletPrefix_prod` at line 67
- `intervalIntegrable_gaussianPrefixMean` at line 94
- `integral_gaussianPrefixMean_swap` at line 101
- `exists_integral_gaussian_fourthPolynomial_le` at line 111
- `critical_norm_matches_existing` at line 140
- `fourth_height_power_identity` at line 146
- `exists_fourth_dyadic_budget` at line 160
- `exists_scaled_gaussian_fourthPolynomial_le` at line 205

### MathCollab.Density.Stronger.Fourth.SquarePrefix

File: `lean/MathCollab/Density/Stronger/Fourth/SquarePrefix.lean`; 134 source lines; SHA-256 `90702293003fbc4642ee787bf679b213ea12a6ea6e238d124b19554668de08dc`.

- `integral_weighted_sq_le` at line 25
- `exists_norm_sq_fourthPrefix_le_gaussian` at line 60

### MathCollab.Density.Stronger.Fourth.FourthMoment

File: `lean/MathCollab/Density/Stronger/Fourth/FourthMoment.lean`; 122 source lines; SHA-256 `61a8aecb16ba4aea8939cd4a5498971d86331dcb05d06261bd5b0e99e517b6f2`.

- `zeta_fourth_dyadic` at line 25

### MathCollab.Density.FiniteDetector

File: `lean/MathCollab/Density/FiniteDetector.lean`; 139 source lines; SHA-256 `e18a0a74df0ff731843347101feff6239eefdd5916d8af185e80b5c9246711aa`.

- `firstDetectorCoefficient` at line 16
- `finiteDetector` at line 23
- `firstDetectorCoefficient_support` at line 26
- `firstDetectorCoefficient_real_support` at line 34
- `firstDetectorCoefficient_norm_le` at line 40
- `firstDetectorX_one_le` at line 49
- `detectorTerm_finite_split` at line 54
- `finiteDetector_decomposition` at line 83
- `finiteDetector_eventually_large_of_zeta_bound` at line 105

### MathCollab.Density.DetectorTaylorFamily

File: `lean/MathCollab/Density/DetectorTaylorFamily.lean`; 133 source lines; SHA-256 `db8fbb20c7a46418623d187ded37a123b577a910a3fc6ab144d371b299886bb9`.

- `detectorTaylorCoefficient` at line 17
- `detectorTaylorPolynomial` at line 20
- `detectorTaylorRatio` at line 24
- `detectorTaylorWeight` at line 27
- `detectorTaylorRatio_bounds` at line 30
- `abs_detectorTaylorWeight_le` at line 38
- `sum_abs_detectorTaylorWeight_le` at line 46
- `norm_detectorTaylorCoefficient_le` at line 54
- `exists_large_taylor_component` at line 71
- `norm_detectorTaylorPolynomial_le` at line 93
- `norm_detectorTaylor_tail_le` at line 113

### MathCollab.Density.DetectorBinomial

File: `lean/MathCollab/Density/DetectorBinomial.lean`; 76 source lines; SHA-256 `1d2c2396f1351884d31c9ddb3176d78f1596266fc0e319c407ce3b89de84036d`.

- `detectorTaylorRatio_eq_prod_div` at line 16
- `detector_descPochhammer_neg` at line 27
- `choose_neg_eq_detectorTaylorRatio` at line 39
- `hasSum_detector_binomial` at line 46
- `hasSum_detector_rpow` at line 66

### MathCollab.Density.DetectorDyadic

File: `lean/MathCollab/Density/DetectorDyadic.lean`; 92 source lines; SHA-256 `72a84836a267f173e83432102914dead522c90c9b2b80bdf3ebbf98fd2460d70`.

- `detectorBlock` at line 15
- `detectorDyadicCount` at line 19
- `sum_dyadic_Ioc` at line 21
- `finiteDetector_eq_dyadic_sum` at line 32
- `exists_detector_dyadic_block` at line 61
- `detectorBlock_scale_bounds` at line 80

### MathCollab.Density.DetectorBlockExpansion

File: `lean/MathCollab/Density/DetectorBlockExpansion.lean`; 96 source lines; SHA-256 `6242bbf712a2d1ad83b3d19a8ccd8b930233ca4e68e7612958c7c965e5ec4016`.

- `normalizedDetectorBlock` at line 16
- `cpow_neg_eq_real_phase` at line 20
- `detectorBlock_eq_normalized` at line 29
- `norm_normalizedDetectorBlock` at line 46
- `hasSum_detectorTaylorPolynomial` at line 53
- `norm_detectorTaylor_tsum_ge` at line 88

### MathCollab.Density.DetectorFamilyScales

File: `lean/MathCollab/Density/DetectorFamilyScales.lean`; 93 source lines; SHA-256 `dca92fff239f967457e64293d0abc25ab35679c2f99c913dd3673c40e2fc5b37`.

- `detectorTaylorCutoff` at line 16
- `firstDetectorCutoff_eventually_le_sq` at line 19
- `detectorDyadicCount_le_log` at line 31
- `detectorTaylorCutoff_le_log` at line 50
- `detectorTaylorCutoff_geometric_le` at line 57
- `detector_family_scales_eventually` at line 71

### MathCollab.Density.Stronger.GenericTaylorFamily

File: `lean/MathCollab/Density/Stronger/GenericTaylorFamily.lean`; 212 source lines; SHA-256 `69cfd8c4f9e6eb02e9f665edb4446ae8a3799178e8aca4901fdd20f7a9ba800b`.

- `genericTaylorCoefficient` at line 17
- `genericTaylorPolynomial` at line 20
- `genericBlock` at line 23
- `norm_genericTaylorCoefficient_le` at line 26
- `norm_genericTaylorPolynomial_le` at line 42
- `norm_genericTaylor_tail_le` at line 62
- `normalizedGenericBlock` at line 82
- `genericBlock_eq_normalized` at line 87
- `norm_normalizedGenericBlock` at line 104
- `hasSum_genericTaylorPolynomial` at line 111
- `norm_genericTaylor_tsum_ge` at line 146
- `norm_fixedGenericTaylor_tail_le` at line 156
- `exists_genericTaylor_component` at line 177

### MathCollab.Density.Stronger.SmoothShortBlock

File: `lean/MathCollab/Density/Stronger/SmoothShortBlock.lean`; 157 source lines; SHA-256 `85f6c7179e58179bd293e57e76c32aa9102886406e0a76e6f72ae19a69e98416`.

- `smoothShortCoefficient` at line 17
- `norm_smoothShortCoefficient_le` at line 21
- `smoothShortCoefficient_zero_of_le_half` at line 34
- `smoothShortCoefficient_zero_of_two_le` at line 39
- `smoothShortCoefficient_support` at line 44
- `smoothShortCoefficient_tsum_split` at line 55
- `smoothShortCoefficient_term_eq` at line 83
- `norm_smoothShortTaylorCoefficient_le` at line 89
- `summable_smoothShortTerm` at line 96
- `smoothDetector_tail_half_split` at line 108
- `exists_smoothShort_half` at line 127
- `exists_smoothShortTaylor_component` at line 146

### MathCollab.Density.FixedDetectorCover

File: `lean/MathCollab/Density/FixedDetectorCover.lean`; 122 source lines; SHA-256 `9525970768378086a278b45c4581ec620103263107f829ff57c7c6fb7caa4373`.

- `fixedDetectorIndices` at line 17
- `fixedDetectorIndices_card_le` at line 20
- `norm_fixedDetector_tail_le` at line 32
- `exists_fixedDetector_component` at line 52
- `fixedDetector_cover_of_zeta_bound` at line 89

### MathCollab.Density.DetectorConvolution

File: `lean/MathCollab/Density/DetectorConvolution.lean`; 141 source lines; SHA-256 `1fb33a50f3603111a24b458799ed14fba6bff82a186c72379bc4ca377d6dcfce`.

- `detectorBlockCoefficients` at line 16
- `detectorBlockCoefficients_apply` at line 20
- `detectorBlockCoefficients_norm_le` at line 24
- `arithmeticFunction_pow_norm_le` at line 34
- `detectorBlockCoefficients_pow_support` at line 63
- `detectorBlockCoefficients_pow_lower` at line 86
- `detectorBlockCoefficients_pow_LSeriesSummable` at line 108
- `detectorBlockCoefficients_LSeries_pow` at line 126

### MathCollab.Density.DetectorPowerScales

File: `lean/MathCollab/Density/DetectorPowerScales.lean`; 94 source lines; SHA-256 `402b4590110b6687bcf2ef7c3da6f244a5a79cca49919f447013844e615e7202`.

- `detectorPower` at line 15
- `densityAmbient` at line 20
- `detectorPower_spec` at line 23
- `detectorPower_base_le` at line 43
- `detectorPower_piece_scales` at line 58
- `detectorPower_support_scale` at line 78

### MathCollab.Density.DetectorPoweredPieces

File: `lean/MathCollab/Density/DetectorPoweredPieces.lean`; 148 source lines; SHA-256 `8d27c239ea10ee20d70470b2161b320b7d84a6c7864fe6e04ef246e8b082e7d8`.

- `poweredDetectorCoefficient` at line 18
- `dirichletPhase_div` at line 21
- `dirichletPhase_conj` at line 28
- `norm_detectingPolynomial_conj` at line 34
- `norm_detectingPolynomial_eq_cpow_sum` at line 41
- `detectorBlockCoefficients_LSeries` at line 61
- `norm_detectorTaylorPolynomial_LSeries` at line 73
- `sum_scaled_dyadic_Ioc` at line 81
- `detectorBlockCoefficients_pow_LSeries_sum` at line 92
- `exists_poweredDetector_piece` at line 114

### MathCollab.Density.Stronger.BoundedConvolution

File: `lean/MathCollab/Density/Stronger/BoundedConvolution.lean`; 69 source lines; SHA-256 `4def6655564057b4e27b2d3e12d2f680f02bd1f3af7709e64703588c1a60bd40`.

- `bounded_convolution_subpower` at line 18
- `bounded_convolution_eventually_le` at line 42

### MathCollab.Density.Stronger.FiniteConvolution

File: `lean/MathCollab/Density/Stronger/FiniteConvolution.lean`; 140 source lines; SHA-256 `43052bb2031890f5b3ceca2ba8924c0955bc54362d6b8d3a23952512cb48c38a`.

- `finiteBlock_pow_support` at line 17
- `finiteBlock_pow_lower` at line 36
- `finiteBlock_pow_LSeriesSummable` at line 52
- `finiteBlock_LSeries_pow` at line 71
- `finiteBlock_pow_LSeries_sum` at line 86
- `exists_finiteBlock_powered_piece` at line 108

### MathCollab.Density.Stronger.PowerScales

File: `lean/MathCollab/Density/Stronger/PowerScales.lean`; 124 source lines; SHA-256 `cb792cee7b1aa75b4af795992c590951da03c3e3b3c737141a03c3dc62b3ee9e`.

- `bounded_power_exponent` at line 19
- `bounded_power_scale` at line 43
- `short_scale_bounded_power` at line 74
- `bounded_power_piece_scales` at line 93
- `bounded_power_support_scale` at line 106
- `fixed_scale_factor_eventually_below_height` at line 115

### MathCollab.Density.Stronger.ShortFixedFamily

File: `lean/MathCollab/Density/Stronger/ShortFixedFamily.lean`; 160 source lines; SHA-256 `4321a943a490733c7710debc9d624fe7b6e79134fc8de583bcdcc144b4d5ff79`.

- `smoothHalfScale` at line 20
- `smoothHalfScale_pos` at line 22
- `smoothDetectorBlock_index_pos` at line 26
- `smoothHalfScale_zero_eq` at line 31
- `smoothHalfScale_one_eq` at line 39
- `smoothHalfScale_bounds` at line 44
- `smoothDetectorBlock_eq_halves` at line 58
- `exists_smoothBlock_Taylor_member` at line 68
- `smoothTaylorArithmetic` at line 101
- `smoothTaylorArithmetic_support` at line 107
- `smoothTaylorArithmetic_norm_le` at line 115
- `smoothTaylorArithmetic_LSeries` at line 122
- `norm_smoothTaylor_LSeries` at line 138
- `smoothPoweredCoefficient` at line 146
- `exists_smoothTaylor_powered_piece` at line 149

### MathCollab.Density.Stronger.ShortTaylorCover

File: `lean/MathCollab/Density/Stronger/ShortTaylorCover.lean`; 116 source lines; SHA-256 `500ea27ee7a2a6339605bdd864150fbdc81d800001ddfba2e8a9a750e88ef061`.

- `smoothTaylorIndices` at line 17
- `smoothTaylorMember` at line 21
- `smoothTaylorIndices_card_le_log` at line 26
- `shortTaylor_cutoff_error_eventually` at line 38
- `smooth_short_Taylor_cover` at line 56
- `smooth_long_or_short_Taylor_cover` at line 95

### MathCollab.Density.Stronger.ShortPoweredHeight

File: `lean/MathCollab/Density/Stronger/ShortPoweredHeight.lean`; 140 source lines; SHA-256 `fcc1f88a0437d02fdcb84f3463b4497f6377bfb96545d9aac81143c185eac861`.

- `smoothHeightConstant` at line 16
- `smoothHeightConstant_pos` at line 18
- `exists_smoothPowered_height` at line 22
- `smoothHeightConstant_eventually` at line 64
- `normalizedSmoothPoweredCoefficient` at line 77
- `detectingPolynomial_normalizedSmoothPowered` at line 80
- `normalizedSmoothPoweredCoefficient_eventually` at line 90
- `exists_normalizedSmoothPowered_height` at line 111

### MathCollab.Density.Stronger.ShortPoweredFamily

File: `lean/MathCollab/Density/Stronger/ShortPoweredFamily.lean`; 148 source lines; SHA-256 `a14a94741aa4ce2a834998118a2c9448f15bc90cea7fd07e0beb45f863934e4e`.

- `smoothPowerBound` at line 16
- `smoothPoweredFamilyScale` at line 18
- `smoothPoweredIndices` at line 23
- `smoothPoweredFamilyCoefficient` at line 30
- `smoothPoweredFamilyScale_pos` at line 34
- `mem_smoothPoweredIndices` at line 39
- `smoothTaylorIndices_card_eventually` at line 57
- `smoothPoweredIndices_card_eventually` at line 70
- `smoothPoweredFamily_admissible` at line 92
- `smooth_long_or_short_powered_cover` at line 120

### MathCollab.Density.DetectorNormalization

File: `lean/MathCollab/Density/DetectorNormalization.lean`; 99 source lines; SHA-256 `0e7f07e2aed7313e99b95d251ef3b29930f358bd05add4b597d1d275c2cb2971`.

- `poweredDetectorCoefficient_subpower` at line 16
- `densityAmbient_eventually_le_sq` at line 37
- `poweredDetectorCoefficient_eventually_le` at line 48
- `normalizedPoweredCoefficient` at line 77
- `normalizedPoweredCoefficient_eventually` at line 80
- `detectingPolynomial_normalizedPowered` at line 91

### MathCollab.Density.DetectorPoweredHeight

File: `lean/MathCollab/Density/DetectorPoweredHeight.lean`; 104 source lines; SHA-256 `444c65be7abb3d29e0e65642f24e2d051e6230364ceaa749390503108d5f4e3a`.

- `detectorHeightConstant` at line 15
- `exists_poweredDetector_height` at line 19
- `detectorHeightConstant_eventually` at line 60
- `exists_normalizedPowered_height` at line 76

### MathCollab.Density.PoweredDetectorFamily

File: `lean/MathCollab/Density/PoweredDetectorFamily.lean`; 104 source lines; SHA-256 `88b8a52fce6c6d5fec4f5e4bd3fb8a740cea86aed3518f5189e4468c05178f96`.

- `poweredDetectorIndices` at line 17
- `poweredDetectorScale` at line 23
- `poweredDetectorFamilyCoeff` at line 26
- `poweredDetectorIndices_card_le` at line 29
- `poweredDetectorFamily_scales` at line 40
- `poweredDetectorFamily_cover_of_zeta_bound` at line 64
- `poweredDetectorFamily_coefficients` at line 91

### MathCollab.Density.DetectorAdmissibility

File: `lean/MathCollab/Density/DetectorAdmissibility.lean`; 84 source lines; SHA-256 `7e5ce4701a88efb683270857c8c6a6c7d2c6f5a577c4a9325ff4be3a26953ff1`.

- `densityAmbient_eventually_cubeRoot_le` at line 16
- `detectorHeight_ge_scale` at line 37
- `poweredDetectorFamily_admissible` at line 53

### MathCollab.Density.DensityExponentAccounting

File: `lean/MathCollab/Density/DensityExponentAccounting.lean`; 155 source lines; SHA-256 `1cb0bbe606f2cb60d40a60c6b5f4423d0a7bffd79620ffc1b1befb12c11e7867`.

- `normalizedHeight_quotient` at line 16
- `densityAmbient_small_rpow` at line 27
- `density_largeValue_term_le` at line 45
- `density_logarithms_eventually` at line 94
- `density_family_sum_eventually` at line 104

### MathCollab.Density.Stronger.ShortExponentAccounting

File: `lean/MathCollab/Density/Stronger/ShortExponentAccounting.lean`; 173 source lines; SHA-256 `688f7fe4cbac4010d1170880c40344ba3e49d5242d2c1b05423c7599eba79614`.

- `sqrt_le_stronger_lower_scale` at line 18
- `smoothPoweredFamily_largeValues_admissible` at line 28
- `smooth_largeValue_term_le` at line 59
- `smooth_family_sum_eventually` at line 117

### MathCollab.Density.IndexedZeroLargeValues

File: `lean/MathCollab/Density/IndexedZeroLargeValues.lean`; 75 source lines; SHA-256 `bca4e38bd87872077b52e53df62a44715b54826efb37e343eaea0ac39e006bd1`.

- `zetaSlab_large_values_cover_indexed` at line 22

### MathCollab.Density.ZetaJensenInputs

File: `lean/MathCollab/Density/ZetaJensenInputs.lean`; 199 source lines; SHA-256 `dfdc07c0349868ac0ab1548baba5fdbaf6f26fb682b2f2fb915f0603fa35972e`.

- `finset_analyticOrderNatAt_le_finsum_divisor` at line 26
- `zeta_jensen_sphere_bound` at line 74
- `moebius_coeff_norm_le_one` at line 128
- `moebius_LSeries_norm_lt_five_thirds` at line 135
- `euler_product_lower_bound_2` at line 176

### MathCollab.Density.LocalZeroCount

File: `lean/MathCollab/Density/LocalZeroCount.lean`; 256 source lines; SHA-256 `3d040eb65da8b5f3458ae0b317080739ef91f4b9ea9af7dd00f3c6d7753ad473`.

- `zeta_unit_bin_sum_le_jensen` at line 24
- `zeta_local_multiplicity_bound` at line 164
- `zeta_separated_representatives` at line 239

### MathCollab.Density.Stronger.ShortZeroCount

File: `lean/MathCollab/Density/Stronger/ShortZeroCount.lean`; 166 source lines; SHA-256 `90118d955bb8ce68f7d3ed6c7b84eb4d519e4bf62abd6e1dbe9c2fed0bc75042`.

- `zetaSubset_large_values_cover_indexed` at line 22
- `smoothShortZeroFinset` at line 86
- `smoothShortZeroCount` at line 95
- `smoothShortZeroFinset_subset` at line 98
- `smoothShortZeroCount_bound` at line 105
- `smooth_remaining_zeros_have_long_detector` at line 148

### MathCollab.Density.Stronger.LongMeanScale

File: `lean/MathCollab/Density/Stronger/LongMeanScale.lean`; 54 source lines; SHA-256 `9eba859af13257ce1ec33bf2f00c4484290dfd7054f2c21212b3caaecef97912`.

- `weightedCriticalMean_detecting_scale` at line 16
- `weightedCriticalMean_long_scale` at line 39

### MathCollab.Density.Stronger.PhysicalTwelfthTail

File: `lean/MathCollab/Density/Stronger/PhysicalTwelfthTail.lean`; 88 source lines; SHA-256 `20ea8eee94de512d666cdcc1db98ead00861b36f9dd475e631f63e65f0c7d896`.

- `physical_tail_geometry` at line 17
- `weightedCriticalTwelfth_tail_pointwise` at line 35
- `integrable_translated_critical_twelfth` at line 61
- `weightedCriticalTwelfth_physical_tail` at line 67

### MathCollab.Density.Stronger.SeparatedCriticalSampling

File: `lean/MathCollab/Density/Stronger/SeparatedCriticalSampling.lean`; 85 source lines; SHA-256 `ac604c02b1dcb63f9c8b22ccb4b1c187e819eae5b4e61639f8bc71ad8004c56e`.

- `weightedCriticalTwelfth_le_physical_interval` at line 15
- `separated_weightedCriticalMean_twelfth_le_with_card` at line 27
- `separated_card_in_height_slab` at line 51
- `separated_weightedCriticalMean_twelfth_le` at line 66

### MathCollab.Density.Stronger.SmallResidue

File: `lean/MathCollab/Density/Stronger/SmallResidue.lean`; 54 source lines; SHA-256 `077bf0b39cfe618d95b090484fb2f3a0524e9b28a2d65687aa38b201f5cf492b`.

- `smoothDetectorResidue_eventually_small` at line 17

### MathCollab.Density.Stronger.LongBlockDetection

File: `lean/MathCollab/Density/Stronger/LongBlockDetection.lean`; 104 source lines; SHA-256 `54eb6fe597c0619c14aeea0f1e6d3a6eb519c44f7f5878832e90aa4a9ecd27b5`.

- `negligible_residue_le_detector_height` at line 16
- `smoothMollifierBlock_eventually_detects_mean` at line 31
- `smoothDetector_eventually_detects_mean` at line 58

### MathCollab.Density.Stronger.LongMeanCounting

File: `lean/MathCollab/Density/Stronger/LongMeanCounting.lean`; 117 source lines; SHA-256 `fcea45865abad928828c985a327d0f43f82c1b5db1eadadd86ae8df4fa48c919`.

- `long_mean_twelfth_count` at line 19
- `smooth_long_mean_or_short_powered_cover` at line 44
- `long_mean_count_le_physical_moment` at line 105

### MathCollab.Density.Stronger.LongMultiplicityReduction

File: `lean/MathCollab/Density/Stronger/LongMultiplicityReduction.lean`; 135 source lines; SHA-256 `801924188a949b0169cda1f890421a9a800b20eb6e311e22010af6d62385ad4d`.

- `smoothLongZeroFinset` at line 18
- `smoothLongZeroCount` at line 22
- `smoothLongZeroFinset_subset` at line 25
- `smooth_zeroCount_partition` at line 29
- `smoothLongZeroFinset_eventually_detects_mean` at line 37
- `smoothLongZeroCount_physical_moment_reduction` at line 56

### MathCollab.Density.Stronger.LongScalarBudget

File: `lean/MathCollab/Density/Stronger/LongScalarBudget.lean`; 94 source lines; SHA-256 `32c5cf2a56230d6d06bdc8bd29ea04dab117da0b50e425f67582368d164c192a`.

- `log_pow_eventually_le_rpow` at line 16
- `log_twelfth_eventually_le_rpow` at line 24
- `long_count_scale_identity` at line 29
- `long_count_scalar_log_eventually` at line 40
- `long_count_scalar_eventually` at line 62
- `long_count_scalar_local_log_eventually` at line 72

### MathCollab.Density.Stronger.FinalParameters

File: `lean/MathCollab/Density/Stronger/FinalParameters.lean`; 27 source lines; SHA-256 `bcc5078a2fa65b1e2ad3321306150ee6aeaa2de35a92620be9507b9e35e12291`.

- `exists_stronger_loss_parameters` at line 15

### MathCollab.Density.ZetaConjugation

File: `lean/MathCollab/Density/ZetaConjugation.lean`; 92 source lines; SHA-256 `fea66c7a6aa9ac576633618089f0fd6c22c5b1cac2f8946890f74cf17a8f7cff`.

- `analyticAt_conj_conj_local` at line 18
- `isNontrivialZetaZero_conj` at line 26
- `zetaMultiplicity_conj` at line 32
- `zetaSlabCount_conj` at line 46
- `zetaSlabCount_split_le` at line 66
- `zetaDensityCount_le_twice_positive` at line 83

### MathCollab.Density.DensityDyadicSummation

File: `lean/MathCollab/Density/DensityDyadicSummation.lean`; 108 source lines; SHA-256 `de4db5d6e25fdd0b6f50fe01c3dbf070d42839c6224d87216f0511e709b28e92`.

- `zetaSlab_extend_power_bound` at line 18
- `zetaPositive_bound_of_slabs` at line 39
- `zetaDensity_bound_of_eventual_slabs` at line 94

### MathCollab.Density.Stronger.ConditionalDensity

File: `lean/MathCollab/Density/Stronger/ConditionalDensity.lean`; 103 source lines; SHA-256 `8566580282010f55aee74fa856bdd44eb97953e76ab9284b374ab9d9ef7594a4`.

- `smoothLongZeroCount_bound_of_twelfth_moment` at line 20
- `stronger_slab_bound_of_twelfth_moment` at line 56
- `stronger_density_bound_of_twelfth_moment` at line 81

### MathCollab.Density.Stronger.MomentFromPeaks

File: `lean/MathCollab/Density/Stronger/MomentFromPeaks.lean`; 69 source lines; SHA-256 `07a5974bdf9b3166d633a86b618b8cf2a245849f183b0ddd9c0dda21fa6bea11`.

- `actual_fourth_moment_eventually` at line 19
- `pointValue_volume_le_of_peak_card` at line 29
- `zeta_twelfth_physical_of_peak_card` at line 43
- `stronger_density_bound_of_peak_card` at line 58

### MathCollab.Density.Stronger.NativePeaks

File: `lean/MathCollab/Density/Stronger/NativePeaks.lean`; 43 source lines; SHA-256 `7fd1f4e24ba01e3af65e23faaef7520c5aaf4194e15109e1374cdf190488dc14`.

- `pointValue_peak_card_native` at line 25
- `pointValue_volume_native` at line 34

### MathCollab.Density.Stronger.NativeMoment

File: `lean/MathCollab/Density/Stronger/NativeMoment.lean`; 36 source lines; SHA-256 `8a96412e979f70df54f0a473e92b32bd915809d6437f06db4e261552cbaafbc4`.

- `zeta_twelfth_dyadic_native` at line 21
- `zeta_twelfth_physical_native` at line 29

### MathCollab.Density.DensitySlabBound

File: `lean/MathCollab/Density/DensitySlabBound.lean`; 58 source lines; SHA-256 `217bccdfe8e7bcfaaa18b72708f0a5b5f4316fdb9fe58939bf51e7a0fdeff8aa`.

- `zetaSlab_density_bound_of_weyl` at line 19

### MathCollab.Density.DensityConclusion

File: `lean/MathCollab/Density/DensityConclusion.lean`; 62 source lines; SHA-256 `3b0eb0bf761eb5f6c7b7843feffca2b838ef85e65f58bbd3bcb18240355ea433`.

- `densityCountingEta` at line 17
- `densityCountingEta_margins` at line 19
- `zetaDensityCount_eq_zero_of_one_le` at line 28
- `zeta_density_bound_of_weyl` at line 40

### MathCollab.Density.Stronger.NativeDensity

File: `lean/MathCollab/Density/Stronger/NativeDensity.lean`; 35 source lines; SHA-256 `a5c3f3e777161c37b5654f595de6047cf3b647389e67e4bb78e968bb83b6e54b`.

- `stronger_density_bound_native` at line 24

### Solution

File: `lean/Solution.lean`; 76 source lines; SHA-256 `2316b521f6b5e1775c7498f797e04a92dcc53960416e98c6602b4e1debd8d11f`.

- `exact_membership` at line 13
- `exact_multiplicity` at line 26
- `density_bound` at line 36
- `actual_moment_integrable` at line 55
- `twelfth_moment` at line 62
- `empty_region` at line 73

