# 📒 ItJournal - Django Application

  This is a simple Python and Django App that allows you to create news, articles and other notes with filtering by categories.

## :triangular_ruler: Project stack: 
  - Python 3.13 (Django, Pillow)
  - Django Templates, HTML5, CSS (Bootstrap 5.3.3)
  - DB SQLite
  - etc...

## 🔧 Requirements

  Before you begin, make sure you have the following installed:

  - Python (version 3.13 or higher recommended)
  - pip (Python package manager)
  - Git (version control system)

## 🔨 Setup

  - The first thing to do is to clone the repository:

  ```sh
  $ git clone https://github.com/ekatylynx/itjournal_app_django.git
  $ cd itjournal_app_django
  ```


  - Create a Python virtual environment and activate it

  ```
  $ python -m venv venv
  $ venv\Scripts\activate.bat - for Windows / source venv/bin/activate - for Linux and MacOS
  ```
  

  - Installing project dependencies

  ```
  $ pip install -r requirements.txt
  ```


  - Make sure you are in the directory where the file `manage.py` is located and apply database migrations:

  ```sh
  $ cd .\ItJournalApp\
  python manage.py migrate
  ```


  - Create a superuser to access the Django admin panel:

  ```sh
  python manage.py createsuperuser
  ```


  - Start the Django development server:

  ```
  $ python manage.py runserver
  ``` 


  - Open your browser and go to `http://127.0.0.1:8000/` to see your application.


  ## 📝 Feedback

  Now your project is installed and ready to work. You can start developing or testing the application. If you have any questions or problems, please create an issue in this repository
