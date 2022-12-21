#KILOGRAMS AND METRICS

def bmi_klg():
    name = input("What is your name? ")
    weight = int(input(name + " what is your weight: \n"))
    height = float(input(name + " Whatis your height: \n"))
    bmi = float(weight / height / height)


    underweight = bmi < 18.5
    normal = 18.5 <= bmi < 25
    overweight = 25 <= bmi < 29.9
    obesity = bmi >= 30

    print("\n", name, "Your Bmi is ", bmi)

    if underweight:
        print("\nYou are Underweight ")
    if normal:
        print("\nYou are at the Normal weight from 18.5 to 24.9")
    if overweight:
        print("\nYou are Overweight from 25 to 29.9")
    if obesity:
        print("\nYou are on Obesity when your bmi is over 30")


    again = input("\n Do you want to do other BMI?  \n Yes or No:  ")

    while again == "yes":
        bmi_klg() == True
    if again == "no":
        print("Thanks for do BMI on python!")
        bmi_klg == False



if(__name__=="__main__"):
    bmi_klg()