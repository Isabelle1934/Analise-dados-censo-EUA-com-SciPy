# 📊 Census Data Statistical Analysis

📌 Overview

A statistical analysis system that processes U.S. census data to compare demographic variables using hypothesis testing. The goal is to identify statistically significant differences between population groups.

---

🧠 Tech Stack

- Python 3
- Pandas (data manipulation and aggregation)
- NumPy (numerical operations)
- SciPy (statistical testing – t-test)

---

⚙️ How It Works

The system follows a simple pipeline:

1. Data Ingestion
   Reads two datasets: within-state migration and between-state migration.

2. Aggregation
   Groups data by geographic levels (state, region, division, county) and aggregates demographic metrics.

3. Filtering
   Selects specific subsets for comparative analysis (e.g., specific states or regions).

4. Statistical Analysis
   Applies independent t-test (ttest_ind) to compare means between two groups.

5. Output
   Generates statistical metrics:

- t-statistic (difference between groups)
- p-value (statistical significance)

---

📊 Analyses Performed

- Within-state vs between-state migration
- Naturalized citizens vs non-citizens
- Native vs naturalized citizens
- Education levels by region
- Marital status by division

---

⚠️ Considerations

- Assumes independence between samples
- Assumes approximately normal distribution
- No missing data handling
- No additional statistical validation tests

---

🎯 Purpose

To provide a direct and efficient statistical analysis for hypothesis validation on census demographic data.