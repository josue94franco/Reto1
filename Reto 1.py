print ("Programa para calcular la velocidad de la tierra en un punto determinado")

import math
lat = float (input ('Ingresa la latitud "en decimales" '))
t = 24
rt = 6371
v = ((2 * math.pi * rt) * (math.cos(lat))) / t

print ("Tu velocidad es  ", v, "Km/h")






