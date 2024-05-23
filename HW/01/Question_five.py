# print("Printing current and previous number sum in a range(10)")
# for i in range(1, 10):
#     print(f"Current Number {i} Previous Number {i-1} Sum: {i + i - 1}")


for i in range(0,10):
    if i == 0:
        print(f"Current Number {i} Previous Number {i} Sum: {i}")
    elif i != 0:
        print(f"Current Number {i} Previous Number {i-1} Sum: {i+i-1}")