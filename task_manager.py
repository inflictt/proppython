from datetime import date
import mysql.connector

with open("error.log", "r") as f:
    db_password = f.readline().strip()

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password=db_password,
        database='task_manager'
    )
    cursor = conn.cursor()
except mysql.connector.Error as err:
    print("Database connection error:", err)
    exit()

def creating_a_list(num_tasks, tasks_list):
    for i in range(1, num_tasks + 1):
        task_details = input(f"Enter the details for Task {i}: ")
        tasks_list.append(task_details)
        cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task_details,))
        conn.commit()

def number_of_tasks():
    while True:
        try:
            num_tasks = int(input("Enter the number of tasks you want to deal with: "))
            if num_tasks > 0:
                return num_tasks
            else:
                print("Number must be greater than 0.")
        except:
            print("Invalid input. Please enter a valid number.")

def checking_results_for_choice(choice, tasks_list, user_name, completed_tasks_list, recurring_tasks_list):
    if choice == 1:
        print(f"Creating a list for {user_name}")
        num_tasks = number_of_tasks()
        creating_a_list(num_tasks, tasks_list)

    elif choice == 2:
        to_edit = int(input("Enter the index of the task you want to replace: "))
        new_task = input("Enter the new task: ")
        old_task = tasks_list[to_edit]
        tasks_list[to_edit] = new_task
        cursor.execute("UPDATE tasks SET task = %s WHERE task = %s", (new_task, old_task))
        conn.commit()
        print("Task updated.")

    elif choice == 3:
        print("Tasks before deletion:", tasks_list)
        to_delete = input("Enter the task to delete: ")
        tasks_list.remove(to_delete)
        cursor.execute("DELETE FROM tasks WHERE task = %s", (to_delete,))
        conn.commit()
        print("Task deleted.")

    elif choice == 4:
        print("Tasks:", tasks_list)
        print("Completed tasks:", completed_tasks_list)
        print("Recurring tasks:", recurring_tasks_list)

    elif choice == 5:
        comp_task = int(input("Enter the index of task to mark completed: "))
        task = tasks_list.pop(comp_task)
        completed_tasks_list.append(task)
        cursor.execute("UPDATE tasks SET status = 'completed' WHERE task = %s", (task,))
        conn.commit()

    elif choice == 6:
        num_tasks = number_of_tasks()
        for i in range(num_tasks):
            rec_task = input(f"Enter recurring task {i+1}: ")
            recurring_tasks_list.append(rec_task)
            cursor.execute("INSERT INTO tasks (task, status) VALUES (%s, 'recurring')", (rec_task,))
            conn.commit()

    elif choice == 7:
        comp_rec_task = int(input("Enter index of recurring task to complete: "))
        task = recurring_tasks_list.pop(comp_rec_task)
        completed_tasks_list.append(task)
        cursor.execute("UPDATE tasks SET status = 'completed' WHERE task = %s", (task,))
        conn.commit()

def checking_user_input_for_integer():
    while True:
        try:
            choice = int(input(
                "\n1. Create a list\n"
                "2. Replace a task\n"
                "3. Delete a task\n"
                "4. View lists\n"
                "5. Mark task completed\n"
                "6. Add recurring tasks\n"
                "7. Complete recurring task\n"
                "8. Exit\n"
                "Enter your choice: "))
            if 1 <= choice <= 8:
                return choice
            else:
                print("Enter a number between 1 and 8.")
        except:
            print("Invalid input. Enter a number.")

def task_manager():
    user_name = input("Enter your name: ")
    print(f"Welcome, {user_name}!")

    tasks_list = []
    completed_tasks_list = []
    recurring_tasks_list = []

    while True:
        choice = checking_user_input_for_integer()
        if choice == 8:
            print("Exiting...")
            break
        checking_results_for_choice(choice, tasks_list, user_name, completed_tasks_list, recurring_tasks_list)

    cursor.close()
    conn.close()

task_manager()
