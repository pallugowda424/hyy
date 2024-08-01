from matplotlib import pyplot as p
import numpy as n
k=n.random.normal(160,49,67)
p.hist(k,color='b')
p.xlabel("height in cm"),p.ylabel("people")
p.title("height of 160 people")
p.show() 