import numpy as np

a = np.array([[-5, -1, 2], [4, 12, -6], [1, 0.5, 3.5]])
b= np.array([1, 4, 16])
x = np.array([0, 0.0002, 0])
tolerance = 1e-6

for j in range(100):
    oldx = x.copy()
    for i in range(3):
        sum_ax = np.dot(a[i, :i], x[:i]) + np.dot(a[i, i+1:], oldx[i+1:])
        x[i] = (b[i] - sum_ax) / a[i, i]
        
    print(f"Iteration {j + 1}:\n", f"x1: {x[0]:.4f}", f"x2: {x[1]:.4f}", f"x3: {x[2]:.4f}")

    if np.linalg.norm(np.abs(x - oldx) < tolerance):
        print(f"\nFinal solution after {j + 1} iteration:\n", f"x1: {x[0]:.4f}", f"x2: {x[1]:.4f}", f"x3: {x[2]:.4f}")
        break