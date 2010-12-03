#!/usr/bin/env python

from webgraph import determine_from_links

class TestDetermineFromLinks:    
    def test_for_empty(self):
        determine_from_links([])

