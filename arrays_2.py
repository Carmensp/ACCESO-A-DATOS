import numpy as np
#np.array
#np.zeros
#np.eye
#np.arange

a1 = np.array(([5,8,10],[6,3,8],[10,20,30]))
print(a1)
print(a1[1,1])
print(a1[1][1]) #hace lo mismo que lo de arriba
a1[2,1] = 90;
print(a1)

print(a1[:,:])
print(a1[:2,:])
print(a1[:,-1:]) #saca los ultimos números
print(a1[:,:1]) #saca los primeros números
print(a1[:,1:-1]) #saca los números del medio

a2 = np.zeros((5,10))
print(a2)
a2[2] = 15
print(a2)
a2[[0,2,-1]] = 25
print(a2)
print(a2[[4,0,1,0,4]])

print("-------------------")

for fila in a2:
    print(fila)
    
for i,fila in enumerate(a2):
    a2[i] = i
    print(a2)
    
print("-------------------")

una = np.array([1,2])
dos = np.array(([1,2],[3,4]))
tres = np.array(([[1,2],[3,4],[5,6]]))
cuatro = np.array([[[[1,2],[3,4]],[[5,6],[7,8]]],[[[9,10],[11,12]],[[13,14],[15,16]]]])
print(cuatro)
print("-------------------")
tresZeta = np.zeros([2,2,2])
print(tresZeta)

