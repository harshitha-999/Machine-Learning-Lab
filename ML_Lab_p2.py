#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3


# In[3]:


conn = sqlite3.connect('exp2.db')
print("opened database")


# In[5]:


conn.execute('''CREATE TABLE COMPANY2
(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50),
SALARY REAL);''')
print("Table created");


# In[6]:


conn.execute("Insert into COMPANY2 (ID , NAME ,AGE, ADDRESS ,SALARY)             VALUES (1,'Paul',32, 'California', 20000.00)");
conn.execute("Insert into COMPANY2 (ID , NAME ,AGE, ADDRESS ,SALARY)             VALUES (2,'Allen',35, 'Texas', 15000.00)");
conn.execute("Insert into COMPANY2 (ID , NAME ,AGE, ADDRESS ,SALARY)             VALUES (3,'Teddy',23, 'Norway', 20000.00)");
conn.execute("Insert into COMPANY2 (ID , NAME ,AGE, ADDRESS ,SALARY)             VALUES (4,'Mark',25, 'Rich-Mond', 65000.00)");
conn.commit()
print("Records created sucessfully");


# In[7]:


for row in conn.execute('select * from COMPANY2'):
  print(row)


# In[8]:


conn.commit()


# In[9]:


conn.close()


# In[ ]:




