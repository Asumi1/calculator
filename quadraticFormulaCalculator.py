import math

a = float(input("Enter a-value: "))
b = float(input("Enter b-value: "))
c = float(input("Enter c-value: "))

discrim = (b * b) - (4 * a * c)
print("Discriminant is " + str(discrim))

if discrim < 0:
  print("No real solutions")

if discrim == 0:
  print("1 real solution")
  print( ( (-b) + math.sqrt(discrim) ) / (2 * a) )

if discrim > 0:
  print("2 real solutions")
  print( ( (-b) + math.sqrt(discrim) ) / (2 * a) )
  print( ( (-b) - math.sqrt(discrim) ) / (2 * a) )