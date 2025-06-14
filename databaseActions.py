# Task actions module
# Please note: safe values are assumed throughout.

from tabulate import tabulate
from constants import *


def insertTask(conn, table, name, time, status):
    """
    Inserts a task to a table given three variables:
    - name, the name for the task (string)
    - time, a time in unix millis (int)
    - status, a task's binary status (int)
    """

    cursor = conn.cursor()

    insert_query = f"""
    INSERT INTO {table} ({TASK_NAME}, {TASK_TIME}, {TASK_STATUS})
    VALUES (?, ?, ?);
    """

    cursor.execute(insert_query, (name, time, status))
    conn.commit()


def deleteByProperty(conn, table, property, value):
    """
    Deletes all tasks from a table that match a query composed of:
    - property, a table header (string)
    - value, of property
    """

    cursor = conn.cursor()

    delete_query = f"DELETE FROM {table} WHERE {property} = ?"
    cursor.execute(delete_query, (value,))
    conn.commit()


def printTasks(conn, table):
    """
    Prints all tasks from a table
    """

    cursor = conn.cursor()

    select_query = f"SELECT * FROM {table};"
    cursor.execute(select_query)
    tasks = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]

    print(tabulate(tasks, headers=headers, tablefmt="grid"))
