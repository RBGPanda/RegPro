import datetime
import sys
import pickle

def writePickle(file, obj):
	pickle.dump(obj, open(file, "wb"))

def readPickle(file):
	return pickle.load(open(file, "rb"))

class User(object):
	ID = None #String(user email)
	password = None
	priorityLevel = None #int(0-3)

	def __init__(self, ID, password, priorityLevel):
		#TODO:
		# Set the attributes to their initial values.
		# self.ID = ID
		# self.priorityLevel = priorityLevel
		self.ID = ID
		self.priorityLevel = priorityLevel
		self.password = password

	def getPassword(self):
		#TODO:
		# return self.ID
		return self.password

	def setPassword(self, ID):
		#TODO:
		# Set the ID attribute for the user
		# self.ID = ID
		# Return True if ID was set successfully otherwise False
		self.password = password
		if(self.password == password):
			return True
		return False

	def getID(self):
		#TODO:
		# return self.ID
		return self.ID

	def setID(self, ID):
		#TODO:
		# Set the ID attribute for the user
		# self.ID = ID
		# Return True if ID was set successfully otherwise False
		self.ID = ID
		if(self.ID == ID):
			return True
		return False

	def getPriority(self):
		#TODO:
		# return self.priorityLevel
		return self.priorityLevel

	def setPriorityLevel(self, priorityLevel):
		#TODO:
		# Set the PriorityLevel for the user
		# self.priorityLevel = priorityLevel 
		# Return True if priorityLevel was set Successfully Otherwise False
		self.priorityLevel = priorityLevel
		if(self.PriorityLevel == priorityLevel):
			return True
		return False

