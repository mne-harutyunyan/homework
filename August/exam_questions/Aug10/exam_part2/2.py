# Ի՞նչ տարբերություն(ներ) ունեն shallow copy և deep copy-ն։ Բերել օրինակներ,
# որտեղ հստակ նկարագրված կլինեն այդ տարբերությունները։

    #Shallow copy-ն մակերեսային պատճենումն է, դրա ստեղծում է նոր օբյեկտ, որը հղվում է այլ հասցեի վրա,
    #սակայն պատճենվող օբյեկտի ներսում առկա բոլոր օբյեկտների հասցեները մնում են նույնը։
    #Deep copy-ն առկա է copy գրադարանում, որը լուծում է shallow copy-ի խնդիրը, այսինքն՝ կատարում է խորքային պատճենում։
    #Անկախ նրանից, թե ինչ խորություն կունենա պատճենվող օբյեկտը, միևնույն է, թե օբյեկտի հասցեն, և թե օբյեկտի ներսում
    #գտնվող օբյեկտները կպատճենվեն և հիշողության մեջ կպահվեն լրիվ այլ հասցեում։ 

# shallow copy
ls = [[1],[2],[[[3]]]]
ls2 = ls * 1
print(f"this is ls[0]: {id(ls[0])}")
print(f"this is ls[1]: {id(ls[1])}")
print(f"this is ls[2]: {id(ls[2])}")
print(f"this is ls2[0]: {id(ls2[0])}")
print(f"this is ls: {id(ls)}")
print(f"this is ls2: {id(ls2)}")

# deep copy
import copy
ls3 = copy.deepcopy(ls)
print(f"this is ls3[0]: {id(ls3[0])}")
print(f"this is ls3[1]: {id(ls3[1])}")
print(f"this is ls3[2]: {id(ls3[2])}")
print(f"this is ls3: {id(ls3)}")

