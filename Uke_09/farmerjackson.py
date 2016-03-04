#!/usr/bin/python
# farmer.py -- Solves the farmer/chicken/grain/fox problem
# Tim Raupach <tim@timq.com>

import random
import copy

# the farmer must transport these objects from the near side of the river
near_objects = ['chicken', 'grain', 'fox']
# pairs of objects that can't be left together
incompatible = [['chicken', 'grain'], ['chicken', 'fox']]

# stores objects on the far side of the river
far_objects = [];
# stores the object in the boat
boat_object = ""

# keep transporting objects until all have been moved
while near_objects != []:
    i = -1
    rem_obj = []
    rem_obj_rev = []

    # pick the first object that can be taken
    while (incompatible.count(rem_obj) > 0 \
           or incompatible.count(rem_obj_rev) > 0 \
           or rem_obj == [] and rem_obj_rev == []) \
           and i < len(near_objects)-1:
        i = i + 1
        rem_obj = near_objects[:i] + near_objects[i+1:]
        rem_obj_rev = copy.copy(rem_obj)
        rem_obj_rev.reverse()

    print "The farmer puts the " + near_objects[i] + " in the boat."
    boat_object = near_objects[i]

    print "The farmer rows to the far side of the river."

    print "The farmer leaves the " + boat_object + \
          " on the far side of the river."

    far_objects.append(boat_object)
    near_objects.remove(boat_object)

    # but will it conflict with anything? Don't bother to check if
    # everything is already moved
    if len(near_objects) != 0:
        for obj in far_objects:
            if incompatible.count([obj, boat_object]) > 0 \
                   or incompatible.count([boat_object, obj]):
                # there is a conflict on the far side!
                # swap the object in the boat for the one that causes a
                # conflict
                print "The farmer puts the " + \
                      obj + " in the boat."
                # put the swapped object back on the near side
                near_objects.append(obj)
                far_objects.remove(obj)
                break

        print "The farmer rows to the near side of the river " + \
              "and unloads everything."

print "The farmer gets out of the boat and is on his way."