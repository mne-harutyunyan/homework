# 10. Ունենք ամբողջ թվերից բաղկացած մատրից, որի վրա պետք է իրականացնել transpose։ 
# Transpose կատարել նշանակում է մատրիցի տողերը փոխադրել սյուներով: Օրինակ՝
# matrix = [[1, 2, 3]       
#          ,[4, 5, 6]
#          ,[7, 8, 9]]
# # transposing a matrix
# transposed = [[1, 4, 7]
#              ,[2, 5, 8]
#              ,[3, 6, 9]]
import numpy as np
def transposing_matrix(matrix):
    transposed = np.transpose(matrix)
    return transposed

matrix = [[1, 2, 3]       
         ,[4, 5, 6]
         ,[7, 8, 9]]

print(f"This is the transposed matrix:\n{transposing_matrix(matrix)}")
