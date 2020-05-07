class Student():
    leave = 8
    pass

parth = Student()

#instamce variable
parth.name = "Parth Patel"
#Access the instance variable
print(parth.name)

#Access the class variable using the object
print(parth.leave)
print(Student.__dict__)
#Access the class variable using the class
print(Student.leave)

#Now change the Parth leave
parth.leave = 15
#now change the Student leave
Student.leave = 22
#Acess the instance variable of parth object using dict
print(Student.__dict__)
print("Parth leave:-",parth.leave)


print(parth.__dict__)
