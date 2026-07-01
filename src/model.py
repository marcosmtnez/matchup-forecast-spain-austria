import numpy as np
import pandas as pd


def impute_xg(row, prefix="team"):
    xg = row.get(f"{prefix}_xg")
    if pd.notna(xg):
        return float(xg)
    goals = float(row.get(f"{prefix}_goals", 0))
    shots = float(row.get(f"{prefix}_shots", 0))
    sot = float(row.get(f"{prefix}_sot", 0))
    return max(0.10, 0.06 * shots + 0.14 * sot + 0.10 * goals)


def weighted_mean(values, weights):
    values = np.asarray(values, dtype=float)
    weights = np.asarray(weights, dtype=float)
    mask = ~np.isnan(values)
    values = values[mask]
    weights = weights[mask]
    if len(values) == 0:
        return np.nan
    return float(np.average(values, weights=weights))


def poisson_simulation(home_lambda, away_lambda, n=50000, seed=42):
    rng = np.random.default_rng(seed)
    home_goals = rng.poisson(home_lambda, n)
    away_goals = rng.poisson(away_lambda, n)
    return pd.DataFrame({"spain_goals": home_goals, "austria_goals": away_goals})
