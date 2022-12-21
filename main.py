import bmi_lbs
import bmi_klg


metric = input("Do you prefer klg or lbs? ").lower().strip()

if metric == "klg":
    print("You chose klg!")
    bmi_klg.bmi_klg()
elif metric == "lbs":
    print("You chose lbs!")
    bmi_lbs.bmi_lbs()