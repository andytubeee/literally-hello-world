import os
import random
import time
from functools import partial

from letters.EmptyFile import writeEmptyFile
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

if os.path.exists(fileName):
    os.remove(fileName)

writeEmptyFile(fileName)

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

file = open(fileName, 'r')

while str(file.read().split('\n')[-1]) != "Hello World!":
    [callFunc() for callFunc in writeFunctions]
    writeNewLine(fileName)
    print(file.readline())
    random.shuffle(writeFunctions)
    time.sleep(0.5)

file.close()
if os.path.exists(fileName):
    os.remove(fileName)
    
    
    
input("Okay so that's it...")
