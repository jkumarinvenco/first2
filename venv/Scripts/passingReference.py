birthdays = {'JK': 'Jan 10', 'Hugo': 'Dec 12', 'Qiang': 'Mar 4', 'Jonathan': 'Feb 24', 'Yujie': 'July 14'}

# while True:
#     print('Enter a name: (blank to quit)')
#     name = input()
#     if name == '':
#         break
#
#     if name in birthdays:
#         print(birthdays[name] + ' is the birthday of ' +name)
#     else:
#         print('I do not have birthday information for ' + name)
#         print('What is their birthday?')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated.')

for k in birthdays.keys():
    print(k)
print()
for v in birthdays.values():
    print(v)
print()
for items in birthdays.items():
    print(items)
print()
print(birthdays.keys())