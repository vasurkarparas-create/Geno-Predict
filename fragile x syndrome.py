# Fragile X Syndrome Inheritance
# it is a x chrmosomal disorder so male child is more chances of affected than female 
# male xy chromosome 
#female  xx chromosome


print(" FRAGILE X SYNDROME PREDICTION ")

father = input("Enter father's status (normal/carrier/affected): ").lower()
mother = input("Enter mother's status (normal/carrier/affected): ").lower()

if father == "carrier" and mother == "carrier":
    print("\nPrediction")
    print("Normal Child   : 25%")
    print("Carrier Child  : 50%")
    print("Affected Child : 25%")
    print("if male child born itnhas more risk than female ")

elif (father == "affected" and mother == "carrier") or \
     (father == "carrier" and mother == "affected"):
    print("\nPrediction")
    print("Normal Child   : 0%")
    print("Carrier Child  : 50%")
    print("Affected Child : 50%")
    print(" male child born itnhas more risk than female ")


elif father == "affected" and mother == "affected":
    print("\nPrediction")
    print("Normal Child   : 0%")
    print("Carrier Child  : 0%")
    print("Affected Child : 100%")

elif (father == "normal" and mother == "carrier") or \
     (father == "carrier" and mother == "normal"):
    print("\nPrediction")
    print("Normal Child   : 50%")
    print("Carrier Child  : 50%")
    print("Affected Child : 0%")

elif (father == "normal" and mother == "affected") or \
     (father == "affected" and mother == "normal"):
    print("\nPrediction")
    print("Normal Child   : 0%")
    print("Carrier Child  : 100%")
    print("Affected Child : 0%")

elif father == "normal" and mother == "normal":
    print("\nPrediction")
    print("Normal Child   : 100%")
    print("Carrier Child  : 0%")
    print("Affected Child : 0%")

else:
    print("\nInvalid input!")
    print("Enter only: normal, carrier, or affected.")