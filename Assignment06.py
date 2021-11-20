# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Cli,11.17.21,Modified code to complete assignment 6
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name_str = "ToDoFile.txt"  # The name of the data file
file_obj = None   # An object that represents a file [not used in program]
row_dic = {}  # A row of data separated into elements of a dictionary {Task,Priority} [not used in program]
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection
task_str = ""  # Captures the user task data
priority_str = ""  # Captures the user priority data
status_str = ""  # Captures the status of an processing functions

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, 'r')
        for line in file:
            task, priority = line.split(', ')
            row = {'Task': task.strip(), 'Priority': priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Creates a new row with inputted task and its priority and adds it to a list of dictionary rows
        
        :param task: (string) with task to input into list/table of data:
        :param priority: (string) with priority of the task:
        :param list_of_rows: (list) of dictionary rows:
        :return: (list) of dictionary rows with newly added row of task & priority
        """
        row = {'Task': task, 'Priority': priority}
        list_of_rows.append(row)
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(task, list_of_rows, row_removed=None, status=''):
        """ Removes user inputted task if it is found in the list of dictionary rows
        
        :param task: (string) with task to input into list of dictionary rows:
        :param list_of_rows: (list) of dictionary rows:
        :param row_removed: (boolean flag) to validate if row was removed:
        :param status: (string) initialized for return status:
        :return: modified (list) of dictionary rows, (string) with status of row removal
        """
        for row in list_of_rows:
            if row['Task'].lower() == task.lower():
                list_of_rows.remove(row)
                row_removed = True  # boolean flag, True to show row was removed
            if row_removed == True:
                status = 'Success. Task is removed'
            else:
                status = 'I\'m sorry. I cannot find the task.'
        return list_of_rows, status

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes current list of dictionary rows (inputted data) into a file
        
        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want write to file:
        :return: (list) of dictionary rows written to file
        """
        file = open(file_name, 'w')
        for row in list_of_rows:
            file.write(row['Task'] + ', ' + row['Priority'] + '\n')
        file.close()
        return list_of_rows, 'Success'

class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: (string) with user's menu selection
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
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
    def input_new_task_and_priority():
        """ Asks user for task and priority

        :return: 2 (strings) - task and priority
        """
        task = str(input('Enter a task: '))
        priority = str(input('Enter its priority: '))
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """ Asks user for the task name s/he want to remove

        :return: (string) with name of task to be removed
        """
        task = str(input('Which task do you want to remove? '))
        return task

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(file_name_str, table_lst)  # read file data

while True:
    # Step 2 Show current data
    IO.print_current_Tasks_in_list(table_lst) # Show current data in the list/table
    # Step 3 - Display a menu of choices to the user
    IO.print_menu_Tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if choice_str.strip() == '1':  # Add a new Task
        task_str, priority_str = IO.input_new_task_and_priority()
        table_lst, status_str = Processor.add_data_to_list(task_str, priority_str, table_lst)
        IO.input_press_to_continue(status_str)  # shows if action was successful via a status
        continue  # to show the menu

    elif choice_str == '2':  # Remove an existing Task
        task_str = IO.input_task_to_remove()
        table_lst, status_str = Processor.remove_data_from_list(task_str, table_lst)
        IO.input_press_to_continue(status_str)
        continue  # to show the menu

    elif choice_str == '3':   # Save Data to File
        choice_str = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if choice_str.lower() == "y":
            table_lst, status_str = Processor.write_data_to_file(file_name_str, table_lst)
            IO.input_press_to_continue(status_str)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif choice_str == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        choice_str = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if choice_str.lower() == 'y':
            table_lst, status_str = Processor.read_data_from_file(file_name_str, table_lst)
            IO.input_press_to_continue(status_str)
        else:
            IO.input_press_to_continue("File Reload Cancelled!")
        continue  # to show the menu

    elif choice_str == '5':  # Exit Program
        print("Goodbye!")
        break  # and Exit

    else:
        IO.input_press_to_continue('Please enter a value from 1 to 5!')