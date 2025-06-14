import time

from constants import *
from databaseActions import *
from utilities import *


def new_task(args, conn):
    if args.name is not None:
        task_name = args.name
    else:
        task_name = input("give your task a name > ")
    current_time = int(time.time())
    task_status = STATUS_PENDING

    insertTask(conn, TABLE_NAME, task_name, current_time, task_status)
    print(f"added a new task named {task_name}!")

def delete_task(args, conn):
    if args.property is not None:
        task_property = args.property
        if task_property not in PROPERTY_OPTIONS:
            raise Exception("oh no! it looks like that's not a valid property.")
    else:
        task_property = listSelect(
            PROPERTY_OPTIONS,
            intro="properties by which to select tasks:",
            names_allowed=True,
        )
        if task_property == None:
            raise Exception("ah! that's not an option.")

    if args.value is not None:
        task_property_value = args.value
    else:
        task_property_value = input("a value to look for: ")

    deleteByProperty(conn, TABLE_NAME, task_property, task_property_value)
    print("\n done! all tasks:")
    printTasks(conn, TABLE_NAME)

def all_tasks(args, conn):
    print("all tasks:")
    printTasks(conn, TABLE_NAME)

commands = {
    "new": {
        "help_text": "add a new task",
        "function_code": new_task,
        "arguments": {
            "name": {
                "help_text": "a name for your task",
                "kind": "positional",
                "type": "str",
                "nargs": "?",
            },
        },
    },
    "delete": {
        "help_text": "delete tasks",
        "function_code": delete_task,
        "arguments": {
            "property": {
                "help_text": "a property by which to select tasks",
                "kind": "positional",
                "type": "str",
                "nargs": "?",
            },
            "value": {
                "help_text": "a property value to look for",
                "kind": "positional",
                "type": "str",
                "nargs": "?",
            },
        },
    },
    "all": {
        "help_text": "show all tasks",
        "function_code": all_tasks,
    },
}