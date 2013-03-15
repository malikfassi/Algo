class Seq:
	def __init__(self):
		self.__grille=[]
		self.__solution=[]

	def __repr__(self):
		return(self.__solution)

	def __appendGrille(self,element):
		self.__grille.append(element)

	def __getLen(self):
		return(len(self.__grille),len(self.__grille[0]))

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

	def __trouveMax(self):
		maxima=[]
		for i in range(self.__getLen()[0]):
			lineTmp=self.__getGrille()[i][:]
			for j in lineTmp:
				if (j.isalpha()):
					lineTmp[lineTmp.index(j)]="0"
			maximum=max(lineTmp)
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
		res=False
		for i in grille[0]:
			if ("x" not in i):
				res=True
			if (res==False):
				break
		return(res)



	def __checkDirections(self,infoGrille):
		if (self.__isSolutionFound(infoGrille)): return
		nextSolution = []
		for i in [0,1,-1]:
			for j in [0,1,-1]:
				if (abs(i)!=abs(j)):
					lengthI, lengthJ=self.__getLen()
					extreme,departI,departJ=infoGrille[1]
					nextI=departI+i
					nextJ=departJ+j
					grille=[]
					for line in infoGrille[0]:
						grille.append(line[:])
					if(0<=nextI<=lengthI-1 and 0<=nextJ<=lengthJ-1):
						if(grille[nextI][nextJ]==str(int(extreme)-1) or grille[nextI][nextJ]=="x"):
							nextSolution.append((grille,(str(int(extreme)-1),nextI,nextJ)))
							self.__changeSolution(-1,nextI,nextJ,str(int(extreme)-1))
		return nextSolution

	def chargerGrille(self,nomDuFichier):
		fichier=open(nomDuFichier+".txt", "r")
		line=fichier.readline()
		if('\n' in line):
				line = line[:-1]
		while (line!=""):
			if('\n' in line):
				line = line[:-1]
			line=line.split(" , ")
			self.__appendGrille(line)
			line=fichier.readline()

		print(self.__grille)



	def solutionExiste(self):
		for grille in self.__getSolution():
			if (not(self.__isSolutionFound(grille))): return(False)
		return(True)		

	def trouvePuits(self):
		maximum=self.__trouveMax()
		self.__appendSolution((self.__getGrille(),maximum))
		while(not self.solutionExiste()):
			nextStep = None
			for i in self.__solution:
				nextStep.append(self.__checkDirections(i))
			if(nextStep == []):
				break
			else:
				self.__solution, nextStep = nextStep, self.__solution

	def afficheSolution(self):
		for grille in self.__getSolution():
			for line in grille[0]:
				print(line)
			print("-------------------------------------------")

if (__name__=="__main__"):
	objects=Seq()
	objects.chargerGrille("grille2")
	objects.trouvePuits()
	objects.afficheSolution()