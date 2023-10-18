"""
Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).

Examples:

    solution('abc', 'bc') # returns true
    solution('abc', 'd') # returns false
"""


#Create unit test using those cases:
fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)

fixed_tests_False = (
    ( "sumo",    "omo"   ),
    ( "samurai", "ra"    ),
    ( "abc",     "abcd"  ),
    ( "ails",    "fails" ),
    ( "this",    "fails" ),
    ( "spam",    "eggs"  )
)

"""
import unittest
class  Def:
    def __init__(self, fixed_tests_False, fixed_tests_True):
        self.fixed_tests_False = fixed_tests_False
        self.fixed_tests_True = fixed_tests_True




class Exo2Test(unittest.TestCase):
    w = Def(fixed_tests_False, fixed_tests_True)
    def test_text_construction(self):
        for j in range(len(self.w[0])):
            for i in range(len(self.fixed_tests_True[0])):
                 if not self.assertEqual(self.fixed_tests_False[0][i:], self.fixed_tests_False[1]):
                     continue
        print("false test")

"""
def solution(string, ending):
    return string.endswith(ending)

# Unit tests for true cases
for test_case in fixed_tests_True:
    input_string, ending_string = test_case
    assert solution(input_string, ending_string) == True
# Unit tests for false cases
for test_case in fixed_tests_False:
    input_string, ending_string = test_case
    assert solution(input_string, ending_string) == False
