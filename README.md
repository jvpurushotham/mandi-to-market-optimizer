# Mandi-to-Market Supply Chain Optimizer

A tool that cleans up messy farm market data and turns it into a simple dashboard — so a State Agriculture Board can see, at a glance, how crops are moving through Mandis, whether farmers are getting a fair price, and where problems might be building up.

---

## What problem does this solve?

Agriculture data almost never comes in clean. In real life, the same information ends up spread across different files, written in different languages, using different units, and full of typos, missing values and duplicate entries. Before anyone can actually study the data, someone has to fix all of that first.

This project takes five such messy files — crop arrivals, prices, MSP (Minimum Support Price), weather readings, and transport logs — and turns them into one clean, connected dataset. On top of that, it gives you:

- A dashboard to see arrivals, prices, and risk at a glance
- A way to check if farmers are being paid below MSP
- Simple forecasts, so you know what's likely to happen next
- A way to spot unusual days (a sudden price crash, a strange spike in arrivals, etc.)
- An AI assistant you can just type a question to, in plain English, and get an answer

## What does it actually look like?

**The dashboard** — five pages you can click through and filter by state, district, Mandi, crop, or date:
1. **Executive Overview** — the big picture: total arrivals, market value, average prices, risk score
2. **Mandi Intelligence** — drill down into any single Mandi
3. **MSP Monitor** — where and how often farmers are being paid below MSP
4. **Weather Impact** — how rainfall, temperature and humidity affect arrivals and prices
5. **Supply Chain Risk** — a risk score for every Mandi, plus forecasts and anomaly alerts

**The AI Assistant** — a simple chat box where you can type things like:
- *"Which wheat Mandis have the highest arrivals?"*
- *"Show me the Mandis where wheat price is below MSP."*
- *"What is the average temperature and rainfall?"*

and get a direct answer, calculated from the real, cleaned data — no need to know SQL or click through filters.

🔗 **Try the live demo:** http://ae65172f6181b40eaa68183327ce2efe-1222467219.eu-north-1.elb.amazonaws.com

## How the data gets cleaned

Real Mandi data is messy in predictable ways, and this project handles each one on purpose:

| Problem | Example | How it's fixed |
|---|---|---|
| Crop names mixed in English/Hindi, different spellings | "Wheat", "wheat", "Gehun" | All mapped to one standard name, e.g. "Wheat" |
| Different units for the same thing | KG, Quintal, Tonnes | Everything converted to Quintal |
| Dates written in different formats | 01/09/2026, 2026-09-01, 1-Sep-2026 | All converted to one standard date format |
| Weather times in different time zones | UTC vs IST | All converted to Indian Standard Time |
| Missing values | blank prices, missing quantities | Kept and clearly marked as missing, never guessed or faked |
| Duplicate rows | the same record entered twice | Removed, but only genuine duplicates — not similar-looking real records |

Every one of these steps is logged, so you can see exactly how many rows came in, how many were fixed, and how many were removed — nothing is silently thrown away.

## How it's built (in simple terms)

The project works like an assembly line — data goes in messy at one end, and comes out clean and ready to use at the other:

```
Raw files (CSV, JSON, Excel)
      ↓
Read the data in
      ↓
Check how messy it actually is
      ↓
Clean it up (fix duplicates, missing values)
      ↓
Standardize it (crop names, units, dates, time zones)
      ↓
Double-check everything makes sense
      ↓
Combine everything into one connected dataset
      ↓
Store it in a database
      ↓
Dashboard + AI Assistant read from that database
```

You only need to run one command to do all of this — see "How to run it" below.

## What's inside this repository

```
mandi-to-market-optimizer/
├── data/
│   ├── raw/            → the original, messy input files
│   ├── processed/      → the cleaned data and database, created automatically
│   └── external/       → any extra reference data
├── notebooks/          → step-by-step notebooks showing the cleaning process
├── src/                → the actual Python code that cleans and processes the data
├── sql/                → the database structure and saved queries
├── dashboard/          → the Streamlit dashboard app
├── docs/               → detailed write-ups (see below)
├── tests/               → automated checks that make sure the cleaning logic works
├── requirements.txt    → the list of Python packages needed
└── README.md           → this file
```

For more detail, see:
- `docs/data_dictionary.md` — what every column means
- `docs/methodology.md` — exactly how and why each cleaning decision was made
- `docs/architecture.md` — a full diagram of how everything connects

## How to run it yourself

You'll need Python installed. Then:

```bash
# 1. Set up a clean environment
python -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate

# 2. Install everything the project needs
pip install -r requirements.txt

# 3. Clean the data and build the database
python -m src.pipeline

# 4. Open the dashboard
streamlit run dashboard/app.py
```

That's it — the dashboard will open in your browser.

If you want to check that everything is working correctly, you can also run:
```bash
pytest tests/
```

## What tools were used

- **Python** — for reading, cleaning and processing the data
- **pandas / numpy** — for working with the data itself
- **SQLite** — a lightweight database to store the cleaned data
- **Streamlit + Plotly** — for building the interactive dashboard and charts
- **scikit-learn / statsmodels** — for the forecasting, anomaly detection and grouping features
- **pytest** — to automatically test that the cleaning logic behaves correctly

## Honest limitations

- All data here is synthetic — it was generated to be realistic, not pulled from any government source.
- Weather readings aren't tied to a specific Mandi's exact location in this version — they're grouped by date only.
- The AI Assistant currently answers with text, not charts — that's on the list for later.

## What we'd like to add next

- Plug in real government Mandi/MSP data instead of the synthetic version
- Link weather sensors to specific Mandis instead of just dates
- Let the AI Assistant show charts, not just text answers
- Try more advanced forecasting models for seasonal crops

---

Built as part of a data engineering and analytics submission (Track 3 — AgriTech).
