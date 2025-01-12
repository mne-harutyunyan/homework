import numpy as np
matrix = [[x+y for x in range(4)] for y in range(1, 16, 4)]

print("\nThis is the old  matrix\n")
for i in matrix:
	for j in i:
		print(j, end=" ")
	print(" ")

print("\nThis is the rotated matrix\n")
matrix2 = np.rot90(matrix,2)

for i in matrix2:
	for j in i:
		print(j, end=" ")
	print(" ")

