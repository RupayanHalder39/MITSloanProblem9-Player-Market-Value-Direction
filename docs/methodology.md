# Methodology

## Prediction unit and target

Each observation is a player valuation date. Predictors are restricted to information available before that date. The target is the residual change in the logarithm of the next observed published market value.

## Feature ladder

M1 uses current market value. The wider feature ladder adds six valuation-history features and 25 recent-football features across playing time, attacking, goalkeeping, defending, creation, and possession progression. M5 is the locked comparison of current value plus recent performance.

## Evaluation

The primary held-out evaluation contains 752 Championship valuation events from 606 players. Metrics are residual MAE, three-class rise/stable/fall accuracy, and Spearman rank correlation. External evaluation covers 27 competitions. The 2,000-draw bootstrap resamples players, not individual rows, to preserve within-player dependence.

## Interpretation boundary

The design is chronological, predictive, and observational. It evaluates incremental forecasting information; it does not identify causal effects of football performance on market value or predict realized transfer fees.
