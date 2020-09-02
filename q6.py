from functools import reduce

def collapse(L):
    if (isinstance(L,str)):
        return L
    else:
        if len(L) == 1:
            return collapse(L[0])
        return (reduce(lambda x,y: ' '.join([collapse(x),collapse(y)]),L))
