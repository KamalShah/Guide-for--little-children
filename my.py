import random

while True:
	print("""Hello, friend!
	Today we will play !""")

	a = input("1 Start, 2 Over")
	if a == "1":
		print("Okay, let's start!")
	else:
		print("Goodbye")
		break

	print("""You hit there!
	If you want win, you must play cool! 
	""")

	print(""" You was hit in dark city.
	What will you doing?""")

	a = input("1 Go away, 2 Go to the city")
	if a == "1":
		print("Game over")
		break
	else:
		print("Wow! Let's go!")

	print(""" You see a robber!
	What will you do?""")	
			   
	a = input("1 kill him, 2 run away")
	if a == "1":
		print("You are a hero!")
	else:
		print("""I am sorry, but you was died
			because you was saved him!""")	
		break

	print("""Okay, you passed this mini-game!
		""")
input()

	a = input("1 continue, 2 over") 
	if a == "1":
		print("Okay, let's go!")
	else:
		print("Goodbye")
		break		

		board = list(range(1,10))

def draw_board(board):
    print ("-" * 13)
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-" * 13)

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print ("Эта клеточка уже занята")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    draw_board(board)

main(board)	

