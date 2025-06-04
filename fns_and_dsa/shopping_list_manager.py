def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

# Prompt for and add an item
        if choice == '1':
            item_to_add = input("Enter the item to add: ").strip()
            if item_to_add:
                shopping_list.append(item_to_add) 
                print(f"{item_to_add} added in your shopping list")
            else:
                print("Item cannot be empty")
        elif choice == '2':
            # Prompt for and remove an item
            if not shopping_list:
                print("Shopping list is empty. Nothing to remove")
            else:
                item_to_remove = input("Enter the item to remove: ").strip()
                if item_to_remove:
                    if item_to_remove in shopping_list:
                        shopping_list.remove(item_to_remove)
                        print(f"{item_to_remove} has ben removed from shoppig list")
                    else:
                        print(f"{item_to_remove} is not in your  shopping list")
                else: 
                    print("Item cannot be empty ")
       
        
        elif choice == '3':
            if shopping_list:
                print("---Your current shopping list---")
                for i , item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("No items in your shopping list")    
    
            
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()