from cmath import phase
z = complex(input().replace("+ -", '-').replace(" ", ""))
print(abs(z))
print(phase(z))