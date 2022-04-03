import random
continue_game=True

while continue_game:

    user_choice=int(input('Enter  your choice - 0 for rock  1 for paper  2 for scissors\n'))


    if user_choice == 0:
        print('you choose rock')
    elif user_choice == 1:
        print('you choose paper')
    else:
        print('you choose scissors')

    computer_choice=random.randint(0,2)

    if computer_choice == 0:
        print('computer choose rock')
    elif computer_choice == 1:
        print('computer choose paper')
    else:
        print('computer choose scissors')

    if user_choice == 0:
        if user_choice == computer_choice:
            print("it is a draw")

        elif computer_choice== 1:
            print('you loose')
        else:
            print('you win')

    if user_choice == 1:
        if user_choice==computer_choice:
            print('it is draw')

        elif computer_choice == 2:
            print('you loose')
        else:
            print('you win')

    else:
        if computer_choice==user_choice:
            print('it is draw')

        elif computer_choice== 0:
            print('you loose')

        else:
            print('you win')

    choice=input('Do tou want to continue y/n')
    choice=choice.lower()
    if choice =='y':
        continue_game=True

    else:
        continue_game=False