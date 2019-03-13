from   bag import Bag
import unittest  # use unittest.TestCase
import random    # use random.shuffle,random.randint

#random.shuffle(alist) mutates its alist argument to be a random permutation
#random.randint(1,10)  returns a random number in the range 1-10 inclusive


class Test_Bag(unittest.TestCase):
    def setUp(self):
        self.alist = ['d','a','b','d','c','b','d']
        self.bag = Bag(self.alist)
    
    def test_len(self):
        self.assertEqual(len(self.bag), len(self.alist), 'Initial wrong length')
        for t in range(len(self.alist)):
            i = random.randint(0,len(self.alist) - 1)
            self.alist.pop(i)
            self.bag = Bag(self.alist)
            self.assertEqual(len(self.bag), len(self.alist), 'wrong length')
            
            
    def test_unique(self):
        self.assertEqual(self.bag.unique(), len(set(self.alist)), 'Initial wrong unique')
        for t in range(len(set(self.alist))):
            self.alist.remove(set(self.alist).pop())
            self.bag = Bag(self.alist)
            self.assertEqual(len(set(self.alist)), len(self.bag.counts), 'wrong unique')
    
    def test_contains(self):
        self.assertEqual([set(self.alist)], [self.bag.counts.keys()],'wrong contains')
    
    def test_count(self):
        bd = dict()
        for a in self.alist:
            if bd.get(a,None) != None:
                bd[a]  += 1
            else:
                bd.setdefault(a, 1)
        self.assertTrue(bd == self.bag.counts, 'Initial wrong counts')
        for t in range(len(self.alist)):
            i = random.randint(0,len(self.alist) - 1)
            r = self.alist.pop(i)
            if (bd.get(r)-1) == 0:
                bd.pop(r)
            else:
                bd.update({r:bd.get(r)-1})
            self.bag = Bag(self.alist)
            self.assertTrue(bd == self.bag.counts, 'wrong counts')
           
    def test_equals(self):
        alist = [random.randint(1,10) for t in range(1000)]
        bag1 = Bag(alist)
        random.shuffle(alist)
        bag2 = Bag(alist)
        self.assertTrue(bag1==bag2,'Wrong ==')
        
    def test_add(self):
        alist = [random.randint(1,10) for t in range(1000)]
        bag1 = Bag(alist)
        bag2 = Bag([])
        random.shuffle(alist)
        for a in alist:
            bag2.add(a)
        self.assertTrue(bag1==bag2, 'Wrong add method')
    
    def test_remove(self):
        alist = [random.randint(1,10) for t in range(1000)]
        bag1 = Bag(alist)
        self.assertRaises(ValueError, lambda :bag1.remove(53))
        bag2 = Bag(alist)
        for a in alist:
            bag2.add(a)
        for a in alist:
            bag2.remove(a)
        self.assertTrue(bag1==bag2,'Wrong remove')
        
        
            
            
            
            
            
            
        