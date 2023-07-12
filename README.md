# About tasksmanager
# Bookmark Manager Documentation

## Introduction
Bookmark Manager is a web application developed using Django, Python, HTML, CSS, and JavaScript. It allows users to organize and manage their bookmarks efficiently. This documentation provides an overview of the key features and functionality of the Bookmark Manager.

## Features
The Bookmark Manager offers the following key features:

1. **Bookmark Management**: Users can add, edit, and delete bookmarks. Each bookmark consists of a title, URL, and optional description.

2. **Category Management**: Users can create categories to organize their bookmarks. Each bookmark can be assigned to one or more categories.

3. **Import Bookmarks**: Users can import bookmarks from a JSON file. This feature allows users to bulk import bookmarks into the application.

## Technology Stack
The Bookmark Manager is built using the following technologies:

- **Django**: A high-level Python web framework that provides the foundation for the application's backend logic and database management.

- **Python**: The primary programming language used for building the backend logic and handling server-side operations.

- **HTML**: The markup language used for structuring the web pages and content presentation.

- **CSS**: The styling language used for defining the visual appearance and layout of the web pages.

- **JavaScript**: The programming language used for implementing interactive features and client-side functionality.

- **MySQL Database**: The database management system used for storing bookmark data and managing relationships between bookmarks and categories.

## Usage
Once the Bookmark Manager is set up and running, users can perform the following actions:

- **Add Bookmarks**: Users can add new bookmarks by providing a title, URL, and optional description.

- **Edit Bookmarks**: Users can edit existing bookmarks to update their title, URL, or description.

- **Delete Bookmarks**: Users can delete bookmarks that are no longer needed.

- **Create Categories**: Users can create categories to organize their bookmarks. Each bookmark can be assigned to one or more categories.

- **Import Bookmarks**: Users can import bookmarks from a JSON file. The JSON file should contain an array of bookmark objects with the necessary properties (title, URL, description).

## Getting the local server running

- Install `mysql`: https://dev.mysql.com/doc/mysql-installation-excerpt/8.0/en/

```bash
# Clone repository
git clone <repo-link>
cd tasksmanager

# creating virtual env
# python3 -m venv path/to/venv
python3 -m venv .venv
source .venv/bin/activate

# create a new database
mysql -u root -p --default-character-set=utf8mb4
CREATE DATABASE tasksmanager_db CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
CREATE DATABASE test_tasksmanager_db CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;

# Create MySQL users
create user 'py-user' identified by 'p@@sWord';
grant all privileges on tasksmanager_db.* to 'py-user';
grant all privileges on test_tasksmanager_db.* to 'py-user';
flush privileges;
exit

# install dependencies
pip install --upgrade pip
pip install wheel
pip install -r requirements/requirements-dev.txt

# install pre-commit hooks
pre-commit install

# Provide database authentications
cp .env.sample .env
# update the .env file with mysql username, password and database name
vi .env

# Create database and tables
python manage.py migrate

# Start development server
python manage.py runserver
```
