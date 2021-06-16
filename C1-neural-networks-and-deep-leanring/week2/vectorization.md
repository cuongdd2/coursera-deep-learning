- numpy.dot(w, x)
- CPU/GPU: SIMD single instruction multiple data
    - parallel calculation
    - hardware / specific function
 - avoid explicit for-loops
 - numpy can support multiple  vectorization methods, such as np.exp, np.dot, np.log, np.sum ...
 - 1/m * np.sum(np.dot(X, dz))
 - reshape(1, 4) -> transform (4,1) to (1,4)
 - Vector.sum(axis = 0) sum by axis


Broadcasting in Python
 - expand single number -> vector
 - vector(3,4) / (1, 4) expand (1, 4) vector....
 - (m, n) */+- (1, n) ->> (m,n)
 - (m, n)      (m, 1) ->> (m, n)
 - np.random.randn(5) -> array (5,)
 - np.random.randn(5, 1) -> vector (5, 1) column vector. vector (1, 5) is row vector
 - a.T -> transpose
 - a.shape -> return (m, n)
 - a.reshape((5,1))

Shift Enter to RUN
