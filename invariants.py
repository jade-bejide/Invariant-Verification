from multipledispatch import dispatch
from typing import List

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


