print("11-2.     20173087 노원진\n")
import matplotlib.pyplot as plt
plt.title('20173087, Noh won jon')
x  = [x for x in range(-20, 20)] 
y1 = [t**2+2*t+1 for t in x]
y2 = [t**2 -20 for t in x]  
y3 = [5*t+5 for t in x] 
plt.plot(x, y1, 'r--', x, y2, 'g^-', x, y3, 'b*:')
plt.axis([-30, 30, -30, 30])
plt.show()