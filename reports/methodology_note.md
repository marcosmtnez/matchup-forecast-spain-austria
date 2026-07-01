# Methodology note

The model is designed as a transparent pre-match sports analytics framework.

It combines:

- recent team match logs;
- style labels for each opponent;
- comparable-match factors;
- team style profiles;
- matchup-specific adjustments;
- a Monte Carlo simulation based on model-generated expected goals.

The model intentionally avoids external predictions. It does not import betting odds, media score predictions or third-party win probabilities.

The strongest methodological idea is the comparable-style layer:

- Spain is evaluated against opponents that resemble Austria: compact, pressing, transition-oriented or physically disruptive teams.
- Austria is evaluated against opponents that resemble Spain: high-possession, territorially dominant, technically strong teams.

The output is not meant to be a definitive truth. It is a structured forecast that can be validated after the match.
