#import math

from math import sqrt, hypot

print("#"*30)
print("Teorema de Pitagoras")
print("#"*30)
cat_a= int(input("digite el cateteto a: "))
cat_b= int(input("digite el cateteto b: "))
#hypo = math.sqrt(cat_a**2 + cat_b**2)
#hypo = sqrt(cat_a**2 + cat_b**2)
hypo = hypot(cat_a, cat_b)
print("el valor de la hipotesunsa es: ", hypo)
print("-"*30)