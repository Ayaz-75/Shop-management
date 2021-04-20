


departs=[]
def menu():
    print("1= Adding Department to university ")
    print("2= Updating Department ")
    print("3= Deleting Department from university ")
    print("4= View All Department of university ")

    choice=int(input("Enter Your choice: "))





    if choice==1:
        print("------Adding department to university------")
        print()
        depart=input("Enter department name: ")
        departs.append(depart)
        print(depart,"is Added to the departments list. ")
        print()

        menu()


    if choice==2:
        print("------Updating department------")
        print()
        depart=input("Enter department name: ")
        if depart in departs:
            d=input("Enter new Department: ")
            index=departs.index(depart)
            departs.insert(index,d)
            departs.remove(depart)
            print()
            print(depart," is updated to: ",d)
            print()

            menu()
















print()
print("------Welcome to the University------")
print()
menu()