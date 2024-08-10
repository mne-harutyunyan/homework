# Իրականացնել make_multiplier closure, որն ընդունում է մեկ n արգումենտ ր վերադարձնում է մեկ այլ ֆունկցիա։ 
# Այս վերադարձված ֆունկցիան պետք է ընդունի մեկ X արգումենտ և վերադարձնի n և X արտադրյալը։
# Իրականացնել ծրագիրը օգտագործելով միայն Lambda ֆունկցիաներ։
# Example usage of the closure
# multiplier_of_3 = make_multiplier(3)
# print(multiplier_of_3(10))  # Expected output: 30

make_multiplier = lambda n: lambda x: x*n
multiplier_of_3 = make_multiplier(4)
print(f"The result is {multiplier_of_3(29)}.")