class Student(User):
	schedule = [] #(List of Class objects)
	waitlist = []#(List of Class objects)
	registrationStatus = False #(Boolean) set to False initially
	completedClasses  = []#(List of Class objects)
	registeredHours = 0#(int)
	MAX_HOURS = 18

	def __init__(self, ID, password, priorityLevel):
		#TODO:
		# User.__init__(ID, priorityLevel)
		User.__init__(self, ID, password, priorityLevel)

	def addClass(self, newClass):
		#TODO:
		# Append newClass to schedule if newClass.isFull() is False, Student meets all the prereqs for the newClass, registration is open, self.getRegistrationStatus() is True, there are no time slot issues and self.getRegisteredHours() + newClass.getHours() <= MAX_HOURS
		# If above conditions are True, call newClass.addPeople(self) and call self.updateRegisteredHours(newClass, True)
		# Returns True if newClass was added otherwise False
		isFull = newClass.isFull()
		classRegStatus = newClass.getRegistrationStatus()
		studentRegStatus = self.getRegistrationStatus()
		enoughHours = self.getRegisteredHours() + newClass.getHours() <= MAX_HOURS
		meetsPreReqs = True
		for preReq in newClass.getPreReqs():
			if preReq not in self.getCompletedClasses():
				meetsPreReqs = False
				break

		noTimeConficts = True
		newClassTimeSlot = newClass.getTimeSlot()
		newStartTime = newClassTimeSlot.getStartTime()
		newEndTime = newClassTimeSlot.getEndTime()
		for currentClass in self.getSchedule():
			currClassTimeSlot = currentClass.getTimeSlot()
			sameTerm = currClassTimeSlot.getTerm() == newClassTimeSlot.getTerm()
			sameYear =  currClassTimeSlot.getYear() == newClassTimeSlot.getYear()
			currStartTime = currClassTimeSlot.getStartTime()
			currEndTime = currClassTimeSlot.getEndTime()
			duringSameTime = ((newStartTime >= currStartTime) and (newStartTime <= currEndTime)) and ((newEndTime >= currStartTime) and (newEndTime <= currEndTime))
			onSameDay = False 
			for day in currClassTimeSlot.getDaysOfWeek():
				if day in newClassTimeSlot.getDaysOfWeek():
					onSameDay = True
					break
			if sameTerm and sameYear and duringSameTime and onSameDay:
				noTimeConficts = False
				break

		if not isFull and classRegStatus and studentRegStatus and enoughHours and meetsPreReqs and noTimeConficts:
			newClass.addPeople(self)
			self.updateRegisteredHours(newClass, True)
			self.getSchedule().append(newClass)
			return True
		return False

	def removeClass(self, oldClass):
		#TODO:
		# Remove oldClass from schedule if schedule contains oldClass
		# If above condition is True call oldClass.removePerson(self) and self.updateRegisteredHours(oldClass, False)
		# Returns True if oldClass was removed otherwise False

		if oldClass in self.getSchedule():
			self.getSchedule().remove(oldClass)
			oldClass.removePerson(self)
			self.updateRegisteredHours(oldClass, False)
			return True
		return False

	def joinWaitlist(self, newClass):
		#TODO:
		# Append newClass to self.waitlist if newClass.ifFull() is True, Student meets all the prereqs for the newClass, registration is open, self.getRegistrationStatus() is True, there are no time slot issues and self.getRegisteredHours() + newClass.getHours() <= MAX_HOURS
		# If above condition is true call newClass.addWaitlistPerson(self)
		# Return True if newClass was added otherwise False
		isFull = newClass.isFull()
		classRegStatus = newClass.getRegistrationStatus()
		studentRegStatus = self.getRegistrationStatus()
		enoughHours = self.getRegisteredHours() + newClass.getHours() <= MAX_HOURS
		meetsPreReqs = True
		for preReq in newClass.getPreReqs():
			if preReq not in self.getCompletedClasses():
				meetsPreReqs = False
				break

		noTimeConficts = True
		newClassTimeSlot = newClass.getTimeSlot()
		newStartTime = newClassTimeSlot.getStartTime()
		newEndTime = newClassTimeSlot.getEndTime()
		for currentClass in self.getSchedule():
			currClassTimeSlot = currentClass.getTimeSlot()
			sameTerm = currClassTimeSlot.getTerm() == newClassTimeSlot.getTerm()
			sameYear =  currClassTimeSlot.getYear() == newClassTimeSlot.getYear()
			currStartTime = currClassTimeSlot.getStartTime()
			currEndTime = currClassTimeSlot.getEndTime()
			duringSameTime = ((newStartTime >= currStartTime) and (newStartTime <= currEndTime)) and ((newEndTime >= currStartTime) and (newEndTime <= currEndTime))
			onSameDay = False 
			for day in currClassTimeSlot.getDaysOfWeek():
				if day in newClassTimeSlot.getDaysOfWeek():
					onSameDay = True
					break
			if sameTerm and sameYear and duringSameTime and onSameDay:
				noTimeConficts = False
				break

		if isFull and classRegStatus and studentRegStatus and enoughHours and meetsPreReqs and noTimeConficts:
			newClass.addWaitlistPeople(self)
			self.getWaitlist().append(newClass)
			return True
		return False

	def leaveWaitlist(self, oldClass):
		#TODO:
		# Remove oldClass from waitlist if waitlist contains oldClass
		# If above condition is True call oldClass.removeWaitlistPerson(self)
		# Returns True if oldClass was removed otherwise False
		if oldClass in self.getWaitlist():
			self.getWaitlist().remove(oldClass)
			oldClass.removeWaitlistPeople(self)
			return True
		return False

	def getSchedule(self):
		#TODO:
		# Return self.schedule
		return self.schedule

	def getWaitlist(self):
		#TODO:
		# Return self.waitlist
		return self.waitlist

	def updateRegistrationStatus(self, newStatus):
		#TODO:
		# Set self.registrationStatus to newStatus
		self.registrattionStatus = newStatus
		if self.registrationStatus == newStatus:
			return True
		return False

	def getRegistrationStatus(self):
		#TODO:
		# Return self.registrationStatus
		return self.registrationStatus

	def updateCompletedClasses(self, completedClass):
		#TODO:
		# Append completedClass to self.completedClasses
		# Return True is completedClass was appended to self.completedClass otherwise false
		if completedClass in self.completedClasses:
			return False
		else:
			self.completedClasses.append(completedClass)
			return True

	def getCompletedClasses(self):
		#TODO:
		# Return self.completedClasses
		return self.completedClasses

	def updateRegisteredHours(self, newClass, appending):
		#TODO:
		# If appening is True add newClass.getHours() to self.registeredHours otherwise subtract it
		# Return True if self.registeredHours was successfully updated False otherwise
		if appening:
			self.registeredHours += newClass.getHours()
			return True
		else:
			self.registeredHours -= newClass.getHours()
			return True
		return False

