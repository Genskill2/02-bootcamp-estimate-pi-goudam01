import math
import unittest
import random

def wallis(n):
    #First I am assigning pi value as 1
    pi_value=1    
    for i in range (1,n+1):
       #Calculating pi using the Wallis formula 
       pi_value = pi_value * ((4*i*i) / (4*i*i - 1))
    return 2*(pi_value)

def monte_carlo(n):
   #First I am assigning points inside the circle as 0
   p_circle = 0   
   for i in range(n):
        x,y=random.random(),random.random()
        #Calculating the distance between the random point (x,y) and the centre of the cirlce
        d = (((x-0.5)**2)+((y-0.5)**2))**0.5
        if d <= 0.5:
            p_circle = p_circle + 1
   #Calculating the pi value using the monte carlo simulation           
   pi_value = (p_circle/n)*4 
   return pi_value
   


class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
