import time
import sys
import argparse

from constants import *
from databaseActions import *
from commands import *


def registerCommands(parser):
    actions_subparser = parser.add_subparsers(help="task actions", dest="command")
    actions = {}
    for command_key, command_info in commands.items():
        actions[command_key] = actions_subparser.add_parser(
            command_key, help=command_info.get("help_text", "")
        )
        if "arguments" in command_info:
            for argument_key, argument_info in command_info["arguments"].items():
                if argument_info["kind"] == "positional":
                    actions[command_key].add_argument(
                        argument_key,
                        type=toType(argument_info["type"]),
                        nargs=argument_info["nargs"],
                    )
                elif argument_info["kind"] == "flag":
                    actions[command_key].add_argument(
                        f"--argument_key",
                        *argument_info["flag_aliases"],
                        type=toType(argument_info["type"]),
                        nargs=argument_info["nargs"],
                    )


def processInput(args, conn):
    if args.command in commands:
        commands[args.command]["function_code"](args, conn)
    else:
        print(f"😺 {TOOL_NAME} v0.0.1!")
        print("use --help to show all commands.\n")
        print("all tasks:")
        printTasks(conn, TABLE_NAME)
