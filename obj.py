# # class Person:
# #     def __init__(self, name):
# #         self.name = name
# #
# #     def print_name(self):
# #         print(self.name)
# #
# #     def __str__(self):
# #         return 'Person object of {}'.format(self.name)
# #
# #     def __repr__(self):
# #         return self.__str__()
# #
# # chris = Person('Chris')
# # chris = Person('Chris')
# #
# # print([chris])
#
# import bankaccount
#
#
# acc1 = bankaccount.BankAccount(100, 'Katie')
# acc2 = bankaccount.BankAccountSpecial(200, 'Chris')
#
#
# # acc2.withdraw(1010)

"""
Document docstring.
"""

class Card:
    # TODO: fix this
    """
    Docstring.
    """
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


class Deck:
    def __init__(self):
        self.cards = self.create_deck()

    def create+_deck():
        cards = []
        for x in range(52):
            cards.append(Card(1, 1))
        return cards
d = Deck()
print(d.cards)
