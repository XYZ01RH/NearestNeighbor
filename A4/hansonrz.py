import math

class Sample:
	
	def __init__(self, inputList, label=0):
		self.inputList = inputList
		self.label = label
		self.index = len(inputList)
	
	def __str__(self):
		return '[%s]' % ','.join(map(str, self.inputList))
	
class EuclideanSample(Sample):
	def __init__(self, inputList):
		Sample.__init__(self, inputList)
		
	def distance(self, inputList2):
		x = 0
		y = 0
		dif = abs(self.index - inputList2.index)
		if dif != 0:
			if self.index < inputList2.index :
				while(x < dif):
					self.inputList.append(0)
					x = x + 1
			else:
				while(x < dif):
					inputList2.inputList.append(0)
					x = x + 1			
		total = 0
		while(y < self.index):
			total = (self.inputList[y] - inputList2.inputList[y]) ** 2 + total	
			y = y + 1
		return '%f' % (math.sqrt(total))	


class TaxicabSample(Sample):
	def __init__(self, inputList):
		Sample.__init__(self, inputList)
		
	def distance(self, inputList2):
		x = 0
		y = 0
		dif = abs(self.index - inputList2.index)
		if dif != 0:
			if self.index < inputList2.index :
				while(x < dif):
					self.inputList.append(0)
					x = x + 1
			else:
				while(x < dif):
					inputList2.inputList.append(0)
					x = x + 1
		total = 0
		while(y < self.index):
			total = math.fabs(self.inputList[y] - inputList2.inputList[y]) + total
			y = y + 1
		return '%f' % total		


class MaximumSample(Sample):
	def __init__(self, inputList):
		Sample.__init__(self, inputList)
	
	def distance(self, inputList2):
		x = 0
		y = 0
		dif = abs(self.index - inputList2.index)
		if dif != 0:
			if self.index < inputList2.index :
				while(x < dif):
					self.inputList.append(0)
					x = x + 1
			else:
				while(x < dif):
					inputList2.inputList.append(0)
					x = x + 1
		total = []
		
		while(y < self.index):
			total.append(abs(self.inputList[y] - inputList2.inputList[y]))
			y = y + 1
		
		return max(total)
	
class Classifier():
	def __init__(self):
		self.points = []
		
	
	def addSample(self, inputList):
		self.points.append(inputList)
		
	def predictLabel(self, inputList2):
		x = 0
		min = None
		distance = None
		currentLable = None
		while(x < len(self.points)):
			distance = inputList2.distance(self.points[x])
			if min is None:
				min = distance
				currentLable = self.points[x].label
			elif min > distance:
				min = distance
				currentLable = self.points[x].label
			x = x + 1
		return currentLable						
			
			
			
			
cl=Classifier()
cl.addSample(Sample([2, 2, 2, 2, 2],-1))
cl.addSample(Sample([0, 0, 0],1))
cl.addSample(Sample([0, 0, 0, 0],-1))
p=cl.predictLabel(EuclideanSample([-1, -1, -1, -1 ,-1]))
print(p)  #should print 1

cl2=Classifier()
cl2.addSample(Sample([0, 0],["list","number",1]))
cl2.addSample(Sample([2.1, 5.2],["list","number",2]))
p=cl2.predictLabel(EuclideanSample([0, 3.3]))
print(p)  #should print ['list', 'number', 2]
p=cl2.predictLabel(TaxicabSample([0, 3.3]))
print(p)  #should print ['list', 'number', 1]

cl3=Classifier()
cl3.addSample(Sample([3, 1, 1],"a"))
cl3.addSample(Sample([2, 2, 2],"b"))
cl3.addSample(Sample([4, 0, 0],"c"))
p=cl3.predictLabel(EuclideanSample([0, 0, 0]))
print(p)  #should print a
p=cl3.predictLabel(TaxicabSample([0, 0, 0]))
print(p)  #should print c
p=cl3.predictLabel(MaximumSample([0, 0, 0]))
print(p)  #should print b