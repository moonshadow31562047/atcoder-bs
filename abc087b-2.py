a = int(input())
b = int(input())
c = int(input())
x = int(input())
num_combination = 0
for n500 in range(0,a+1):
    for n100 in range(0,b+1):
        n50 = (x - n500*500 - n100*100)//50
        if n50 <=c and n50>=0:
            num_combination += 1
print(num_combination)