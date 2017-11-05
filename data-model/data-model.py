# some behaviour that i want to implement -> write some __function__ (data model methode)
# comment pattern,
# top level function or top level syntax-> corresponding __

# Pattern
# x + y --> __add__
# init --> __init__
# reprt(x) --> __repr__
# x() --> __call__

class Polynomial:

    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        """
        :return:
        """
        return 'Polynomial(*{!r})'.format(self.coeffs)

    def __add__(self, other):
        return Polynomial(*(x+y for x, y in zip(self.coeffs, other.coeffs)))

    def __sub__(self, other):
        return Polynomial(*(x-y for x, y in zip(self.coeffs,other.coeffs)))

    def __len__(self):
        return len(self.coeffs)

    def __call__(self):
        pass

p1 = Polynomial(1, 2, 3)
p2 = Polynomial(2, 3, 3)

print p1
print p2

print p1+p2
print len(p1)
print p1-p2, p2-p1
