import datetime as dt
# imported datetime and saved it as 'dt'

def reg_user():
    # created a register user function
        new_username = input("Please enter a new username:").lower()  # ask the user to input a new username
        new_password = input("Please enter a new password:").lower()  # ask the user to input a new password
        confirm_password = input("Please confirm your new password:").lower()  # ask the user to input to confirm the password

        if confirm_password == new_password and new_username not in user_names:  # if statement to confirm that the user inputted the same passwords for the new and the confirmed one
            file = open('new_user.txt', 'a')  # open the user file and use the append mode in order add stuff to the file
            file.write(
                '\n' + new_username + ',' + ' ' + confirm_password)  # use .write with the previous append mode in order to write the new username and password to the file. add the \n in order to skip a line in the file, add the new username and add a comma and space so that the structure of the other things in the file are correct and finally add the new password.

        elif confirm_password == new_password and new_username in user_names:
            # elif statement for if the username is already in use, by making sure that the new_username input is within the user_names list
            print("Username already in use... Please enter another username.")

        else:  # else statement if the users new password does not equal their confirmed password
            print('Password does not match.\n')

        print('\n')

def add_task():
    # created an add task function
    assigned_username = input("Please input which username the task is assigned too:")  # inputs to ask the user for the things in which the previous ''' statement asks for
    task_title = input("Please enter the title of the task:")
    task_description = input("Please enter the description of the task:")
    due_date = input("Please enter the due date of the task *in the format yyyy-mm-dd*:")
    current_date = input("Please enter the current date *in the format yyyy-mm-dd*: ")
    completed = "No"

    task_file = open("new_tasks.txt","a")  # open the task file and append to it; thereafter use the write function in order to add the inputs in the correct structure with adding spaces and commas
    task_file.write("\n" + assigned_username + "," + " " + task_title + "," + " " + task_description + "," + " " + due_date + "," + " " + current_date + "," + " " + completed)

    print('\n')

def view_all():
    # created a function to view all the tasks
    task_file = open("new_tasks.txt", "r")  # open the task file and read it
    task_line = []  # create a list for the task info to be put in

    for line in task_file:  # for loop in order to add the info from the task file to the task_line list
        task_line = line.strip()
        task_line = task_line.split(", ")  # strip and split for the structure of the info to be correct

        print(f'''      
                         Task: {task_line[1]}                                                        
                         Assigned to: {task_line[0]}
                         Date assigned: {task_line[3]}
                         Due date: {task_line[4]}
                         Task complete: {task_line[5]}
                         Task description: {task_line[2]} \n''')  # printing the info that they asked for in the list with the correct indexes, like the example in output 2 which was given before the question

        print('\n')

