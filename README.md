# India-Japan Economic Relations: FDI & Trade Analysis

A data analysis project examining Japanese Foreign Direct Investment (FDI) into India and India-Japan bilateral trade trends, using publicly available government and industry body data.

## Motivation

This project extends my earlier academic study on India-Japan business practices (Hofstede framework, Toyota Kirloskar / Maruti Suzuki / SoftBank-Paytm case studies) into a quantitative, data-driven analysis of the economic relationship between the two countries built as part of my preparation for an MBA in Japan (Hitotsubashi ICS / UTokyo).

That earlier project was mostly qualitative theory and comparison. I wanted to come back and look at the actual numbers behind the relationship. One thing that genuinely surprised me while pulling this together, I expected Japanese FDI into India to show a steady upward climb given how much both governments talk about the partnership, but it's actually quite volatile year to year. Large FDI commitments seem to move in lumps rather than a smooth trend  a more realistic picture than the usual headline narrative.

See `notebook/analysis_notebook.ipynb` for the full walkthrough with commentary, including a correlation check between FDI and trade growth.

## What this project does

- Loads and cleans real FDI and bilateral trade data (2007-2026) from government and industry sources
- Calculates FDI CAGR and total trade growth over the available period
- Visualizes:
  - Japanese FDI inflows into India by financial year
  - India-Japan trade balance (exports vs. imports)
  - Total bilateral trade volume trend

## Data Sources

All figures are drawn directly from primary/official or industry-standard sources — no estimated or invented numbers:

- Ministry of External Affairs, Government of India — India-Japan Bilateral Relations brief
- Indian Embassy, Tokyo — official India-Japan Commercial Relations page
- India Briefing (Dezan Shira & Associates) — Doing Business in India guide
- IBEF (India Brand Equity Foundation) — India-Japan Trade report
- Business Standard — reporting on Commerce Minister Piyush Goyal's statement (Feb 2025)

Full citations are included in the `source` column of each CSV file. Where a source only provided a partial-year figure or didn't disaggregate exports/imports, this is explicitly labeled in the data rather than estimated.

## Project Structure

```
india-japan-economic-relations/
├── data/
│   ├── japan_fdi_into_india.csv       # FDI inflows by financial year
│   └── india_japan_trade.csv          # Bilateral trade (exports/imports) by financial year
├── charts/
│   ├── fdi_inflows.png
│   ├── trade_balance.png
│   └── total_trade_trend.png
├── notebook/
│   └── analysis_notebook.ipynb        # Full walkthrough with commentary and correlation check
├── analysis.py                        # Standalone script version (regenerates charts)
└── README.md
```

## How to Run

```bash
pip install pandas matplotlib
python analysis.py
```

This will print summary statistics to the console and regenerate all charts in the `charts/` folder.

## Key Findings

- Japanese FDI into India has been volatile year to year (ranging from ~$1.49B to ~$3.2B across FY2020-21 to FY2025-26) rather than following a smooth growth curve, reflecting the project-based, lumpy nature of large FDI commitments.
- India runs a persistent and widening trade deficit with Japan — India's imports from Japan (largely electrical machinery, chemicals, and industrial equipment) consistently outweigh exports (largely marine products, organic chemicals, and vehicle components).
- Total bilateral trade grew from roughly $10 billion (FY2007-08) to over $25 billion (FY2024-25), even as Japan's overall share of India's total trade remains modest pointing to real but still underdeveloped economic ties relative to the strategic partnership between the two countries.

## Limitations

- Some years have partial-year or non-disaggregated figures depending on what was publicly reported at the time of writing (marked accordingly in the data files).
- This is a snapshot analysis using published figures, not primary data collection intended as a portfolio/academic exercise, not a research publication.

## Author

Abeer Upadhyay BBA (Finance), Indian Institute of Technology Patna
