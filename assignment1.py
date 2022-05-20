from numpy import *
import numpy as np

'''
we have to find matrix C
(5)(C)=(A^(2))-((5)(B^(2)))
'''

A= matrix('1,3;3,4')
B= matrix('-2,1;-3,2')
D= matrix('5,0;0,5')
C=A@A-5*B@B
C=C/5

print(C)