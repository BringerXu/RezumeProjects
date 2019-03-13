# Submitter: zhengyix(Xu, Zhengyi)
import goody
from collections import defaultdict
from goody import safe_open

def read_voter_preferences(file : open):
    result = dict()
    for i in file: 
       con = i.rstrip().split(';')
       result.update({con[0]:con[1:]})
    return result


def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    return ''.join('  ' + k + ' -> ' + str(d[k]) + '\n' for k in sorted((k for k in d), key = key, reverse=reverse))


def evaluate_ballot(vp : {str:[str]}, cie : {str}) -> {str:int}:
    result = defaultdict(int)
    for k in vp:
        for v in vp[k]:
            if v in cie:
                result[v]+=1
                break
    return dict(result)
        
def remaining_candidates(vd : {str:int}) -> {str}:
    return {c for c in vd if vd[c]!=min(vd[c] for c in vd)}


def run_election(vp_file : open) -> {str}:
    votes = read_voter_preferences(vp_file)
    print('Voter name -> [Preferences]')
    print(dict_as_str(votes))
    rc = {c for c in (list(votes.values())[0])}
    ballot_number = 0
    while len(rc) > 1:
        ballot_number += 1
        solution_turn = evaluate_ballot(votes, rc)
        print('Vote count on ballot #'+str(ballot_number)+': candidates (alphabetically ordered) with remaining candidate set = '+str(rc))
        print(dict_as_str(solution_turn, key = lambda obj:obj))
        print('Vote count on ballot #'+str(ballot_number)+': candidates (numerically ordered) with remaining candidate set = '+str(rc))
        print(dict_as_str(solution_turn, key = lambda obj:solution_turn[obj]))
        rc = remaining_candidates(solution_turn)
    print('Winner is '+str(rc))    
    return rc
  
  
  
  
    
if __name__ == '__main__':
    # Write script here
    object_vote_file = safe_open('Enter some voter preferences file name','r','error')
    run_election(object_vote_file)   
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
