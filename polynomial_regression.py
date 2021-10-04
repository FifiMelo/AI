import numpy as np


class Polynomial:
    def __init__(self,order):
        self.order = order
        self.factors = np.random.uniform(low=-10.0, high=10.0, size=(order + 1))
    
    def get_value(self, x):
        out = 0
        for index, factor in zip(range(self.order + 1), self.factors):
            out += x**index*factor
        return out

    def regrression(value, output):
        pass


my_polynomial = Polynomial(3)

print(my_polynomial.factors)
print(my_polynomial.get_value(10))