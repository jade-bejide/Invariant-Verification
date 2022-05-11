def assertInvariant(s, i, invariant, n=None): #n is value or collection
    if n == None: assert(s == invariant(i))
    else: assert(s == invariant(i, n))

