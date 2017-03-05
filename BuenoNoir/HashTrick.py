class hashTrick():
    def __init__(self,dimension,width):
        from random import randint
        self.d = dimension
        self.w = width
        self.p = 2**31 - 1
        self.ranPrimeA = [0] * self.d
        self.ranPrimeA = map(lambda x: randint(1, self.p), self.ranPrimeA)
        self.ranPrimeB = [0] * self.d
        self.ranPrimeB = map(lambda x: randint(1, self.p), self.ranPrimeB)

    def _hash(self,value,i):
        return ((self.ranPrimeA[i] * hash(value) + self.ranPrimeB[i]) % self.p) % self.w


if __name__ == "__main__":
    testnumber = hashTrick(3,10)
    print testnumber._hash('test',0)

    pass