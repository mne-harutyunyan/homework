# Python-ում ցիկլային գործողությունների հետ հնարավոր է կիրառել else պայմանական հայտարարությունը։ 
# Բերել օրինակ որտեղ ներկայացված կլինի այդ հայտարարության օգտագործումը և սահմանել,
# թե ինչու է ցանկալի խուսափել նման հայտարարություններից։

def upper1(str):
    for i in str:
        if i.upper() == i:
            return f"The first uppercase letter is {i}"
    else:
        return "there isn't uppercase letter"
str = "hElLo worlD"
print(upper1(str))

#Ցանկալի չէ օգտագործել հայտարարությունը բարդ և ծավալուն խնդիրների դեպքում. else -ը հիմնականում օգտագործվում է
#if պայմանի հետ, և եթե խնդրի մեջ արդեն իսկ օգտագորված լինի մի քանի if ... else հայտարարություն,
# for-ում էլ այն օգտագործելիս կարող է մեզ շփոթության մեջ գցել։

