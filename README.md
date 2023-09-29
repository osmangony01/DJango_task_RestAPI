## Task Manager

- First of All, Clone the project given github repository

- If you do not have python environment and then create environment first

- Then install necessary packages like pip, django, pillow, psycopy2, python-dotnet, djangorestframework, markdown, django-filter 

- After that, Configure the database setting for PostgreSQL in env file and add or changes other necessary configuration in setting.py file if you have needed

- Create makemigrations and migrate


- For this assignment task, I create there app like **authAPP** for user authentication, **task** for task management, **apiApp** for handling Django RestAPI. For task app, I create two model one for task data and another one is for task images , task images model have foreign key relation with task model


### Here I developed Django RestAPI
 
- Task API are - 
  
  => Handle method (GET, POST) = http://127.0.0.1:8000/api/task/

  => Handle method (GET, PUT, DELETE) each task = http://127.0.0.1:8000/api/task/{key}/

- TaskImage API are -
  => Handle method (GET) = http://127.0.0.1:8000/api/taskImage/

---
    
Github Link : https://github.com/osmangony01/DJango_task_RestAPI 
