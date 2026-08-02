# Coronary Artery Disease (CAD) Risk Prediction
# Educational Project

print("Coronary Artery Disease Risk Predictor ")

# Hereditary Factor
family_history = input("Family history of CAD (yes/no): ").lower()

# Lifestyle Factors
smoking = input("Do you smoke? (yes/no): ").lower()
alcohol = input("Do you consume alcohol frequently? (yes/no): ").lower()
exercise = input("Do you exercise regularly? (yes/no): ").lower()
diet = input("Is your diet healthy? (yes/no): ").lower()
obesity = input("Are you overweight/obese? (yes/no): ").lower()
stress = input("Do you have high stress? (yes/no): ").lower()
diabetes = input("Do you have diabetes? (yes/no): ").lower()
blood_pressure = input("Do you have high blood pressure? (yes/no): ").lower()
cholesterol = input("Do you have high cholesterol? (yes/no): ").lower()

risk = 0

# Hereditary

if family_history == "yes":
    risk += 3

# Lifestyle

if smoking == "yes":
    risk += 3

if alcohol == "yes":
    risk += 2

if exercise == "no":
    risk += 2

if diet == "no":
    risk += 2

if obesity == "yes":
    risk += 2

if stress == "yes":
    risk += 2

if diabetes == "yes":
    risk += 3

if blood_pressure == "yes":
    risk += 3

if cholesterol == "yes":
    risk += 3

print("\n]RESULT ]\n")

if risk <= 4:
    print("Risk Level : LOW")
    print("Prediction : Low probability of Coronary Artery Disease.")
    print("Recommendation:")
    print("- Continue healthy diet")
    print("- Exercise regularly")
    print("- Avoid smoking and alcohol")

elif risk <= 10:
    print("Risk Level : MODERATE")
    print("Prediction : Moderate probability of Coronary Artery Disease.")
    print("Recommendation:")
    print("- Improve lifestyle habits")
    print("- Monitor blood pressure and cholesterol")
    print("- Exercise at least 30 minutes daily")
    print("- Consult a doctor for regular check-ups")

else:
    print("Risk Level : HIGH")
    print("Prediction : High probability of Coronary Artery Disease.")
    print("Recommendation:")
    print("- Consult a cardiologist immediately")
    print("- Stop smoking and limit alcohol")
    print("- Control diabetes, blood pressure, and cholesterol")
    print("- Follow a heart-healthy diet")
    print("- Exercise under medical supervision")