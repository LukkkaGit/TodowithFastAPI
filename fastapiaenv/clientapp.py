import requests

class TaskClient:
    BASE_URL = "http://127.0.0.1:8000/tasks/"

    def create_task(self, **task):
        return requests.post(f"{TaskClient.BASE_URL}", json=task).json()

    def get_task(self, task_id):
        return requests.get(f"{TaskClient.BASE_URL}{task_id}").json()

    def get_all_tasks(self):
        return requests.get(f"{TaskClient.BASE_URL}").json()

    def update_task(self, task_id, **task):
        return requests.put(f"{TaskClient.BASE_URL}{task_id}", json=task).json()

    def delete_task(self, task_id):
        return requests.delete(f"{TaskClient.BASE_URL}{task_id}").json()
    

client = TaskClient()



def checker(id):
    tasks = client.get_all_tasks()
    task_match = False

    for task in tasks:
        if task["id"] == id:
            task_match = True
    return task_match




while True:
    a = input("What do you want:\n 1. Create \n 2. Read One Task \n 3. Read All \n 4. Update \n 5. Delete \n 6. Exit \n N: ")
    
        
    try:
        a = int(a)   

        if a == 1:
            i = int(input("Please input task id: "))
            tasks = client.get_all_tasks()
            check = checker(i)

            if check is True:
                print("Task is already added. If you want to update Task choose N4.")
                break
            else:
                t = input("Please input task title: ")
                c = str(input("Please input task completed: (True/False): "))
                client.create_task(id=i, title=t, completed=c)
                print("Successful Completed!")
                continue
    
        if a == 2:
            i = int(input("Please input task id: "))
            check = checker(i)
            if check is False:
                print("Task is not exist. If you want to create Task choose N1.")
            else:
                print(client.get_task(i))
    
        if a == 3:
       
            tasks = client.get_all_tasks()
            for index,task in enumerate(tasks,1):
                print(index,task)
            
            print("\n")  

    
        if a == 4:
            i = int(input("Please input task id: "))
            check = checker(i)
            if check is False:
                print("Task is not exist. If you want to create Task choose N1.")
            else:
                t = input("Please input task title: ")
                c = str(input("Please input task completed: (True/False): "))
                client.update_task(i, id=i, title=t, completed=c)
                print("Task successful updated.")
    
        if a == 5:
            i = int(input("Please input task id: "))
            check = checker(i)
            if check is False:
                print("Task is not exist. If you want to create Task choose N1.")
            else:
                client.delete_task(i)
                print(f"Task {i} successful deleted!")

        if a == 6:
            print("Good bye")
            break
   
    except ValueError:
        print("Please enter only number!!!")
        continue

    if a < 0 or a > 6:
        prompt_text = "Invalid input. Please choose a number from 1 to 6."
        print(prompt_text)
task = client.get_task(1)
print(task)


