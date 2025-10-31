

#child (0-12 years)
# a teenager (13-19 years), 
# an adult (20-64 years),
#or a senior (65+ years)
age = int(input("Enter Your Age: "))
if age <= 12 and age > 0:
    print("Child")
elif age >=13 and age <=19:
    print("A teenage")
elif age >=20 and age <=64:
    print("Adult")
elif age >= 65 and age <= 110:
    print("Senior")
else:
    print("Enter Proper Age")
