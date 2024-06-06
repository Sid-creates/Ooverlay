import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('Database/tasks.db')

# Create a cursor object
c = conn.cursor()

# Create MasterTasks table
c.execute('''
    CREATE TABLE MasterTasks (
        id INTEGER PRIMARY KEY,
        name TEXT,
        description BLOB,
        priority TEXT,
        completed BOOLEAN,
        sessions TEXT,
        due_date TEXT,
        frequency TEXT
    )
''')

# Create SubTasks table
c.execute('''
    CREATE TABLE SubTasks (
        id INTEGER PRIMARY KEY,
        masterTaskId INTEGER,
        name TEXT,
        FOREIGN KEY(masterTaskId) REFERENCES MasterTasks(id)
    )
''')

# Create Objectives table
c.execute('''
    CREATE TABLE Objectives (
        id INTEGER PRIMARY KEY,
        subTaskId INTEGER,
        name TEXT,
        FOREIGN KEY(subTaskId) REFERENCES SubTasks(id)
    )
''')

# Create Sessions table
c.execute('''
    CREATE TABLE Sessions (
        id INTEGER PRIMARY KEY,
        subTaskId INTEGER,
        dateTime TEXT,
        duration INTEGER,
        FOREIGN KEY(subTaskId) REFERENCES SubTasks(id)  
    )
''')

# Create Repeating tasks table, type is either daily, weekly(mon,tue,wed,thu,fri), monthly(01,31), or yearly(01-01, 12-31) repeating on date
c.execute('''
    CREATE TABLE RepeatingTasks (
        id INTEGER PRIMARY KEY,
        frequency TEXT,
        time TEXT,
        duration INTEGER
    )
''')



# Save (commit) the changes
conn.commit()

# Query the tasks
c.execute('SELECT * FROM MasterTasks')
rows = c.fetchall()

for row in rows:
    print(row)

# Close the connection
conn.close()