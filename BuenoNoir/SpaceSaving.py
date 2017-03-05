# inputText "7dayslat interact comedi seri featur..." (the Text processing after TextClean)
# nCounter is the number of counter
class SpcSaving():
    def __init__(self,inputText,nCounter):
        self.text = inputText.split(" ")
        self.k = nCounter
        self.TopN = {}

    # Return a dict({word : freq})
    def GetFreqDict(self):
        for word in self.text:
            if not self.TopN.has_key(word):
                if len(self.TopN) < self.k:
                    self.TopN[word] = 1
                else:
                    LeastValueKey = min(self.TopN,key=self.TopN.get)
                    self.TopN[word] = self.TopN.pop(LeastValueKey)
                    self.TopN[word] += 1
            else:
                self.TopN[word] += 1
        # return self.TopN
        return self.TopN

