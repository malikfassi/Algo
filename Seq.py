class Seq:
	def __init__(self):
		self.__grille=[]
		self.__solution=[]

	def __repr__(self):
		return(self.__solution)

	def __appendGrille(self,element):
		self.__grille.append(element)

	def __getLen(self):
		return(len(self.__grille))

	def __getGrille(self):
		return(self.__grille)

	def __getSolution(self):
		return(self.__solution)

	def __appendSolution(self,element):
		self.__solution.append(element)

	def __changeSolution(self,i,j,k,element):
		self.__solution[i][0][j][k]=element

	def __getIndexSolution(self,grille):
		return(self.__solution.index(grille))

	def __trouve(self):
		maxima=[]
		for i in range(self.__getLen()):
			maximum=max(self.__getGrille[i])
			maxima.append((maximum,i))
		maximum,i=max(maxima)
		j=self.__getGrille()[i].index(maximum)
		return(maximum,i,j)

	def __trouveStep(self,extreme):
		steps=[]
		for i in self.__getGrille:
			for j in i:
				if (j not in ["x","-",extreme,"0"]):
					steps.append()

	def __isSolutionFound(self,grille):
		for i in grille:
			if ("x" not in i):
				res=True
			if (res==False):
				break
		return(res)



	def __checkDirections(self,grille):
		if (self.__isSolutionFound(grille)): return
		numeroGrille=self.__getSolution().index(grille)
		del self.__getSolution()[numeroGrille]
		for i in [0,1,-1]:
			for j in [0,1,-1]:
				if (abs(i)!=abs(j)):
					length=self.__getLen()
					departI,departJ=grille[1]
					nextI=departI+i
					nextJ=departJ+j
					grille=grille[0]
					if(0<=nextI<=length and 0<=nextJ<=length and (grille[nextI][nextJ]==str(int(extreme)-1) or grille[nextI][nextJ]=="x")):
						self.__appendSolution((grille,(nextI,nextJ)))
						self.__changeSolution(-1,nextI,nextJ,str(int(extreme)-1))

	def chargerGrille(self,nomDuFichier):
		fichier=open(nomDuFichier+".txt", "r")
		line=fichier.readline()
		while (line!=""):
			self.__appendGrille(line.split(", "))
			line=fichier.readline()
			

	def solutionExiste(self):
		for grille in self.__getSolution():
			if (not(self.__isSolutionFound(grille))): return(False)
		return(True)		

	def trouvePuits(self):
		self.__appendSolution(self.__getGrille(),)
		while(not self.solutionExiste()):
			for grille in self.__getSolution():
				self.__checkDirections(grille)

	def afficheSolution(self):
		for grille in self.__getSolution():
			for line in grille[0]:
				print(line)

if (__name__=="__main__"):
	objects=Seq()
	objects.chargerGrille("grille1")
	objects.trouvePuits()
	objects.afficheSolution()