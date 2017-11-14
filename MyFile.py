
def check_input(var_input):
	if len(var_input) > 2:
		print 'Enter a maximum of two alphanumeric characters'
		return False
	elif var_input[0].upper() not in ['X','O']:
		print 'Enter either X or O as the first character. This is your marker for the game '
		return False
		
	elif int(var_input[1]) not in range(1,10):
		print 'Enter a valid number from 1 through 9 in the second character '
		return False
	else:
		return True
			
def print_board(p1,p2,p3,p4,p5,p6,p7,p8,p9):
	print '    *    *    '
	print '  ',p7,'* ',p8,' *',p9
	print '    *    *    ' 
	print '**************' 
	print '    *    *    '  
	print '  ',p4,'* ',p5,' *',p6
	print '    *    *    ' 
	print '**************' 
	print '    *    *    ' 
	print '  ',p1,'* ',p2,' *',p3
	print '    *    *    ' 


def check_game_status1(i):
	
	print(i) 
	if i == 4:
		return True
	else:
		return False

def check_game_status(p_board,p_marker):
	if (p_board[0] == p_board[1] == p_board[2] == p_marker) or (p_board[0] == p_board[4] == p_board[8] == p_marker) or (p_board[0] == p_board[3] == p_board[6] == p_marker) or (p_board[1] == p_board[4] == p_board[7] == p_marker) or (p_board[2] == p_board[4] == p_board[6] == p_marker) or (p_board[2] == p_board[5] == p_board[8] == p_marker) or (p_board[3] == p_board[4] == p_board[5] == p_marker) or (p_board[6] == p_board[7] == p_board[8] == p_marker):
		print 'Player ',p_marker.upper() ,' wins!!'
		return 'Win'
	elif (len(p_board[0]) == 0) or (len(p_board[1]) == 0) or (len(p_board[2]) == 0) or (len(p_board[3]) == 0) or (len(p_board[4]) == 0) or (len(p_board[5]) == 0) or (len(p_board[6]) == 0) or (len(p_board[7]) == 0) or (len(p_board[8]) == 0):
		return 'Ongoing'		
	else:
		return 'It''s a Tie'

	
			
def tictactoe():
	x = True
	board = ['','','','','','','','','']
	end_of_game = 'Ongoing'
	#i = 0 
	
	
	
	while x == True and end_of_game == 'Ongoing':
		
		board_input =   input('Enter 2 digit Marker Position: ')
		x = check_input(board_input)
		if x == False: 
			print 'GoodBye!! '
		else:
			marker = board_input[0]
			mnum = int(board_input[1]) - 1
			
			if len(board[mnum]) > 0:
				print 'Enter a different location'
			else:	
				board[mnum] = marker
				print_board(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8])
				#i +=1
				#end_of_game = check_game_status1(i)
				end_of_game = check_game_status(board,marker)
				if end_of_game == 'It''s a Tie':
					print 'It''s a Tie'
		
		
		
		
	YesNo = input('Do you want to play a new game? (y/n)')
	if YesNo.upper() == 'Y':
		tictactoe()
	else:
		print 'End of Game'	




tictactoe()
#print_board('X','O','X','X','O','O','O','O','O')	
