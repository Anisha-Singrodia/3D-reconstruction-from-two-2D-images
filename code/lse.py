import numpy as np

def least_squares_estimation(X1, X2):
  """ YOUR CODE HERE
  """
  # print("x1 : ", X1)
  # print("x2 : ", X2)
  n = X1.shape[0]
  a = np.zeros((n,9))
  for i in range(n):
    temp_arr = []
    for j in range(3):#p
      for k in range(3):#q
        temp_arr.append(X1[i][j]*X2[i][k])
    a[i] = np.array(temp_arr)
  # print("a : ", a)
  U, S, Vt = np.linalg.svd(a)
  E_ = Vt[:][-1]
  # print("e' : ", E_)
  E = np.zeros((3,3))
  E[:,0] = E_[0:3]
  E[:,1] = E_[3:6]
  E[:,2] = E_[6:9]
  # print("E : ", E)
  U, S, Vt = np.linalg.svd(E)
  E = np.matmul(np.matmul(U, np.diag(np.array([1, 1, 0]))), Vt)
  # print("E : ", E)

  """ END YOUR CODE
  """
  return E
