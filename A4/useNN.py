import math

class Sample:
	
	def __init__(self, inList, label=0):
		self.inList = inList
		self.label = label
		self.index = len(inList)
	
	def __str__(self):
		return '[%s]' % ','.join(map(str, self.inList))
	
class EuclideanSample(Sample):
	def __init__(self, inList):
		Sample.__init__(self, inList)
		
	def distance(self, inList2):
		i = 0
		j = 0
		difference = abs(self.index - inList2.index)
		if difference != 0:
			if self.index < inList2.index :
				while(i < difference):
					self.inList.append(0)
					i = i+1
			else:
				while(i < difference):
					inList2.inList.append(0)
					i=i+1			
		total = 0
		while(j < self.index):
			total = (self.inList[j] - inList2.inList[j]) ** 2 + total	
			j = j + 1
		return '%f' % (math.sqrt(total))	


class TaxicabSample(Sample):
	def __init__(self, inList):
		Sample.__init__(self, inList)
		
	def distance(self, inList2):
		i = 0
		j = 0
		difference = abs(self.index - inList2.index)
		if difference != 0:
			if self.index < inList2.index :
				while(i < difference):
					self.inList.append(0)
					i = i+1
			else:
				while(i < difference):
					inList2.inList.append(0)
					i=i+1
		total = 0
		while(j < self.index):
			total = math.fabs(self.inList[j] - inList2.inList[j]) + total
			j = j + 1
		return '%f' % total		


class MaximumSample(Sample):
	def __init__(self, inList):
		Sample.__init__(self, inList)
	
	def distance(self, inList2):
		i = 0
		j = 0
		difference = abs(self.index - inList2.index)
		if difference != 0:
			if self.index < inList2.index :
				while(i < difference):
					self.inList.append(0)
					i = i+1
			else:
				while(i < difference):
					inList2.inList.append(0)
					i=i+1
		total = []
		
		while(j < self.index):
			total.append(abs(self.inList[j] - inList2.inList[j]))
			j = j+1
		
		return max(total)
	
class Classifier():
	def __init__(self):
		self.inSelf = []
		
	
	def addSample(self, inList):
		self.inSelf.append(inList)
		
	def predictLabel(self, inList2):
		i = 0
		min = None
		distance = None
		currentL = None
		while(i < len(self.inSelf)):
			distance = inList2.distance(self.inSelf[i])
			if min is None:
				min = distance
				currentL = self.inSelf[i].label
			elif min > distance:
				min = distance
				currentL = self.inSelf[i].label
			i = i+1
		return currentL						
			
			
			
			
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