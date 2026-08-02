import random

genotypes = {
    "normal": "AA",
    "carrier": "Aa",
    "affected": "aa"
}

def get_gametes(genotype):
    """Return possible gametes."""
    return list(genotype)

def infant_genotype(parent1, parent2):
    """Generate one infant's genotype."""
    g1 = random.choice(get_gametes(parent1))
    g2 = random.choice(get_gametes(parent2))

    genotype = ''.join(sorted(g1 + g2))

    if genotype == "AA":
        phenotype = "Normal/pure" 
    
    elif genotype in ["Aa", "aA"]:
      genotype = "Aa"
      phenotype = "Carrier"

    else:
        genotype = "aa"
        phenotype = "Affected (Phenylketonuria)"

    return genotype, phenotype

def pedigree(parent1_name, parent2_name, infants=5):

    p1 = genotypes[parent1_name]
    p2 = genotypes[parent2_name]

    print("="*55)
    print(f"Parents: {parent1_name.upper()} ({p1}) {parent2_name.upper()} ({p2})")
    print("="*55)

    for i in range(infants):
        g, p = infant_genotype(p1, p2)
        print(f"Infant {i+1}: {g} --> {p}")

    print("\n") 

cases =[

("normal","normal"),
("normal","carrier"),
("normal","affected"),

("carrier","carrier"),
("carrier","affected"),

("affected","affected")
]

for c in cases:
    pedigree(c[0], c[1], infants=8)