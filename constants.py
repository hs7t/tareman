# Tool name
TOOL_NAME = "tareman"

# Database constants
DATABASE_FILENAME = "tasks.db"
TABLE_NAME = "Tasks"

# Task status constants
STATUS_PENDING = 0
STATUS_DONE = 1
TABLE = {
    "name": "Tasks",
    "headers": {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "name": "TEXT NOT NULL",
        "time": "INTEGER",
        "status": "INTEGER",
    },
}
