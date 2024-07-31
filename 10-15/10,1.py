matrix = [[x+y for x in range(3)] for y in range(1, 10, 3)]

print("This is the old  matrix")
for i in matrix:
	for j in i:
		print(j, end=" ")
	print(" ")

print("This is the transposed matrix")

rez = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

for row in rez:
    for column in row:
        print(column, end=" ")
    print(" ")
