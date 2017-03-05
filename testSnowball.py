from nltk.stem.snowball import SnowballStemmer
from ChocoNoir.StemNStpw import CleanStw
import re

# Text = ["7dayslater is an interactive comedy series featuring an ensemble cast of YouTube celebrities Each week the audience writes the brief via social media for an all-new episode featuring a well-known guest-star Seven days later that weeks episode premieres on TV and across multiple platforms",
#         1]
word = ["body",1]

if __name__ == "__main__":
    from BuenoNoir import TextClean
    testproc = TextClean.TextClean(word, 0)
    print testproc.GetLine()
    pass