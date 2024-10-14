

info = {
    'Name' : 'Awdhesh',
    'std' : 'CSE',
    'Pro' : 'Flutter',
    
}
print(info.keys()) 
print(info.values()) 

userName = input("Hey, what's your name? ") 
userAge = int(input("What's your age? "))

# if-elif-else ladder ------------>>>

if userAge >= 18:
    print('Hey, ' + userName)
    print('YES... you entered ' + str(userAge))
    print('Yeah... you are eligible to vote')
else:
    print('Sorry, ' + userName)
    print('You are not eligible to vote as you are only ' + str(userAge) + ' years old.')

#  Comparision operator ---------->>>>>>

a1 = int(input("Enter Number 1: "))
a2 = int(input("Enter Number 2: "))
a3 = int(input("Enter Number 3: "))
a4 = int(input("Enter Number 4 : "))

if(a1>a2 and a1>a3 and a1>a4 ):
    print("Gratest Number is A1 ", a1)

elif(a2>a1 and a2>a3 and a2>a4 ):
    print("Gratest Number is A2 ", a2)

elif(a3>a2 and a3>a4 and a3>a1 ):
    print("Gratest Number is A3 ", a3)

elif( a4>a1 and a4>a2 and a4>a3 ):
    print("Gratest Number is A4 ", a4)
    
    
