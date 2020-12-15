# Welcome to the Digimon app
this app uses Django web framework and python 3.8
## please follow instructions below to run the app locally:
1. install python on your machine from  [here](https://python.org/downloads/ ) .
2. install virtualenv using: `pip install virtualenv`
3. directory style is optional for the project but the prefered style is as follows:    	
~~~~
project_main_directory/
| env/
| src/
~~~~
4. cd to the env directory and create the virtualenv using :`virtualenv .`
5. if you're using Linux OS activate the virtualenv using: `source bin/activate`
6. if you're using Windows OS activate the virtualenv using: `.\bin\activate`
7. then cd out of env directorey and head to src where you should clone the app
8. after cloning cd to the cloned project and run the command: `pip install -r docs/requirements.txt`
9. migrate the database using: `python manage.py migrate`
10. create superuser using: `python manage.py createsuperuser` and follow the prompt
11. start the server using: `python manage.py runserver`

Enjoy exploring Digimons :) !
