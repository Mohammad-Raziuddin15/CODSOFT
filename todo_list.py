tasks = []

print("=====  TO-DO LIST APPLICATION  =====")

while True:

    print("\n1. Add Task")
    print("2. View Task")
    print("3. Update Task")
    print("4. Remove Task")
    print("5. Exit")

    user_choice = input("\nEnter your choice:-")

    if user_choice == '1':

        task = input("Enter new task: ")

        tasks.append(task)

        print("Task added successfully!")

    # VIEW TASKS
    elif user_choice == '2':

        if len(tasks) == 0:

            print("No tasks available.")

        else:

            print("\nYour Tasks:")

            for i, task in enumerate(tasks, start = 1):
                print(i, ". ", task)

    # UPDATE TASK
    elif user_choice == '3':

        if len(tasks) == 0:
            print("No tasks available to update.")

        else:
            print("\nYour Tasks:")

            for i, task in enumerate(tasks, start = 1):
                print(i, ". ", task)

            task_number = int(input("Enter task number to update:-"))

            if 1 <= task_number <= len(tasks):
                
                new_task = input("Enter updated task: ")

                tasks[task_number - 1] = new_task

                print("Task updated Successfully!")

            else:

                print("Invalid task number.")

    # REMOVE TASK
    elif user_choice == '4':

        if len(tasks) == 0:

            print("No tasks available to remove.")

        else:

            print("\nYour Tasks:")

            for i, task in enumerate(tasks, start = 1):

                print(i, ". ", task)

            remove_task = int(input("Enter task number to remove: "))

            if 1 <= remove_task <= len(tasks):

                removed = tasks.pop(remove_task - 1)

                print(removed, "removed successfully!")

            else:

                print("Inavlid task number.")

    # EXIT
    elif user_choice == '5':

        print("To-Do List Closed")

        break

    # INVALID INPUT
    else:

        print("Invalid choice. please try again.")
