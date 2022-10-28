def input_num(reminder):
    running = True
    num = input(reminder)
    while running:
        try:
            int(num)
            running = False
        except ValueError:
            num = input("[Invalid Input]" + reminder)
    return int(num)

int("sd")

num = input_num("Input the number of experiments\n")
values = []
if int(num) and 10 <= int(num) <= 20:
    for i in range(6):
        value = input_num(f"Input the {i+1} value\n")
        values.append(value)

print(f"average is {round(sum(values)/len(values), 2)}")