def view_mine():
    # created a function to view the users own tasks
    count = 0
    # created a count
    task_file = open("new_tasks.txt", "r")
    # open and read the new_tasks text file
    task_list = []
    # created an empty list

    for line in task_file:
        # for loop in order to loop through the file and strip and split, for better indexing' as well as appending the data into the task list
        task_line = line.strip()
        task_line = task_line.split(", ")
        task_list.append(task_line)
        count += 1
        # allowed the counter to concatenate by 1 in order for each task to be numbered correctly

        if task_line[0] == user_input_name:
            # if statement for if the first user index equals to the name in which the user inputted, so only their tasks will appear
            print(f'''   Task #{count}
                         Task: {task_line[1]}
                         Assigned to: {task_line[0]}
                         Date assigned: {task_line[3]}
                         Due date: {task_line[4]}
                         Task complete: {task_line[5]}
                         Task description: {task_line[2]} \n''')  # repeated what was done in the previous elif statement, but added an if statement for if the username in the index [0] of the task file inputted their name, so just their tasks pop up.
            # added the count to the print statement in order for each task to be numbered correctly

    user_selection = int(input("Please enter the task you wish to edit by inserting the number of the task:")) - 1
    # made a user input to ask the user which task they would like to check and made it into an integer so that the user has to enter a number; add a -1 to correct the indexing
    selected_task = task_list[user_selection]
    # for if the user_selection is within the task list
    print(f'''
                    Task: {selected_task[1]}
                    Assigned to: {selected_task[0]}
                    Date assigned: {selected_task[3]}
                    Due date: {selected_task[4]}
                    Task complete: {selected_task[5]}
                    Task description: {selected_task[2]}''')
    # printed out the selected task list with the correct indexing to be easily read

    print("\n")

    while True:
        # while loop for the new menu that will be inputted
        menu_2 = input('''Select one of the following Options below:
    m - mark the test as complete
    ed - edit the task
    -1 - to return to main menu
    :''').lower()
        # ask for the user to input any of the given options and implement .lower for less chance of error

        if menu_2 == "m":
            # if statement for whether the user inputted m
            selected_task[-1] = "Yes"
            # if the last index of the list equals yes

            file_new_user = open("new_tasks.txt","w")
            # opened and asked to write to the new tasks file

            for i in task_list:
                # for loop to iterate through the task list
                file_new_user.write(", ".join(i) + "\n")
                # writing the iteration with .join to ensure that the iteration will be implementing yes into the file instead of no

            file_new_user.close()
            # closed the file

        elif menu_2 == "ed":
            # elif statement for if the user inputted ed; to edit
            user_choice = input("Please enter if you wish to edit the username or the due date *simply enter 'username' or 'due date'*").lower()
            # ask the user to input whether they will be editing the username or the due date

            if user_choice == "username":
                # if statement within the elif statement for if the user chose to edit the username
                selected_task[0] = input("Please enter the new username you wish to input:").lower()
                # if the first index within the selected task list equals to the username that the user inputted

                file_new_user = open("new_tasks.txt", "w")
                # open and write to the new tasks file

                for i in task_list:
                    # for loop for the i that iterates through the list and the username inputted should be added to the file by .join
                    file_new_user.write(", ".join(i) + "\n")

                file_new_user.close()
                # closed the file

            elif user_choice == "due date":
                # elif statement for if the user inputted to edit the due date
                selected_task[4] = input("Please enter the new due date to wish to input:")
                # the fourth input within the list should be equal to the users input

                file_new_user_2 = open("new_tasks.txt", "w")

                for j in task_list:
                    file_new_user_2.write(", ".join(j) + "\n")

                file_new_user_2.close()
                # repeat what was done in previous if statement

            else:
                print("Invalid input")
                # else for if the user does not input username or due date

        elif menu_2 == "-1":
            # elif for if the user inputs -1, so it will be returned to the main menu
            return

        else:
            print("Invalid input")
            # else statement for invalid input

