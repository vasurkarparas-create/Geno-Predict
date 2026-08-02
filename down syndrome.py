# Nuchal translucency (NT) is a fluid-filled space at the back of a developing baby's neck
# visible on an ultrasound. If the user knows this NT (Nuchal translucency) number, it is possible to predict risk. 
# An NT scan measures this fluid to help assess the baby's risk for certain genetic and structural conditions,
# such as Down syndrome, during the first trimester.

def predict_down_syndrome(mother_age, nt_value, father_has_ds=False):
    """
    Simplified prediction logic based on NT value and parental ages.
    Data to consider for prediction:
    - Normal: Age 22-30, NT 1.2-2.0 mm
    - Medium: Age 32-36, NT 2.3-2.8 mm
    - High: Age 38-42, NT 3.2-4.0 mm
    """
    risk_level = "Unknown"
    instructions = ""
    
    # We use OR conditions to escalate risk if any parameter falls into a higher risk category
    if mother_age >= 38 or nt_value >= 3.2:
        risk_level = "High"
        instructions = "Required instructions: genetic counseling, further testing, and monitoring during pregnancy."
    elif 32 <= mother_age < 38 or 2.3 <= nt_value < 3.2:
        risk_level = "Medium"
        instructions = "Required instructions: genetic counseling, further testing, and monitoring during pregnancy."
    else:
        risk_level = "Low"
        instructions = "No risk of Down syndrome based on maternal factors."

    paternal_risk = (
        "Risk of passing is 2% to 4% due to the father having Down syndrome." 
        if father_has_ds 
        else "No risk of passing from the father (except via random mutation)."
    )
    
    return {
        "maternal_risk": risk_level,
        "maternal_instructions": instructions,
        "paternal_risk": paternal_risk
    }
