# Define parent carrier statuses (true means the parent carries the mutated gene)
carrier_male = True
carrier_female = True

# Calculate inheritance probabilities based on parent statuses

if carrier_male and carrier_female:
    print("Both parents are carriers of Tay-Sachs disease.")
    print("Probability of an affected child (has the disease): 25%")
    print("Probability of a carrier child (carries the gene but is healthy): 50%")
    print("Probability of an unaffected, non-carrier child: 25%")

elif carrier_male or carrier_female:
    print("Only one parent is a carrier.")
    print("Probability of an affected child: 0%")
    print("Probability of a carrier child: 50%")
    print("Probability of an unaffected, non-carrier child: 50%")

else:
    print("Neither parent is a carrier.")
    print("Probability of an affected child: 0%")
    print("Probability of a carrier child: 0%")
    print("Probability of an unaffected, non-carrier child: 100%")