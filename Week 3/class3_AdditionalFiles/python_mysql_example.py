#!/usr/bin/env python
# coding: utf-8

# In[2]:


import mysql.connector as con


# In[3]:


mydb=con.connect(host="localhost",user="root",passwd="admin", buffered=True)


# In[4]:


mycursor = mydb.cursor()


# In[5]:


cmd_1 = "SHOW DATABASES"
mycursor.execute(cmd_1)


# In[6]:


for db in mycursor:
    print(db)


# In[7]:


mycursor.execute("DROP SCHEMA IF EXISTS Student;")
mycursor.execute("CREATE DATABASE `Student`")
mycursor.execute("CREATE TABLE Student.Students (name VARCHAR(255), address VARCHAR(255))")


# In[9]:


sql = "INSERT INTO Student.Students (name, address) VALUES (%s, %s)"
value = ("Rijesh", "Minnetonka")
mycursor.execute(sql, value)
mydb.commit()


# In[10]:


sql = "INSERT INTO Student.Students (name, address) VALUES (%s, %s)"
values = [
  ('Meen', 'Duluth'),
  ('Amanda', 'Minneapolis'),
  ('Avinash', 'Frisco')]

mycursor.executemany(sql, values)
mydb.commit()


# In[ ]:




