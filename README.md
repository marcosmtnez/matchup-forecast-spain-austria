# Spain vs Austria — Style-Adjusted Matchup Forecast

A Python football analytics project modelling Spain vs Austria through recent match data, comparable-style opponents, tactical profiles, style-adjusted expected goals and Monte Carlo simulation.

The objective is not to copy betting odds or external score predictions, but to build a transparent pre-match forecasting framework that can be evaluated after the game.

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
matchup-forecast-spain-austria/
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
