import random

biscuits = []


def addBiscuits():
    biscuits.extend(['Monte Carlo'] * 6)
    biscuits.extend(['Shortbread Cream'] * 6)
    biscuits.extend(['Delta Cream'] * 6)
    biscuits.extend(['Orange Slice'] * 6)
    biscuits.extend(['Kingston'] * 7)


# Add biscuits to packet
biscuits.extend(['Monte Carlo'] * 7)
biscuits.extend(['Shortbread Cream'] * 7)
biscuits.extend(['Delta Cream'] * 6)
biscuits.extend(['Orange Slice'] * 6)
biscuits.extend(['Kingston'] * 5)
print('\nASSORTED CREAMS\n')
choice = random.randint(0, len(biscuits) - 1)
print('Your biscuit is : ', biscuits[choice])
del biscuits[choice]

print(f"the biscuits remaining : {biscuits}")

option = "Y"
while option.capitalize() == "Y":
    option = input("another biscuit? \ny: Yes\nn: No\n")
    if option.capitalize() == "Y":
        choice = random.randint(0, len(biscuits) - 1)
        print('Your biscuit is : ', biscuits[choice])
        del biscuits[choice]
        print(f"left {len(biscuits)}")
        if len(biscuits) == 0:
            addBiscuits()

