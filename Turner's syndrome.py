def predict_turner(
    maternal_age,
    gestational_age,
    fetal_fraction,
    x_monosomy_probability
):

    # LOW RISK
    if (
        maternal_age < 35 and
        10 <= gestational_age <= 22 and
        fetal_fraction >= 4 and
        x_monosomy_probability < 1
    ):
        print("LOW RISK")

    # MEDIUM RISK
    elif (
        maternal_age >= 35 and
        10 <= gestational_age <= 22 and
        fetal_fraction >= 4 and
        1 <= x_monosomy_probability < 70
    ):
       print("MEDIUM RISK")

    # HIGH RISK
    elif (
        10 <= gestational_age <= 22 and
        fetal_fraction >= 4 and
        x_monosomy_probability >= 70
    ):
        print("HIGH RISK")

    else:
        print ("INSUFFICIENT SAMPLE / REPEAT TEST")