#!/usr/bin/env python
# -*- coding: utf-8 -*-

#1.2.4
# a) Vi velger en vanlig representasjon av kortstokk med 52 kort
import itertools, random, unittest

# b) Det er 14 forskjellige av hver type
deck = list(itertools.product(range(1,14),['Spar', 'Hjerte', 'Ruter', 'Kløver']))

#c) Shuffler kortene
random.shuffle(deck)


for i in range(5):
    print(deck[i][0], "av", deck[i][1]) 
    
# d) 