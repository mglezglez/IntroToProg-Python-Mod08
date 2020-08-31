# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Mercedes Gonzalez Gonzalez,8.30.2020,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

import pickle

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Mercedes Gonzalez Gonzalez,8.30.2020,Modified code to complete assignment 8
    """

    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

    @property
    def product_name(self):
        return self.__product_name

    @product_name.setter
    def product_name(self, value):
        if not value.isnumeric():
            self.__product_name = value.strip().upper()
        else:
            raise Exception("Error Detected: product name cannot be a number")

    @property
    def product_price(self):
        return self.__product_price

    @product_price.setter
    def product_price(self, value):
        if isinstance(value, float):
            self.__product_price = value
        else:
            raise Exception("Error Detected: product price must be a float number")

    def __str__(self):
        return "Product Name: {}, Price: ${}".format(self.product_name, str(self.product_price))


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Mercedes Gonzalez Gonzalez,8.30.2020,Modified code to complete assignment 8
    """

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """ Serialize a list of product objects to a file using Python Pickle module
        :param file_name: (string) with name of file:
        :param list_of_product_objects: (list) of product objects containing product data:
        :return: (tuple of boolean, string) indicating whether data was successfully serialized (True)
        or not (False)
        """
        with open(file_name, "wb") as fh:
            try:
                pickle.dump(list_of_product_objects, fh)
                return True, 'Success'
            except pickle.PicklingError as e:
                error_message = """Error detected while trying to pickle object to file {}. Object is not pickable.
                Make sure it does not contain any non-pickable object such as: generators, inner classes, nested 
                functions, lambda functions, defaultdicts, database connections, network sockets or running 
                threads. \nException occurred {}""".format(file_name, e)
                return False, error_message

    @staticmethod
    def read_data_from_file(file_name):
        """  Read data from a file into a list of product objects using Python Pickle module
        :param file_name: (string) with name of file:
        :return: (list) of product objects
        """
        list_of_product_objects = []
        try:
            with open(file_name, "rb") as fh:
                try:
                    list_of_product_objects = pickle.load(fh)
                    message = "Data was successfully deserialized and loaded into a list of product objects in memory!"
                    return list_of_product_objects, message
                except pickle.UnpicklingError:
                    error_message = """Error detected while trying to unpickle an object from file {}.
                    This could be due to the file might be corrupted, the file may contain non-serialized data
                    or an access violation. Initializing list of customers with empty list. """.format(file_name)
                    return list_of_product_objects, error_message
        except FileNotFoundError:
            error_message = """Filename {} does not exist in the filesystem.
            Initializing list of customers with empty list""".format(file_name)
            return list_of_product_objects, error_message


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output operations with products"""

    @staticmethod
    def print_menu():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print("""
            Menu of Options
            1) Add a new Product
            2) Remove an existing Product
            3) Save Products List to File        
            4) Reload Products List from File
            5) Exit Program
            """)
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_products_in_list(list_of_product_objects):
        """ Shows the current products in the list

        :param list_of_product_objects: (list) of product objects you want to display
        :return: nothing
        """
        print("******* The current products are: *******")
        for product in list_of_product_objects:
            print(product)
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def add_new_product(list_of_product_objects):
        """ Adds a new product to the list of product objects
        :param list_of_product_objects:  Original list of product objects before adding the new product
        :return: list_of_product_objects - New list of product objects after adding the new product
        """
        product_name = input("Please enter a new product name: ")
        try:
            product_price = float(input("Please enter a new product price: $"))
        except ValueError as e:
            error_message = """The product price you provided is not a valid number. This product will 
            not be added at this time. Exception occurred: {}""".format(e)
            return list_of_product_objects, error_message
        try:
            list_of_product_objects.append(Product(product_name, product_price))
        except Exception as e:
            error_message = "An error occurred while trying to add a new product to the list: {}".format(e)
            return list_of_product_objects, error_message

        return list_of_product_objects, "Success"

    @staticmethod
    def remove_product(list_of_product_objects):
        """ Removes an existing product from the list of product objects
        :param list_of_product_objects:  Original list of product objects before removing any product
        :return: list_of_product_objects - New list of product objects after removing the selected product
        """
        print("You have selected to remove an existing product from the list")
        product_name = input("Please, provide the name of the product you wish to remove: ")
        found = False
        for product in list_of_product_objects:
            if product.product_name == product_name.strip().upper():
                list_of_product_objects.remove(product)
                found = True
                break
        if not found:
            return list_of_product_objects, 'Error: The product name you want to remove was not found'
        else:
            return list_of_product_objects, 'Success'


# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
def main():
    # Load data from file into a list of product objects when script starts
    lstOfProductObjects, result = FileProcessor.read_data_from_file(strFileName)
    print(result)

    # Show user a menu of options
    while (True):
        # Show current data
        IO.print_current_products_in_list(lstOfProductObjects)  # Show current data in the product list
        IO.print_menu()  # Shows menu
        strChoice = IO.input_menu_choice()  # Get menu option

        # Process user's menu choice
        if strChoice.strip() == '1':  # Add a new Product
            lstOfProductObjects, result = IO.add_new_product(lstOfProductObjects)
            strStatus = "Your attempt to add a new product to the list ended with the following result: {}".format(result)
            IO.input_press_to_continue(strStatus)
            continue  # to show the menu

        elif strChoice == '2':  # Remove an existing product
            lstOfProductObjects, result = IO.remove_product(lstOfProductObjects)
            strStatus = "Your attempt to remove a product from the list ended with the following result: {}".format(result)
            IO.input_press_to_continue(strStatus)
            continue  # to show the menu

        elif strChoice == '3':  # Save Data to File
            strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
            if strChoice.lower() == "y":
                result_b, result_message = FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
                strStatus = "Your attempt to save all data to a file ended with the following result: {}".format(result_message)
                IO.input_press_to_continue(strStatus)
            else:
                IO.input_press_to_continue("Save Cancelled!")
            continue  # to show the menu

        elif strChoice == '4':  # Reload Product Data from File
            print("Warning: Unsaved Data Will Be Lost!")
            strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
            if strChoice.lower() == 'y':
                lstOfProductObjects, result = FileProcessor.read_data_from_file(strFileName)
                strStatus = "Your attempt to reload data from file ended with the following result: {}".format(result)
                IO.input_press_to_continue(strStatus)
            else:
                IO.input_press_to_continue("File Reload  Cancelled!")
            continue  # to show the menu

        elif strChoice == '5':  # Exit Program
            print("Goodbye!")
            break  # and Exit

if __name__ == "__main__":
    main()