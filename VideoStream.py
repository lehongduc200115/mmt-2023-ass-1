FPS = 24
class VideoStream:
	def __init__(self, filename):
		self.filename = filename

		#meta data
		self.totalFrames = self.getTotalFrames()

		try:
			self.file = open(filename, 'rb')
		except:
			raise IOError
		self.frameNum = 0
		
	def nextFrame(self):
		"""Get next frame."""
		data = self.file.read(5) # Get the framelength from the first 5 bits
		if data: 
			framelength = int(data)
							
			# Read the current frame
			data = self.file.read(framelength)
			self.frameNum += 1
		return data
						
	def moveToFrame(self, frameNo):
		"""Move to frame."""
		self.frameNum = 0
		try:
			self.file = open(self.filename, 'rb')
		except:
			raise IOError
		
		for i in range(0, frameNo - 1):
			self.nextFrame()

	def nextFrameTemp(self, temp):
		"""Get next frame."""
		data = temp.read(5) # Get the framelength from the first 5 bits
		if data: 
			framelength = int(data)
							
			# Read the current frame
			data = temp.read(framelength)
			# self.frameNum += 1
		return data

	def frameNbr(self):
		"""Get frame number."""
		return self.frameNum

	def getTotalFrames(self):
		"""Get total number of frames."""
		count = 0
		try:
			temp = open(self.filename, 'rb')
			while self.nextFrameTemp(temp):
				count += 1
		except:
			raise IOError

		# print("total frames: ", count)
		return count

	def backwardByFrame(self, time = 2):
		framesToBeAdded = time * FPS
		frameNum = 1
		if not (self.frameNum - framesToBeAdded < 1):
			frameNum = self.frameNum - framesToBeAdded
		self.moveToFrame(frameNum)
	
	def forwardByFrame(self, time = 2):
		framesToBeAdded = time * FPS
		frameNum = self.totalFrames - 1
		if not (self.frameNum + framesToBeAdded >= self.totalFrames):
			frameNum = self.frameNum + framesToBeAdded

		self.moveToFrame(frameNum)

		# print("forwardByFrame: " + str(self.frameNum) + ", " + str(self.totalFrames))