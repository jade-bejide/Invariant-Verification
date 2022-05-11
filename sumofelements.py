import invariants

def sumElems(a):
    n = len(a)
    s = a[0]
    for i in range(1, n):
        invariants.assertInvariant(s, i, sumElemsInvariant, a)
        s = s + a[i]
    
    return s

def sumElemsInvariant(i, arr):
    sum_= 0
    for j in range(0, i):
        sum_ += arr[j]

    return sum_

print(sumElems([1,2,3,4,5]))
