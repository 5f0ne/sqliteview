import os
import time

from datetime import datetime

from hash_calc.HashCalc import HashCalc


class Controller():
    def __init__(self, path) -> None:
        self.startTime = time.time()
        self._path = path
        self._hash = HashCalc(self._path)

    def printHeader(self):
        print("################################################################################")
        print("")
        print("sqliteview by 5f0")
        print("Visualizes SQLite files")
        print("")
        print("Current working directory: " + os.getcwd())
        print("")
        print("-->    Path: " + self._path)
        print("-->     MD5: " + self._hash.md5)
        print("-->  SHA256: " + self._hash.sha256)
        print("")
        print("Datetime: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print("")
        print("################################################################################")

    def printExecutionTime(self):
        end = time.time()
        print("################################################################################")
        print("")
        print("Execution Time: " + str(end-self.startTime)[0:8] + " sec")
        print("")

    def printTableNames(self, tableNames):
        print("")
        print("Tables")
        print("---")
        for name in tableNames:
            print("     --> " + name)

    def printTableInfoHeader(self):
        print("")
        print("")
        print("Table Information")
        print("---")
        print("")

    def printTableInformation(self, name, columns, count, rows):
        print(" --> Table: " + name)
        print("   Columns: " + str(columns))
        print(" Row Count: " + str(count))
        print("       ---")
        if(count == 0):
            print("       No rows in table!")
        else:
            for row in rows:
                print("       " + str(row))
        print("       ---")
        print("")
        print("")