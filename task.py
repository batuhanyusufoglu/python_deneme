tasks=[]
def add_task(task):
    tasks.append(task)
    print("successfully added")
def complete_task(task_index):
    if task_index >= 0 and task_index < len(tasks) :
        tasks[task_index] += " - completed"
    else:
        print("invalid index")
def display_tasks() :
  if tasks:
    print("Tasks : ")
    for index, task in enumerate(tasks) :
        print(str(index + 1) + "." + task)
  else :
     print("no tasks has been added")
def main() :
   while True:
    choice=input("Welcome to the App. Please choose what to do: 1:add task 2: complete task 3:display tasks 4:exit")
   
    if choice=="1":
      task_to_add=input("please enter the name of the task: ")
      add_task(task_to_add)
    elif choice=="2" :
      index_task=int(input("enter the index of the task"))
      complete_task(index_task - 1)
    elif choice=="3" :
      display_tasks()
    elif choice=="4" :
      print("thank you for using the app")
      break
    else:
      print("invalid input")
if __name__ == "__main__":
    main()
      
   