def gen_rep():
    # created a function to generate reports
    file_new_tasks = open("new_tasks.txt", "r")
    new_tasks_list = []

    for line in file_new_tasks:
        temp = line.strip()
        temp = temp.split(", ")
        new_tasks_list.append(temp)

        # repeated what was done the previous times reading from a list and putting it into a list, just in different function

    len_tasks = len(new_tasks_list)
    # get the amount of the tasks by getting the length of the list which counts each index

    complete_counter = 0
    # complete counter
    for yes in new_tasks_list:
        # for loop within the new tasks list to iterate through the list
        if yes[-1] == "Yes":
            # if the iterations last index equals to yes then the counter will increase by 1
            complete_counter += 1

    incomplete_counter = 0
    # incomplete counter
    for no in new_tasks_list:
        # for loop within the new tasks list to iterate through the list
        if no[-1] == "No":
            # if the iterations last index equals to no then the counter will increase by 1
            incomplete_counter += 1

    now = dt.datetime.now()
    # get the date and time now by using the datetime function called at the start and using .now

    overdue_counter = 0
    # overdue counter
    for x in new_tasks_list:
        # for loop within the new tasks list to iterate through the list
        y = dt.datetime.strptime(x[4], "%Y-%m-%d")
        # stripping the time from datetime and indexing the fourth index,
        # which is the due date and the the second argument being the order i want the date in
        if x[-1] == "No" and y < now:
            # if the last index equals to no and the y variable is smaller than now,
            # it means the task is incomplete and overdue, thus increasing the overdue counter by 1
            overdue_counter += 1

    incomplete_percentage = incomplete_counter/len_tasks * 100
    # getting the percentage of the incomplete counter
    incomplete_percentage = round(incomplete_percentage, 2)
    # rounding off the percentage given by 2 decimal places
    incomplete_percentage = str(incomplete_percentage)
    # making it into a string to help with writing to the file

    overdue_percentage = overdue_counter/len_tasks * 100
    # getting the percentage of the complete counter
    overdue_percentage = round(overdue_percentage, 2)
    # rounding off the percentage given by 2 decimal places
    overdue_percentage = str(overdue_percentage)
    # making it into a string to help with writing to the file

    len_tasks = str(len_tasks)
    # making it into a string to help with writing to the file
    complete_counter = str(complete_counter)
    # making it into a string to help with writing to the file
    incomplete_counter = str(incomplete_counter)
    # making it into a string to help with writing to the file
    overdue_counter = str(overdue_counter)
    # making it into a string to help with writing to the file

    file_task_overview = open("task_overview.txt","a")
    # opening and appending to the task overview file
    file_task_overview.write(f'''Your total number of tasks is {len_tasks}
Your total number of completed tasks are {complete_counter}
Your total number of tasks are incomplete are {incomplete_counter}
Your total number of incomplete as well as overdue tasks are {overdue_counter}
The percentage of tasks that are incomplete is {incomplete_percentage}%
The percentage of tasks that are overdue is {overdue_percentage}%''')
    # writing the given things into a list in an easy to read format

    file_new_user = open("new_tasks.txt", "r")
    new_user_list = []

    for line2 in file_new_user:
        user = line2.strip()
        user = user.split(", ")
        new_user_list.append(user)
        # repeated what was done the previous times reading from a list and putting it into a list

    len_users = len(new_user_list)
    # getting the total number of users by getting the length of the list

    user_selection = input("Please enter which username you wish to observe:")
    # ask the user to input which username they wish observe

    user_tasks = 0
    incomplete_counter2 = 0
    complete_counter2 = 0
    overdue_counter2 = 0
    # implement counters for each line within the task that the question asks

    for l in new_user_list:
        # for loop to iterate through the new user list
        if user_selection in l:
            # if the user selection is within the iterating l in the list, then the user tasks counter will add 1
            user_tasks += 1

            if l[-1] == "No":
                # if the last index for the l that is indexing equal to no then the incomplete counter will add 1
                incomplete_counter2 += 1

            elif l[-1] == "Yes":
                # if the last index for the l that is indexing equal to yes then the incomplete counter will add 1
                complete_counter2 += 1

            user_task_date = l[4]
            # created a variable for the 4th index for the l that is indexing, which is the due date
            z = dt.datetime.strptime(user_task_date, "%Y-%m-%d")
            # created variable z to get the datetime and strip the time, with the first argument in the striptime is the 4th index of the l iteration and the second argument is the format that i want the dates to be in

            if z.date() <= dt.datetime.today().date() and l[-1] == "No":
                # if statement for if the z.date is smaller than or equal to now and if the last index equals to zero; then the overdue counter will add 1
             overdue_counter2 += 1

    user_tasks_percentage = user_tasks / len_users * 100
    # getting the percentage of the user tasks counter
    user_tasks_percentage = round(user_tasks_percentage, 2)
    # rounding off the percentage given by 2 decimal places
    user_tasks_percentage = str(user_tasks_percentage)
    # making it into a string to help with writing to the file

    complete_percentage = complete_counter2 / user_tasks * 100
    # getting the percentage of the complete counter
    complete_percentage = round(complete_percentage, 2)
    # rounding off the percentage given by 2 decimal places
    complete_percentage = str(complete_percentage)
    # making it into a string to help with writing to the file

    incomplete_percentage2 = incomplete_counter2 / user_tasks * 100
    # getting the percentage of the incomplete counter 2
    incomplete_percentage2 = round(incomplete_percentage2, 2)
    # rounding off the percentage given by 2 decimal places
    incomplete_percentage2 = str(incomplete_percentage2)
    # making it into a string to help with writing to the file

    overdue_percentage2 = overdue_counter2 / user_tasks * 100
    # getting the percentage of the overdue counter 2
    overdue_percentage2 = round(overdue_percentage2, 2)
    # rounding off the percentage given by 2 decimal places
    overdue_percentage2 = str(overdue_percentage2)
    # making it into a string to help with writing to the file

    file_user_overview = open("user_overview.txt", "a")
    # open the user overview file and appending to it
    file_user_overview.write(f'''The total number of tasks assigned to your user of choice is {user_tasks}
The percentage of the total number of tasks assigned to your user of choice is {user_tasks_percentage}%
The percentage of the completed tasks of your user of choice is {complete_percentage}%
The percentage of the tasks that are incomplete of your user of choice is {incomplete_percentage2}%
The percentage of the tasks that are incomplete and overdue of your user of choice is {overdue_percentage2}%''')
    # using .write and using the format to put the given counters and percentages into an easy to read format


