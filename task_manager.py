from datetime import date
import mysql.connector

class TaskManager:
    def __init__(self):
        with open("error.log", "r") as f:
            db_password = f.readline().strip()

        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password=db_password,
                database='task_manager'
            )


            self.cursor = self.conn.cursor()
        except mysql.connector.Error as err:
            print("Database connection error:", err)
            exit()

        self.tasks_list = []
        self.completed_tasks_list = []
        self.recurring_tasks_list = []
        self.user_name = input("Enter your name: ")
        print(f"Welcome, {self.user_name}!")

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
            task_details = input(f"Enter the details for Task {i}: ")
            self.tasks_list.append(task_details)
            self.cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task_details,))
            self.conn.commit()

    def replace_task(self):
        try:
            to_edit = int(input("Enter the index of the task you want to replace: "))
            new_task = input("Enter the new task: ")
            old_task = self.tasks_list[to_edit]
            self.tasks_list[to_edit] = new_task
            self.cursor.execute("UPDATE tasks SET task = %s WHERE task = %s", (new_task, old_task))
            self.conn.commit()
            print("Task updated.")
        except (IndexError, ValueError):
            print("Invalid index or input.")

    def delete_task(self):
        print("Tasks before deletion:", self.tasks_list)
        to_delete = input("Enter the task to delete: ")
        if to_delete in self.tasks_list:
            self.tasks_list.remove(to_delete)
            self.cursor.execute("DELETE FROM tasks WHERE task = %s", (to_delete,))
            self.conn.commit()
            print("Task deleted.")
        else:
            print("Task not found.")

    def view_lists(self):
        print("Tasks:", self.tasks_list)
        print("Completed tasks:", self.completed_tasks_list)
        print("Recurring tasks:", self.recurring_tasks_list)

    def mark_task_completed(self):
        try:
            comp_task = int(input("Enter the index of task to mark completed: "))
            task = self.tasks_list.pop(comp_task)
            self.completed_tasks_list.append(task)
            self.cursor.execute("UPDATE tasks SET status = 'completed' WHERE task = %s", (task,))
            self.conn.commit()
        except (IndexError, ValueError):
            print("Invalid index or input.")

    def add_recurring_tasks(self):
        num_tasks = self.number_of_tasks()
        for i in range(num_tasks):
            rec_task = input(f"Enter recurring task {i + 1}: ")
            self.recurring_tasks_list.append(rec_task)
            self.cursor.execute("INSERT INTO tasks (task, status) VALUES (%s, 'recurring')", (rec_task,))
            self.conn.commit()

    def complete_recurring_task(self):
        try:
            comp_rec_task = int(input("Enter index of recurring task to complete: "))
            task = self.recurring_tasks_list.pop(comp_rec_task)
            self.completed_tasks_list.append(task)
            self.cursor.execute("UPDATE tasks SET status = 'completed' WHERE task = %s", (task,))
            self.conn.commit()
        except (IndexError, ValueError):
            print("Invalid index or input.")

    def get_user_choice(self):
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
                self.mark_task_completed()
            elif choice == 6:
                self.add_recurring_tasks()
            elif choice == 7:
                self.complete_recurring_task()
            elif choice == 8:
                print("Exiting...")
                break
        self.cursor.close()
        self.conn.close()

tm = TaskManager()
tm.run()
