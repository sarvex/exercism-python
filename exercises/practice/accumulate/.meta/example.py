# [collection(x) for x in collection] would be nice but trivial


def accumulate(collection, operation):
    return [operation(ellement) for ellement in collection]
