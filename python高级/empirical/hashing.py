from goody import irange
from performance import Performance

class pset:
    def __init__(self,iterable=[],load_factor_threshold=1):
        self._bins = [[]]
        self._len  = 0      # cache, so don't have to recompute from bins
        self._lft  = load_factor_threshold
        for v in iterable:
            self.add(v)
    
    def __str__(self):
        return str(self._bins)
    
    def __len__(self):
        return self._len  # cached
    
    def __contains__(self,v):
        return v in self._bins[self._bin(v)]

    def add(self,v):
        index = self._bin(v)
        if v in self._bins[index]:
            return
        
        self._len += 1
        self._bins[index].append(v)
        if self._len/len(self._bins) > self._lft:
            self._rehash()
        
    def remove (self,v):
        index = self._bin(v)
        for i in range(len(self._bins[index])):
            if self._bins[index][i] == v:
                del self._bins[index][i]
                self._len -= 1
                return
    
    def __iter__(self):
        return self._gen()
        
    def analyze(self):
        from collections import defaultdict
        d = defaultdict(int)
        for b in self._bins:
            d[len(b)] += 1
        ct = 0
        for c in sorted(d):
            ct += c*d[c]
            print('bins with {c:2} values = {d:9,} for a total of {t:9,} values; cumulative total = {ct:9,}'.format(c=c,d=d[c],t=c*d[c],ct=ct))
#            print('bins with',c,'values = ',d[c],'(for a total of',c*d[c],'words')
    
    def _rehash(self):
        old       = self._bins
        #double the number of bins (to drop the load_factor_threshold
        # rehash old values: len(self._bins) has changed
        self._bins = [[] for i in range(2*len(old))]
        self._len = 0
        for bins in old:
            for v in bins:
                self.add(v)
                
    def _bin(self,v):
        return abs(hash(v))%len(self._bins)
                
    def _gen(self):
        for b in self._bins:
            for v in b:
                yield v
    
    
if __name__ == '__main__':
    import prompt,random,traceback
    
    def build_set(n,m=26):
        s = pset()
        word = list('abcdefghijklmnopqrstuvwxyz'[:m])
        for i in range(n):
            random.shuffle(word)
            s.add(''.join(word))
        return s
    
    def experiment(n,m=26):
        s = build_set(n,m)
        s.analyze()
    
    def check_performance():
        s  = pset()
        def setup(n):
            nonlocal s
            s = build_set(n,26)
                
        def code(n):
            word = list('abcdefghijklmnopqrstuvwxyz')
            for i in range(n):
                random.shuffle(word)
                ''.join(word) in s
            
        for i in irange(0,8):
            n = 1000 * 2**i
            p = Performance(lambda : code(n),lambda : setup(n),20,'Sets via Hash Table')
            p.evaluate()
            p.analyze()
        
    # Try:
    #check_performance()
    #experiment(1000000)
    #s=build_set(100,4) # then
    #for i in s: print(i)
    
    while True:
        try:
            exec(prompt.for_string('Command'))
        except Exception:
            traceback.print_exc()
     

    