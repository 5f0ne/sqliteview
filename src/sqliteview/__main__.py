import sys

import argparse

from sqliteview.Controller import Controller
from sqliteview.model.Database import Database

def main(args_=None):
    """The main routine."""
    if args_ is None:
        args_ = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "-p", type=str, required=True, help="Path to SQLite file")
    args = parser.parse_args()

    ctrl = Controller(args.path)
    ctrl.printHeader()

    db = Database(args.path)

    names = db.getTableNames()

    ctrl.printTableNames(names)
    ctrl.printTableInfoHeader()

    for name in names:
        count = db.getRowCountForTable(name)
        rows = db.getRowsForTable(name)
        columns = db.getColumnsForTable(name)
        ctrl.printTableInformation(name, columns, count, rows)

    ctrl.printExecutionTime()

if __name__ == "__main__":
    sys.exit(main())
