# KLINEFELTER SYNDROME (47,XXY) NIPT SCREENING MODEL
"""


| Parameter                     | Normal / Low Risk |            Medium Risk |        High Risk |
| ----------------------------- | ----------------: | ---------------------: | ---------------: |
| Maternal Age             |        < 30 years |            30<=34 years |       ≥ 35 years |
| Gestational Age           |       10<=14 weeks |            10<=14 weeks |      10<=14 weeks |
| Fetal Fraction            |              ≥ 8% |                 4<=7.9% |             ≥ 8% |
| X Chromosome Ratio        |         0.90<=1.05 |              1.06<=1.20 |           > 1.20 |
| Y Chromosome Signal Ratio |         0.30<=0.60 | 0.20<=0.29 or 0.61<=0.80 | Abnormal pattern |
| XXY Probability       |             < 10% |                 10<=69% |            ≥ 70% |
| Overall Result            |          Low Risk |            Medium Risk |        High Risk |
"""



def predict_klinefelter(
    maternal_age,
    gestational_age,
    fetal_fraction,
    x_ratio,
    y_ratio,
    xxy_probability
):
    # Determine the highest risk factor based on the inputs
    # Typically, any parameter in a higher risk category raises the overall risk.
    if maternal_age >= 35 or x_ratio > 1.20 or (y_ratio < 0.20 or y_ratio > 0.80) or xxy_probability >= 70:
        return {
            "risk_level": "High Risk",
            "recommendation": "Must consult a genetic expert for early treatment"
        }
    elif (30 <= maternal_age <= 34) or (1.06 <= x_ratio <= 1.20) or (0.20 <= y_ratio <= 0.29) or (0.61 <= y_ratio <= 0.80) or (10 <= xxy_probability <= 69):
        return {
            "risk_level": "Medium Risk",
            "recommendation": "Consult a genetic expert"
        }
    elif maternal_age < 30 and 0.90 <= x_ratio <= 1.05 and 0.30 <= y_ratio <= 0.60 and xxy_probability < 10:
        return {
            "risk_level": "Low Risk / Normal",
            "recommendation": "No immediate action required based on these parameters"
        }
    else:
        return {
            "risk_level": "Inconclusive",
            "recommendation": "Consult Genetic Counselor"
        }




