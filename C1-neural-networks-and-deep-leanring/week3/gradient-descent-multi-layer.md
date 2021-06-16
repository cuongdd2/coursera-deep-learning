dz2 = A2 - Y
dw2 = 1/m*dz2*A1.T   (A1 is input of layer 2 network)
db2 = 1/m*np.sum(dz2, axis=1, keepdims=True)
dz1 = W2.T . dz2 * dA1
dw1 = 1/m dz1 X.T
db1 = 1/m np.sum(dz1, axis=1, keepdims= True)

dz = da . g'(z)

dw = dz.x
db = dz


back-propagation is the hard part

dz(l-1) = W(l).T . dz(l) * dA(l-1)