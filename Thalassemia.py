import random

# Genotypes
genotypes = {
    "normal": "AA",
    "carrier": "Aa",
    "affected": "aa"
}

# Function to generate one infant's

def child(parent1, parent2):

    allele1 = random.choice(parent1)
    allele2 = random.choice(parent2)

    genotype = ''.join(sorted(allele1 + allele2))

    if genotype == "AA":
        phenotype = "Normal"

    elif genotype == "Aa":
        phenotype = "Carrier"

    else:
        phenotype = "Affected (Thalassemia)"

    return genotype, phenotype


# Function to display family and crossing

def pedigree(parent1, parent2):

    print("\n")
    print("Parents:", parent1, "X", parent2)
    print("")

    for i in range(5):

        g, p = child (parent1, parent2)

        print("Child", i+1, ":", g, "-->", p)



# ALL possiable cases of pedigree


pedigree("AA", "AA")   # Normal × Normal

pedigree("AA", "Aa")   # Normal × Carrier

pedigree("AA", "aa")   # Normal × Affected

pedigree("Aa", "Aa")   # Carrier × Carrier

pedigree("Aa", "aa")   # Carrier × Affected

pedigree("aa", "aa")   # Affected × Affected