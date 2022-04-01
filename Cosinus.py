import math

intwinkel =0
floatcos =0

while intwinkel <181:
    floatcos = math.cos(math.radians(intwinkel))
    print("Cosinus von", intwinkel, "ist:",floatcos)
    intwinkel +=10
    