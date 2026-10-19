from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from helper_functions import bass_cumulative

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
IMG = ROOT / "img"

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

# Figure 1: historical fit
grid = np.linspace(0, 8.5, 300)
plt.figure(figsize=(7.5, 4.6))
plt.scatter(t, y, label="Nintendo reported sales")
plt.plot(grid, bass_cumulative(grid, p, q, M), label="Bass model")
plt.xlabel("Years since original Switch launch")
plt.ylabel("Cumulative hardware sales (million)")
plt.title("Original Nintendo Switch: Bass model fit")
plt.legend()
plt.grid(alpha=0.2)
plt.tight_layout()
plt.savefig(IMG / "image1.png", dpi=200)
plt.close()

# Figure 2: Switch 2 annual forecast
forecast = pd.read_csv(DATA / "dataset3.csv")
future = forecast[forecast["type"] == "Forecast"]
plt.figure(figsize=(7.5, 4.6))
plt.bar(future["fiscal_year_end"].astype(str), future["new_adopters_m"])
plt.xlabel("Fiscal year ending March 31")
plt.ylabel("Predicted new units (million)")
plt.title("Nintendo Switch 2: predicted adoption by year")
plt.xticks(rotation=45)
plt.grid(axis="y", alpha=0.2)
plt.tight_layout()
plt.savefig(IMG / "image2.png", dpi=200)
plt.close()
