import matplotlib.pyplot as plt

# Run C program
with open('output.txt', 'r') as f:
    lines = f.readlines()
values = [float(line) for line in lines]

pointSet = [0.0, 0.02, 0.04, 0.06, 0.1, 0.15, 0.18, 0.2, 0.22, 0.25, 0.3, 0.33, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.73, 0.75, 0.8, 0.83, 0.85, 0.9, 0.95, 0.97, 1.0]

plt.plot(pointSet, values, 'bo-')
plt.xlabel('x')
plt.ylabel('e^x')
plt.title('Exponential Function')
plt.grid()
plt.show()
