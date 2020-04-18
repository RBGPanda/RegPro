from BackEnd import RegPro

userDataBase = RegPro.UserDataBase()
student1 = RegPro.Student("mab0183@auburn.edu", "FuckMe", 0)
userDataBase.addUser(student1)

RegPro.writePickle("UserDataBase.p", userDataBase)
