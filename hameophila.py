def check_hemophilia_inheritance(father, mother):
    """
    Calculates the inheritance probabilities for Hemophilia (X-linked recessive).
    
    father: 'normal' or 'affected'
    mother: 'normal', 'carrier', or 'affected'
    """
    father = father.lower().strip()
    mother = mother.lower().strip()
    
    if father not in ['normal', 'affected'] or mother not in ['normal', 'carrier', 'affected']:
        return "Invalid input."

    # X-linked inheritance logic
    if father == "affected" and mother == "normal":
        son_affected = 0
        daughter_affected = 0
        daughter_carrier = 100
        
    elif father == "normal" and mother == "carrier":
        son_affected = 50
        daughter_affected = 0
        daughter_carrier = 50
        
    elif father == "affected" and mother == "carrier":
        son_affected = 50
        daughter_affected = 50
        daughter_carrier = 50
        
    elif father == "normal" and mother == "affected":
        son_affected = 100
        daughter_affected = 0
        daughter_carrier = 100
        
    elif father == "affected" and mother == "affected":
        son_affected = 100
        daughter_affected = 100
        daughter_carrier = 0
        
    elif father == "normal" and mother == "normal":
        son_affected = 0
        daughter_affected = 0
        daughter_carrier = 0

    return {
        "Chance for Sons to have Hemophilia": f"{son_affected}%",
        "Chance for Daughters to have Hemophilia": f"{daughter_affected}%",
        "Chance for Daughters to be Carriers": f"{daughter_carrier}%"
    }

print("=== Hemophilia Inheritance Predictor ===")
cases = [
    ("affected", "normal"),
    ("normal", "carrier"),
    ("affected", "carrier"),
    ("normal", "affected"),
    ("affected", "affected"),
    ("normal", "normal")
]

for f, m in cases:
    print(f"\nParents: Father ({f}) x Mother ({m})")
    results = check_hemophilia_inheritance(f, m)
    for k, v in results.items():
        print(f"  - {k}: {v}")