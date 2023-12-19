
number=[]
for i in range(5):
    number.append(int(input()))

hamberger = min(number[0:3])
beverage = min(number[3:5])
set = hamberger + beverage - 50

print(set)

