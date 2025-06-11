import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host='localhost',        
        user='root',    
        password='PASSWORD',
        database='task_manager' 
    )

def create_task(cursor, conn, num_tasks):
    for i in range(1, num_tasks + 1):
        task_details = input(f"Enter the details for Task {i}: ")
        cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task_details,))
    conn.commit()
    print("Tasks inserted successfully.")

def number_of_tasks():
    while True:
        try:
            num_tasks = int(input("Enter the number of tasks you want to deal with: "))
            if num_tasks > 0:
                return num_tasks
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def update_task(cursor, conn):
    view_tasks(cursor)
    try:
        task_id = int(input("Enter the ID of the task to update: "))
        new_value = input("Enter the new task description: ")
        cursor.execute("UPDATE tasks SET task = %s WHERE id = %s", (new_value, task_id))
        conn.commit()
        print("Task updated successfully.")
    except ValueError:
        print("Invalid input.")

def delete_task(cursor, conn):
    view_tasks(cursor)
    try:
        task_id = int(input("Enter the ID of the task to delete: "))
        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        conn.commit()
        print("Task deleted successfully.")
    except ValueError:
        print("Invalid input.")

def view_tasks(cursor):
    cursor.execute("SELECT id, task, status FROM tasks")
    rows = cursor.fetchall()
    print("\nTask List:")
    for row in rows:
        print(f"ID: {row[0]}, Task: {row[1]}, Status: {row[2]}")
    print()

def mark_completed(cursor, conn):
    view_tasks(cursor)
    try:
        task_id = int(input("Enter the ID of the task to mark as completed: "))
        cursor.execute("UPDATE tasks SET status = 'completed' WHERE id = %s", (task_id,))
        conn.commit()
        print("Task marked as completed.")
    except ValueError:
        print("Invalid input.")

def add_recurring_tasks(cursor, conn):
    num_tasks = number_of_tasks()
    for i in range(num_tasks):
        task = input(f"Enter recurring task {i + 1}: ")
        cursor.execute("INSERT INTO tasks (task, status) VALUES (%s, 'recurring')", (task,))
    conn.commit()
    print("Recurring tasks added.")

def complete_recurring(cursor, conn):
    cursor.execute("SELECT id, task FROM tasks WHERE status = 'recurring'")
    rows = cursor.fetchall()
    print("\nRecurring Tasks:")
    for row in rows:
        print(f"ID: {row[0]}, Task: {row[1]}")
    try:
        task_id = int(input("Enter the ID of the recurring task to mark as completed: "))
        cursor.execute("UPDATE tasks SET status = 'completed' WHERE id = %s", (task_id,))
        conn.commit()
        print("Recurring task marked as completed.")
    except ValueError:
        print("Invalid input.")

def get_user_choice():
    print("\nMenu:")
    print("1. Create a task list")
    print("2. Update a task")
    print("3. Delete a task")
    print("4. View all tasks")
    print("5. Mark a task as completed")
    print("6. Add recurring tasks")
    print("7. Complete recurring task")
    print("8. Exit")
    try:
        choice = int(input("Enter your choice: "))
        if 1 <= choice <= 8:
            return choice
        else:
            print("Please enter a number between 1 and 8.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return None

def task_manager():
    conn = connect_db()
    cursor = conn.cursor()
    user_name = input("Enter your name: ")
    print(f"Welcome {user_name} to the Task Manager.")

    while True:
        choice = get_user_choice()
        if choice == 1:
            num_tasks = number_of_tasks()
            create_task(cursor, conn, num_tasks)
        elif choice == 2:
            update_task(cursor, conn)
        elif choice == 3:
            delete_task(cursor, conn)
        elif choice == 4:
            view_tasks(cursor)
        elif choice == 5:
            mark_completed(cursor, conn)
        elif choice == 6:
            add_recurring_tasks(cursor, conn)
        elif choice == 7:
            complete_recurring(cursor, conn)
        elif choice == 8:
            print("Exiting the application...")
            break

    cursor.close()
    conn.close()

if __name__ == '__main__':
    task_manager()