# ====Login Selection====

file = open('new_user.txt', 'r')          # variable file entered to open and read the user.txt file
user_names = []                       # 1 list for usernames so its easier to read from the file
pass_words = []                       # 1 list for passwords so its easier to read from the file

task_file = open('new_tasks.txt', 'r')    # variable task file entered to open and read the tasks.txt file
task_line = []                        # list for the info in the tasks file to be appended too

for tasks in task_file:               # for statement to read the things in the task file and extract them effectively
    data_tasks = tasks.strip()        # variable data_tasks in order to strip the \n within the file
    data_tasks = data_tasks.split(", ") # splitting the info in the file to make it easier to index and remove ',' for proper inputs to be done
    task_line.append(data_tasks)        # reading the info in the task file and appending it to the list

for name in file:                     # for statement to read things in file in order to extract the things from the file effectively
    data_name = name.strip()          # variable data_name in order to strip the \n within the file
    data_name = data_name.split(", ")  # splitting the info in the file to make it easier to index and remove ',' for proper inputs to be done
    user_names.append(data_name[0])   # reading first words in file for the usernames
    pass_words.append(data_name[1])   # reading second words in file for the passwords

while True:                                                              # while loop for the user to enter; using if statements
    user_input_name = input('Please enter your username:').lower()       # asking user to input their username with .lower so the user can input in anyway they want
    user_input_password = input('Please enter your password:').lower()   # asking the user to input their password with .lower

    if user_input_name not in user_names:                                # if statement if the user inputs their username, but the username inputted is not found in the usernames list, so the if statement will output the print
        print("Invalid username inputted.\n Please Try Again:")
        continue

    elif user_input_password not in pass_words:                          # elif statement if the user inputs a password, but the password inputted is not found in the list
        print("Invalid password.\n Please Try Again:")

    else:
        print(f"Welcome {user_input_name}\n")                            # else the user therefore inputted the correct username as well as the correct password,so then the system will allow them to continue to the main menu
        break

while True:                                                              # while loop which includes the menu that was given
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    menu = input('''Select one of the following Options below:
r - registering a user (admin use only)
d - display statistics (admin use only)
a - adding a task
va - view all my tasks
vm - view my tasks
gr - generate reports
e - exit
:''').lower()

    if menu == 'r' and user_input_name == 'admin':                                   # if statement for if the user asks to request a new user to be added, but will only work if the username inputted was the admin
        reg_user()

    elif menu == 'd' and user_input_name == 'admin':                                 # added display statistics for the admin, with a new elif statement
        gen_rep()
        len_usernames = len(user_names)                                              # got the length of the user_names list, which will count each line; therefore counting each name in the file
        print(f"The total amount of users is {len_usernames}.")                      # print the length

        len_tasks = len(task_line)                                                   # got the length of the task lines in the task_line list; therefore does the same thing as the previous length calculation
        print(f"The total amount of tasks is {len_tasks}.\n")

        read_task_overview = open("task_overview.txt","r")
        # open and read the task overview file
        list1 = read_task_overview.readlines()
        # create variable list1 to readlines in the file

        print(f'''Display of the task_overview text file:
{list1[0]}
{list1[1]}
{list1[2]}
{list1[3]}
{list1[4]}
{list1[5]}\n''')
        # print out the list1 indexing so its in an easy to read format

        read_user_overview = open("user_overview.txt","r")
        # open and read the user overview file
        list2 = read_user_overview.readlines()
        # create variable list2 to readlines in the file

        print(f'''Display of the user_overview text file:
{list2[0]}
{list2[1]}
{list2[2]}
{list2[3]}
{list2[4]}\n''')
        # print out the list2 indexing so its in an easy to read format

    elif menu == 'a':       # elif statement for the user to add a task
        add_task()

    elif menu == 'va':      # elif statement for the user to view all the tasks
        view_all()

    elif menu == 'vm':      # elif statement for the user to view their specific tasks
        view_mine()

    elif menu == 'gr':      # elif statement for the user to generate reports
        gen_rep()

    elif menu == 'e':       # elif statement for the user to exit the menu 
        print('Goodbye!!!') # printed out "Goodbye!!!
        exit()

    else:                   # else statement for if the user inputted something which does not align with the options
        print("You have made a wrong choice, Please Try again") # printed out error statement
