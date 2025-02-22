import random
rock='''
 _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper='''
 _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)'''

scissors='''
 _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''
user_choice=int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors"))
computer_choice=random.randint(a:0, b:2)
print(f"Computer chose{computer_choice}")

if user_choice>=3 or user_choice<0:
    print("You tyoed an invalid number. You lose!")
elif user_choice==0 and computer_choice==2:
    print("You win!")
elif user_choice==2 and computer_choice==0:
    print("You lose!")    