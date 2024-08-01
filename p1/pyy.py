from matplotlib import pyplot as p
x=[2,4,5,6,8,9,10]
y=[1,5,2,4,6,8,7]
c=['k','b']
p.scatter(x,y,label='value of x y',color='k')
p.xlabel('x')
p.ylabel('y')
p.legend()
p.show()