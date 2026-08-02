# Marfan Syndrome Prediction


print(" MARFAN SYNDROME PREDICTION ")

father = input("Enter father's status (normal/affected): ").lower()
mother = input("Enter mother's status (normal/affected): ").lower()

print("\n RESULT ")

if father == "affected" and mother == "normal":

    print("Affected Child : 50%")
    print("Normal Child   : 50%")

    print("\nTreatment / Management")
    print("- Regular cardiology check-ups")
    print("- Beta-blockers or ARBs (as prescribed)")
    print("- Annual echocardiogram")
    print("- Regular eye examinations")
    print("- Avoid heavy weight lifting and contact sports")

elif father == "normal" and mother == "affected":

    print("Affected Child : 50%")
    print("Normal Child   : 50%")

    print("\nTreatment / Management")
    print("- Regular cardiology check-ups")
    print("- Beta-blockers or ARBs (as prescribed)")
    print("- Annual echocardiogram")
    print("- Regular eye examinations")
    print("- Avoid strenuous physical activity")

elif father == "affected" and mother == "affected":
    print("Affected Child : 75% (educational approximation)")
    print("Normal Child   : 25%")

    print("\nTreatment / Management")
    print("- Immediate genetic counseling")
    print("- Frequent cardiovascular monitoring")
    print("- Blood pressure control")
    print("- Surgical repair if aortic aneurysm develops")
    print("- Lifelong specialist follow-up")

elif father == "normal" and mother == "normal":
    
    print("Affected Child : Very Low (except new mutation)")
    print("Normal Child   : Very High")

    print("\nRecommendation")
    print("- Routine health check-ups")
    print("- No inherited risk expected from parents")

else:
    print("Invalid input!")
    print("Please enter only 'normal' or 'affected'.")
