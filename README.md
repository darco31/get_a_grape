# Get A Grape - Stephen D'Arcy

![Home Page](static/img/)

# Table of contents

1. [Overview](#Overview)
    * [About](#about)
    * [Scope](#Scope)
    * [Agile](#Agile)

2. [Business Model](#Business-Model)

3. [Database](#Database)
   
4. [Marketing](#Marketing)
   
5. [User Experience](#UserExperience)
    * [Project Goals](#Project-goals)
    * [User Stories](#Userstories)

6. [Features](#Features)

7. [FlowChart Data Structure](#Flow-chart-and-data-structure)

8. [WireFrames](#Wireframes)

9. [Technology Used In Design](#Technology-Used-In-Design)

10. [Testing](#Testing)
    * [HTML Validator](#HTML-Validator)
    * [CSS Validator](#CSS-Validator)
    * [PEP 8](#PEP8)
    * [Automatic testing](#Automatic-testing)

11. [Deployment](#Deployment)

12. [Credits](#Credits)

13. [Issues](#Issues)

# Get A Grape Wine store

## Overview

### About
* This was a full stack project based around a fictional e-commerce wine store. The store stocks and sells all manner of wines , Champagne and sparkling
wines from around the world. This the final project in a five project series for my Diploma iof full stack we development.

### Scope

* The initial scope of the project is to develop a website where users can register if they like and login to have a profile available to them. The user was not required to register and can still purchase items without a registration process. I believe this is important as it would take away from the user experience if forced to sign up.

* The structure of the website is simple and intuitive with standout call to action buttons for each step of the user experience.

## Agile

The functionality and design process was managed in Github and Github projects and issues.

There were no specific sprints as my workload and family dictated how much time I could dedicate on a weekly basis to the design of the website. But in saying that I have outlined a timeline of the design events below and what order they were carried out.

### Sprint 1:

* Install Django
* Install AllAuth
* Created the base and index html pages.
* Added some styling to first pages.
* Started README file

### Sprint 2:

### Sprint 3:

### Sprint 4:

### Sprint 5:

### Sprint 6:

### Sprint 7:


### User Stories

### EPIC 1 - Basic Web Functionality

* As a shopper/user I can receive alerts/messages so that I can can clearly see what I have added to my bag and what I may have removed.
* As a shopper I can easily contact the site owners by several means so that I can ask advise on orders etc.
* As a shopper I can click on links for social media so that I can contact the site owners in more ways than by email.
* As a user I can view the home page and clearly understand the purpose of the website so that I can navigate through products and search products.
* As a User of the website I can view the site on smaller screens so that I can use the app on mobile devices.
* As a user of the web app I can navigate around the website so that I can view all relevant pages.

![Basic Web Functionality](static/imgs/basic_functions.PNG)

### EPIC 2 - User Registration

* As a shopper I can easily login and logout of the website so that I can view and update orders.
* As a shopper I can easily view my profile page so that I can update my current information.
* As a new shopper I can register for a new account so that I can browse and order products.
* As a site user I want to be able to setup new passwords and recover my passwords so that I can get access to my account.

![Basic Web Functionality](static/imgs/usr_reg.PNG)

### EPIC 3 - Products

* As a shopper I can add/delete products in my basket so that I can purchase/not purchase the products.
* As a shopper I can easily view product price, rating etc. so that I can decide to buy or not.
* As a shopper I can use the search box so that I can search for all products I am looking for.

![Basic Web Functionality](static/imgs/products.PNG)

### EPIC 4 - Orders

* As a User I can view and click on posts so that I can read through them weather logged in or logged out

### EPIC 5 - Admin Functions

* As a User I can **like and unlike posts ** so that there is site interaction

### EPIC 6 - Product Views

* As a site owner I can manage users and their posts so that I can manage content if required

# Business Model

# Marketing

# Database

![Database Schema](static/imgs/gag.db.jpg)

# Features

### Home Page


* User can open the webpage from the URL provided and do not need to be registered to view the posts on the site. If not logged in the have the option to sign up or if already 
signed up to login. No unauthorized users can comment or like the posts already shown.

### Posts Page


* The site user can view posts , add comments or likes if logged in. They can delete their own posts and update the posts but cant alter or delete other users posts.

### Posts with Comments


* The user can view the comments here.

### Login Page


* The user can login from here.

### Sign up Page

* The user can sign up for the site here.

# Colors

* The inspiration for the colors used on the website where taken from [Canva](https://www.canva.com/)



#### [Back to content](#table-of-contents)

# FlowChart Data Structure

* Tuneshack flowcart



* Tuneshack data model



#### [Back to content](#table-of-contents)

## Wireframes

* All wireframes can be found [here](docs/project_four.pdf)

#### [Back to content](#table-of-contents)

# Technology-Used-In-Design

* Django framework
* HTML5
* CSS3
* Javascript
    - Used to implement the change in year on in the copyright section of the footer.
    - Also used to hid the field for the author name in the add post section, if this was visible the ID would appear and cause issues.
    - Used to remove the alert from the screens.
* Python
    - Used in conjunction with the Django framework to implement the website.
* Heroku
    - Use to deploy the project on to the live site.

# Frameworks

* [Django](https://docs.djangoproject.com/en/4.0/)
    - Used to create the URLS, Views, Forms and models in the site. Also uses the Django Template Language within the HTML files.
* [Bootstrap](https://getbootstrap.com/)
    - Bootstrap is mainly used to style the page and add responsiveness to the website.
* [Cloudinary](https://cloudinary.com/)
    - Cloudinary is used to store all the images used withing the project.
* [Google Fonts](https://fonts.google.com/)
    - Used as the main fonts throughout the project.
* [Git](https://git-scm.com/)
    - Git is used for version control
* [Github](https://github.com/)
    - Github is being used to write the code and store the project as a whole.
* [Am I responsive](http://ami.responsivedesign.is/)
    - Used to display the main image in the README file.
* [Font Awesome](https://fontawesome.com/)
    - Font awesome is used for the like and dislike icons.
* [All Auth](https://django-allauth.readthedocs.io/en/latest/)
    - All Auth used for authentication od website.
* [PostGres](https://www.postgresql.org/download/)
    - Database used through heroku.
* [SQLite](https://django-allauth.readthedocs.io/en/latest/)
    - https://www.sqlite.com/index.html
* [SmartDraw](https://django-allauth.readthedocs.io/en/latest/)
    - To draw out the database schema.
* [Balsamiq](https://django-allauth.readthedocs.io/en/latest/)
    - To create the wireframes.

## Requirements file
* asgiref==3.5.2
* boto3==1.24.28
* botocore==1.27.28
* dj-database-url==0.5.0
* Django==3.2
* django-allauth==0.41.0
* django-countries==7.2.1
* django-crispy-forms==1.14.0
* django-storages==1.12.3
* gunicorn==20.1.0
* jmespath==1.0.1
* oauthlib==3.2.0
* Pillow==9.1.1
* psycopg2-binary==2.9.3
* python3-openid==3.2.0
* pytz==2022.1
* requests-oauthlib==1.3.1
* s3transfer==0.6.0
* sqlparse==0.4.2
* stripe==3.5.0



#### [Back to content](#table-of-contents)

# Testing (Manual)

## I have tested the full CRUD functionality on the project.

### Users can:

- Create posts by clicking Add Post.
- A user can delete or edit their own posts.
- All users of the website can read posts.
- A user can contact the site owner.

### HTML Validator



### CSS-Validator



### PEP8



### Lighthouse Scores



### Javascript-Validations



# Automatic-testing

* I have performed some basic automatic tests as shown below on the forms and views.


* I installed Coverage with pip3 install coverage and ran the program in the terminal with coverage run manage.py test. The file was generated with coverage html and the results can be found in the htmlcov file in the index.html file.


#### [Back to content](#table-of-contents)

# Deployment

The live deployed application can be found here 

### Gitpod and GitHub

To use the terminal designed by The Code Institute I used the [Code Institute Full Template](https://github.com/Code-Institute-Org/gitpod-full-template).
This allows the code that is used to run the terminal be viewed in the browser.

### Steps:

* Click create new repository.
* Give the repository a name.
* Under Repository template pick the [Code Institute Full Template](https://github.com/Code-Institute-Org/gitpod-full-template).
* Click create repository
- Use GIT ADD .
- GIT COMMIT -m "Comments"
- GIT PUSH
- To commit the code and push to Github

## Forking the Github Repository

- Locate the desired Github repository.
- In the top right corner click the Fork button.
- The repository has been forked and you can now work 0on the copy.

## Cloning a Github repository

- Locate the desired Github repository.
- Use the code button and copy the link.
- Open Gitpod and select your directory where you want the clone to be created.
- Type git clone in the terminal and paste the link in.
- The clone will be created


### Creating an Application with Heroku

I used the video tutorial provided by The Code Institute to create a Heroku account, add the details of the app and deploy the application to a live environment.

- Log in to Heroku [Heroku](https://dashboard.heroku.com/)
- Click New 
- Give the app a name and choose the region
- Click on settings first and set the Reveal Config Vars
- Click Deploy at the top to go to the Deployment settings
- Choose GiHub as the deployment method
- Search for your app and connect
- Use Automatic deploys if you would like a new build when changes are pushed to GitHub from Gitpod
- Use Manual deploy for a new build every time this button is clicked.
- Once completed click View App

### Updated as Heroku had a security breach and deployment was needed to be completed from the Github CLI.

* Deploying your app to heroku
1. Login to heroku and enter your details.
command: heroku login -i
2. Get your app name from heroku.
command: heroku apps
3. Set the heroku remote. (Replace <app_name> with your actual app name)
command: heroku git:remote -a <app_name>
4. Add, commit and push to github
command: git add . && git commit -m "Deploy to Heroku via CLI"
5. Push to both github and heroku
command: git push origin main
command: git push heroku main


* MFA/2FA enabled?
1. Click on Account Settings (under the avatar menu)
2. Scroll down to the API Key section and click Reveal. Copy the key.
3. Enter the command: heroku_config , and enter your api key you copied when prompted
4. Complete the steps above, if you see an input box at the top middle of the editor...
 a. enter your heroku username
 b. enter the api key you just copied

#### [Back to content](#table-of-contents)

# Credits

### Crispy forms instruction
* https://www.geeksforgeeks.org/styling-django-forms-with-django-crispy-forms/

### Django authentication help

* https://django-allauth.readthedocs.io/en/latest/

### Slack Community

* davidwatters_5P and Daniel_C_5p for their help.
* Matt Bodden_5P on always wanting to help out.

* My Mentor Miguel Martinez for his support through the whole process.

* The Slack community as a whole for being awesome.

#### [Back to content](#table-of-contents)

# Issues/Bugs

### Static files were not loading in the productions environment.

Fix:
* Move Docs in to the main folder from the static folder and re run collect static. This worked and all files are loading in Heroku.

### Messages were not displaying correctly.

FIX:
* Login and log out message were not appearing when the connected buttons were clicked byt the user. I installed all auth and this fixed the issues.

### HTML Validator failing.

FIX:
* Removed stray div tag from the home.html page.

#### [Back to content](#table-of-contents)