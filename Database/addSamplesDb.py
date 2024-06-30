import sqlite3

# Connect to the database
conn = sqlite3.connect('Database/tasks.db')

# Create a cursor object to execute SQL queries
c = conn.cursor()

# Define your data
data = ('John Doe', 25, 'john.doe@example.com')

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

# Insert sample data (Shower,Brush,Excersice,Face,Bed,Laundry[weekly],Cleaning,) into sessions table
c.execute('''
    INSERT INTO Sessions (subTaskId, dateTime, duration)
    VALUES (1, '2022-01-03 10:00:00', 60)
''')
#------------------------------------------------------------#
# Commit the changes to the database
conn.commit()

# Close the cursor and the connection
c.close()
conn.close()