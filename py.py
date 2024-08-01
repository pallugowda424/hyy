import pandas as p
d=p.DataFrame([[2,4,5],[9,8,3],[11,2,1]],columns=["maths","java","python"])
print(d)
c=d.agg(['sum','min','max','count','mean','std','size'])
print()
print(c)