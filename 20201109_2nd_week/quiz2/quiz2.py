def solution(_array):
    _dict = dict()

    for i in _array:
        if i in _dict:
            del _dict[i]
        else:
            _dict[i] = True

    return list(_dict.keys())[0]