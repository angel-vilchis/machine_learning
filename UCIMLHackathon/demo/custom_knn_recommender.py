import numpy as np 

IDs = {"Wine": 106,
       "Ecoli": 38,
       "Iris": 51,}

context_distance = np.load(r"C:\Users\Angel\Downloads\MLHackathon\demo\context_distance.npy")
popularity_distance = np.load(r"C:\Users\Angel\Downloads\MLHackathon\demo\popularity_distance.npy")
characteristics_distance = np.load(r"C:\Users\Angel\Downloads\MLHackathon\demo\characteristics_distance.npy")

def knnRecommendation(name, k=3, weights=[1/3] * 3):
    con_weight, pop_weight, char_weight = weights
    distances = (con_weight*context_distance) + (pop_weight*popularity_distance) + (char_weight*characteristics_distance)
    
    output = np.zeros((602, k))
    indices = np.argsort(distances, axis=1)[:,:k+1]
    for row_i in range(indices.shape[0]):
        k_neighbors = indices[row_i, 0:k]
        for col_i in range(indices.shape[1]):
            if indices[row_i][col_i] == row_i:
                k_neighbors = np.delete(indices[row_i], col_i)
                break
        output[row_i] = k_neighbors
    
    return output.astype(int)[IDs[name]]