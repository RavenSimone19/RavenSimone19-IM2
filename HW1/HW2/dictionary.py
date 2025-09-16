def dictionary_program():
    my_dict = {}
    matrix_size = 3  

    print(f"Matrix size: {matrix_size}")

    for i in range(matrix_size):
        while True:
            item = input(f"Shopping items{i+1}: ").strip()
            if item:
                my_dict[i] = item
                break
            else:
                print("Please enter a valid shopping item.")

    print(f"\nYou have {len(my_dict)} items in the cart\n")

    while True:
        action = input("What would you like to do [C]hange items [R]emove [D]isplay S[earch] ? ").strip().upper()

        if action == 'D':
            print("Displaying Values")
            print("Key     Value")
            for key, value in my_dict.items():
                print(f"{key}       {value}")

        elif action == 'S':
            search_item = input("Enter item to search: ").strip()
            found = False
            for key, value in my_dict.items():
                if value.lower() == search_item.lower():
                    print(f"Found {value} item")
                    found = True
                    break
            if not found:
                print("Im sorry, not in the cart")

        elif action == 'R':
            key_to_remove = input("Enter key to search: ").strip()
            try:
                key_to_remove = int(key_to_remove)
                if key_to_remove in my_dict:
                    removed_value = my_dict.pop(key_to_remove)
                    print(f"The key {key_to_remove} with value {removed_value} has been deleted")
                else:
                    print("Key not found")
            except ValueError:
                print("Invalid key. Please enter an integer key.")
            except Exception as e:
                print(f"An error occurred: {e}")

        elif action == 'C':
            key_to_change = input("Enter key to search: ").strip()
            try:
                key_to_change = int(key_to_change)
                if key_to_change in my_dict:
                    print(f"Found {my_dict[key_to_change]} item")
                    new_value = input("Enter value: ").strip()
                    my_dict[key_to_change] = new_value
                    print("Item successfully changed")
                else:
                    print("Im sorry, not in the cart")
            except ValueError:
                print("Invalid key. Please enter an integer key.")
            except Exception as e:
                print(f"An error occurred: {e}")

        else:
            print("Bye")
            break

dictionary_program()
