# This is a simple Python program to predict the likelihood of sickle cell anemia in infants based on the genetic information of the parents.

sickle_cell_anemia = {
    "sickle cell anemia ss": 1,
    "non sickle cell anemia aa": 0,
    "carrier sickle cell anemia as": 2
}
#defining the genetic status of the parents
patient1 = {"male": "male", "age": 23, "sickle cell anemia ss": 1}
patient2 = {"female": "female", "age": 20, "sickle cell anemia ss": 1}

# defining the infant probabilty based on the genetic status of the parents

if patient1["sickle cell anemia ss"] == 1 and patient2["sickle cell anemia ss"] == 1:
    print("infant with sickle cell anemia." \
    "100% chance of having sickle cell anemia." \
    "REquired medical Bone marrow transplant.")
else:
    print("infant without sickle cell anemia.")

# case2:defining the genetic status of the parents

patient1 = {"male": "male", "age": 30, "sickle cell anemia ss": 1}
patient2 = {"female": "female", "age": 29, "non sickle cell anemia aa": 0}

if patient1["sickle cell anemia ss"] == 1 and patient2["non sickle cell anemia aa"] == 0:
    print("all children will be carrier of sickle cell anemia."
          "100% chance of having sickle cell anemia carrier." \
          "medical treatment is  required.")
else:    
       print("infant without sickle cell anemia.")

 # case 3:defining the genetic status of the parents    
 #                                                                          
patient1 = {"male": "male", "age": 35, "sickle cell anemia ss": 1 }
patient2 = {"female": "female", "age": 24, "sickle cell anemia as": 2 }

if patient1 ["sickle cell anemia ss"] == 1 and patient2 ["sickle cell anemia as"] == 2:

# if they had 4 children according the genetic gender was 2 male nad  2 female 

    print("son ss with 50% sickle cell anemia." \
    "son as with 50% carrier sickle cell anemia." \
    " daughter 50% with carrier sickle cell anemia." \
    "daughter 50% with sickle cell anemia." \
    "medical treatment is required for the children with sickle cell anemia.")

else:
    print("infant without sickle cell anemia." \
    "has a aa normal gene." \
    "No medical intervention required.")



# case 4:defining the genetic status of the parents 


patient1 = {"male": "male", "age": 30, "non sickle cell anemia aa": 0}
patient2 = {"female": "female", "age": 29, "non sickle cell anemia aa": 0}

if patient1["non sickle cell anemia aa"] == 0 and patient2["non sickle cell anemia aa"] == 0:
    print("infant without sickle cell anemia." \
    "no medical intervention required.")
else:
    print("infant may carry sickle cell trait. genetic counseling is recommended.")

# case 5:defining the genetic status 0of the parents 


patient1 = {"male": "male", "age": 30, "non sickle cell anemia aa": 0}
patient2 = {"female": "female", "age": 29, "carrier sickle cell anemia": 2}

if patient1["non sickle cell anemia aa"] == 0 and patient2["carrier sickle cell anemia"] == 2:
    print("0% chance of child having sickle cell anemia (SS)." \
    " 50% chance of child being a carrier (AS)." \
    " 50% chance of child being unaffected (AA)." \
    " no medical treatment required, genetic counseling is recommended.")
else:
    print("infant without sickle cell anemia." \
    " no medical intervention required.")

# case 6:defining the genetic status of the parents

patient1 = {"male": "male", "age": 30, "carrier sickle cell anemia as": 2}
patient2 = {"female": "female", "age": 29, "carrier sickle cell anemia as": 2}

if patient1["carrier sickle cell anemia as"] == 2 and patient2["carrier sickle cell anemia as"] == 2:
    print("25% chance of child being unaffected (AA), 50% chance of being a carrier (AS), and 25% chance of having sickle cell anemia (SS)." \
    " medical treatment is required for affected children." \
    " Genetic counseling is strongly recommended for family planning.")

else:
    print("0% chance of having sickle cell anemia, no worry of death.")
