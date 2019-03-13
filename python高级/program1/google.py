# Submitter: zhengyix(Xu, Zhengyi)
import prompt 
from goody       import safe_open,irange
from collections import defaultdict # Use defaultdict for prefix and query


def all_prefixes(fq : (str,)) -> {(str,)}:
    return {fq[:i] for i in irange(len(fq))}


def add_query(prefix : {(str,):{(str,)}}, query : {(str,):int}, new_query : (str,)) -> None:
    for n_prefix in all_prefixes(new_query):
        prefix[n_prefix].add(new_query)
    query[new_query] += 1


def read_queries(open_file : open) -> ({(str,):{(str,)}}, {(str,):int}):
    prefix = defaultdict(set)
    query = defaultdict(int)
    for line in open_file:
        add_query(prefix,query,tuple(line.rstrip().split()))
    return (prefix, query)

def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    return ''.join(['  {} -> {}\n'.format(k,d[k]) for k in sorted([k for k in d], key = key, reverse = reverse)])

def top_n(a_prefix : (str,), n : int, prefix : {(str,):{(str,)}}, query : {(str,):int}) -> [(str,)]:
    return sorted([q for q in prefix.get(a_prefix,[])], key = lambda q:-query[q])[:n]

# Script
if __name__ == '__main__':
    # Write script here
    google = safe_open('Enter some full query file', 'r', 'error')
    pq = read_queries(google)
    p = pq[0]
    q = pq[1]
    while True:
        print('Prefix dictionary:\n' + dict_as_str(p, key = lambda obj:(len(obj),obj)))
        print('Query dictionary:\n' + dict_as_str(q, key = lambda obj:(-q[obj],obj)))
        s_prefix = prompt.for_string('Enter some prefix (else quit)')
        if s_prefix == 'quit':
            break
        print('  Top 3 (maybe less) full queries: {}\n'.format(str(top_n(tuple(s_prefix.rstrip().split()), 3 , p, q))))
        f_query = prompt.for_string('Enter some full query (else quit)')
        if f_query == 'quit':
            break
        add_query(p, q, tuple(f_query.rstrip().split()))
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc5.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
