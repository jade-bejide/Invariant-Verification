def sumElems(a):
    n = len(a)
    s = a[0]
    for i in range(1, n):
        assertInvariant(s, i, sumElemsInvariant, a)
        s = s + a[i]
        

    return s

def sumElemsInvariant(i, arr):
    sum_= 0
    for j in range(0, i):
        sum_ += arr[j]

    return sum_

def assertInvariant(s, i, invariant, n=None): #n is value or collection
    if n == None: assert(s == invariant(i))
    else: assert(s == invariant(i, n))

print(sumElems([1,2,3,4,5]))
