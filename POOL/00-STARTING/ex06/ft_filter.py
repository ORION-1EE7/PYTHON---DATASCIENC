

def ft_filter(func, iterable):
    result = []
    for item in iterable:
        if func is None:
            if item:
                result.append(item)
        else:
            if func(item):
                result.append(item)
    return (x for x in result)


