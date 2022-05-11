import invariants
from multipledispatch import dispatch

def maxElem(arr):
    n = len(arr)

    if n == 1:
        return arr[0]

    m = arr[0]

    for i in range(1, n):
        invariants.assertInvariant(m, i, maxElemInvariant, arr)
        if m < arr[i]:
            m = arr[i]

    return m

def getYComplementUnordered(arr, arrSet):
    a = []
    for item in arr:
        if item in arrSet:
            a.append(item)

    return a

def max2Elems(arr):
    n = len(arr)

    assert(n >= 2)

    if arr[0] <= arr[1]:
        x = arr[0]
        y = arr[1]
    else:
        x = arr[1]
        y = arr[0]

    for i in range(2, n):
        invariants.assertInvariant(y, i, maxElemInvariant, arr)
        
        invariants.assertInvariant(x, i, maxElemInvariant, arr, y)
        if y < arr[i]:
            x = y
            y = arr[i]
        else:
            if x < arr[i]:
                x = arr[i]


    return (x,y)

@dispatch(int, object)
def maxElemInvariant(i, arr):
    return max(arr[0:i])

@dispatch(int, object, int)
def maxElemInvariant(i, arr, n):
    y_compl = list(set(arr[0:i])-set([n]))
    a = getYComplementUnordered(arr[0:i], y_compl)
    return max(a)

print(max2Elems([1,5,42,-5,6,7,106,2,4,5,8,9]))
