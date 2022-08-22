# #Compound interest Program
# # R = float(input("INTREST RATE:    ")) #intrest_rate
# # P = float(input("PRINCIPAL AMOUNT:    ")) #principal
# # T = float(input("TIME PERIOD:    ")) #Time Period
# # N = 1.0 #if intrest rate is given per anum
# # compound_interest = float(P*(1 + R/N)^(N*T))
# # print(f"The compound intrest paid will be:  {compound_interest}")

# #Skill-Luck Generator
# import random
# from random import randint

# count = 0
# array = []
# while count < 10:    
#     skill = float(randint(0,100))
#     luck = float(randint(0,100))
#     total = 0.95*skill+0.05*luck

#     print(f"Skill:  {skill},Luck:   {luck}")
#     # print(f"Total:  {total}")
#     #Insert values into an empty array???
#     array.append(total)
#     #Order totals descending then ... what? show luck and skill?
#     count +=1

# print(array)
# array.sort()
# print(array)


def to_camel_case(text):
    i= 0
    for i in text:
        if text[0].isCapitalized() == True:
            text.upper()
            i +=1
        else:
            text.upper()
            i +=1
    return text

to_camel_case("Test data here")