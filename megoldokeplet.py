import unittest
import math

def keplet_plusz(a:int, b:int, c:int) -> int:
    return (-b+math.sqrt((b**2)-4*a*c))%2*a

def keplet_minusz(a:int, b:int, c:int) -> int:
    return (-b-math.sqrt((b**2)-4*a*c))%2*a

class TestEgyenlet(unittest.TestCase):
    
    def Test_egy(self):
        fgv = keplet_plusz(2,-2,-2)
        self.assertEqual(fgv,10)
    
    def Test_ketto(self):
        fgv = keplet_minusz(2,-2,-2)
        self.assertEqual(fgv,10)

unittest.main()