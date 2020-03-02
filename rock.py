"""
Rock Paper Scissors game

Justin G Mitchell
jgmitchell@gmail.com
"""

import random    

playing = None

computer_score = 0
player_score = 0
tied = 0
    
while playing != 'q':
    print('\nWhat are you going to throw?')
    human = input('\n\nr: Rock\np: Paper\ns: Scissors\n\nq: Quit\nPlayer\'s choice is:\n')
    if human == 'r':
        computer = random.choice(['rock','paper','scissors'])
        print('Human throws ROCK!')
        if computer == 'rock':
            tied = tied + 1
            print('The other player threw ' + computer + '. It\'s a tie')
        elif computer == 'paper':
            computer_score = computer_score + 1
            print('The other player threw ' + computer + '. Computer wins!')
        elif computer == 'scissors':
            player_score = player_score + 1
            print('The other player threw ' + computer + '. Human wins!')
    elif human == 'p':
        computer = random.choice(['rock','paper','scissors'])
        print('Human throws PAPER!')
        if computer == 'rock':
            player_score = player_score + 1
            print('The other player threw ' + computer + '. Human wins')
        elif computer == 'paper':
            tied = tied + 1
            print('The other player threw ' + computer + '. It\'s a tie')
        elif computer == 'scissors':
            computer_score = computer_score + 1
            print('The other player threw ' + computer + '. Computer wins!')
    elif human == 's':
        computer = random.choice(['rock','paper','scissors'])
        print('Human throws SCISSORS!')
        if computer == 'rock':
            computer_score = computer_score + 1
            print('The other player threw ' + computer + '. Computer wins!')
        elif computer == 'paper':
            player_score = player_score + 1
            print('The other player threw ' + computer + '. Human wins!')
        elif computer == 'scissors':
            tied = tied + 1
            print('The other player threw ' + computer + '. It\'s a tie')
    elif human == 'q':
        human = 'q'
        print('\nHuman chooses to quit! Good bye :)')
        print('\n\nHuman won ' + str(player_score) + ' times')
        print('\nComputer won ' + str(computer_score) + ' times')
        print('\nYou tied ' + str(tied) + ' times')
        if player_score > computer_score:
            print('\nThe human beat us this time')
        elif player_score < computer_score:
            print('\nWe beat the human! ha ha ha')
        elif player_score == computer_score:
            print('\nWe were evenly matched this time')
        exit()