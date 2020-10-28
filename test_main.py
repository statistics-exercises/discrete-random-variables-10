import scipy.stats as st
import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_xvalues(self) :
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        self.assertTrue( len(this_x)==100, "you have plotted the wrong number of points" )
        for i in range( len(this_x) ) :
            self.assertTrue( np.abs(i + 1 - this_x[i])<1e-7, "one or more of your x-coordinates has the wrong value" )
  
  def test_yvalues(self) : 
      fighand=plt.gca()
      figdat = fighand.get_lines()[0].get_xydata()
      this_x, this_y = zip(*figdat)
      self.assertTrue( len(this_y)==100, "you have plotted the wrong number of points" )
      for i in range( len(this_x) ) :
          self.assertTrue( (this_y[i]-np.floor(this_y[i])) < 1e-7, one of your random variables is not an integer" )
          self.assertTrue( this_y[i]>=kval, "one of your random variables is less than kval, which should not be possible" )
      mean = sum(this_y) / len(this_y) 
      var = (kval*(1-prob)) / (prob*prob) 
      bar = np.sqrt(var/100)*st.norm.ppf( (0.99 + 1) / 2 )
      self.assertTrue( np.fabs( mean - kval/prob )<bar, "you appear to be sampling the wrong distributon" )
