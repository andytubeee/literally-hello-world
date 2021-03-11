import os
import time

from letters.H import writeH
from letters.E import writeE
from letters.L import writeL
from letters.O import writeO
from letters.Space import writeSpace
from letters.W import writeW
from letters.R import writeR
from letters.D import writeD
from letters.Explanation import writeExplanation

fileName = 'printMe'

writeH(fileName)
writeE(fileName)
writeL(fileName)
writeL(fileName)
writeO(fileName)
writeSpace(fileName)
writeW(fileName)
writeO(fileName)
writeR(fileName)
writeL(fileName)
writeD(fileName)
writeExplanation(fileName)

file = open(fileName, 'r')
print(file.readline())
file.close()

if os.path.exists(fileName):
    os.remove(fileName)
