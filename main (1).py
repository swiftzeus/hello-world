
# grid prints out the grid using list L1.

def grid(L1):
	line = '---   ---   ---'
	entry = ' {}  |  {}  |  {} '
	print(entry.format(L1[6],L1[7],L1[8]))
	print(line)
	print(entry.format(L1[3],L1[4],L1[5]))
	print(line)
	print(entry.format(L1[0],L1[1],L1[2]))

#turn takes the turn and amends L1 to reflect the cell selected.

def turn(x):
    j = 0
    while j == 0:
        if x%2 != 0:
            turn = int(input('{} it is your turn.'. format(player1)))
            if L1[turn-1] == ' ':
                L1[turn-1] = 'X'
                break
            else:
                print('This space is already taken. Try again.')
                j = 0
        else:
            turn = int(input('{} it is your turn.'. format(player2)))
            if L1[turn-1] == ' ':
                L1[turn-1] = 'O'
                break
            else:
                print('This space is already taken. Try again.')
                j = 0
    return L1

# tests the input to check whether it leads to a winning result. 

def test_winner(L1,x):
    if x%2 == 0:
        f = player2
    else:
        f = player1
    winning_combos = [(0,3,6),(1,4,7),(2,5,8),(0,1,2),(3,4,5),(6,7,8),(0,4,8),(2,4,6)]
    for a,b,c in winning_combos:
        if L1[a] == L1[b] == L1[c] != ' ':
            print('{} you won!!'.format(f))
            x = x - 1
            break
    x = x + 1
    return x

# The actual game incorporating the different functions below.
print('Hello this is Noughts and Crosses'.upper())

game = 1
while game == 1:
    L1 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1 = input("Please give player 1's name:  ")
    player2 = input("Please give player 2's name:  ")
    print('Welcome to the game {} and {}'.format(player1,player2))
    grid(L1)
    x = 1
    while x < 9:
        i = x
        turn(x)
        grid(L1)
        x = test_winner(L1,x)
        if x == i:
            print('THE END')
            break
    again = input('Would you like to play again? Y or N.')
    if again == 'Y'.upper() or 'Y'.lower():
        game = 1
    else:
        break

