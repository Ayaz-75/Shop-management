
students=[]
def menu():


    
    print()
    print(" 1= Adding student ")
    print(" 2= Updating student ")
    print(" 3= deleting student ")
    print(" 4= view all students ")
    print(" 5= EXIT ")
    choice=int(input("Enter your choice:  "))




    if choice==1:
        print()
        print("------Adding Student to the class------")
        student=input("Enter Name of student: ")
        students.append(student)
        print("The Students in the class are: ",student)



        menu()

    if choice==2:
        print()
        print("------Updating Student------")
        student=input("Enter Name of student: ")
        if student in students:
            s=input("Update student: ")
            index=students.index(student)
            students.insert(index,s)
            students.remove(student)
            print(student,"is updated to: ",s)


            
        menu()



    if choice==3:
        print()
        print("------Deleting Student------")
        student=input("Enter Student name: ")
        if student in students:
            students.remove(student)
            print("Student data is deleted")
            print()


        menu()



    if choice==4:
        print("------All students in Class------")
        print()
        for i in students:
            print("     ",i)
            print()
            



        menu()





    if choice==5:
        print("Thsnks for visiting good bye.....")








menu()