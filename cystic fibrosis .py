import random

# Genotypes
genotypes = {
    "normal": "CC",
    "carrier": "Cc",
    "affected": "cc"
}

# Function to generate one child

def child(parent1, parent2):

    allele1 = random.choice(parent1)
    allele2 = random.choice(parent2)

    genotype = ''.join(sorted(allele1 + allele2))

    if genotype == "CC":
        phenotype = "Normal"

    elif genotype == "Cc":
        phenotype = "Carrier"

    else:
        phenotype = "Affected (Cystic Fibrosis)"

    return genotype, phenotype


# Function to display pedigree
def pedigree(parent1, parent2):

    print("\n")
    print("Parents:", parent1, "×", parent2)
    print("=")

    for i in range(5):

        g, p = child(parent1, parent2)

        print("Child", i+1, ":", g, "-->", p)



# ALL possible CASES are here


pedigree("CC", "CC")   # Normal × Normal

pedigree("CC", "Cc")   # Normal × Carrier

pedigree("CC", "cc")   # Normal × Affected

pedigree("Cc", "Cc")   # Carrier × Carrier

pedigree("Cc", "cc")   # Carrier × Affected

pedigree("cc", "cc")   # Affected × Affected