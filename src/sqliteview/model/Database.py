import sqlite3

from sqliteview.sqlite.Command import Command
from sqliteview.model.Table import Table

class Database():
    def __init__(self, path) -> None:
        self.tables = []
        self.dbHandle = sqlite3.connect(path)
        self.dbCursor = self.dbHandle.cursor()
        self._processTables()
        
    def _processTables(self):
        tables = self.dbCursor.execute(Command.TABLE_NAMES).fetchall()
        for table in tables:
            self._createTable(table[0])

    def _createTable(self, tableName):
        rows = self.dbCursor.execute(Command.SELECT_ALL.substitute(table=tableName)).fetchall()
        columns = self._processColumns(self.dbCursor.description)
        t = Table(tableName, columns)
        self.tables.append(t)

    def _processColumns(self, columns):
        result = []
        for row in columns:
            result.append(row[0])
        return result   
    
    def getTableNames(self):
        result = []
        for table in self.tables:
            result.append(table.name)
        return result
    
    def getColumnsForTable(self, tableName):
        result = []
        for table in self.tables:
            if(tableName == table.name):
                result = table.columns
        return result
    
    def getRowsForTable(self, table):
        cmd = Command.SELECT_ALL.substitute(table=table)
        rows = self.dbCursor.execute(cmd).fetchall()
        return rows
    
    def getRowCountForTable(self, table):
        cmd = Command.COUNT_ROWS.substitute(table=table)
        count = self.dbCursor.execute(cmd).fetchall()
        return count[0][0]