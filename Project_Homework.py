# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 22:11:01 2020

@author: okkes
"""

class Student(object):
    def __init__(self,name,surname):
        self.name=name.lower()
        self.surname=surname.lower()
        self.course_list=["Python Programming","Java Programming","Linear Algebra","Physics","Mathematics"]
        self.courses=[]
        self.course=""
        self.grades={}
        self.grade=0
        self.check_login=False




    def login(self):
        for i in range(3):
            name=input("Please enter your name: ")
            surname=input("Please enter your surname: ")
            
            if name.lower()==self.name and surname.lower()==self.surname:
                
                print(f"Welcome {self.name} {self.surname}")
                break
            
            else:
                if i == 3:
                    print("Please try again later...")
                    
  
        
        
    def yourCourses(self):
        print("Courses List: ")
        
        for i in range(len(self.course_list)):
            print(f"{i+1}. {self.course_list[i]} ","\n\n")
            
        course_count=int(input("How many courses will you take?: "))  
        if course_count<3 or course_count>5:
            return "You failed in class! :(( "
        else:
            for i in range(course_count):
                course=input(f"Enter your {i+1}. course name: ")
                self.courses.append(course.title())
                
        print("You take following courses...")        
        for i in range(course_count):
            print(f"{i+1}. {self.courses[i]}")
            
         
            
            
    def examCourse(self):
        print("Your Courses List: ")
        
        for i in range(len(self.courses)):
            print(f"{i+1}. {self.courses[i]}")
            
        print("\n\n")
        
        while True:
            self.course = (input("Enter a course name for exam : ")).title()
            if self.course in self.courses:
                
                midterm=input(int("Please enter your midterm grade: "))
                final=input(int("Please enter your final grade: "))
                project=input(int("Please enter your project grade: "))
                
                self.grades["midterm":midterm,"final":final,"project":project]
                
                self.grade=midterm*0.3 + final*0.5 + project*0.2
                
                if self.grade > 90:
                    print("Your grade is AA...PASSED :)) ")
                
                elif 70 < self.grade <90:
                    print("Your grade is BB...PASSED :)) ")
                    
                elif 50 < self.grade < 70:
                    print("Your grade is CC...PASSED :)) ")
                    
                elif 30 < self.grade < 50:
                    print("Your grade is DD...EHH İŞTE PASSED :)) ")  
                    
                elif self.grade < 30:
                    print("Your grade is FF...FAILURE :(( ") 
                    
                break
                
            else:
                print(f"There is not course {self.course} in your courses...!")
                

#--------------------------------------------------
print("Please Choise...")
print("""
         Choise1:New Student \n
         Choise2:Student Login
         Choise3:Take your courses. (3-5) \n
         Choise4:choise a course for exam \n
         Choise5:Your Exam Results \n
         Choise6:Show Your Grade \n
         Choise7:Exit the system

      """)
while True:
    
    try:
        
        ch=int(input("Enter your choise(1-7): "))
        break
    except:
        print("Please enter integer values between 1-6")
        
if ch==1:
    name=input("Please enter your name: ")
    surname=input("Please enter your surname: ")
    user = Student(name,surname)
    
    
    print("*"*50)
    
elif ch==2:
    try:
        user.login()
        print("*"*50)
        
        if user.check_login == False:
            print("Exiting the system...")
            

    except Exception as inst:
        print("Please register...Enter your name and surname again!!!")
        print("*"*50)
        
        
    
    
elif ch==3:
    
    try:
        if student.check_login == False:
                print("Please create an account or login")
                print("*"*50)
                
        else:
            
            if len(user.courses)!=0:
                print("You have already courses... \n\n")
                print("*"*50)
            else:
                user.yourCourses()
                print("*"*50)
    except Exception as inst:
        print("Please register...Enter your name and surname again!!!")
        print("*"*50)
            
        
        
elif ch==4:
    try:
        if user.check_login == False:
                print("Please create an account or login")
                print("*"*50)
        else:
            
            if len(user.courses)==0:
                print("Please take your courses")
            else:
                user.examCourse()
    except Exception as inst:
        print(inst)
        print("*"*50)
        
elif ch==5:
    try:
        if student.check_login == False:
                print("Please create an account or login")
                print("-"*20)
        else:
        
            if len(user.courses)==0:
                print("Please take your courses \n\n")
        
            elif len(user.grades)==0:
                print("Please enter your exam \n\n")
        
            else:
                for i in user.grades.keys():
                    print(f" {i} : {user.grades[i]} \n\n")
    
    
    except Exception as inst:        
        print(inst)
        print("*"*50)
    
elif ch==6:
    try:
        if student.check_login == False:
                print("Please create an account or login")
                print("-"*20)
        else:
        
            if len(user.courses)==0:
                print("Please take your courses... \n")
            elif len(user.grades)==0:
                print("Please make your exam... \n")
        
            else:
                print(f"Your {user.course} grade : {user.grade} \n\n")
    except Exception as inst:
        print(inst)
        print("*"*50)
        
        
elif ch==7:
    print("Exiting from system... \n")
    

        
        
    
    

 
            
                
        