a = int(input('what do you have left in pesos?: '))
b = int(input('what do you have left in soles?: '))
c = int(input('what do you have left in reais?: '))

x = a*0.054
y = b*0.29
z = c*0.18

USD = x+y+z
print(USD)