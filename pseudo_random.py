class PseudoRandom:
    def __call__(self, round=10):
        self.threshold = 1000000000
        return f'{self.rng() / 1000000000:.{round}f}'
    def __init__(self, threshold=9):
        self.threshold = threshold
        self.stored_objects = []

    def rng(self):
        self.threshold += 1
        obj = object()
        lst = list()
        s = str()
        i = int()
        f = float()

        self.stored_objects.extend([obj, lst, s, i, f])

        mix = (
            id(obj) ^
            (id(lst) >> 1) ^
            (id(s) >> 2) ^
            (id(i) >> 3) ^
            (id(f) >> 4)
        )

        mix ^= hash((id(obj), id(lst), id(s), id(i), id(f)))

        if (mix >> 3) & 1:
            mix += 1

        return mix % self.threshold

    def shuffle(self, string):
        new = list(string)
        for i in range(len(new) - 1, 0, -1):
            j = self.rng() % (i + 1)
            new[i], new[j] = new[j], new[i]
        return new
    
    def randint(self, low, high):
        self.threshold = high
        while True:
            res = self.rng()
            if res > low:
                return res
    def randrange(self, low, high):
        self.threshold = high - 1
        while True:
            res = self.rng()
            if res > low:
                return res
    def choice(self, seq):
        self.threshold = len(seq) - 1
        return seq[self.rng()]
