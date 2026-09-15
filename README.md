# Mandi-to-Market Supply Chain Optimizer

A data engineering + analytics project for a State Agriculture Board to monitor
daily crop arrivals across Mandis, track prices against MSP, and understand
how weather relates to supply and price.

> **Note:** All data in `data/raw/` is **synthetically generated**
> (`scripts/generate_raw_data.py`) to simulate realistic messiness. It is not
> sourced from any government or real Mandi system.

## Tech Stack
- **Python** (pandas, numpy) — ETL and standardization
- **SQLite** — analytical database
- **statsmodels / scikit-learn** — forecasting, anomaly detection, clustering
- **Streamlit + Plotly** — interactive dashboard
- **pytest** — unit tests
- **Jupyter** — profiling / cleaning / analysis notebooks

## Project Structure
- `data/` — raw, processed and external data
- `notebooks/` — profiling, cleaning, analysis (runnable end-to-end)
- `src/` — reusable ETL modules + advanced analytics
- `sql/` — schema, views, reference analytical queries
- `dashboard/` — Streamlit app (5 pages)
- `docs/` — data dictionary, methodology, architecture
- `tests/` — unit tests

## Getting Started
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# run the full ETL pipeline
python -m src.pipeline

# launch the dashboard
streamlit run dashboard/app.py

# run tests
pytest tests/
```

## Data Cleaning Proof
Running the pipeline prints a raw-vs-cleaned row count summary and writes a
full `data/processed/data_quality_report.json`. See `docs/methodology.md` for
every cleaning decision and `docs/data_dictionary.md` for column-level detail.

## Limitations & Future Improvements
Weather sensors aren't Mandi-located in this synthetic dataset (aggregated by
date only); an AI agent for natural-language querying was intentionally
excluded from this build. Future work: real government data sources, sensor-
to-Mandi mapping, and richer seasonal forecasting models.
