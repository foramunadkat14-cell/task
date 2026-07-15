# w.a.p. to print naturals number
for i in range(1, 11):
    print(i)



# w.a.p. to print 1 to 10 numbers and find odd numbers only
for i in range(1, 11):
    if i % 2 != 0:
        print(i)



# w.a.p. to print 1 to 10 numbers and find even numbers only
for i in range(1, 11):
    if i % 2 == 0:
        print(i)



# w.a.p. to find infinite loop
while True:
    print("Infinite Loop")



# w.a.p. to find factorial of number
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is {factorial}")



# w.a.p. to find armstrong number
num = int(input("Enter a number: "))
order = len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if num == sum:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")  



# w.a.p. to find numbers is prime or not
num = int(input("Enter a number: "))
is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")



# create a list and itrate via for loop
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)




# w.a.p to find choice based calculator choice a number
print("------calculator------")
print("1 for add")
print("2 for sub")
print("3 for multi")
print("4 for div")
print("5 for exit")

while True:
    num=(input("Enter a number : "))
    if num=='1':
        print("you have chosen addition")
        a=int(input("ENTER A NUMBER : "))
        b=int(input("ENTER A NUMBER : "))
        c=a+b
        print(c)
    
    if num=='2':
        print("you have chosen subtraction")
        a=int(input("ENTER A NUMBER : "))
        b=int(input("ENTER A NUMBER : "))
        c=a-b
        print(c)

    if num=='3':
        print("you have chosen multiply")
        a=int(input("ENTER A NUMBER : "))
        b=int(input("ENTER A NUMBER : "))
        c=a*b
        print(c)

    if num=='4':
        print("you have chosen division")
        a=int(input("ENTER A NUMBER : "))
        b=int(input("ENTER A NUMBER : "))
        c=a/b
        print(c)

    if num=='5':
        print("THE PROGRAM HAS ENDED THANK YOU")
        
        break

    


# create a dictionary and itrate via for loop
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():    
    print(f"{key}: {value}")



# create a tuple and itrate via for loop
my_tuple = (1, 2, 3, 4, 5)
for item in my_tuple:     
    print(item)
