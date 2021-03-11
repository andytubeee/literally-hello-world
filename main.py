import os
import random
import time
from functools import partial

from letters.H import writeH
from letters.E import writeE
from letters.L import writeL
from letters.O import writeO
from letters.Space import writeSpace
from letters.W import writeW
from letters.R import writeR
from letters.D import writeD
from letters.Explanation import writeExplanation
from letters.NewLine import writeNewLine

fileName = 'printMe'
writeFunctions = [
    partial(writeH, fileName),
    partial(writeE, fileName),
    partial(writeL, fileName),
    partial(writeL, fileName),
    partial(writeO, fileName),
    partial(writeSpace, fileName),
    partial(writeW, fileName),
    partial(writeO, fileName),
    partial(writeR, fileName),
    partial(writeL, fileName),
    partial(writeD, fileName),
    partial(writeExplanation, fileName),
]

random.shuffle(writeFunctions)

while randomOrder != correctOrder:
    random.shuffle(randomOrder)
    [callFunc() for callFunc in randomOrder]
    writeNewLine(fileName)
    file = open(fileName, 'r')
    print(file.readline())
    time.sleep(1)


file = open(fileName, 'r')
file.close()
if os.path.exists(fileName):
    os.remove(fileName)
