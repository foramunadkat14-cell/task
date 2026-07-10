# 1) w.a.p. to Check Positive, Negative, or Zero

number = int(input("Enter a number: "))

if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
else:
    print("Number is Zero")



# 2) w.a.p. to Find the Largest of Two Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First number is largest")
elif b > a:
    print("Second number is largest")
else:
    print("Both numbers are equal")



# 3) w.a.p. to Check Leap Year

year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")



# 4)  w.a.p. to Check Vowel or Consonant

letter = input("Enter a character: ")

if letter in ('a','e','i','o','u','A','E','I','O','U'):
    print("Vowel")
else:
    print("Consonant")



# 5) w.a.p. to  Electricity Bill Calculator

units = int(input("Enter total units used:"))
if(units>=100):
    print("Bill is:",4*units)
elif(units>=50):
    print("Bill is:",3*units)
elif(units>=10):
    print("Bill is:",2*units)
else:
    print("No bill")



# 6) w.a.p. to check Loan eligibility

credit_score = int(input("Enter your credit score:"))
monthly_income = int(input("Enter your monthly_income:"))
if credit_score>=700 and monthly_income>=30000:
    print("Loan approved")
else:
    print("Loan not approved")



# 7) w.a.p. to check Scholarship eligibility

marks = int(input("Enter your marks:"))
family_income = int(input("Enter your income:"))
if(marks>=75 and family_income<=30000):
    print("Eligible")
else:
    print("Not eligible")



# 8) w.a.p. to check Temperature-Based Weather Message

temp = int(input("Enter temperature:"))
if(temp>=30):
    print("Weather is hot")
elif(temp>=10):
    print("Weather is normal")
else:
    print("Weather is cold")



# 9) w.a.p. to check Age-Based Movie Rating

age = int(input("Enter your age:"))
if(age>=18):      
    print("You can watch R-rated movies")
elif(age>=13):
    print("You can watch PG-13 movies")
else:     
    print("You can watch G-rated movies")



# 10) w.a.p. to check student attendance

attendance= int(input("Enter the attendance percentage: "))
if attendance>=90:
    print("excellent attendance")
elif attendance>=89 or attendance>=75:
    print("good attendance")
elif attendance>=74 or attendance>=50:
    print("average attendance")
else:
    print("poor attendance")