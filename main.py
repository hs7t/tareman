import sqlite3

from constants import *
from databaseActions import *
from cli import *


def setUpDB(connection, table_name):
    cursor = connection.cursor()

    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        {TASK_ID} INTEGER PRIMARY KEY AUTOINCREMENT,
        {TASK_NAME} TEXT NOT NULL,
        {TASK_TIME} INTEGER,
        {TASK_STATUS} INTEGER
    );
    """
    cursor.execute(create_table_query)
    connection.commit()


def main():
    parser = argparse.ArgumentParser()
    registerCommands(parser)

    # Register debug mode flag
    parser.add_argument('-d', '--debugmode', action="store_true", help="show errors")

    args = parser.parse_args()

    # Hide tracebacks if debug mode flag not present
    if not getattr(args, "debugmode", False):
        sys.tracebacklimit = 0

    with sqlite3.connect(DATABASE_FILENAME) as conn:
        setUpDB(conn, TABLE_NAME)
        processInput(args, conn)



if __name__ == "__main__":
    main()
