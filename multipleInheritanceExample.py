# class A:
#     def __init__(self):
#         self.a = 1

#     def eat(self):
#         print("eat A Class")


# class B:
#     def __init__(self):
#         self.b = 2

#     def eat(self):
#         print("eat B Class")


# class C(A, B):
#     def __init__(self):
#         self.c = 3


# c = C()
# c.eat()


# class A:
#     def __init__(self):
#         print('A')


class B:
    def __init__(self):
        print('B')


class X:
    def __init__(self):
        print('X')


class Forward(B, X):
    def __init__(self):
        super().__init__()


class Backward(X, B):
    def __init__(self):
        super().__init__()


c = Forward()
