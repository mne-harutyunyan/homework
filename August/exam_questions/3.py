# Իրականացնել ֆունկցիա, որն ընդունում է բառերի ցուցակ և վերադարձնում է համապատասխան բառերի
# երկարությունները ներկայացնող ամբողջ թվերի ցուցակ: Օգտագործել ցուցակի ըմբռնումը(list comprehension), 
# ինչպես նաև տրամադրել այլընտրանքային լուծում ՝ օգտագործելով map ֆունկցիա:

def word_lenght(ls:list)->list:
    return [len(word) for word in ls]

ls=['summer','telephone','books','homework','university','bus']
print(f"My function: words lenghts are {word_lenght(ls)}")

result = list(map(lambda word : len(word), ls) )
print(f"Map function: words lenghts are {result}")