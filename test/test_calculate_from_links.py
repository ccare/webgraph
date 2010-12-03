#!/usr/bin/env python

from webgraph import determine_from_links
    
url_a = 'http://www.example.com/path/to/resource'
url_b = 'http://www.domain.com/abc'
url_c = 'http://www.example.com/another/path'

class TestDetermineFromLinks:
    
    def test_for_empty(self):
        links = determine_from_links([])
        assert links == []
    
    def test_for_single_site(self):
        siteInfo =  [ url_a, [ url_b, url_c ] ]
        links = determine_from_links( [ siteInfo ] )
        
        expected = [
            [ url_b, [ url_a ] ],
            [ url_c, [ url_a ] ]
        ]
        
        assert links == expected
        
