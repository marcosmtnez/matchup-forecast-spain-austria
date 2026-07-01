# Data notes

This project separates three types of inputs:

1. `observed`: match statistics reported by public match centres or articles.
2. `derived`: metrics calculated from observed values inside the notebook.
3. `scouting_proxy`: tactical labels or style scores created for the model when no public event-data feed is available.

The prediction does not use external score predictions, betting odds or third-party forecast probabilities. It uses observed match logs, comparable-style factors and a transparent style-adjusted model.

If more reliable event data becomes available, replace the CSV values and rerun the notebook.
