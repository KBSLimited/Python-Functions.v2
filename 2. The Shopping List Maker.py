#Task 1: Write a function that lets the user add items to a list.
def add_items_to_list():
    # Initialize an empty list
    items_list = []
    
    while True:
        # Ask user for input
        item = input("Enter an item to add to the list (or type 'done' to finish): ")
        
        # Check if the user wants to finish
        if item.lower() == 'done':
            break
        
        # Add the item to the list
        items_list.append(item)
    
    # Return the final list of items
    return items_list

# Example of usage:
my_list = add_items_to_list()
print("The final list is:", my_list)

#Task 2: Include a function to remove items from the list.
def add_items_to_list():
    # Initialize an empty list
    items_list = []
    
    while True:
        # Ask user for input
        item = input("Enter an item to add to the list (or type 'done' to finish): ")
        
        # Check if the user wants to finish
        if item.lower() == 'done':
            break
        
        # Add the item to the list
        items_list.append(item)
    
    # Return the final list of items
    return items_list

def remove_items_from_list(items_list):
    while True:
        # Ask user which item to remove
        item = input(f"Current list: {items_list}\nEnter an item to remove from the list (or type 'done' to finish): ")
        
        # Check if the user wants to finish
        if item.lower() == 'done':
            break
        
        # Try to remove the item if it exists in the list
        if item in items_list:
            items_list.remove(item)
            print(f"'{item}' has been removed.")
        else:
            print(f"'{item}' is not in the list.")
    
    # Return the modified list
    return items_list

# Example of usage:
my_list = add_items_to_list()
print("The initial list is:", my_list)

# Remove items from the list
my_list = remove_items_from_list(my_list)
print("The final list is:", my_list)

#Task 3: Add a function that prints out the entire list in a formatted way.
def add_items_to_list():
    # Initialize an empty list
    items_list = []
    
    while True:
        # Ask user for input
        item = input("Enter an item to add to the list (or type 'done' to finish): ")
        
        # Check if the user wants to finish
        if item.lower() == 'done':
            break
        
        # Add the item to the list
        items_list.append(item)
    
    # Return the final list of items
    return items_list

def remove_items_from_list(items_list):
    while True:
        # Ask user which item to remove
        item = input(f"Current list: {items_list}\nEnter an item to remove from the list (or type 'done' to finish): ")
        
        # Check if the user wants to finish
        if item.lower() == 'done':
            break
        
        # Try to remove the item if it exists in the list
        if item in items_list:
            items_list.remove(item)
            print(f"'{item}' has been removed.")
        else:
            print(f"'{item}' is not in the list.")
    
    # Return the modified list
    return items_list

def print_list(items_list):
    # Print the entire list in a formatted way
    if items_list:
        print("\nYour list contains the following items:")
        for index, item in enumerate(items_list, 1):
            print(f"{index}. {item}")
    else:
        print("\nThe list is currently empty.")

# Example of usage:
my_list = add_items_to_list()
print("The initial list is:")
print_list(my_list)

# Remove items from the list
my_list = remove_items_from_list(my_list)
print("The final list is:")