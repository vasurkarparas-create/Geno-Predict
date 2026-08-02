# Familial Alzheimer's Disease (Autosomal Dominant)


print("Familial Alzheimer's Disease Prediction")
print("Enter parent status: affected or normal")

father = input("Enter father's status: ").lower()
mother = input("Enter mother's status: ").lower()

if father == "affected" and mother == "normal":
    print("\nPrediction:")
    print("Affected Child : 50%")
    print("Normal Child   : 50%")

elif father == "normal" and mother == "affected":
    print("\nPrediction:")
    print("Affected Child : 50%")
    print("Normal Child   : 50%")

elif father == "affected" and mother == "affected":
    print("\nPrediction:")
    print("Affected Child : 75%")
    print("Normal Child   : 25%")

elif father == "normal" and mother == "normal":
    print("\nPrediction:")
    print("Affected Child : 0%")
    print("Normal Child   : 100%")

else:
    print("\nInvalid Input!")
    print("Please enter only 'affected' or 'normal'.")


if"parent is carrier further it be affected dut to its is a dominant autosomal":
    print("carrier get affected after the time due to autosomal dominance")