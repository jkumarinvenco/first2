catName = []
while True:
    print("Enter name of cat" +str(len(catName)+1) + " or press enter to exit")
    names = input()
    if names == '':
        break
    catName = catName + [names]
print("the cat names are:")
for allcats in catName:
    print(allcats)

print("enter to search your cat")
catToSearch = input()
if catToSearch not in allcats:
    print(" sorry bhai, no find")
else:
    print("party, found it here")

print("enter to search again")
catToSearch1 = input()
if catToSearch1 in allcats:
    print("party, found again")
else:
    print(" sorry bhai, again")
