# if
# if else
# elif

# Syntax:
    
# if condition :
#     #statement



print("Check Eligiblity")
age=15
if age>=18 :  # 15>=18 F
    print("you are eligible to get License")
print("You are done Checking")



print("Check Eligiblity")
text="you are not Eligible"
age=20
if age>=18 :  # 15>=18 F
    text="you are eligible to get License"
    
print(text)
print("Thanks for Checking")


# if else:
# syntax:
# if condition :
#     if block 
# else:
#     else block    



is_logged_in=False
if is_logged_in :
    print("You are Logged In") 
else :
    print("you are not logged in")
    
mark =34 
if mark>=35:
    print("Pass")
else:
    print("Fail")
    
# elif
# Syntax:
# if condition :
#     if block 
# elif condition :
#     elif block
# elif condition :
#     elif block 
# else:
#     else block

a=135
b=45
c=70

if a>b and a>c :
    print(" a is Bigger ")
elif b>c:
    print("b is Bigger")
else :
    print("C is Bigger ")


day = 6
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekdays")
    case _ :
        print("Weekend")
        
    
print("Even" if 4%2==0 else "Odd")

age=18
has_voter_id=True
if age>=18 :
    if has_voter_id :
        print("Eligible to Vote")
    else:
        print("Get Voter Id ")
else:
    print(" Above 18 is Eligible to Vote ")
    
# Ternary operator:

age=19
print("You are Above 18 " if age>=18 else " You are minor")

a=5
print("Even" if a%2==0 else " Odd")

