# Gjennom å utøve denne operasjonen, søker datamaskinen gjennom lister for å finne ut hvor lang tid de individuelle maskinene bruker på og komme igjennom de.
# Målet er å finne ut hvor rask hver enkelt maskin kan prossessere elementer gjennom en algoritme.

def search_fast(haystack, needle):
    for item in haystack:
        if item == needle:
            return True
        return False
    
# search_fast søker gjennom mindre lister en search_slow, dette for å gi en kontrast mellom hvordan en PC fungerer ved forskjellige byrder.
# Denne testen blir gjort for å gi en pekepinn på komponentene til maskinen, og hva slags hastighet de kan kjøre python i.    
    
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

# Her printer funksjonen ut en liste over hastighetene maskinen bruker til å kjøre igjennom elementene.

if __name__ == '__main__':
    import timeit
    print("Search_fast took in seconds") 
    print(timeit.timeit("search_fast(haystack, needle)", setup="from __main__ import search_fast, haystack, needle"))
    print("Search_slow took in seconds") 
    print(timeit.timeit("search_slow(haystack, needle)", setup="from __main__ import search_slow, haystack, needle"))
   

