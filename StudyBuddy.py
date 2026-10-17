import json
print("╔══════════════════════════╗")
print("║        StudyBuddy        ║")
print("║ Plan Today, Win Tomorrow ║")
print("╚══════════════════════════╝")
try:
    with open("tasks.json", "r") as f:
        task = json.load(f)
except FileNotFoundError:
    task = []
while True: 
   print(" 1. Add a task")
   print(" 2. View tasks")
   print(" 3. Mark task as done")
   print(" 4. Delete a task")
   print(" 5. Exit")
   n = input("enter your choice: ")
   if n == "1" :
        name = input("enter task name: ")
        task.append({"name": name, "done": False}) 
        print("task added!")
   elif n == "2" :
        if not task:
             print("no task yet")
        else:
            for number, item in enumerate (task,1):
             if item["done"]:
               mark = "x"
             else:
                 mark = " "
             print(f"{number}. [{mark}] {item['name']}")
   elif n == "3":
          num = int(input("enter task number: "))
          if num < 1 or num > len(task):
              print("invalid task number")
          else:
              task[num -1]["done"] = True 
              print("task marked as done!")
   elif n == "4":
          num = int(input("enter task number: ")) 
          if num < 1 or num > len(task):
              print("invalid task number")
          else:
              task.pop(num - 1)
              print("task deleted!")
   elif n == "5" :
        with open("tasks.json", "w") as f:
         json.dump(task, f)
         print("Goodbye")
         break
   else:
        print("Invalid Choice ")




