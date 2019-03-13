# Submitter: zhengyix(Xu, Zhengyi)
from collections import defaultdict


def err(f : callable, p : float) -> callable:
    def so(x):
        return tuple(sorted((f(x)*(1-p),f(x)*(1+p))))
    return so


def rank(db : {str:{(str,int)}}) -> [str]:
    return sorted([k for k,v in db.items()], key = lambda k : len(db[k]), reverse = True)


def who(db : {str:{(str,int)}}, job: str, min_skill : int) -> [(str,int)]:
    assert type(min_skill)==int and 0<=min_skill<=5
    result = []
    for k in db:
        for l in db[k]:
            if l[0] == job and l[1] >= min_skill:
               result.append((k,l[1]))
    return sorted(result,key=lambda s:(-s[1],s[0])) 
    
def by_job (db : {str:{(str,int)}}) -> {str:{(str,int)}}:
    result = defaultdict(set)
    for k,v in db.items():
        for i in v:
            result[i[0]].add((k,i[1]))
    return result
            

def scramble(l : [str], ordering : str) -> [str]:
    return sorted([ob for ob in l], key = lambda ob : [ordering.index(i) for i in ob])


def longest_match(top : str, bottom : str) -> (int,int):
    def max_same(top_start : int) -> int:
        return len([b for t,b in zip(top[top_start:top_start+len(bottom)],bottom) if b == t])
    return max([(i, max_same(i)) for i in range(len(top))], key = lambda ob: ob[1])


if __name__ == '__main__':
    # This code is useful for debugging your functions, especially
    #   when they raise exceptions: better than using driver.driver().
    # Feel free to add more tests (including tests showing in the bsc.txt file)
    # Use the driver.driver() code only after you have removed anybugs
    #   uncovered by these test cases.
    
    print('Testing err')
    f = err(lambda x : x, .01)
    print(f(-1),f(0),f(1))
    f = err(lambda x : x**2 - 2.5, .1)
    print(f(0),f(2),f(4))
 
 
    print('\nTesting rank')
    db = {'Adam':    {},
          'Betty':   {('Gardening', 2), ('Tutoring', 1), ('Cleaning',3)},
          'Charles': {('Plumbing', 2),  ('Cleaning', 5)},
          'Diane':   {('Laundry', 2),   ('Cleaning', 4), ('Gardening', 3)}}
    print(rank(db))
    db = {'Adam':    {('Cleaning', 4),  ('Tutoring', 2), ('Baking', 1)},
          'Betty':   {('Gardening', 2), ('Tutoring', 1), ('Cleaning',3)},
          'Charles': {('Plumbing', 2),  ('Cleaning', 5)},
          'Diane':   {('Laundry', 2),   ('Cleaning', 4), ('Gardening', 3)}}
    print(rank(db))
 
 
    print('\nTesting who')
    db = {'Adam':    {('Cleaning', 4),  ('Tutoring', 2), ('Baking', 1)},
          'Betty':   {('Gardening', 2), ('Tutoring', 1), ('Cleaning',3)},
          'Charles': {('Plumbing', 2),  ('Cleaning', 5)},
          'Diane':   {('Laundry', 2),   ('Cleaning', 4), ('Gardening', 3)}}
    print(who(db,'Cleaning',4))
    print(who(db,'Gardening',0))
    print(who(db,'Tutoring',3))
    print(who(db,'Gambling',0))
    
    
    print('\nTesting by_jobs')
    db = {'Adam':    {('Cleaning', 4),  ('Tutoring', 2), ('Baking', 1)},
          'Betty':   {('Gardening', 2), ('Tutoring', 1), ('Cleaning',3)},
          'Charles': {('Plumbing', 2),  ('Cleaning', 5)},
          'Diane':   {('Laundry', 2),   ('Cleaning', 4), ('Gardening', 3)}}
    print(by_job(db))
    db = {'Adam':    {},
          'Betty':   {('Cleaning', 4),  ('Tutoring', 2), ('Baking', 1)},
          'Charles': {('Laundry', 2)},
          'Diane':   {('Gardening', 2), ('Tutoring', 1)}}
    print(by_job(db))
    
    
    print('\nTesting scramble')
    print(scramble(['abc', 'bac', 'abb'], 'abc'))
    print(scramble(['abc', 'bac', 'abb'], 'cba'))
    print(scramble(['amobea', 'ambian', 'amount', 'amgen'], 'abcdefghijklmnopqrstuvwxyz'))
    print(scramble(['amobea', 'ambian', 'amount', 'amgen'], 'zyxwvutsrqponmlkjihgfedcba'))
 

    print('\nTesting longest_match')
    print(longest_match('accgt','a'))
    print(longest_match('accgt','ccg'))
    print(longest_match('accgt','at'))
    print(longest_match('accgt','ccgt'))
    print(longest_match('accgt','x'))
 
 
    print('\ndriver testing with batch_self_check:')
    import driver
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()           

