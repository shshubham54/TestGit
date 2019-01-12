# a=["first","Code"]
# b={var.lower()[::-1] for var in a}
# c=[var[::-1] for var in a]
# print(b)
# print(c)





# a="amazing"
# b = list(''.join(a))
# print(b)
# c=''.join(char for char in b if char not in "aeiou")
# print(c)





  
# This code picks a random food item:
# from random import choice #DON'T CHANGE!
# food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

# #DON'T CHANGE THIS DICTIONARY EITHER!
# bakery_stock = {
#     "almond croissant" : 12,
#     "toffee cookie": 3,
#     "morning bun": 1,
#     "chocolate chunk cookie": 9,
#     "tea cake": 25
# }
# if food in bakery_stock:
#     a=(bakery_stock[food])
#     b=f" {a} left"
#     print(b)
# else:
#     print("We don't make out")



def single_letter_count(a,b):
    return a.upper().count(b.upper())
print(single_letter_count("Hello World", "h")) # 1
print(single_letter_count("Hello World", "z")) # 0
print(single_letter_count("HelLo World", "l")) # 3