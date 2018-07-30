# ![]()INSTAGRAM CLONE
This is an Independent project for Moringa Core Django module, July 20th 2018.

## Description

InstaClone is a social  web application that is used by users to post their pictures, follow other users and like other their pictures. They can also follow other users as in instagram app.


## Features
- Users create an account and confirm through email verification.
- User can log in to application and view other peoples posts.
- Users can follow other users and unfollow them.
- A user can like and comment on a post.
- A user can upload posts and edit their profile.
- A user can view other users profle pages and full details of an image by clicking on the image.
- Admin can regulate images uploaded by deleting from the admin dashboard as well as completely close a users account.

## View Live Site here
View the complete site [here](https://instaclone-sophia.herokuapp.com/)


## Technologies Used
    - Python 3.6
    - Django MVC framework
    - HTML, CSS and Bootstrap
    - JavaScript
    - Postgressql
    - Heroku

## Specifications
To view the user dtories or BDD check the [specs file](specs.md).

### Prerequisite
The Instaclone project requires a prerequisite understanding of the following:
- Django Framework
- Python3.6
- Postgres
- Python virtualenv

## Setup and installation

#### Clone the Repo
####  Activate virtual environment
Activate virtual environment using python3.6 as default handler
    `virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate`
####  Install dependancies
Install dependancies that will create an environment for the app to run `pip3 install -r requirements.txt`
####  Create the Database
    - psql
    - CREATE DATABASE instagramdb;
####  .env file
Create .env file and paste paste the following filling where appropriate:

    SECRET_KEY = '<Secret_key>'
    DBNAME = 'instagramdb'
    USER = '<Username>'
    PASSWORD = '<password>'
    DEBUG = True
#### Run initial Migration
    python3.6 manage.py makemigrations instagram
    python3.6 manage.py migrate
#### Run the app
    python3.6 manage.py runserver
    Open terminal on localhost:8000

## Known bugs
No known bugs so far. If found drop me an email.


## Contributors
    - Sophia Murage

### Contact Information
njerimurage92@gmail.com | snmurage1@gmail.com
