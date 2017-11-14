
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

def check_game_status(i):
	print 'a'
	

	
			
def tictactoe():
	x = True
	board_marker = ['','','','','','','','','']
	end_of_game = False
	i = 0 
	
	
	
	while x == True and end_of_game == False:
		
		board_input =   input('Enter 2 digit Marker Position: ')
		x = check_input(board_input)
		if x == False: 
			print 'GoodBye!! '
		else:
			marker = board_input[0]
			mnum = int(board_input[1]) - 1
			
			if len(board_marker[mnum]) > 0:
				print 'Enter a different location'
			else:	
				board_marker[mnum] = marker
				print_board(board_marker[0],board_marker[1],board_marker[2],board_marker[3],board_marker[4],board_marker[5],board_marker[6],board_marker[7],board_marker[8])
				i +=1
				end_of_game = check_game_status1(i)
				
				
	













	
	YesNo = input('Do you want to play a new game? (y/n)')
	if YesNo.upper() == 'Y':
		tictactoe()
	else:
		print 'End of Game'	




tictactoe()
#print_board('X','O','X','X','O','O','O','O','O')	
