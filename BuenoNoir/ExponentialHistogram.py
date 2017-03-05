class ExponentialHisto():
    def __init__(self,expired_time):
        self.expired = expired_time
        self.buckets = []
        self.backu = 0

    def _add(self,num):
        if not len(self.buckets)==0:
            for i in xrange(len(self.buckets)):
                self.buckets[i][0] -= 1
                if self.buckets[i][0] == 0:
                    self.backu = self.buckets[i][1]
                    self.buckets.pop(i)
        if num == 1:
            self.buckets.insert(0,[self.expired,0])
            # self.buckets[0][1] += 1
            for i in xrange(len(self.buckets)):
                if len(self.buckets) > i+2 and self.buckets[i][1] == self.buckets[i+2][1]:
                    self.merge_buckets(i+2)
                else:
                    break

    def merge_buckets(self,index_a):
        self.buckets[index_a][1] += 1
        # self.buckets[index_a][1] += self.buckets[index_a-1][1]
        self.buckets.pop(index_a-1)



if __name__ == "__main__":

    testExpo = ExponentialHisto(100)
    lis = [1]*30+[0]*10+[1]*110
    for i in lis:
        testExpo._add(i)

    print testExpo.buckets
    print testExpo.backu




