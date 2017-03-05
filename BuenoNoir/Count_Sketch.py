import HashTrick
from numpy import *

class CountSketch(HashTrick.hashTrick):
    def __init__(self,dimension,width):
        HashTrick.hashTrick.__init__(self,dimension,width)
        self.sketchMod = zeros((dimension,width))

    def addNewSample(self, inputText):
        InputLine = inputText.split(" ")
        for word in InputLine:
            for i in xrange(len(self.sketchMod)):
                self.sketchMod[i][self._hash(word,i)] += 1

    def removeSample(self, inputText):
        InputLine = inputText.split(" ")
        for word in InputLine:
            for i in xrange(len(self.sketchMod)):
                self.sketchMod[i][self._hash(word,i)] -= 1

    def _hash(self,value,i):
        return ((self.ranPrimeA[i] * hash(value) + self.ranPrimeB[i]) % self.p) % self.w

    def GetSketchMod(self,range=None):
        return self.sketchMod if range==None else self.sketchMod[range[0]:range[1]+1][:]

    def CountMinEstimate(self,word):
        freq_estimate = self.sketchMod[0][self._hash(word,0)]
        for i in xrange(self.d):
            if self.sketchMod[i][self._hash(word,i)] < freq_estimate:
                freq_estimate = self.sketchMod[i][self._hash(word,i)]
        return freq_estimate

    def CountMeanEstimate(self,word):
        mean_estimate = 0
        for i in xrange(self.d):
            mean_estimate += self.sketchMod[i][self._hash(word,i)]
        return mean_estimate/self.d