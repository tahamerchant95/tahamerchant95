# can use python debugger to understand the errors better 

import pdb

x= [1,2,3]

y = 2 

z = 10 

print(y+z)
pdb.set_trace()
print(z + x) # when doing this we can see it produced a TypeError 



