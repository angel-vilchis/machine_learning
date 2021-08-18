from math import sqrt

def predict_label(examples, features, k, label_key="is_intrusive"):
    k_nearest_neighbors = find_k_nearest_neighbors(examples, features, k)
    k_nearest_neighbors_labels = [examples[pid][label_key] for pid in k_nearest_neighbors]
    return round(sum(k_nearest_neighbors_labels) / k)


def find_k_nearest_neighbors(examples, features, k):
    distances = {}
    for pid, features_label_map in examples.items():
        curr_features = features_label_map["features"]
        distance = get_euclidean_distance(features, curr_features)
        distances[pid] = distance
    return sorted(distances, key=distances.get)[:k]

def get_euclidean_distance(features, other_features):
    num_features = len(features)
    assert num_features == len(other_features), "Parameters must have same number of features."

    squared_differences = [(features[i]-other_features[i]) ** 2 for i in range(num_features)]

    return sqrt(sum(squared_differences))
