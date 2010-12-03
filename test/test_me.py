import unittest

# Test as function
def test_b():
    assert 'b' == 'b'

# Test in class
class TestExampleTwo:
    def test_c(self):
        assert 'c' == 'c'

# Old style unit test
class ExampleTest(unittest.TestCase):
    def test_a(self):
        self.assert_(1 == 1)