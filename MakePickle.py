from BackEnd import RegPro
import datetime

userDataBase = RegPro.readPickle("UserDataBase.p")
instructor = RegPro.Instructor("szs0117@auburn.edu", "toor", 1)
userDataBase.addUser(instructor)

classDataBase = RegPro.ClassDataBase()
startDate = datetime.datetime(2020, 5, 20)
endDate = datetime.datetime(2020, 7, 31)
timeSlot1 = RegPro.TimeSlot("Summer", 2020, 800, 930, ['M', 'T', 'W', 'TH', 'F'])
timeSlot2 = RegPro.TimeSlot("Summer", 2020, 945, 1100, ['M','W'])
timeSlot3 = RegPro.TimeSlot("Summer", 2020, 1300, 1400, ['M','W', "F"])
class1 = RegPro.Class(3, startDate, endDate, timeSlot1, 50, [], instructor, 11998, "Intro To Operating Systems")
class2 = RegPro.Class(1, startDate, endDate, timeSlot2, 50, [], instructor, 12539, "Computer Ethics")
class3 = RegPro.Class(3, startDate, endDate, timeSlot3, 50, [], instructor, 13726, "Special Topics")

classDataBase = RegPro.ClassDataBase()
classDataBase.addClass(class1)
classDataBase.addClass(class2)
classDataBase.addClass(class3)

RegPro.writePickle("UserDataBase.p", classDataBase)
RegPro.writePickle("ClassDataBase.p", classDataBase)
