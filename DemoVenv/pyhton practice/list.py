list1 = [1,2,3]
choice = 0
while True:
    print("Menu:")
    print("1. Append an element.")
    print("2. Insert an element.")
    print("3. Append a list to given list.")
    print("4. Modify an exesting element.")
    print("5. Delete an exesting from its position.")
    print("6. Delete an exesting ith a given value.")
    print("7. Sort the list in ascending order.")
    print("8. Sort the list in decending order")
    print("9. Display List.")
    print("10. Exit")
    choice = int(input("Enter your choice: "))

    if choice==1:
        ele=int(input("Enter Element to append: "))
        list1.append(ele)
        print("Element appended")

    elif choice==2:
        ele=int(input("Enter Element to insert: "))
        pos=int(input("Enter postion to insert: "))
        list1.insert(pos,ele)
        print("Element inserted")

    elif choice ==3:
        lis=input("Enter element ith space for the list: ").split()
        list1.extend(lis)
        print("List appended")

    elif choice==4:
        ele=int(input("Enter Element to change: "))
        pos=int(input("Enter postion to change: "))
        list1[pos]=ele
        print("Elemet modified")

    elif choice ==5:
        pos=int(input("Enter postion to delete: "))
        del list1[pos]
        print("Element deleted")
    
    elif choice == 6:
        ele=int(input("Enter Element to delete: "))
        list1.remove(ele)
        print("Element deleted")
    
    elif choice == 7:
        list1.sort()
        print("List Sorted")

    elif choice == 8:
        list1.sort(reverse=True)
        print("List Sorted")

    elif choice == 9:
        print(list1)

    elif choice == 10:
        break

    else:
        print("Invalid Option")