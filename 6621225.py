import numpy as np

import numpy as np

matrices = np.array([[[1, 2, 2], [1, 3, 5], [2, 4, 5]],
                    [[1, 3, 5], [2, 4, 5], [1, 3, 2]],
                    [[2, 4, 5], [1, 3, 2], [1, 2, 3]],
                    [[1, 3, 2], [1, 2, 3], [1, 5, 3]]])

for i in range(4):
    evalue, evector = np.linalg.eig(matrices[i])
    print(f"\nEigenvalues and eigenvectors of a{i + 1}:\n")
    print("\nEigenvalues:\n", evalue)
    print("\nEigenvectors:\n", evector)
    print()
