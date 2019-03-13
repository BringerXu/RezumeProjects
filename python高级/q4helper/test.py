def hide(iterable):
    for v in iterable:
        yield v
def windows(iterable,n,m=1):
    p = 0
    all_ = [item for item in iter(iterable)]
    while True:
        result = all_[p*m:p*m+n]
        if len(result) == n:
            yield result
            p += 1
        else:
            raise StopIteration
a = [v for v in windows(hide('abcdefghijk'),4,2)]
print(a)
