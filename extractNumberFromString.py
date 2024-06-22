class Solution:
    def ExtractNumber(self,sentence):
        for i in sorted(sentence.split(), key = lambda x: (len(x), x), reverse=True):
            if i.isnumeric() and '9' not in i:
                return i
        return -1
