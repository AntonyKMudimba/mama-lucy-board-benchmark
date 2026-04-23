# Mama Lucy Hospital Board Appointment Benchmarking

This project benchmarks the appointment of Gaucho to the Mama Lucy Hospital board against global governance standards. It follows the Socrato Data Science Methodology (Phases 0, 2, 7).

## What we did
- Built a synthetic dataset of 200 typical hospital board members using WHO, King IV, and OECD guidelines.
- Scored Gaucho on six criteria: education, board experience, healthcare knowledge, governance training, financial oversight, ethical compliance.
- Created a radar chart and percentile comparison.

## Key finding
Gaucho’s profile is at the 0th–2nd percentile on all measures — completely outside the normal range for hospital board members worldwide.

## Data source
Synthetic data modelled on WHO (2022), King IV (2016), OECD (2019). Gaucho’s profile from public commentary. No real personal data used.

## How to reproduce
- Requires Python with pandas, numpy, matplotlib.
- Run `python analysis.py`.
- Outputs: `gaucho_benchmark_radar.png` and console summary.

## Recommendations
1. Review the appointment against a written board competency checklist.
2. Set minimum governance standards for all future hospital board appointments.

**Author:** Antony Mudimba – Socrato Sprint Analyst