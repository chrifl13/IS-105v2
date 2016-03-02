
def search_fast(haystack, needle):
    for item in haystack:
        if item == needle:
            return True
        return False
    
def search_slow(haystack, needle): 
    return_value = False
    for item in haystack:
        if item == needle:
            return_value = True
            print needle
    return return_value    

haystack = open('komponenter105.txt')
haystack.read()

needle = 'needle'

if __name__ == '__main__':
    import timeit
    print("Search_fast took in seconds") 
    print(timeit.timeit("search_fast(haystack, needle)", setup="from __main__ import search_fast, haystack, needle"))
    print("Search_slow took in seconds") 
    print(timeit.timeit("search_slow(haystack, needle)", setup="from __main__ import search_slow, haystack, needle"))
   

