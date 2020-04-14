class User(object):
	ID #String(user email)
	priorityLevel #int(0-3)

	def __init__(self, ID, Priority):
	#TODO:
	# Set the attributes to their initial values.
	# self.ID = ID
	# self.priorityLevel = priorityLevel

	def getID(self):
		#TODO:
		# return self.ID

	def setID(self, ID):
		#TODO:
		# Set the ID attribute for the user
		# self.ID = ID
		# Return True if ID was set successfully otherwise False

	def getPriority(self):
		#TODO:
		# return self.priorityLevel

	def setPriorityLevel(self, priorityLevel):
		#TODO:
		# Set the PriorityLevel for the user
		# self.priorityLevel = priorityLevel 
		# Return True if priorityLevel was set Successfully Otherwise False

class Student(User):
	schedule #(List of Class objects)
	waitlist #(List of Class objects)
	registrationStatus #(Boolean) set to False initially
	completedClasses #(List of Class objects)
	registeredHours #(int)
	MAX_HOURS = 18

	def __init__(self, ID, Priority):
		#TODO:
		# User.__init__(ID, priorityLevel)

	def addClass(self, newClass):
		#TODO:
		# Append newClass to schedule if newClass.isFull() is False, Student meets all the prereqs for the newClass, registration is open, self.getRegistrationStatus() is True, there are no time slot issues and self.getRegisteredHours() + newClass.getHours() <= MAX_HOURS
		# If above conditions are True, call newClass.addPeople(self) and call self.updateRegisteredHours(newClass, True)
		# Returns True if newClass was added otherwise False

	def removeClass(self, oldClass):
		#TODO:
		# Remove oldClass from schedule if schedule contains oldClass
		# If above condition is True call oldClass.removePerson(self) and self.updateRegisteredHours(oldClass, False)
		# Returns True if oldClass was removed otherwise False

	def joinWaitlist(self, newClass):
		#TODO:
		# Append newClass to self.waitlist if newClass.ifFull() is True, newClass.waitlistIsFull() is False, Student meets all the prereqs for the newClass, registration is open, self.getRegistrationStatus() is True, there are no time slot issues and self.getRegisteredHours() + newClass.getHours() <= MAX_HOURS
		# If above condition is true call newClass.addWaitlistPerson(self)
		# Return True if newClass was added otherwise False

	def leaveWaitlist(self, oldClass):
		#TODO:
		# Remove oldClass from waitlist if waitlist contains oldClass
		# If above condition is True call oldClass.removeWaitlistPerson(self)
		# Returns True if oldClass was removed otherwise False

	def getSchedule(self):
		#TODO:
		# Return self.schedule

	def getWaitlist(self):
		#TODO:
		# Return self.waitlist

	def updateRegistrationStatus(self, newStatus):
		#TODO:
		# Set self.registrationStatus to newStatus

	def getRegistrationStatus(self):
		#TODO:
		# Return self.registrationStatus

	def updateCompletedClasses(self, completedClass):
		#TODO:
		# Append completedClass to self.completedClasses
		# Return True is completedClass was appended to self.completedClass otherwise false

	def getCompletedClasses(self):
		#TODO:
		# Return self.completedClasses

	def updateRegisteredHours(self, newClass, appending):
		#TODO:
		# If appening is True add newClass.getHours() to self.registeredHours otherwise subtract it
		# Return True if self.registeredHours was successfully updated False otherwise

class Administrator(User):

	def __init__(self, ID, priorityLevel):
		#TODO:
		# User.__init__(ID, priorityLevel)

	def openRegistration(self):
		#TODO:
		# For class in ClassDataBase.getClasses() call class.updateRegistrationStatus(True)
		# Send notification email to each user in UserDataBase.getAllUsers()
		# Return True if successful False otherwise

	def closeRegistration(self):
		#TODO:
		# For class in ClassDataBase.getClasses() call class.updateRegistration(False)
		# Send notification email to each user in UserDataBase.getAllUsers()
		# Return True if successful False otherwise

	def changePermissionUser(self, user, newLevel):
		#TODO:
		# Call user.setPriority(newLevel)
		# Return True if successful False otherwise

