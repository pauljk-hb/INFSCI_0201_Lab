def make_set(data: list) -> list:
    for i in data:
        if data.count(i) > 1:
            data.remove(i)
    return data

def is_set(data: list) -> list:
    if data == None:
        return False
    if len(data) == 0:
        return True
    for i in data:
        if data.count(i) == 1:
            return True
    return False

def union(setA: list, setB: list) -> list:
    if is_set(setA) == False or is_set(setB) == False:
        return []
    return make_set(setA + setB)

def intersection(setA: list, setB: list) -> list:
    if is_set(setA) == False or is_set(setB) == False:
        return []
    return make_set([i for i in setA if i in setB])