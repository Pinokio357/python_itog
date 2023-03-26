import  main


pb = main.PhoneBook("phone_book.txt")


while True:
    print(pb.main_menu())
    lenght_menu = len(pb.main_menu().split("\n")) - 1
    choice = main.get_number("select menu item: ",f"************* it must be digit from 1 to {lenght_menu} *****************")

    match choice:
        case 1:
            print(pb)
        case 2:
            name = input("enter name: ")
            phone = input("enter phone: ")
            comment = input("enter comment: ")
            pb.new_contact(name, phone, comment)
        case 3:
            find = input("enter information of contact: ")
            print(pb.search(find))
        case 4:
            print(pb)
            index = main.get_number("enter number of changing contact: ",f"try again it must be digit from 1 to {len(pb.phone_list)}") - 1
            name = input("enter name or press 'Enter' to leave without changes: ")
            phone = input("enter phone or press 'Enter' to leave without changes: ")
            comment = input("enter comment or press 'Enter' to leave without changes: ")
            pb.change(index, name, phone, comment)
        case 5:
            print(pb)
            index = main.get_number("enter number of deleted contact: ", f"try again it must be digit from 1 to {len(pb.phone_list)}") - 1
            pb.delete(index)
        case 6:
            pb.save()
        case 7:
            break

