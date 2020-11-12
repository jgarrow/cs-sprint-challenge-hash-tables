def get_indices_of_item_weights(weights, length, limit):
    cache = {}

    if length < 2:
        return None

    for i, el in enumerate(weights):
        if limit - el in cache:
            return (i, cache[limit - el])
        
        if el not in cache:
            cache[el] = i
