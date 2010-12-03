#!/usr/bin/env python

def determine_from_links(input):
    if (input == []):
        return input
    else:
        return map_function(input[0], input[1])
   
def map_function(key, values):
    return [ [key, v] for v in values ]

    
    
