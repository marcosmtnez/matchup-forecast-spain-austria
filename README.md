# Spain vs Austria — Style-Adjusted Prediction Model

A Python sports analytics project for Spain vs Austria, built as a transparent pre-match prediction model.

The model does **not** use betting odds, external score predictions or third-party forecast probabilities. It builds its own projection from:

- observed recent match logs;
- Spain against Austria-like opponents;
- Austria against Spain-like opponents;
- tactical style profiles;
- style-adjusted expected goals;
- Monte Carlo simulation;
- model-derived projected match statistics.

## Project structure

```text
spain-austria-style-adjusted-prediction-model/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── spain_match_log.csv
│   ├── austria_match_log.csv
│   ├── comparable_matches.csv
│   ├── team_style_profiles.csv
│   ├── model_weights.csv
│   ├── source_register.csv
│   └── README.md
├── notebooks/
│   └── spain_austria_prediction_model.ipynb
├── outputs/
├── reports/
│   └── methodology_note.md
└── src/
    ├── model.py
    └── visualizations.py
```

## How to run

```bash
pip install -r requirements.txt
jupyter notebook notebooks/spain_austria_prediction_model.ipynb
```

Then run:

```text
Kernel → Restart & Run All
```

The notebook will generate the charts and CSV outputs inside `outputs/`.

## Main outputs

```text
01_style_adjusted_xg_decomposition.png
02_monte_carlo_outcome_probabilities.png
03_scoreline_probability_matrix.png
04_projected_match_stats_forecast_card.png
05_tactical_style_radar.png
06_composite_tactical_indexes.png
07_matchup_advantage_heatmap.png
08_tactical_preview_map.png
model_derived_projected_stats.csv
post_match_validation_template.csv
```

## Methodological idea

The core model is not a simple average. It includes a comparable-style adjustment:

- Spain is evaluated against compact, disruptive and transition-oriented opponents.
- Austria is evaluated against possession-dominant and territorially dominant opponents.

The projected statistics are then derived from the model output, not manually inserted.

## Data quality

The project separates:

- `observed_public_report`: values taken from public match reports or match centres;
- `research_input`: pre-World-Cup comparable values added as structured research inputs;
- `scouting_proxy`: tactical style values used for the model adjustment layer.

This is intentional: the notebook shows what is observed, what is inferred and what is model-generated.

## Validation

After the match, fill in `outputs/post_match_validation_template.csv` with actual match statistics to evaluate whether the model captured the game structure correctly.
