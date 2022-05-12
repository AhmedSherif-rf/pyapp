weight = int(input(""))
sum = 0
print ("")
for x in range(weight):
  x, y, z = input("").split()
  x = int(x)
  y = int(y)
  z = int(z)
  if x + z + y >= 2:
    sum += 1
print(sum)
