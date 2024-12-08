
import task as cl
import utility as uti
import json

from utility import split_seg as sps 
from utility import clear_screen as cls
from utility import bold 

with open("command_desc.txt") as file:
    cmnd_desc_file = file.readlines()


task_list = []
need_task_cmnd = ["see", "del"] 


#Title of program showing when program is booted
cls()
print(f"{uti.bold("Task Maestro")} 1.0")


def run() -> None:
    sps(1)
    
    user_input = input(f"Enter command: ").lower().strip()
    
    #Reminder to save before exiting
    if user_input == "exit": 
        while True:
            
            fail_safe = input("\n\u26A0 Do not forget to save. Enter 'save' if unsure, else 'exit':  ")
            
            match fail_safe:
                
                case "exit":
                    quit()
                
                case "save":
                    pass

                case _:
                    print("\n\u26A0 Invalid command. Try again")
                    
    #Some commands don't work without atleast one task
    elif len(task_list) == 0 and user_input in need_task_cmnd:     
        print("\n\u26A0 Invalid command. No tasks exist\n")
        run()

    #Wrong command input handling
    elif user_input not in cmnd_dict.keys():
        print("\n\u26A0 Invalid command. Enter 'help' to display valid commands\n")
        run()
    
    #Gets cmnd_dict value and calls function with the addition of the parenthesis
    #The commands corresponding description is also passed along to display it when using the command
    else:
        cmnd_dict[user_input][0](cmnd_dict[user_input][1])  

      
def show_cmnd(desc) -> None:
    cls()
    
    print(bold(desc), end=""), sps(1)
    
    for cmnd_name in cmnd_dict.keys():
        print(f"  '{cmnd_name}': {cmnd_dict[cmnd_name][1]}")
    
    print("\n*Not case-sensitive\n")

    run() 


def create_task(desc) -> None:
    cls()
    
    print(bold(desc), end=""), sps(1)
    
    name = input(f"  Task's name: ").strip()

    description = input("\n  Task's description: ").strip()

    deadline = input(f"\n  Task's deadline: ").strip()
    
    new_task = cl.Task(name, description, deadline)

    #So the latest tasks appear on top in show tasks
    task_list.insert(0, new_task)
    
    print(f"\n  Task named '{new_task.name}' created\n")
     
    run()
    

def show_tasks(desc) -> None:
    cls()
    
    print(bold(desc), end="")
    
    #To display all tasks
    for index, tasks in enumerate(reversed(task_list), 1):
        sps(1)
        print(f"  #{index}\n  Task: {tasks.name}\n  Deadline: {tasks.deadline}\n")
        
    while True:
        sps(1)
        see_task = input("  See task number: ").lower().strip()
        
        if see_task == "exit":
            print() 
            break

        try:
            task_num = int(see_task)
            
            if task_num > len(task_list):
                raise

        except:
            print("\n  \u26A0 Invalid task. Task does not exist (Enter 'exit' to cancel)\n")
            continue
        
        task = task_list[task_num - 1]
        
        cls()
        
        print(bold("Task: ") + task.name), sps(1)

        print(f"  Deadline: {task.deadline}\n\n  Created: {task.created}")
        
        print(f"\n  Descritpion: {task.description}\n")

    run()
    

def remove_task(desc) -> None:
    cls()
    
    print(bold(desc), end=""), 

    for index, tasks in enumerate(reversed(task_list), 1):
        sps(1)
        print(f"  #{index}\n  Task: {tasks.name}\n  Deadline: {tasks.deadline}\n")
        

    while True:
        sps(1)
        del_task = input("  Delete task number: ").lower().strip()
        
        if del_task == "exit": 
            print()
            break

        try:
            task_num = int(del_task)
            
            if task_num > len(task_list):
                raise

        except:
            print("\n  \u26A0 Invalid task. Task does not exist (Enter 'exit' to cancel)\n")
            continue
        
        else:
            task_list.pop(task_num - 1)
            print(f"\n  Task number #{task_num} deleted\n")
        
            break
           
    run()
        

def save_data(desc) -> None:
    cls()

    print(bold(desc), end=""), sps(1)
    
    #Warning for user
    while True:
            fail_safe = input("  \u26A0 Previous save will be overwritten. Enter 'save' to proceed, else 'exit': ")
            
            match fail_safe:
                case "exit": print(), run()
                
                case "save": break
                
                case _:
                    print("\n  \u26A0 Invalid command. Try again\n")

    #Dumps tasks attributes as dicts in json.file
    with open("user_data.json", "w") as file:
        to_save = []

        for task in task_list:
            to_save.append(vars(task))
        
        json.dump(to_save, file, indent= 4)
    
    print("\n  Data has been saved\n")
    
    run()


def load_data(desc) -> None:
    cls()
    global task_list

    print(bold(desc), end=""), sps(1)
    
    #Warning for user
    while True:
        fail_safe = input("  \u26A0 Current data will be overwritten. Enter 'load' to proceed, else 'exit': ")
        
        match fail_safe:
            case "exit": print(), run()
            
            case "load": break
            
            case _:
                print("\n  \u26A0 Invalid command. Try again\n")

    #New tasks with identical properties as saved ones are created
    #task_list is cleared and is intsead filled with newly created copies
    
    with open("user_data.json", "r") as file:
        
        try:
            to_load = json.load(file)
            task_list.clear()
        
        except: 
            print("\n  \u26A0 Invalid command. No saved data\n")
            run()

        for task in to_load:
            loaded_task = cl.Task(task["name"], task["description"], task["deadline"])
            loaded_task.created = task["created"]
            task_list.append(loaded_task)
        
        print("\n  Saved data has been loaded\n")
    
    run()
 

cmnd_dict = {
    "new": [create_task, cmnd_desc_file[0]],

    "see": [show_tasks, cmnd_desc_file[1]],

    "del": [remove_task, cmnd_desc_file[2]],

    "help": [show_cmnd, cmnd_desc_file[3]],
    
    "save": [save_data, cmnd_desc_file[4]],
    
    "load": [load_data, cmnd_desc_file[5]],
    
    "exit": ["", cmnd_desc_file[6]]
}


run()
