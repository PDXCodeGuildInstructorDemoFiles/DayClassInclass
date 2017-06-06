# change = float(input('What is the total amount? '))
#
# def change_retrun(ch):
#     total = int(ch * 100)
#     final = {}
#     while total > 0:
#         if total - 25 >= 0:
#             if 'quarters' in final:
#                 final['quarters'] += 1
#             else:
#                 final['quarters'] = 1
#             total -= 25
#         elif total - 10 >= 0:
#             if 'dimes' in final:
#                 final['dimes'] += 1
#             else:
#                 final['dimes'] = 1
#             total -= 10
#         elif total - 5 >= 0:
#             if 'nickles' in final:
#                 final['nickles'] += 1
#             else:
#                 final['nickles'] = 1
#             total -= 5
#         elif total - 1 >= 0:
#             if 'pennies' in final:
#                 final['pennies'] += 1
#             else:
#                 final['pennies'] = 1
#             total -= 1
#     text_return = 'Your change is: '
#     for k, v in final.items():
#         text_return += '{}: {}, '.format(k, v)
#     print(text_return[:-2] + '.')
#
# change_retrun(change)
#
#
#
# from decimal import *
#
# aquarter = Decimal(0.25)
# adime = Decimal(0.10)
# anickel = Decimal(0.05)
# apenny = Decimal(0.01)
#
# amount = Decimal(input("enter amount in dollars: "))
#
# print("This is the amount you entered. ", amount)
#
# def number_of_quarters(change):
#     no_quarters = change // aquarter
#     return no_quarters, change - (no_quarters * aquarter)
#
# def number_of_dimes(change):
#     no_dimes = change // adime
#     return no_dimes, change - (no_dimes * adime)
#
# def number_of_nickels(change):
#     no_nickels = change // anickel
#     return no_nickels, change - (no_nickels * anickel)
#
# def number_of_pennys(change):
#     no_penny = change // apenny
#     return no_penny, change - (no_penny * apenny)
#
# # print(number_of_pennys(Decimal(0.01)))
# while amount > Decimal(0):
#     print(amount)
#     quarters, amount = number_of_quarters(amount)
#     dimes, amount = number_of_dimes(amount)
#     nickels, amount = number_of_nickels(amount)
#     pennies, amount = number_of_pennys(amount)
#
# print("You have {} quarters, {} dimes, {} nickels, and {} pennies.".format(quarters,dimes, nickels, pennies))

#\









