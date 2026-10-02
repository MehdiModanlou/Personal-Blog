# Django Blog

A full-featured blog application built with Django. This project focuses on backend development, authentication, CRUD operations, database relationships, search, comments, categories, and automated testing.

## Features

* Custom user model based on Django's `AbstractUser`
* User registration and authentication
* User profile pages
* Create, read, update, and delete blog posts
* Category-based post filtering
* Search posts by title and body
* Create, update, and delete comments
* Pagination for comments
* Django class-based views
* Form validation
* Automated tests for models, forms, views, and URLs

## Tech Stack

* Python
* Django
* SQLite/PostgreSQL depending on environment
* HTML
* Django Templates
* Django Test Framework

## Project Structure

```text
p_blog/
├── accounts/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── blog/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── templates/
├── manage.py
└── requirements.txt
```

## Main Django Apps

### Blog

The `blog` app contains the main blog functionality:

* Blog post management
* Categories
* Comments
* Search
* Pagination
* Post permissions and CRUD operations

### Accounts

The `accounts` app handles:

* Custom user model
* User registration
* User profiles
* Authentication-related functionality

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd p_blog
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Create a superuser:

```bash
python manage.py createsuperuser
```

Start the development server:

```bash
python manage.py runserver
```

Open the application at:

```text
http://127.0.0.1:8000/
```

## Running Tests

Run the complete test suite:

```bash
python manage.py test
```

The current project test suite contains **69 tests, all passing**.

## Testing Coverage

The test suite covers:

* Blog models
* Blog forms
* Blog views
* Blog URLs
* Account models
* Account forms
* Account views

The goal of the tests is to verify application behavior rather than simply testing Django's built-in functionality.

## What I Practiced

This project helped me practice:

* Django project and app structure
* Class-based views
* Model relationships
* Many-to-many relationships
* Custom user models
* Authentication and user registration
* Django forms
* URL routing
* QuerySets
* Search functionality
* Pagination
* Automated testing
* Debugging Django applications
* Writing maintainable backend code

## Future Improvements

Possible future improvements include:

* Docker support
* PostgreSQL configuration
* REST API
* Better test coverage for edge cases
* Improved pagination and ordering
* Production deployment configuration
* CI/CD integration

## Author

**Mahdi Modanlou**

This project is part of my Django backend development portfolio.
