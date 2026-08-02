def check_protanopia_inheritance(father, mother):
    """
    Calculates the percentage chance of offspring (infant) inheriting protanopia 
    or becoming carriers based on parental genetic status.
    
    Parameters:
    father (str): 'normal' or 'affected'
    mother (str): 'normal', 'carrier', or 'affected'
    """
    # Standardize inputs to lowercase to prevent abnormal infant 
    father = father.lower().strip()
    mother = mother.lower().strip()
    
    # Initialize default 0% probabilities
    son_affected = 0
    daughter_affected = 0
    daughter_carrier = 0
    
    # Scenario 1: Affected Father + Normal Mother
    #it is x linked recessive disorder, so if father is affected and mother is normal, sons will not be affected but daughters will be carriers.
    if father == "affected" and mother == "normal":
        son_affected = 0
        daughter_affected = 0
        daughter_carrier = 100
        
    # Scenario 2: Normal Father + Carrier Mother
    #x linked recessive disorder
    elif father == "normal" and mother == "carrier":
        son_affected = 50
        daughter_affected = 0
        daughter_carrier = 50
        
    # Scenario 3: Affected Father + Carrier Mother
    elif father == "affected" and mother == "carrier":
        son_affected = 50
        daughter_affected = 50
        daughter_carrier = 50
        
    # Scenario 4: Normal Father + Affected Mother
    
    elif father == "normal" and mother == "affected":
        son_affected = 100
        daughter_affected = 0
        daughter_carrier = 100
        
    # Scenario 5: Both Parents Affected
    elif father == "affected" and mother == "affected":
        son_affected = 100
        daughter_affected = 100
        daughter_carrier = 0
        
    # Scenario 6: Both Parents Normal
    elif father == "normal" and mother == "normal":
        pass 
        
    else:
        return "Invalid input. Please use 'normal', 'carrier', or 'affected'."

    # Return results formatted cleanly
    return {
        "Chance for Sons to have Protanopia": f"{son_affected}%",
        "Chance for Daughters to have Protanopia": f"{daughter_affected}%",
        "Chance for Daughters to be Carriers": f"{daughter_carrier}%"
    }

# --- EXAMPLE USAGE ---

# Test Scenario 3: Affected Father and Carrier Mother
father_input = "affected"
mother_input = "carrier"

results = check_protanopia_inheritance(father_input, mother_input)

print(f"Results for marriage between:")
print(f"Father: {father_input.capitalize()} | Mother: {mother_input.capitalize()}\n")
for outcome, percentage in results.items():
    print(f"- {outcome}: {percentage}")


    