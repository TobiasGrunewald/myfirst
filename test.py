import time

class StringSearch():

	charKeyCount = 0 #tegn i key
	progress = 0 #korrekte tegn i træk, den starter på 1, fordi så kan den bruges som key i "keyDict"
	keyDict = {} #dictonary af key, sorteret efter nummer
	string = "ERROR!"
	key = "!RORRE"

	def getProgress(self):
		return self.progress

	def addProgress(self):
		self.progress = self.progress+1

	def resetProgress(self):
		self.progress = 0

	def Search(self):
		stringList = list(self.string)
		for i in range(len(stringList)):
			key = self.getProgress()+1
			char = stringList[i]
			#print(char)
			if key <= 3 and char == self.keyDict[key]:
				#print("progress made="+str(key)+" at char: "+char)
				self.addProgress()
				if key == self.charKeyCount:
					print("found the key at " +str(i+1-self.charKeyCount))
					return True
			else:
				self.resetProgress()
				#print(self.getProgress())
				#print("resat progress")
		print("wasen't able to found key -_-'")
		return False


	def setKeyDict(self, key): #lav key string om til en dictonary 
		val=0
		for i in list(key):
			val=val+1
			self.keyDict[val] = i
			#print("self.keyDict["+str(val)+"]="+i)

	def __init__(self, string, key): #initialize
		self.string = string
		self.key = key
		print("string = "+string)
		print("key = "+key)

		self.charKeyCount = len(key)
		self.setKeyDict(key)
		self.Search()

StringSearch("thisISnothardtofind", "IS")

time.sleep(500)