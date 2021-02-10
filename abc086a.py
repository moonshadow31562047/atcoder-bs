s = input()
token = s.split()
b = int(token[0])
c = int(token[1])

ms=b*c
if ms%2==0:
    print('Even')
else:
    print('Odd')