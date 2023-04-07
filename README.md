# Description

Visualize SQLite files

# Installation

`pip install sqliteview`

# Usage

**From command line:**

`python -m sqliteview --path PATH`

| Option | Short | Type | Default | Description |
|---|---|---|---|---|
|--path | -p | String | - | Path to SQLite file |


# Example

`python -m sqliteview -p path/to/example.db`

```
################################################################################

sqliteview by 5f0
Visualizes SQLite files

Current working directory: path/to/sqliteview

-->    Path: path/to/example.db
-->     MD5: faca5057ffe0b458638c7071bbbae313
-->  SHA256: e0bd07d00cf638d24b10235c02edbb67534ec821c11fc606dbfd5c4ca364c06c

Datetime: 01/01/1970 16:17:18

################################################################################

Tables
---
     --> fish
     --> dog


Table Information
---

 --> Table: fish
   Columns: ['id', 'name', 'species', 'tank']
 Row Count: 2
       ---
       (1, 'Sammy', 'shark', 1)
       (3, 'Carl', 'goldfish', 8)
       ---

 --> Table: dog
   Columns: ['id', 'name', 'species', 'garden']
 Row Count: 2
       ---
       (1, 'Bill', 'shepard', 1)
       (2, 'Tom', 'little', 7)
       ---


################################################################################

Execution Time: 0.000972 sec
```


# License

MIT