#MRO - method resolution order
class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B,C):
    pass

print(D.mro()) #gives the MRO of this class


#---------new---------
class X:pass
class Y:pass
class Z:pass
class A(X,Y):pass
class B(Y,Z):pass
class M(B,A,Z): pass

print(M.mro())
# prediction --> [M, B, A, Z, X, Y]
# actual     --> [M, B, A, X, Y, Z] (depth first search)