from config import client
from planner import Planner

planner = Planner(client)

while True:
    task = input("\nTask: ")

    if task.lower() == "exit":
        break

    plan = planner.create_plan(task)

    print("\nExecution Plan:\n")

    for i, step in enumerate(plan, start=1):
        print(f"{i}. {step}")