import random
alphabets = [
'a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z',
'A','B','C','D','E','F','G','H','I','J','K','L','M',
'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','?']
num_l= int(input("How many letters would you in your password? "))
num_n=int(input("How many numbers would you like in your password? "))
num_s=int(input("How many symbols would you like in your password? "))

password_list=[]
for n in range(num_l):
    password_list.append(random.choice(alphabets))

for n in range(num_n):
    password_list.append(random.choice(numbers))

for n in range(num_s):
    password_list.append(random.choice(symbols))

# password=""
#
# for i in range(len(password_list)):
#     ltr=random.choice(password_list)
#     password += ltr
#     password_list.remove(ltr)
# print(f"Your password is: {password}")

# ANOTHER LOGIC FOR RANDOM IS SHUFFLE
password=""
random.shuffle(password_list)
for char in password_list:
    password += char
print(f"Your password is: {password}")