class Administrator(User):

	def __init__(self, ID, password, priorityLevel):
		#TODO:
		# User.__init__(ID, priorityLevel)
		User.__init__(self, ID, password, priorityLevel)

	def openRegistration(self, classDataBase):
		#TODO:
		# For class in classDataBase.getClasses() call class.updateRegistrationStatus(True)
		# Send notification email to each user in UserDataBase.getAllUsers()
		# Return True if successful False otherwise
		for c in classDataBase.getClasses():
			c.updateRegistrationStatus(True)

	def closeRegistration(self):
		#TODO:
		# For class in ClassDataBase.getClasses() call class.updateRegistration(False)
		# Send notification email to each user in UserDataBase.getAllUsers()
		# Return True if successful False otherwise
		for c in classDataBase.getClasses():
			c.updateRegistrationStatus(False)

	def changePermissionUser(self, user, newLevel):
		#TODO:
		# Call user.setPriority(newLevel)
		# Return True if successful False otherwise
		user.setPriorityLevel(newLevel)
		if user.getPriority() == newLevel:
			return True
		return False 

class Advisor(User):

	def __init__(self, ID, password, priorityLevel):
		#TODO:
		# User.__init__(ID, priorityLevel)
		User.__init__(self, ID, password, priorityLevel)

	def updateStudentRegistrationStatus(self, student, status, userDataBase):
		#TODO:
		# If student is in UserDataBase.getStudents() call student.updateRegistrationStatus(status)
		# Send  an email notification to student
		# Return True if Successful False otherwise
		if student in userDataBase.getStudents():
			student.updateRegistrationStatus(status)
			return True
		return False

	def adviseStudent(self, student):
		#TODO:
		# If student is in UserDataBase.getStudents() send student an email advising them
		# Return True if successful False otherwise
		return None

	def requestPermissions(self, administrator, newPermission):
		#TODO:
		# Send email to administrator requesting newPermission
		# Return True if successful False otherwise
		return None

class Instructor(User):

	def __init__(self, ID, password, priorityLevel):
		#TODO:
		# User.__init__(ID, priorityLevel)
		User.__init__(self, ID, password, priorityLevel)

	def allowOverRegistration(student, selectedClass, userDataBase, classDataBase):
		#TODO:
		# If student is in UserDataBase.getStudents(),  selectedClass is in ClassDataBase.getAllClasses() and self is in class.getPeople() call student.addClass(selectedClass)
		# Return True if successful False otherwise
		if student in userDataBase.getStudents() and selectedClass in classDataBase.getAllClasses() and self in selectedClass.getPeople():
			selectedClass.incTotalSeats()
			if student.addClass(selectedClass):
				return True
			selectedClass.decTotalSeats()
			return False

	def requestPermissions(self, administrator, newPermission):
		#TODO:
		# Send email to administrator requesting newPermission
		# Return True if successful False otherwise
		return None

class TimeSlot(object):
	# term #(String) "fall", "spring" or "summer"
	# year #(int) i.e. 2020
	# startTime #(int) military time between 0 and 2400
	# endTime #(int) military time between 0 and 2400
	# daysOfWeek #(list of strings) i.e. ['M', 'T', 'W', 'TH', 'F']

	def __init__(self, term, year,  startTime, endTime, daysOfWeek):
		self.term = term
		self.year = year
		self.startTime = startTime
		self.endTime = endTime
		self.daysOfWeek = daysOfWeek

	def getTerm(self):
		return self.term

	def getYear(self):
		return self.year

	def getStartTime(self):
		return self.startTime

	def getEndTime(self):
		return self.endTime

	def getDaysOfWeek(self):
		return self.daysOfWeek

