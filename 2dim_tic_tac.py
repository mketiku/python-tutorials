#  Purpose:    Example: a 2D list

tictactoe = [[1,2,3], [4,5,6], [7,8,9]]
print (tictactoe[0])
print (tictactoe[1])
print (tictactoe[2])
print()

row = 1
column = 0
print ("row " + str(row) + " column " + str(column) + " has value")
print (tictactoe[row][column])

row = 2
column = 2
print ("row " + str(row) + " column " + str(column) + " has value")
print (tictactoe[row][column])

print()
print()
tictactoe[2][2] = 0
print ("After changing the value at row 2 and column 2 to 0: ")
print()
print (tictactoe[0])
print (tictactoe[1])
print (tictactoe[2])



