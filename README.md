<h1 align="center">Django CustomUser DRF App</h1>
<h3 align="center">A base project for custom authentication with api and tests</h3>
<p align="center">
<a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
<a href="https://www.djangoproject.com/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-original.svg" alt="django" width="40" height="40"/> </a>
<a href="https://www.django-rest-framework.org/" target="_blank"> <img src="https://www.django-rest-framework.org/img/logo.png" alt="sqlite" width="90" height="40"/> </a>
<a href="https://www.w3.org/html/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank">
</a>
<a href="https://www.sqlite.org/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="sqlite" width="40" height="40"/> </a>
</p>

### Overview
- [Overview](#overview)
- [Features](#features)
- [Setup](#setup)
- [Getting ready](#getting-ready)
- [options](#options)
- [Api and Documents](#api-and-documents)
- [Reformat and check](#reformat-and-check)
- [Database schema](#database-schema)
- [Todo](#todo)
- [Bugs or Opinion](#bugs-or-opinion)


### Features
- Django LTS
- Custom User Model
- Profile model
- Signal attachments
- Django RestFramework
- Token Authentication
- JWT Authentication
- APi Docs
- Black
- Flake8
- Tests

### Setup
To get this repository, run the following command inside your git enabled terminal
```bash
git clone https://github.com/alibigdeli/Django-CustomUser-DRF-App
```

### Getting ready
Create an enviroment in order to keep the repo dependencies seperated from your local machine.
```bash
python -m venv venv
```

Make sure to install the dependencies of the project through the requirements.txt file.
```bash
pip install -r requirements.txt
```

Once you have installed django and other packages, go to the cloned repo directory and run the following command

```bash
python manage.py makemigrations
```

This will create all the migrations file (database migrations) required to run this App.

Now, to apply this migrations run the following command
```bash
python manage.py migrate
```

### options
you can use the createsuperuser option to make a super user.
```bash
python manage.py createsuperuser
```

And lastly let's make the App run. We just need to start the server now and then we can start using our Authentication App. Start the server by following command

```bash
python manage.py runserver
```

Once the server is up and running, head over to http://127.0.0.1:8000 for the App but it will be empty!

### Api and Documents
in order to use the api in document format you can simply head to this url

http://127.0.0.1:8000/swagger/

<p align="center">
<img src="https://user-images.githubusercontent.com/29748439/145015922-9f1d4717-796d-40db-8763-be303ef59bd0.png" alt="database schema" width="720"/>
</p>


or if you prefer redoc you can use :

http://127.0.0.1:8000/redoc/
<p align="center">
<img src="https://user-images.githubusercontent.com/29748439/145016099-db5ffdfe-7911-4af8-88c8-6df19031b925.png" alt="database schema" width="720"/>
</p>
and for importing the api into your postman the link for that will be this:

http://127.0.0.1:8000/swagger/api.json


### Reformat and check
If you want your code to be check by pep8 and all the guide lines, there are two packages added to requirements in order to check and reformat code.
you can use it by this command:
```bash
black -l 79 . && flake8
```


### Database schema
A simple view of the project model schema.
<p align="center">
<img src="https://user-images.githubusercontent.com/29748439/145015815-378fd529-74f9-49f2-9856-2db6f228e3b7.png" alt="database schema" width="300"/>
</p>

### Todo
- [x] complete the documentation
- [ ] add api tests
- [ ] create a video tutorial

### Bugs or Opinion
Feel free to let me know if there are any problems or any request you have for this repo.
