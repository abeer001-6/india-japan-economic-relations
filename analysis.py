"""
India-Japan Economic Relations: FDI & Trade Analysis
------------------------------------------------------
Analyzes Japanese FDI inflows into India and India-Japan bilateral trade
trends using publicly available government and industry-body data
(MEA, Indian Embassy Tokyo, DPIIT, IBEF, India Briefing).

Author: Abeer Upadhyay
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import os

DATA_DIR = "data"
CHART_DIR = "charts"
os.makedirs(CHART_DIR, exist_ok=True)

# ---------------------------------------------------------
# 1. Load data
# ---------------------------------------------------------
fdi = pd.read_csv(os.path.join(DATA_DIR, "japan_fdi_into_india.csv"))
trade = pd.read_csv(os.path.join(DATA_DIR, "india_japan_trade.csv"))

print("=" * 60)
print("JAPAN FDI INTO INDIA (USD Billion)")
print("=" * 60)
print(fdi[["financial_year", "fdi_usd_billion", "period_type"]].to_string(index=False))

print("\n" + "=" * 60)
print("INDIA-JAPAN BILATERAL TRADE (USD Billion)")
print("=" * 60)
print(trade[["financial_year", "india_exports_to_japan_usd_bn",
             "india_imports_from_japan_usd_bn", "total_trade_usd_bn",
             "trade_balance_usd_bn"]].to_string(index=False))

# ---------------------------------------------------------
# 2. Key metrics
# ---------------------------------------------------------
full_year_fdi = fdi[fdi["period_type"] == "full_year"]
cagr_years = full_year_fdi["financial_year"].iloc[[0, -1]].tolist()
start_val = full_year_fdi["fdi_usd_billion"].iloc[0]
end_val = full_year_fdi["fdi_usd_billion"].iloc[-1]
n_periods = len(full_year_fdi) - 1
cagr = ((end_val / start_val) ** (1 / n_periods) - 1) * 100

print(f"\nFDI CAGR from FY{cagr_years[0]} to FY{cagr_years[1]}: {cagr:.1f}%")
print(f"(Note: FDI is volatile year-to-year; CAGR here is illustrative, not a smooth trend.)")

full_year_trade = trade[trade["period_type"] == "full_year"].dropna(subset=["total_trade_usd_bn"])
trade_growth = (
    (full_year_trade["total_trade_usd_bn"].iloc[-1] / full_year_trade["total_trade_usd_bn"].iloc[0]) - 1
) * 100
print(f"Total bilateral trade growth from FY{full_year_trade['financial_year'].iloc[0]} "
      f"to FY{full_year_trade['financial_year'].iloc[-1]}: {trade_growth:.1f}%")

# ---------------------------------------------------------
# 3. Chart 1: FDI inflows over time
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 5))
colors = ["#4C72B0" if p == "full_year" else "#AAB8C2" for p in fdi["period_type"]]
bars = ax.bar(fdi["financial_year"], fdi["fdi_usd_billion"], color=colors)
ax.set_title("Japanese FDI Inflows into India (FY2020-21 to FY2025-26)", fontsize=13, weight="bold")
ax.set_ylabel("FDI (USD Billion)")
ax.set_xlabel("Financial Year")
for bar, val in zip(bars, fdi["fdi_usd_billion"]):
    ax.text(bar.get_x() + bar.get_width() / 2, val + 0.05, f"${val}B",
            ha="center", fontsize=9)
ax.text(0.99, 0.02, "Grey bar = partial-year (Apr-Dec) figure",
        transform=ax.transAxes, ha="right", fontsize=8, style="italic", color="gray")
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "fdi_inflows.png"), dpi=150)
plt.close()

# ---------------------------------------------------------
# 4. Chart 2: Trade balance over time
# ---------------------------------------------------------
trade_plot = trade.dropna(subset=["india_exports_to_japan_usd_bn", "india_imports_from_japan_usd_bn"])
fig, ax = plt.subplots(figsize=(9, 5))
x = trade_plot["financial_year"]
ax.bar(x, trade_plot["india_exports_to_japan_usd_bn"], label="India's Exports to Japan", color="#55A868")
ax.bar(x, -trade_plot["india_imports_from_japan_usd_bn"], label="India's Imports from Japan", color="#C44E52")
ax.axhline(0, color="black", linewidth=0.8)
ax.set_title("India-Japan Trade Balance (Exports vs Imports)", fontsize=13, weight="bold")
ax.set_ylabel("USD Billion")
ax.set_xlabel("Financial Year")
ax.legend()
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "trade_balance.png"), dpi=150)
plt.close()

# ---------------------------------------------------------
# 5. Chart 3: Total trade volume trend
# ---------------------------------------------------------
total_trade_plot = trade.dropna(subset=["total_trade_usd_bn"])
fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(total_trade_plot["financial_year"], total_trade_plot["total_trade_usd_bn"],
        marker="o", color="#4C72B0", linewidth=2)
ax.set_title("India-Japan Total Bilateral Trade Volume", fontsize=13, weight="bold")
ax.set_ylabel("Total Trade (USD Billion)")
ax.set_xlabel("Financial Year")
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "total_trade_trend.png"), dpi=150)
plt.close()

print(f"\nCharts saved to '{CHART_DIR}/' folder:")
print("  - fdi_inflows.png")
print("  - trade_balance.png")
print("  - total_trade_trend.png")
