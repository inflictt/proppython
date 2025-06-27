from datetime import datetime, date
import mysql.connector

class ToDoList:
    def __init__(self):
        with open("error.log", "r") as f:
            db_password = f.readline().strip()

        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password=db_password,
                database='todo_list'  
            )
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as err:
            print("Database connection error:", err)
            exit()

        self.tasks_list = []
        self.completed_tasks_list = []
        self.user_name = input("Enter your name: ")
        print(f"Welcome, {self.user_name}!")

    def get_deadline(self):
        while True:
            user_input = input("Enter the deadline (YYYY-MM-DD): ")
            try:
                deadline = datetime.strptime(user_input, "%Y-%m-%d").date()
                if deadline < date.today():
                    print("Deadline cannot be in the past. Try again.")
                else:
                    return deadline
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

    def number_of_tasks(self):
        while True:
            try:
                num_tasks = int(input("Enter the number of tasks you want to deal with: "))
                if num_tasks > 0:
                    return num_tasks
                else:
                    print("Number must be greater than 0.")
            except:
                print("Invalid input. Please enter a valid number.")

    def create_tasks(self):
        num_tasks = self.number_of_tasks()
        for i in range(1, num_tasks + 1):
            print(f"\n--- Task {i} ---")
            task_details = input("Enter the task details: ")
            deadline = self.get_deadline()
            frequency = input("Enter task frequency ('onetime' or 'recurring') [default: onetime]: ").strip().lower()
            if frequency not in ['onetime', 'recurring']:
                print("Invalid frequency. Defaulting to 'onetime'.")
                frequency = 'onetime'

            self.tasks_list.append((task_details, deadline, frequency))

            try:
                self.cursor.execute(
                    "INSERT INTO todo_list (task, deadline, frequency) VALUES (%s, %s, %s)", 
                    (task_details, deadline, frequency)
                )
                self.conn.commit()
                print(f"Task '{task_details}' added with deadline {deadline} and frequency '{frequency}'.")
            except mysql.connector.Error as err:
                print("Failed to insert task into database:", err)

    def replace_task(self):
        try:
            to_edit = int(input("Enter the index of the task you want to replace: "))
            new_task = input("Enter the new task: ")
            old_task, deadline, frequency = self.tasks_list[to_edit]
            self.tasks_list[to_edit] = (new_task, deadline, frequency)
            self.cursor.execute("UPDATE todo_list SET task = %s WHERE task = %s", (new_task, old_task))
            self.conn.commit()
            print("Task updated.")
        except (IndexError, ValueError):
            print("Invalid index or input.")

    def delete_task(self):
        print("Tasks before deletion:")
        for i, (task, deadline, frequency) in enumerate(self.tasks_list):
            print(f"{i}. {task} (Deadline: {deadline}, Frequency: {frequency})")

        to_delete = input("Enter the task to delete: ")
        found = False
        for task, deadline, frequency in self.tasks_list:
            if task == to_delete:
                self.tasks_list.remove((task, deadline, frequency))
                self.cursor.execute("DELETE FROM todo_list WHERE task = %s", (to_delete,))
                self.conn.commit()
                print("Task deleted.")
                found = True
                break
        if not found:
            print("Task not found.")

    def view_lists(self):
        print("\nYour Current Tasks:")
        for i, (task, deadline, frequency) in enumerate(self.tasks_list):
            print(f"{i}. {task} (Deadline: {deadline}, Frequency: {frequency})")
        print("\nCompleted Tasks:", self.completed_tasks_list)

    def get_user_choice(self):
        while True:
            try:
                choice = int(input(
                    "\n1. Create a list\n"
                    "2. Replace a task\n"
                    "3. Delete a task\n"
                    "4. View lists\n"
                    "5. Exit\n"
                    "Enter your choice: "))
                if 1 <= choice <= 5:
                    return choice
                else:
                    print("Enter a number between 1 and 5.")
            except:
                print("Invalid input. Enter a number.")

    def run(self):
        while True:
            choice = self.get_user_choice()
            if choice == 1:
                self.create_tasks()
            elif choice == 2:
                self.replace_task()
            elif choice == 3:
                self.delete_task()
            elif choice == 4:
                self.view_lists()
            elif choice == 5:
                print("Exiting...")
                break
        self.cursor.close()
        self.conn.close()

todo = ToDoList()
todo.run()
