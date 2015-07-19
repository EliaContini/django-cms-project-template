
# Set up the development environment on Ubuntu 14.04 LTS

sudo apt-get install libxml2-dev libxslt1-dev python-dev

# Before using

Assume that the name of your project is "my_project"

   1. Download the zip, decompress and rename the folder as "my_project"

   2. Rename subfolder "project_name" with the name of your project (e.g. "my_project")

   3. Rename subfolder "my_project/project_name" with the name of your project (e.g. "my_project/my_project")

   4. Open "my_project/manage.py". In line 6 replace "project_name.settings" with "my_project.settings"

   5. Open "my_project/project_name/settings.py".

      1. IMPORTANT Line 19: change SECRET_KEY

      2. Line 87: replace 'project_name.urls' with 'my_project.urls'

      3. Line 91: replace 'project_name.wsgi.application' with 'my_project.wsgi.application'

      4. Line 131: customize DBMS settings

      5. Line 141: customize languages and timezone settings

   6. Open "run_dev_server.sh". In line 9 replace "project_name" with "my_project"

# Setup

Open the console and type cd /path/to/my_project (replace /path/to/ with the path on your computer)

Type ./install.sh and wait util the process is eneded

Then in the console type:

   1. cd my_project

   2. ./../env/bin/python manage.py migrate

   3. ./../env/bin/python manage.py createsuperuser

   4. ./../env/bin/python manage.py cms check

   5. cd ..

   6. ./run_dev_server.sh

   7. Open a browser, go to 127.0.0.1:8000 and you should see the Django CMS welcome page

