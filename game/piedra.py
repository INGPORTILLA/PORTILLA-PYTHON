# proyecto piedra papel o tijera
import random
options = ('piedra', 'papel', 'tijera')

user_option = input('elija piedra papel o tijera=> ' )
user_option = user_option.lower()

if not user_option in options:
  print('accion incorrecta')
computer_option = random.choice(options)

if user_option == computer_option:
  print('empate!')

elif user_option == 'piedra':
  if computer_option == 'tijera':
    print("piedra gana a tijera")
    print('user gana!')

  else:
    print('papel gana a piedra')
    print('computer gana')

elif user_option == 'papel':
  if computer_option == 'piedra':
    print('papel gana a piedra')
    print('gana user!')

  else:
    print('tijera gana a papel')
    print('gana computer')

elif user_option == 'tijera':
  if computer_option == 'papel':
    print('tijera gana papel')
    print('gana user!')

  else:
    print('piedra gana a tijera')
    print('computer gana')
    
