count = 0
for n in list(map(int, bin(int(input()))[2:])):
    if n == 1:
        count+=1
print(count)