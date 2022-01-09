import math 

x = int(input("First: "))
y = int(input("Second: "))
sum = x + y
entropy = (-(x/sum) * math.log(x/sum,2)) - ((y/sum) * math.log(y/sum,2))

print(entropy)
