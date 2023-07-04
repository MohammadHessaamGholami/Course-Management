**Course Management System**

this is a project created for database laboratory.

in the root folder of project do the following:
1. activate a virtualenv with python version 3
    `virtualenv venv -p python3`
    then activate it (in linux do  `source venv/bin/activate`)
2. in course_management/settings folder add a file dev.py
3. `pip install -r requirements.txt`
4. `python manage.py migrate`
5. `python manage.py runserver`
6. open browser and go to localhost:8000
