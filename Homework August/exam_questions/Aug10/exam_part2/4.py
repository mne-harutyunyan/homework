# Ի՞նչ գործողություն է կատարում slicing Python-ում, բերել կոդի օրինակներ։
    # slicing-ը հիմնականում կարող ենք օգտագործել list, tuple, string-ի վրա, ինչպես նաև range-ի.
    # այն ունի start : step : stop 

ls = [x for x in range(1,11,1)]
ls1 = ls[:] #shallow copy with slicing

str = "hello"
str1 = str[::-1] #reversing string with slicing

tp = (1,2,3,4,5,6,7,8,9)
tp1 = tp[::2] 
tp2 = tp1[2:4]
print(ls1)
print(str1)
print(tp1)
print(tp2)