from string import Template

class Command():
    TABLE_NAMES = "SELECT name FROM sqlite_master where type = 'table'"
    SELECT_ALL = Template("SELECT * FROM $table")
    COUNT_ROWS = Template("SELECT COUNT(*) from $table")