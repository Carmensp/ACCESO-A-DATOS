import numpy as np

#CÁLCULOS
a1 = np.array([1,2,3,4])
a2 = np.array([5,6,7,8])

print(a1 + a2) 
print(a1**2) #dos asteriscos es una elevación

a3 = np.array([[1,2],[3,4]])
a4 = np.array([[5,6],[7,8]])
print(a3*a4)

a5 = np.array(np.arange(0,100,5))
print(a5)

prueba = np.arange(0,50,5)
subArray = prueba[0:4]
print(subArray)

subArray[:] = 10
print(subArray)
print(prueba)
