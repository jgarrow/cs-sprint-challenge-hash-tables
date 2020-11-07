def intersection(arrays):
    result = []
    spread_array = []
    cache = {}

    # "spread" arrays into one single array
    for arr in arrays:
        spread_array += arr
    
    for i, num in enumerate(spread_array):
        # for each num, increment cache[num]
        
        cache[num] = 1 if num not in cache else cache[num] + 1

        if cache[num] == len(arrays):
            result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
