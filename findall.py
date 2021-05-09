import re

str = '24*89*92*103*2'

m = re.findall('(-?\d+)', str)
# m = re.findall('((-?\d+\.?\d*)[*/](-?\d+\.?\d*))', str)

print(m)