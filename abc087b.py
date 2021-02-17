a = int(input())
b = int(input())
c = int(input())
x = int(input())
num_combination = 0
for n500 in range(0,a+1):#a>1
    for n100 in range(0,b+1):#b>1
        for n50 in range(0,c+1):#c>1
        #forを使うことで、繰り返しになるから。
            amount = n500*500+n100*100+n50*50
            #print(n500,n100,n50,amount)
            if amount == x:
    #「amount」と、「x」を比較することで、足した部分を活用出来る。
                num_combination += 1

print(num_combination)
#コピペは、エラーが起きるかも知れないから、要注意!