# Nintendo Switch 2 - Bass Model Homework

This project uses the original Nintendo Switch as a historical look-alike to estimate a Bass diffusion model and forecast worldwide adoption of Nintendo Switch 2.

## Project structure

- `img/` - images used in the report.
  - `image1.png` - Bass model fit for the original Nintendo Switch.
  - `image2.png` - predicted annual adoption of Nintendo Switch 2.
- `data/` - datasets used in the analysis.
  - `dataset1.csv` - original Nintendo Switch historical worldwide hardware-sales data.
  - `dataset2.csv` - historical data with fitted Bass-model cumulative values.
  - `dataset3.csv` - Nintendo Switch 2 actual starting value and forecast by fiscal year.
- `report/` - final project report.
  - `report.pdf` - final report in PDF format.
  - `report_source.md` - Markdown source used to generate the report.
- `/` - analysis files in the project root.
  - `script1.py` - estimates the Bass parameters and creates the model output datasets.
  - `script2.py` - generates the two figures used in the report.
  - `helper_functions.py` - contains the cumulative Bass-model function.
  - `bass_model_analysis.ipynb` - Jupyter Notebook version of the analysis.
- `references.md` - references used in the project.
- `requirements.txt` - Python package requirements.

## Model results

The Bass model estimated from the original Switch gives approximately:

- `p = 0.0701`
- `q = 0.4351`
- `M = 170.81 million units`

The Nintendo Switch 2 forecast starts from Nintendo's reported cumulative fiscal-2026 sales of 19.86 million units.

## Running the project

Install the packages in `requirements.txt`, then run:

```bash
python script1.py
python script2.py
```

The first script reproduces the fitted datasets and forecast, and the second reproduces the figures in `img/`.
