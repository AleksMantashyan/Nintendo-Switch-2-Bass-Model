from pathlib import Path
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from helper_functions import bass_cumulative

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"

# Fit the Bass model to the original Nintendo Switch data.
hist = pd.read_csv(DATA / "dataset1.csv")
t = hist["elapsed_years"].to_numpy()
y = hist["cumulative_sales_m"].to_numpy()

params, _ = curve_fit(
    bass_cumulative,
    t,
    y,
    p0=[0.03, 0.40, 165],
    bounds=([1e-6, 1e-6, 120], [1, 3, 300]),
    maxfev=100000,
)
p, q, M = params

hist["bass_fitted_cumulative_m"] = bass_cumulative(t, p, q, M)
hist.to_csv(DATA / "dataset2.csv", index=False)

# Forecast Switch 2 starting from Nintendo's FY2026 cumulative sales.
N = 19.86
rows = [[
    2026,
    N,
    N,
    "Actual",
    "https://www.nintendo.co.jp/ir/pdf/2026/260508e.pdf",
]]
for fy in range(2027, 2036):
    new_adopters = (p + q * N / M) * (M - N)
    N += new_adopters
    rows.append([
        fy,
        new_adopters,
        N,
        "Forecast",
        "Bass model using p, q, and M estimated from dataset1.csv",
    ])

forecast = pd.DataFrame(
    rows,
    columns=[
        "fiscal_year_end",
        "new_adopters_m",
        "cumulative_adopters_m",
        "type",
        "source_or_basis",
    ],
)
forecast.to_csv(DATA / "dataset3.csv", index=False)

print(f"p = {p:.4f}")
print(f"q = {q:.4f}")
print(f"M = {M:.2f} million units")
print(forecast.to_string(index=False))
