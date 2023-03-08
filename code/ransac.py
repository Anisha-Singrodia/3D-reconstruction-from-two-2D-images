from lse import least_squares_estimation
import numpy as np

def ransac_estimator(X1, X2, num_iterations=60000):
    sample_size = 8

    eps = 10**-4

    best_num_inliers = -1
    best_inliers = None
    best_E = None

    for i in range(num_iterations):
        # permuted_indices = np.random.permutation(np.arange(X1.shape[0]))
        permuted_indices = np.random.RandomState(seed=(i*10)).permutation(np.arange(X1.shape[0]))
        sample_indices = permuted_indices[:sample_size]
        test_indices = permuted_indices[sample_size:]

        """ YOUR CODE HERE
        """
        E = least_squares_estimation(X1[sample_indices], X2[sample_indices])
        inliers = sample_indices
        for j in test_indices:
            e3 = np.array([0, 0, 1])
            dist1 = ((np.matmul(X2[j], np.matmul(E, X1[j])))**2)/(np.linalg.norm(np.cross(e3, np.matmul(E, X1[j])))**2)
            dist2 = ((np.matmul(X1[j], np.matmul(E.T, X2[j])))**2)/(np.linalg.norm(np.cross(e3, np.matmul(E.T, X2[j])))**2)
            dist = dist1 + dist2
            if dist<eps:
                inliers = np.append(inliers, [j])

        """ END YOUR CODE
        """
        if inliers.shape[0] > best_num_inliers:
            best_num_inliers = inliers.shape[0]
            best_E = E
            best_inliers = inliers

    return best_E, best_inliers