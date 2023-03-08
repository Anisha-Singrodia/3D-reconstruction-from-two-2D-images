import numpy as np

def pose_candidates_from_E(E):
  transform_candidates = []
  ##Note: each candidate in the above list should be a dictionary with keys "T", "R"
  """ YOUR CODE HERE
  """
  U, S, Vt = np.linalg.svd(E)
  Rz_pi_by_2 = np.array([[0, -1, 0],[1, 0, 0],[0, 0, 1]])
  Rz_minus_pi_by_2 = np.array([[0, 1, 0],[-1, 0, 0],[0, 0, 1]])
  T = U[:, -1]
  T_minus =  -U[:, -1]
  R1 = np.matmul(U, np.matmul(Rz_pi_by_2.T, Vt))
  R2 = np.matmul(U, np.matmul(Rz_minus_pi_by_2.T, Vt))
  transform_candidates.append({"T":T, "R":R1})
  transform_candidates.append({"T":T, "R":R2})
  transform_candidates.append({"T":T_minus, "R":R1})
  transform_candidates.append({"T":T_minus, "R":R2})
  """ END YOUR CODE
  """
  return transform_candidates