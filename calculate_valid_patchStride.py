import numpy as np

odd = np.linspace(1, 99, 50)
#print(odd * 2**3)
even = np.linspace(2, 150, 75)
#print(even * 2**3)

altogether = np.linspace(1,150,150)*2**3
for i,potence in enumerate(altogether):
    if (i+1)%10==0:
        print(f"{i+1}:{altogether[i]};")
        continue
    print(f"{i+1}:{altogether[i]};", end="")
for i,potence in enumerate(altogether):
    if (i+1)%10==0:
        print(f"{altogether[i]};")
        continue
    print(f"{altogether[i]};", end="")