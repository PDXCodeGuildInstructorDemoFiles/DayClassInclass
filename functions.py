def greeting_to_person(n, phone):
    return 'Hello {}, your phone number is {}'.format(n, phone)

name = input('What is your name? ')
phone_number = input('What is your phone number? ')
final = greeting_to_person(name, phone_number)

print(final)
