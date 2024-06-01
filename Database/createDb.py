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


#------------------------------------------------------------#
# Insert sample data into MasterTasks table
c.execute('''
    INSERT INTO MasterTasks (name, description, priority, completed, sessions, due_date, frequency)
    VALUES ('Task 2', 'Description 2', 'Medium', 0, 'Session 2', '2022-01-03', 'Weekly')
''')

c.execute('''
    INSERT INTO MasterTasks (name, description, priority, completed, sessions, due_date, frequency)
    VALUES ('Task 3', 'Description 3', 'Low', 0, 'Session 3', '2022-01-05', 'Monthly')
''')

# Insert sample data into SubTasks table
c.execute('''
    INSERT INTO SubTasks (masterTaskId, name)
    VALUES (2, 'Subtask 2')
''')

c.execute('''
    INSERT INTO SubTasks (masterTaskId, name)
    VALUES (2, 'Subtask 3')
''')

c.execute('''
    INSERT INTO SubTasks (masterTaskId, name)
    VALUES (3, 'Subtask 4')
''')

c.execute('''
    INSERT INTO SubTasks (masterTaskId, name)
    VALUES (3, 'Subtask 5')
''')
# Insert sample data into Objective Tasks table

c.execute('''
    INSERT INTO Objectives (subTaskId, name)
    VALUES (1, 'Objective 1')
''')

c.execute('''
    INSERT INTO Objectives (subTaskId, name)
    VALUES (1, 'Objective 2')
''')
# Insert sample data into sessions table
c.execute('''
    INSERT INTO Sessions (subTaskId, dateTime, duration)
    VALUES (1, '2022-01-03 10:00:00', 60)
''')

#------------------------------------------------------------#

# Save (commit) the changes
conn.commit()

# Query the tasks
c.execute('SELECT * FROM MasterTasks')
rows = c.fetchall()

for row in rows:
    print(row)

# Close the connection
conn.close()