class Advisor(User):

	def __init__(self, ID, priorityLevel):
		#TODO:
		# User.__init__(ID, priorityLevel)

	def updateStudentRegistrationStatus(self, student, status):
		#TODO:
		# If student is in UserDataBase.getStudents() call student.updateRegistrationStatus(status)
		# Send  an email notification to student
		# Return True if Successful False otherwise

	def adviseStudent(self, student):
		#TODO:
		# If student is in UserDataBase.getStudents() send student an email advising them
		# Return True if successful False otherwise

	def requestPermissions(self, administrator, newPermission):
		#TODO:
		# Send email to administrator requesting newPermission
		# Return True if successful False otherwise

class Instructor(User):

	def __init__(self, ID, priorityLevel):
		#TODO:
		# User.__init__(ID, priorityLevel)

	def allowOverRegistration(student, selectedClass):
		#TODO:
		# If student is in UserDataBase.getStudents(),  selectedClass is in ClassDataBase.getAllClasses() and self is in class.getPeople() call student.addClass(selectedClass)
		# Return True if successful False otherwise

	def requestPermissions(self, administrator, newPermission):
		#TODO:
		# Send email to administrator requesting newPermission
		# Return True if successful False otherwise

class Class(object):
	people #(list of User objects)
	registrationStatus #(boolean) initially set to False
	hours #(int)
	startDate #(python datetime object)
	endDate #(python datetime object)
	timeSlot #(String i.e. “MWF@9AM” or possibly custom timeSlot object that would require another class)
	waitlistPeople #(list of User objects)
	totalSeats #(int) = number of available seats for this class
	preReqs #(list of Class objects) = other classes required to take this class

	def __init__(self, hours, startDate, endDate, timeSlot, totalSeats, preReqs, instructor, registrationStatus=False):
		#TODO:
		# self.hours = hours
		# self.startDate = startDate
		# self.endDate = endDate
		# self.timeSlot = timeSlot
		# self.totalSeats = totalSeats
		# self.preReqs = preReqs
		# self.registraionStatus = registrationStatus

	def isFull(self):
		#TODO:
		# Return True if len(self.people) == self.totalSeats

	def getPeople(self):
		#TODO:
		# Return self.people

	def addPeople(self, user):
		#TODO:
		# If self.isFull is False append user to self.people
		# Return True if successful otherwise False

	def removePeople(self, user):
		#TODO:
		# Remove user from self.people
		# Return True if successful otherwise False

	def updateRegistrationStatus(self, status):
		#TODO:
		# self.registrationStatus = status

	def getHours(self):
		#TODO:
		# Return self.hours

	def getStartDate(self):
		#TODO:
		# Return self.startDate

	def getEndDate(self):
		#TODO:
		# Return self.endDate

	def getTimeSlot(self):
		#TODO:
		# Return self.timeSlot

	def addWaitlistPeople(self, user):
		#TODO:
		# If self.isFull is True and user is not in self.waitlistPeople append user to waitlistPeople
		# Return True if successful False otherWise

	def removeWaitlistPeople(self, user):
		#TODO:
		# If user is in self.waitlistPeople remove user from self.waitlistPeople
		# Return True if successful False otherwise

	def getWatilist(self):
		#TODO:
		# Return self.waitlistPeople

	def getTotalSeats(self):
		#TODO:
		# Return self.totalSeats

	def getPreReqs(self):
		#TODO:
		# Return self.preReqs

class ClassDataBase(object):
	classes #(List of Class objects)

	def __inti__(self, classes):
		#TODO:
		# Self.classes = classes

	def addClass(self, newClass):
		#TODO:
		# If class is not in self.classes append newClass to self.classes
		# Return True if successful False otherwise

	def removeClass(self, oldClass):
		#TODO:
		# Remove oldClass from self.classes
		# Return True if successful False otherwise

	def getAllClasses(self):
		#TODO:
		# Return self.classes

class UserDataBase(object)
	users #(List of User objects)

	def __init__(self, users):
		#TODO:
		# Self.users = users

	def addUser(self, user):
		#TODO:
		# If user is not in self.users append user to self.users
		# Return True if successful False otherwise

	def getAllUsers(self):
		#TODO:
		# Return self.users

	def getAllStudents(self):
		#TODO:
		# Return a list of all of the objects of type Student in self.users
