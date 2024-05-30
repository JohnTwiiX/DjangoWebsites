# Django Website Backend

This backend use the Python Django as Rest API. You can user registration, login and authentication, storage images and productes.

## Table of Contents

- [Project Name](#project-name)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Running Tests](#running-tests)
  - [Deployment](#deployment)
  - [Contributing](#contributing)

## Features

List of key features and functionalities of your project.

- Rest API
- storage images / products
- user authentication

## Requirements

List of software and libraries required to run the project.

- Python 3.12.3
- Django 5.0.6

## Installation

Step-by-step instructions to install the project on a local machine.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/JohnTwiiX/DjangoWebsites.git
   cd your-project
   ```

1. **Create a virtual environment and activate it:**

bash
python3 -m venv env
source env/bin/activate

2. **Install dependencies:**

```bash
    pip install -r requirements.txt
```

3. **Set up the database:**

```bash
    python manage.py migrate
```

4. **Create a superuser:**

```bash
    python manage.py createsuperuser
```

5. **Run the development server:**

```bash
    python manage.py runserver
```

## Usage

How to use the project once it’s installed and running. Include example commands and URLs.

- Access the web application at http://localhost:8000.
- Admin panel at http://localhost:8000/admin.


## Running Tests

Instructions on how to run the test suite.

1. **Run the tests:**

```bash
    python manage.py test
```

2. **Check test coverage (if applicable):**

```bash
    coverage run manage.py test
    coverage report
```

## Deployment
Guidelines for deploying the project to a production environment.

1. **Collect static files:**

```bash
    python manage.py collectstatic
```

2. **Apply migrations:**

```bash
    python manage.py migrate
```

3. **Configure your web server (e.g., Nginx, Apache) and WSGI application (e.g., Gunicorn, uWSGI).**


## Contributing
Guidelines for contributing to the project.

1. **Fork the repository.**

2. **Create a new branch:**

```bash
    git checkout -b feature/your-feature
```

3. **Make your changes and commit them:**

```bash
    git commit -m 'Add some feature'
```

4. **Push to the branch:**

```bash
    git push origin feature/your-feature
```

5. **Submit a pull request.**


