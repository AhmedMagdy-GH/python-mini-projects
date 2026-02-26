import random

rock= """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""

paper= """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

"""
scissor= """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""

ls_game=[rock,paper,scissor]
user = int(input("What do you choose? Type 0 for Rock, 1 for paper,  2 for scissor\n"))
if user >= 0 and user < 3:
    print (f"{ls_game[user]}\n")
cmp=random.randint(0,2)
print(f"Computer chose:")
print(ls_game[cmp])

if user > 2 or user < 0:
    print("You entered an invalid number. You lose!")
elif user == cmp:
    print("Draw")
elif user == 0 and cmp ==2:
    print("user Win")
elif user == 0 and cmp ==1:
    print("user Lose")
elif user ==1 and cmp ==0:
    print("user Win")
elif user == 1 and cmp ==2:
    print("user Lose")
elif user == 2 and cmp ==1:
    print("user Win")
elif user == 2 and cmp ==0:
    print("user Lose")