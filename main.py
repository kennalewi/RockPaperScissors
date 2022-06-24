rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

#create list of choices
choices = ['rock', 'paper', 'scissors']

#get the player's choice
player_choice = input("Choose rock, paper, or scissors: ")

#randomly get the computer's choice
comp_num = random.randint(0,2)
comp_choice = choices[comp_num]

if player_choice == 'rock':
  if comp_choice == 'rock':
    print(f"Player throw: {rock} \n Computer throw: {rock} \n You have tied")
  elif comp_choice == 'paper':
    print(f"Player throw: {rock} \n Computer throw: {paper} \n You have lost")
  else:
    print(f"Player throw: {rock} \n Computer throw: {scissors} \n You have won!")
elif player_choice == 'paper':
  if comp_choice == 'rock':
    print(f"Player throw: {paper} \n Computer throw: {rock} \n You have won!")
  elif comp_choice == 'paper':
    print(f"Player throw: {paper} \n Computer throw: {paper} \n You have tied")
  else:
    print(f"Player throw: {paper} \n Computer throw: {scissors} \n You have lost")  
elif player_choice == 'scissors':
    if comp_choice == 'rock':
      print(f"Player throw: {scissors} \n Computer throw: {rock} \n You have lost")
    elif comp_choice == 'paper':
      print(f"Player throw: {scissors} \n Computer throw: {paper} \n You have won!")
    else:
      print(f"Player throw: {scissors} \n Computer throw: {scissors} \n You have tied")
else:
  print("That choice doesn't count, computer wins.")