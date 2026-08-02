# Huntington Disease Inheritance 

male_parent = input("Enter male parent status (affected/unaffected): ").lower()
female_parent = input("Enter female parent status (affected/unaffected): ").lower()

if male_parent == "affected" and female_parent == "unaffected":
    print("\nResult:")
    print("Father is affected and mother is unaffected.")
    print("Each child has a 50% chance of inheriting Huntington disease.")
    print("for family planing IVF(in vitro fretilization ) with sperm donar is Required ")

elif male_parent == "unaffected" and female_parent == "affected":
    print("\nResult:")
    print("Father is unaffected and mother is affected.")
    print("Each child has a 50% chance of inheriting Huntington disease.")
    print("for family planing IVF(in vitro fretilization ) with egg donar is Require," \
    "surogacy is also opt. ")

elif male_parent == "affected" and female_parent == "affected":
    print("\nResult:")
    print("Both parents are affected.")
    print("The risk is higher than 50% and depends on the parents' genotypes.")

elif male_parent == "unaffected" and female_parent == "unaffected":
    print("\nResult:")
    print("Both parents are unaffected.")
    print("Children are not expected to inherit Huntington disease.")

else:
    print("\nInvalid input!")
    print("Please enter only 'affected' or 'unaffected'.")
    print("if the case have huntington's consider prvention at time of family planing ")

