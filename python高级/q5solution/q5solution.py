def compare(a,b):
    if a == '' and b =='':
        return '='
    elif a == '' and b !='':
        return '<'
    elif a != '' and b == '':
        return '>'
    else:
        if a[0] != b[0]:
            return '<' if a[0] < b[0] else '>'
        else:
            return compare(a[1:],b[1:])
   
def is_sorted(l):
    if len(l) <= 1:
        return True
    else:
        return l[0] < l[1] and is_sorted(l[1:]) 


def merge (l1,l2):
    if l1 == [] and l2 == []:
        return []
    elif l1 == []:
        return l2[:]
    elif l2 == []:
        return l1[:]
    else:
        if l1[0] <= l2[0]:
            return [l1[0]] + merge(l1[1:],l2)
        else:
            return [l2[0]] + merge(l1,l2[1:])


def sort(l):
    if len(l) <= 1:
        return l
    else:
        mid = len(l)//2
        return merge(sort(l[:mid]),sort(l[mid:]))
        # or just return merge(sort(l[:len(l)//2]),sort(l[len(l)//2:]))


def nested_sum(l):
    if l == []:
        return 0
    else:
        if type(l[0]) is not list:
            return l[0] + nested_sum(l[1:])
        else:
            return nested_sum(l[0]) + nested_sum(l[1:])
        # or just return (l[0] if type(l[0]) is int else nested_sum(l[0]))  + nested_sum(l[1:])




if __name__=="__main__":
    import random 
       
    print('\nTesting compare')
    print(compare('',''))
    print(compare('','abc'))
    print(compare('abc',''))
    print(compare('abc','abc'))
    print(compare('bc','abc'))
    print(compare('abc','bc'))
    print(compare('aaaxc','aaabc'))
    print(compare('aaabc','aaaxc'))
   
    
    print('\nTesting is_sorted')
    print(is_sorted([]))
    print(is_sorted([1,2,3,4,5,6,7]))
    print(is_sorted([1,2,3,7,4,5,6]))
    print(is_sorted([1,2,3,4,5,6,5]))
    print(is_sorted([7,6,5,4,3,2,1]))
    
    print('\nTesting merge')
    print(merge([],[]))
    print(merge([],[1,2,3]))
    print(merge([1,2,3],[]))
    print(merge([1,2,3,4],[5,6,7,8]))
    print(merge([5,6,7,8],[1,2,3,4]))
    print(merge([1,3,5,7],[2,4,6,8]))
    print(merge([2,4,6,8],[1,3,5,7]))
    print(merge([1,2,5,7,1],[1,2,6,10,12]))


    print('\nTesting sort')
    print(sort([1,2,3,4,5,6,7]))
    print(sort([7,6,5,4,3,2,1]))
    print(sort([4,5,3,1,2,7,6]))
    print(sort([1,7,2,6,3,5,4]))
    l = list(range(20))  # List of values 0-19
    for i in range(10):  # Sort 10 times
        random.shuffle(l)
        print(sort(l),sep='-->')
    
    
    print('\nTesting nested_sum')
    print(nested_sum([1,2,3,4,5,6,7,8,9,10]))
    print(nested_sum([[1,2,3,4,5],[6,7,8,9,10]]))
    print(nested_sum([[1,[2,3],4,5],[[6,7,8],9,10]]))
    print(nested_sum([[1,[2,3],[[4]],5],[[6,[7,[8]]],[9,10]]]))

    import driver
    print()
    driver.driver()
