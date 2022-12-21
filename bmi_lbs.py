#LBS AND POUNDS

def bmi_lbs():
    name = input("What is your name? ")
    weight = int(input(name + " What is your weight (lb): \n"))

    height = float(input(name + " What is your hieght (inches): \n"))

    bmi = float((weight / height / height) * 703)


    underweight = bmi < 18.5
    normal = 18.5 <= bmi < 24.9
    overweight = 25 <= bmi < 29.9
    obesity = bmi > 30.0

    print("\n", name, "Your Bmi is ", bmi)


    if underweight:
        print("\nYou are Underweight ")
    if normal:
        print("\nYou are at the Normal weight from 18.5 to 24.9")
    if overweight:
        print("\nYou are Overweight from 25 to 29.9")
    if obesity:
        print("\n Obesity is when your bmi is over 30")


    again = input("\n Do you want to do other BMI? \n\n Yes or No ")

    while again == "yes":
        bmi_lbs()== True
    if again == "no":
        print("Thanks for do BMI on python!")
        bmi_lbs == False




if(__name__=="__main__"):
    bmi_lbs()