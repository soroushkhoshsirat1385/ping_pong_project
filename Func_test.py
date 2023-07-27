from ping_pong import Plus 
import unittest 
class TestClass (unittest.TestCase) :
    def test1 (self) : 
        self.assertEqual(2 , Plus(1) , "not equal")
if __name__=='__main__' : 
    unittest.main()