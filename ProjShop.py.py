


# understanding methods in py


items = []


def menu():
    print("1. Add Item")
    print("2. Update Item")
    print("3. Delete Item")
    print("4. View All Item")
    print("5. Exit")
    print()

    choice  = int(input("Enter your choice "))

    if choice == 1:
        # Add item stuff here

        print()
        item = input("Enter item name ")
        
        items.append(item)

        menu()

    elif choice == 2:
        # update stuff here
        print("---------- UPDATE ITEM -------------")
        print()
        item=input(" Enter item name:   ")
        if item in items:
            i=input("Enter New item     ")
            index=items.index(item)
            items.insert(index,i)

            items.remove(item)
            print()
            print(item,"    is updated to:  ",i)
            #print("   ",items)
            
        menu()
        
        
        
        
        
        # take item name input from user
        # check whether its in shop or not
        # if yes then ask for a new name and update item
        # if no then simply print item not in shop





    elif choice == 3:
        # delete item
        print("------------DELETE ITEM------------")
        print()
        item=input(" Enter item name:   ")
        if item in items:
            items.remove(item)
            print()
            print(item,"  is deleted from shop menu")
            print()

            menu()
            
    
    elif choice == 4:
        print("------------------- All Items in the shop --------------")
        for i in items:
            print("     ", i)
        print()
        menu()
    elif choice == 5:
        print("Thanks for visiting. Good Bye!")




print("---------------- WELCOME TO SHOP ------------------")
menu()