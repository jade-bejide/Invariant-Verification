from multipledispatch import dispatch

@dispatch(int, int, object, int)
def assertInvariant(s, i, invariant, n):
    assert(s == invariant(i, n))

@dispatch(int, int, object, object)
def assertInvariant(s, i, invariant, arr):
    assert(s == invariant(i, arr))

@dispatch(int, int, object, object, int)
def assertInvariant(s, i, invariant, arr, n):
    assert(s == invariant(i, arr, n))

@dispatch(int, int, object)
def assertInvariant(s, i, invariant):
    assert(s == invariant(i))

@dispatch(float, int, object, float)
def assertInvariant(s, i, invariant, n):
    assert(s == invariant(i, n))

@dispatch(float, int, object, object)
def assertInvariant(s, i, invariant, arr):
    assert(s == invariant(i, arr))

@dispatch(float, int, object, object, float)
def assertInvariant(s, i, invariant, arr, n):
    assert(s == invariant(i, arr, n))

@dispatch(float, int, object)
def assertInvariant(s, i, invariant):
    assert(s == invariant(i))

@dispatch(int, object, object)
def assertInvariantBool(n, arr, invariant):
    assert(invariant(n, arr))


