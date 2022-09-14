gender = input("enter your biological gender(male/female): ")
hemoglobin_str = input("enter your hemoglobin number in (g/l): ")
hemoglobin = float(hemoglobin_str.replace("g/l", " "))
gender = gender.lower()
if gender == "male":
    if(hemoglobin < 134):
        print("The hemoglobin level is low.")
    elif(hemoglobin > 167):
        print("The hemoglobin level is high. ")
    else:
        print("The hemoglobin level is Normal.")
elif gender == "female":
    if(hemoglobin<117):
      print("The hemoglobin level is low.")
    elif(hemoglobin>155):
      print("the hemoglobin level is high.")

else:
    print("The hemoglobin level is Normal.")




