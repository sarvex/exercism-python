import itertools

def combinations(target, size, exclude):
    result = []
    possible = [index for index in
                range(1, int((target ** 2 /size) ** 0.6))
                if index not in exclude]

    if size == 1:
        return [[target]]
    for index in range(len(possible), 0, -1):
        result.extend(
            list(seq)
            for seq in itertools.combinations(possible, index)
            if sum(seq) == target and len(seq) == size
        )
    return result
