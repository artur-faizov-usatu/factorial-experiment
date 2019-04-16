

class SetGenerator:

    def __init__(self, n , m, symbols):
        self._symbols = symbols
        self._set = [0] * m
        self._m = m
        self._n = n
    
    def _next(self):
        j = self._m - 1
        while j >=0 and self._set[j] == (self._n - 1):
            j -= 1
        if j < 0:
            return False
        self._set[j] += 1
        if j == self._m - 1:
            return True
        k = j + 1
        while(k < self._m):
            self._set[k] = 0
            k += 1
        return True

    def get_matrix(self):
        matrix = []
        while self._next():
            row = []
            for symb in self._set:
                row.append(self._symbols[symb])
            matrix.append(row)
        return matrix

    def get_next(self):
        res = []
        for symb in self._set:
            res.append(self._symbols[symb])
        if self._next():
            return res
        else:
            print(res)
            return None


class Factor:
    def __init__(self, name, min_val, max_val, var_interval, zero_val):
        self._name = name
        self._min = min_val
        self._max = max_val
        self._interval = var_interval
        self._zero = zero_val

    @property
    def name(self):
        return self._name

    @property
    def min(self):
        return self._min

    @property
    def max(self):
        return self._max

    @property
    def zero(self):
        return self._zero

    @property
    def interval(self):
        return self._interval

    def __repr__(self):
        return "Name: {}, Min: {}, Max: {}, Zero: {}, Interval: {}".format(self.name, self.min,
                                                                           self.max, self.zero, self.interval)
