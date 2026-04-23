"""
Socrato Daily Sprint: Gaucho Hospital Board Benchmarking
Phase 0 → Phase 2 → Phase 7
Synthetic data based on global governance standards (WHO, King IV, OECD).
Data is clearly labelled as synthetic.
Non‑interactive version – saves chart, prints all results.
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')          # <-- No display, only file saving
import matplotlib.pyplot as plt
from math import pi

# ============================================================
# 1. SYNTHETIC DATASET GENERATION
# ============================================================
np.random.seed(42)
n = 200

data = {
    'Education_Relevant': np.clip(np.random.normal(9, 1.5, n), 0, 10),
    'Board_Experience_Years': np.random.normal(8, 3, n).clip(0, 15),
    'Healthcare_Sector_Knowledge': np.random.normal(8, 2, n).clip(0, 10),
    'Governance_Training': np.random.normal(7, 2, n).clip(0, 10),
    'Financial_Oversight': np.random.normal(7, 2.5, n).clip(0, 10),
    'Ethical_Compliance': np.random.normal(9, 1, n).clip(0, 10),
}

df_global = pd.DataFrame(data)
df_global['Source'] = 'Global Benchmark (synthetic)'

gaucho = {
    'Education_Relevant': 1.0,
    'Board_Experience_Years': 0.5,
    'Healthcare_Sector_Knowledge': 1.0,
    'Governance_Training': 0.5,
    'Financial_Oversight': 2.0,
    'Ethical_Compliance': 5.0,
}
df_gaucho = pd.DataFrame([gaucho], index=['Gaucho'])

# ============================================================
# 2. QUICK DATA CHECK (Phase 2 – Section 2.2.1, 2.2.3)
# ============================================================
print("=== Data Shape ===")
print(f"Global benchmark samples: {df_global.shape[0]}")
print(f"Gaucho profile: 1 row")
print("\n=== Missing Values ===")
print(df_global.isnull().sum())
print("\n=== Global Benchmark Summary Statistics ===")
print(df_global.describe().round(1))

# ============================================================
# 3. VISUALIZATION – Radar Chart (manual Section 7.3)
# ============================================================
categories = list(df_global.columns[:-1])
N = len(categories)

global_means = df_global[categories].mean().values
global_10th = df_global[categories].quantile(0.1).values
global_90th = df_global[categories].quantile(0.9).values
gaucho_vals = df_gaucho[categories].values.flatten()

angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
plt.xticks(angles[:-1], categories, size=9)

ax.fill(angles, np.append(global_90th, global_90th[0]), alpha=0.1, color='blue',
        label='Typical range (10th-90th pct)')
ax.plot(angles, np.append(global_means, global_means[0]), color='blue', linewidth=2,
        label='Global Average')
ax.plot(angles, np.append(global_10th, global_10th[0]), color='blue', linestyle='--', linewidth=1)
ax.plot(angles, np.append(global_90th, global_90th[0]), color='blue', linestyle='--', linewidth=1)

ax.plot(angles, np.append(gaucho_vals, gaucho_vals[0]), color='red', linewidth=2,
        label='Gaucho Profile')
ax.fill(angles, np.append(gaucho_vals, gaucho_vals[0]), alpha=0.25, color='red')

ax.set_title("Hospital Board Member Governance Profile:\nGaucho vs Global Benchmarks",
             y=1.08, fontsize=14, weight='bold')
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.15))

txt = ("Data Source: Synthetic data modelled on WHO (2022) health governance guidelines, "
       "King IV Report on Corporate Governance (2016), OECD Good Governance Principles (2019). "
       "Gaucho profile based on public commentary.")
fig.text(0.5, -0.05, txt, ha='center', fontsize=7, color='gray')

plt.tight_layout()
plt.savefig('gaucho_benchmark_radar.png', dpi=200, bbox_inches='tight')

# ============================================================
# 4. OUTLIER QUANTIFICATION
# ============================================================
print("\n=== Gaucho’s Percentile Rank vs Global Benchmarks ===")
for cat in categories:
    rank = (df_global[cat] < gaucho[cat]).mean() * 100
    print(f"{cat}: Gaucho is at the {rank:.0f}th percentile (lower means less qualified)")