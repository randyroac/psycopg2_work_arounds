
###Fix your psycopg2 installing issues


###Fastest way (Recommended For Pycharm users)


###From your original Terminal (not in a third-party IDE) type the following:

pip3 uninstall   #whatever non-working latest version that you previously installed

###then

pip3 Install psycopg2-binary==2.8.6


###OR 

###Adapt your bash script to build your local virtual environment with pipenv:

pipenv install --verbose -r ./requirements.txt  # <-- psycopg2-binary>=2.9.1 is installed

### MacOS High Sierra 10.13.6 Hack
if [[ $(sw_vers -productVersion) == "10.13.6" ]]
then
sw_vers
pipenv uninstall --verbose --skip-lock "psycopg2-binary>=2.9.1"
pipenv install --verbose --skip-lock "psycopg2-binary==2.8.6"
fi

pipenv shell python manage.py runserver



###If you haven't installed pipenv you can do so with the following Terminal statement: 


pip3 install pipenv



###if you are having problems installing pipenv then check out this link that works!
### https://stackoverflow.com/questions/67733566/how-to-use-pipenv-on-mac
