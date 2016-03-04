#!/usr/bin/env python
# -*- coding: utf-8 -*-

#source/veiledning: http://codepad.org/cywKyxXO

from PIL import Image

print """
En mann har vaert paa markedet a handlet, og han har behov for aa krysse elva med en kylling, en pose med korn, 
og en rev. Det er kun plass til 2 ting i baaten saa han kan kunne bring en av tinga om gangen.
Dersom reven blir etterlatt med kyllingen alene, saa vil den spise kyllling, og kyllingen alene med korn
fører til at kyllingen vil spise kornposen så game over. Mannen maa tenke seg fram for aa ikke tape en 
eneste ting. æææ


"""

# Solution snatched from the web:
#
# Mannen  tar med seg kylling først til høyre siden av elva, og reiser tilbake alene.
# Han tar da kornposen til høyre siden og tar med seg kyllingen tilbake til venstre siden
# Saa tar han med seg reven til høyre siden og kommer tilbake alene og saa endelig kan han
# ta med seg kyllingen over elva igjen(høyre siden).


# En konfigurasjon er en nested tuple: ((left,right),desc)
# left and right are sets representer "ting" på hver side av elva
# og 'desc' beskriver hvordan denne konfigurasjonen kom til 

mann,kylling,korn,rev=("mann","kylling","korn","rev")
carryables=(kylling,korn,rev,None)

# Ikke tillatte tilstander, game over om det skjer(skjer ikke i koden)
forbiddens=(set((kylling,korn)), set((rev,kylling)))

# return wether a undesirable situation occurs
# TODO: Maybe can rewrite this with any() and all() and listcomps
def mayhem(cfg):
    for shore in cfg[0]:
        if mann not in shore:
            for forbidden in forbiddens:
                if shore.issuperset(forbidden):
                    return True
    return False

# return True when the end condition is reached (when all entities are on the right shore)
def done(cfg):
    left,right=cfg[0]
    return left==set()
    
# Let the mann boat across the river, taking an item with him.
# 'item' can be None is the mann is to take nothing with him.
# Return the new configuration, or None is the crossing can't be performed
# because the item is not on the same shore as the mann
def boat(cfg,item):
    left,right=[set(x) for x in cfg[0]] # make copies, because 'left' and 'right' will be mutated
    # determine on which shore the mann is, and to which shore he will boat
    if mann in left:
        src,dst=left,right
    else:
        src,dst=right,left
    # make sure that if there's an item to carry, it is on the same shore as the mann
    if item and not item in src:
        return None
    # cross the mann and possibly the item
    desc="Mannen reiser over elva  -->" if mann in left else "Mannen reiser tilbake <--"
    src.remove(mann)
    dst.add(mann)
    if item:
        src.remove(item)
        dst.add(item)
        desc+=" med "+item
    else:
        desc+=" alene"
    return ((left,right),desc) # return the resulting configuration

# pretty-print a configuration
def printcfg(cfg,level=0):
    left,right=cfg[0]
    verdict="(Not allowed)" if mayhem(cfg) else "(Ok)"
    print "    "*level,", ".join(left),"  ~~~  ",", ".join(right),cfg[1],verdict

# given a certain configuration, generate the configurations that could result from it
def onegeneration(cfg):
    followups=[]
    for item in carryables:
        followup=boat(cfg,item)
        if not followup: continue
        followups.append(followup)
    return followups

# recursively generate from a given configuration
def generate(cfg,level=0):
    solutionstack.extend([None]*(level-len(solutionstack)+1))
    solutionstack[level]=cfg[1]
    printcfg(cfg,level)
    childs=onegeneration(cfg)
    for child in childs:
        if mayhem(child): # skip configurations which are not allowed
            continue
        if child[0] in previouscfgs: # skip shore configurations which have been seen before
            continue
        previouscfgs.append(child[0])
        generate(child,level+1)
        
 #litt rotete løsning, men bilde som åpnes henviser til de forskjellige tilstandene 
 #etter visse commands
img = Image.open('goose.jpg')
img.show()

# starting configuration
cfg=((set((mann,kylling,korn,rev)), set()),"")

# this records any previously encountered configurations
previouscfgs=[cfg[0]]

# keep a solution stack for later printing
solutionstack=[]

# go!
print "Fremgangsmaate for aa loese problemet:"
generate(cfg)

print "Endelig løsning:"
for step in solutionstack:
    if step:
        print "  ",step
        
        