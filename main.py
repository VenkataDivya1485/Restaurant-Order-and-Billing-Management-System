from restaurant import Restaurant

restaurant = Restaurant()
restaurant.load_menu()

while True:
    print("\n----- RESTAURANT SYSTEM -----")
    print("1. Show Menu")
    print("2. Take Order")
    print("3. Generate Bill")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        restaurant.show_menu()

    elif choice == "2":
        restaurant.take_order()

    elif choice == "3":
        restaurant.generate_customer_bill()

    elif choice == "4":
        print("Thank you! Visit again.")
        break

    else:
        print("Invalid choice. Please try again.")
