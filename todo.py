def print_tasks():
    task_list.sort()
    for row in task_list:
        print(f"{row}")

task_list = []

while True:
    print("""TODO List Management System
    1: Add
    2: View
    3: Remove
    4: Edit
    5: Exit""")
    w = input()
    if w == '1':
        add = input("What do you want to add: ")
        row = [add]
        task_list.append(row)
    elif w == '2':
        print_tasks()
    elif w == '3':
        rem = input("What do you want to remove: ")
        task_list = [row for row in task_list if row[0] != rem]
    elif w == '4':
        old_task = input("Which task do you want to edit? ")
        for i, row in enumerate(task_list):
            if row[0] == old_task:
                new_task = input("What do you want to change it to: ")
                task_list[i] = [new_task]
    elif w == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice, please choose a number between 1-5.")

