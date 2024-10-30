def search_common(a,b):
    return list(set(a) & set(b))

print(search_common([1,2,3,4,5],[3,4,5,6,7]))
