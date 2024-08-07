# Python-ը չի ապահովում ֆունկցիաների գերբեռնում, որպես ներկառուցված գործիք, չենք կարող ունենալ նույն անունով 
# ֆունկցիաներ, բայց տարբեր պարամետրերով։ Սակայն պետք է ընդօրինակել նման պահելաձև՝ օգտագործելով *args 
# փոփոխական երկարության positional արգումենտների համար և **kwargs keyword արգումենտների համար:
# Իրականացնել process_data ֆունկցիա, որն իրեն այլ կերպ է պահում ՝ կախված իրեն փոխանցվող փաստարկների
# քանակից և տեսակից: Օրինակ՝
# print(process_data(5))                 # Should print 25
# print(process_data(5, 10))             # Should print 50
# print(process_data(name="Alice", age=30))  # Should print {'name': 'Alice', 'age': 30}

def process_data(*args, **kwargs):
    if len(args)==1:
        ls = [x*x for x in args] 
        res = ls[0]
    elif len(args)>1:
        x,y = args
        res = x*y
    elif kwargs:
        res = kwargs
    return res
print(process_data(5))                
print(process_data(5, 10))             
print(process_data(name="Alice", age=30)) 