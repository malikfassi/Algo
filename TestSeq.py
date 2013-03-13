import unittest
from Seq import *

class TestSeq(unittest.TestCase):
	
	def setUp(self):
		self.listTest=[]
		self.listTest.append(("grille1.txt",True))		# une solution existe
		self.listTest.append(("grille2.txt",True)) 		# une solution existe
		self.listTest.append(("grille3.txt",False)) 	# aucune solution
	
	def aTest(self,filename,expectedValue):
		S = Seq()
		S.chargerGrille(filename)
		S.trouvePuits()
		self.assertEqual(S.solutionExiste(),expectedValue)
		
	def test_Seq(self):
		for t in self.listTest:
			self.aTest(t[0],t[1]) 
		

if __name__ == '__main__':
	unittest.main()