class Class(object):
	people = [] #(list of User objects)
	registrationStatus = False#(boolean) initially set to False
	hours  = None #(int)
	startDate = None #(python datetime object)
	endDate = None #(python datetime object)
	timeSlot = None #(TimeSlot object)
	waitlistPeople = [] #(list of User objects)
	totalSeats = None #(int) = number of available seats for this class
	preReqs = [] #(list of Class objects) = other classes required to take this class
	crn = None

	def __init__(self, hours, startDate, endDate, timeSlot, totalSeats, preReqs, instructor, crn, registrationStatus=False):
		#TODO:
		# self.hours = hours
		# self.startDate = startDate
		# self.endDate = endDate
		# self.timeSlot = timeSlot
		# self.totalSeats = totalSeats
		# self.preReqs = preReqs
		# self.registraionStatus = registrationStatus
		self.hours = hours
		self.startDate = startDate
		self.endDate = endDate
		self.timeSlot = timeSlot
		self.totalSeats = totalSeats
		self.preReqs = preReqs
		self.registraionStatus = registrationStatus
		self.crn = crn

	def isFull(self):
		#TODO:
		# Return True if len(self.people) == self.totalSeats
		if len(self.people) == self.totalSeats:
			return True
		return False

	def getCRN(self):
		return self.crn

	def getPeople(self):
		#TODO:
		# Return self.people
		return self.people

	def addPeople(self, user):
		#TODO:
		# If self.isFull is False append user to self.people
		# Return True if successful otherwise False
		if self.isFull:
			return False
		else:
			self.people.append(user)

	def removePeople(self, user):
		#TODO:
		# Remove user from self.people
		# Return True if successful otherwise False
		if user in self.people:
			self.people.remove(user)
			return True
		else:
			return False

	def updateRegistrationStatus(self, status):
		#TODO:
		# self.registrationStatus = status
		self.registrationStatus = status
		if self.registrationStatus == status:
			return True
		return False

	def getHours(self):
		#TODO:
		# Return self.hours
		return self.hours

	def getStartDate(self):
		#TODO:
		# Return self.startDate
		return self.startDate

	def getEndDate(self):
		#TODO:
		# Return self.endDate
		return self.endDate

	def getTimeSlot(self):
		#TODO:
		# Return self.timeSlot
		return self.timeSlot

	def addWaitlistPeople(self, user):
		#TODO:
		# If self.isFull is True and user is not in self.waitlistPeople append user to waitlistPeople
		# Return True if successful False otherWise
		if self.isFull and user not in self.waitlistPeople:
			self.waitlistPeople.append(user)
			return True
		else:
			return False

	def removeWaitlistPeople(self, user):
		#TODO:
		# If user is in self.waitlistPeople remove user from self.waitlistPeople
		# Return True if successful False otherwise
		if user in self.waitlistPeople:
			self.waitlistPeople.remove(user)
			return True
		return False

	def getWatilist(self):
		#TODO:
		# Return self.waitlistPeople
		return self.waitlistPeople

	def getTotalSeats(self):
		#TODO:
		# Return self.totalSeats
		return self.totalSeats

	def getPreReqs(self):
		#TODO:
		# Return self.preReqs
		return self.preReqs

	def getRegistrationStatus(self):
		return self.registrattionStatus

	def incTotalSeats(self):
		self.totalSeats = self.totalSeats + 1

	def decTotalSeats(self):
		self.totalSeats = self.totalSeats - 1

class ClassDataBase(object):
	classes = [] #(List of Class objects)

	def __init__(self, classes):
		#TODO:
		# Self.classes = classes
		self.classes = classes

	def addClass(self, newClass):
		#TODO:
		# If class is not in self.classes append newClass to self.classes
		# Return True if successful False otherwise
		if newClass not in self.classes:
			self.classes.append(newClass)
			return True
		return False

	def removeClass(self, oldClass):
		#TODO:
		# Remove oldClass from self.classes
		# Return True if successful False otherwise
		if oldClass in self.classes:
			self.classes.remove(oldClass)
			return True
		return False 

	def getAllClasses(self):
		#TODO:
		# Return self.classes
		return self.classes

class UserDataBase(object):
	users = [] #(List of User objects)

	def __init__(self, users = list()):
		#TODO:
		# Self.users = users
		self.users = users

	def addUser(self, user):
		#TODO:
		# If user is not in self.users append user to self.users
		# Return True if successful False otherwise
		if user not in self.users:
			self.users.append(user)
			return True
		return False

	def getAllUsers(self):
		#TODO:
		# Return self.users
		return self.users

	def getAllStudents(self):
		#TODO:
		# Return a list of all of the objects of type Student in self.users
		studentList = []
		for user in self.users:
			if user.type() is Student:
				studentList.append(user)
		return studentList
