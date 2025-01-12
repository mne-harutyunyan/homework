# Ի՞նչ տարբերութուն truncating division-ի և floor division-ի միջև։ Հիմնավորել պատասխանը։
    #Floor division-ը կատարում է թվի հատակային կլորացում դեպի տվյալ թիվը (օր՝ 2.5 = 2, -2.5 = -3),
    #truncating division-ը կատարում է կլորացում դեպի 0-ն (օր՝ 2.5 = 2, -2.5 = -2): Այն գտնվում է math գրադարանում.

import math
num = math.trunc(-5/3) #-1
num1 = math.trunc(5/3) #1

num2 = 5//3 #1
num3 = -5//3 #-2
print(num)
print(num1)
print(num2)
print(num3)




