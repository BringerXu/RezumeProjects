import random,gc
from stopwatch import Stopwatch
from goody import irange,frange


class Performance:
    def __init__(self,code,setup=lambda:None,times_to_measure=5,title='Generic'):
        self._code             = code
        self._setup            = setup
        self._times            = times_to_measure
        self._evaluate_results = None # yet
        self._title            = title
    
    def evaluate(self,times=None):
        results = []
        s = Stopwatch()
        times = times if times != None else self._times
        for i in range(times):
            self._setup()
            s.reset()
            gc.disable()
            s.start()
            self._code()
            gc.enable()
            results.append(s.read())
        self._evaluate_results = [(min(results),sum(results)/times,max(results))] + [results]
        return self._evaluate_results
    
    def analyze(self,bins=10,title=None):
        if self._evaluate_results == None:
            print('No results from calling evaluate() to analyze')
            return
        
        def print_histogram(bins_dict):
            count = sum(bins_dict.values())
            max_for_scale = max(bins_dict.values())
                
            for k,v in sorted(bins_dict.items()):
                pc = int(v/max_for_scale*50)
                extra = 'A' if k[0] <= avg < k[1] else ''
                print('{bl:.2e}<>{bh:.2e}[{count: 5.1f}%]|{stars}'.format(bl=k[0],bh=k[1],count=v/count*100,stars='*'*pc+extra))

        (mini,avg,maxi),times = self._evaluate_results
        incr = (maxi-mini)/bins
        hist = {(f,f+incr):0 for f in frange(mini,maxi,incr)}
        for t in times:
            for (min_t,max_t) in hist:
                if min_t<= t < max_t:
                    hist[(min_t,max_t)] += 1

        print(title if title != None else self._title)
        print('Analysis of',len(times),'timings')
        print('avg = {avg:.3f}   min = {min:.3f}  max = {max:.3f}  span = {span:.1f}%'.
                format(min=mini,avg=avg,max=maxi,span=(maxi-mini)/avg*100))
        print('\n   Time Ranges    ')   
        print_histogram(hist)    

if __name__ == '__main__':
    from goody import irange
    import random
    
    for i in irange(0,8)  :
        alist = [i for i in range(100000 * 2**i)]
        p = Performance(lambda : alist.sort(), lambda : random.shuffle(alist),10,'Sorting')
        p.evaluate()
        p.analyze()