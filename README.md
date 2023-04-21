- **Social Website**: Create a website to bookmark and share images
  - Implement authentication using the Django authentication framework
  - Extend the user model with a custom profile model
  - Use the Diango messages framework
  - Build a custom authentication backend
  - Implement social authentication (OAuth2) with Facebook, Twitter, and Google using [Python Social Auth](https://github.com/python-social-auth/social-app-django)
  - Use [django-extensions](https://github.com/django-extensions/django-extensions) to run the development server through HTTPS
  - Generate image thumbnails with [easy-thumbnails](https://github.com/SmileyChris/easy-thumbnails)
  - Implement many-to-many relationships in models
  - Build a JavaScript bookmarklet with JavaScript and Django
  - Add asynchronous HTTP requests with the JavaScript Fetch API and Django
  - Implement infinite scroll pagination
  - Build a user follow system
  - Create a user activity stream and optimize QuerySets
  - Learn to use Django signals
  - Use [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar) to obtain relevant debug information
  - Count image views with [Redis](https://redis.io/)
  - Build an image ranking with Redis


## Start project using Docker
1. The first thing to do is to clone the repository:
    ```
    git clone https://github.com/marik177/-django_social_bookmark.git
   ```
2. Using the Dockerfile and docker-compose.yaml run the project:
   ```
   docker-compose up --build
   ```
3. In new terminal window run command:
   ````
   docker-compose exec web sh
   ````
4. Run the migrations in the container, create a superuser, and populate the database with initial data:
   ````
   python manage.py migrate
   
   python manage.py createsuperuser
   
   python3 manage.py loaddata mysite_data.json
   ````



## Start the project without Docker:
1. The first thing to do is to clone the repository:
    ```
    git clone https://github.com/marik177/-django_social_bookmark.git
    
    cd mysite
    ```
2. Create a virtual environment to install dependencies in and activate it:
    ```
    python3 -m venv venv
   
    source venv/bin/activate
    ```   
3. Then install the dependencies:
    ```
   (env)$ pip install -r requirements.txt
    ```
    &emsp; Note the (env) in front of the prompt.

    &emsp; This indicates that this terminal session operates in a virtual environment set.


4. Once pip has finished downloading the dependencies make migrations:
    ```
    python3 manage.py migrate
    ```
5. Create superuser:
    ````
    python3 manage.py createsuperuser
    ````
   
6. Load testing data:
    ````
    python3 manage.py loaddata mysite_data.json
    `````

7. And finally run test server:
    ````
    (env)$ python3 manage.py runserver
