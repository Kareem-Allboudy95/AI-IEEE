# Problem 1
n = int(input("Enter a number: "))
sum = n*(n+1)/2
print(sum)

#####################################
# Problem 2

A = int(input("Enter 1st num: "))
B = int(input("Enter 2nd num: "))
C = int(input("Enter 3rd num: "))
if A < B:
    if B < C:
        print (A, "<", B, "<", C)
    else:
        if A < C:
            print (A, "<", C, "<", B)
        else:
            print (C, "<", A, "<", B)
else:
    if C < B:
        print (C, "<", B, "<", A)
    else:
        if C < A:
            print (B, "<", C, "<", A)
        else:
            print (B, "<", A, "<", C)

#####################################
# Problem 3

X = int(input("Enter a positive number: "))
factorial = 1

if X < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif X == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,X + 1):
       factorial = factorial*i
   print("The factorial of",X,"is",factorial)

#####################################
# Problem 4

input_string = input("Enter family members separated by space ")
family_list  = input_string.split()
for name in family_list:
    print(name)
print ("The list is: " + str(family_list)) 
result = [] 
for i in family_list: 
    if i not in result: 
        result.append(i) 
print ("The list after removing duplicates : " + str(result))

#####################################
# Problem 5

#the output of the code is False because [round(6.5) - round(3.5)] = 2   < 3 