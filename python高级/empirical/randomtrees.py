import prompt,random,math
from goody import irange
from collections import defaultdict


class TN:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left  = left
        self.right = right


def height(atree):
    if atree == None:
        return -1
    else:
        return 1+ max(height(atree.left),height(atree.right))


def add(atree,value):
    if atree == None:
        return TN(value)
    if value < atree.value:
        atree.left = add(atree.left,value)
        return atree
    elif value > atree.value:
        atree.right = add(atree.right,value)
        return atree
    else:
        return atree  # already in tree


def add_all(atree,values):
    for v in values:
        atree = add(atree,v)
    return atree


def print_histogram(title,bins_dict):
    print(title)
    
    count = sum(bins_dict.values())
    min_bin = min(bins_dict.keys())
    max_bin = max(bins_dict.keys())
    max_for_scale = max(bins_dict.values())
    print('Analysis of {count:,} experiments'.format(count=count))
    
    w_sum = 0
    for i in bins_dict:
        w_sum += i*bins_dict[i]
    avg = w_sum/count
    
    print('\navg = {avg:.1f}  min = {min}  max = {max}\n'.format(avg=avg,min=min_bin,max=max_bin))
    for i in irange(min_bin,max_bin):
        pc = int(bins_dict[i]/max_for_scale*50)
        extra = 'A' if int(avg+.5) == i else ''
        print('{bin:4}[{count: 5.1f}%]|{stars}'.format(bin=i,count=bins_dict[i]/count*100,stars='*'*pc+extra))




experiments = prompt.for_int('Enter # of experiments to perform',default=1000)
size        = prompt.for_int('Enter size of tree for each experiment',default=100)

hist  = defaultdict(int)
alist = [i for i in range(size)]
for exp in range(experiments):
    if exp % (experiments//100) == 0:
        print('Progress: {p:d}%'.format(p =int(exp/(experiments//100))))
    random.shuffle(alist)
    hist[ height(add_all(None,alist)) ] += 1

print_histogram('Binary Search Trees',hist)
print('\nminimum possible height =',math.ceil(math.log2(size)-1),'  maximum possible height =',size-1)

