# hextrack-server

Time tracking system for individuals and companies. Server side.

# Dev usage

## Requirements

- python 3.6 or higher
- virtualenv for python 3.6 or higher
- docker and docker-compose

# Installation and run

- Create virtualenv in somewhere for your project and activate
- Go to directory that contains `src` dir
- Execute: `pip install -r requirements.txt` to install all required staff
- Execute: `docker-compose up -d`. If you are not properly configured your docker, it may requires `sudo` or something else
- Go to `src` directory
- Set environment variable 'ENV' to 'dev': `export ENV=dev` or with a command specific to your OS
- Execute: `python manage-py migrate` to apply migrations
- Execute: `python manage.py createsuperuser` to create superuser. Optional.
- Execute: `python manage.py runserver`
- Enjoy hextrack-server