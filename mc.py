import random

class Markov:
    def __init__(self, txt):
        self.table = get_table(txt)

    def predict(self, txt):
        d = self.table.get(txt, {})
        if not d:
            raise KeyError('{} not found'.format(txt))
        l = []
        for k,v in d.items():
            for i in range(v):
                l.append(k)
        return random.choice(l)


def get_table(txt):
    d = {}
    for i in range(len(txt)):
        c = txt[i]
        try:
            c2 = txt[i+1]
        except IndexError:
            break
        if c in d:
            d2 = d[c]
        else:
            d2 = {}
        if c2 not in d2:
            d2[c2] = 0
        d2[c2] += 1
        d[c] = d2
    return d

