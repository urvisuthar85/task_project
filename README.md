# task_project

#create viretual envirement

virtualenv -p python3 venv

#go to directry

source venv/bin/activate

#install requirement files

pip install -r requirments.txt

# stay that directry with manage.py in project if not then 
 
cd project

#Runserve

python manage.py runserver
