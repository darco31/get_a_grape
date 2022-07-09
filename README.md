# Get A Grape - Stephen D'Arcy

![Home Page](static/img/)

# Table of contents

1. [Overview](#Overview)
    * [About](#about)
    * [Scope](#Scope)
    * [Agile](#Agile)

2. [User Experience](#UserExperience)
    * [Project Goals](#Project-goals)
    * [User Stories](#Userstories)

3. [Features](#Features)
    * [Colors](#Colors)

4. [FlowChart Data Structure](#Flow-chart-and-data-structure)

5. [WireFrames](#Wireframes)

6. [Technology Used In Design](#Technology-Used-In-Design)

7. [Testing](#Testing)
    * [HTML Validator](#HTML-Validator)
    * [CSS Validator](#CSS-Validator)
    * [PEP 8](#PEP8)
    * [Automatic testing](#Automatic-testing)

8. [Deployment](#Deployment)

9. [Credits](#Credits)

10. [Issues](#Issues)

# The TuneShack

## Overview

### About
* The Tuneshack is a blog website developed to encourage lovers of all types and genres of music to sign up and talk freely about their love of music, their favorite bands or the best concert they have ever been to. The blog can used to post dates and venues for upcoming concerts. Every body is welcome and encouraged to post and interact with each others posts weather leaving comments or just liking a post.

### Scope

* The initial scope of the project is to develop a website that is primarily used as a blog site for music lovers to use. There is future scope to extend the site to be more commercial in use i.e selling merchandise, tickets, bookings through third party sites.

* The first release wil include:
    - A home page for everyone to view posts and comment.
    - A sign up page /system for new users.
    - users can log in and comment and like posts.
    - Once logged in a user can update or delete their posts.
    - Authentication used to determine who is logged and who can post/update or delete.
    - users can log out at any time.

* Future development
    - Nested comments and a like functionality
    - Images included in comments
    - Possibility of an online store
    - Selling tickets through 3rd party official sites.
    - Search functionality
    - Email verification/password update
    - Categories to pick from

## Agile

![Agile](docs/user_stories.PNG)


# User Experience

## Project goals

* The overall goal of the project is to display my competency in being able to create a website/app using the Django framework in conjunction with Python, Javascript, HTML and CSS. 

* The users of the site will be able to view posts made by all but only create , update and delete posts made by themselves once they have signed up and logged in. Once logged out they will only be able to comment and read posts. Users will be limited to their own content for any updates or removals.

## User Stories

### Sign Up

* As a Site User I can sign up to the app so that I can login and make posts and comment/like other posts

### Delete Posts

* As a User I can delete my posts so that they can be removed if required

### Edit a post

* As a User I can delete my posts so that they can be removed if required

### View a post

* As a User I can view and click on posts so that I can read through them weather logged in or logged out

### Like/unlike posts

* As a User I can **like and unlike posts ** so that there is site interaction

### Manage Posts

* As a site owner I can manage users and their posts so that I can manage content if required

### Make comments

* As a user I can make comments so that give feedback to other posts


# Features

### Home Page
![Home Page](static/img/home.PNG)

* User can open the webpage from the URL provided and do not need to be registered to view the posts on the site. If not logged in the have the option to sign up or if already 
signed up to login. No unauthorized users can comment or like the posts already shown.

### Posts Page
![Posts Page](static/img/post_page.PNG)

* The site user can view posts , add comments or likes if logged in. They can delete their own posts and update the posts but cant alter or delete other users posts.

### Posts with Comments
![Comments Page](static/img/comment_likes.PNG)

* The user can view the comments here.

### Login Page
![Login Page](static/img/login.PNG)

* The user can login from here.

### Sign up Page
![Sign Up Page](static/img/signup.PNG)

* The user can sign up for the site here.

# Colors

* The inspiration for the colors used on the website where taken from [Canva](https://www.canva.com/)

![Colors](docs/colors.PNG)

#### [Back to content](#table-of-contents)

# FlowChart Data Structure

* Tuneshack flowcart

![Flow Chart TuneShack](docs/Flowchart.PNG)

* Tuneshack data model

![Data Model TuneShack](docs/datamodel.PNG)

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
* asgiref==3.5.0
* cloudinary==1.29.0
* dj-database-url==0.5.0
* dj3-cloudinary-storage==0.0.6
* Django==3.2
* django-allauth==0.50.0
* django-ckeditor==6.4.0
* django-crispy-forms==1.14.0
* django-js-asset==2.0.0
* gunicorn==20.1.0
* oauthlib==3.2.0
* psycopg2==2.9.3
* PyJWT==2.3.0
* python3-openid==3.2.0
* pytz==2022.1
* requests-oauthlib==1.3.1
* sqlparse==0.4.2


#### [Back to content](#table-of-contents)

# Testing (Manual)

## I have tested the full CRUD functionality on the project.

### Users can:

- Create posts by clicking Add Post.
- A user can delete or edit their own posts.
- All users of the website can read posts.
- A user can contact the site owner.

### HTML Validator

![HTML Validations](docs/htmlvals.PNG)

### CSS-Validator

![CSS Validations](docs/css_validation.PNG)

### PEP8

* All PEP8 validations can be found [here](docs/PEP8.pdf)

### Lighthouse Scores

![LightHouse](docs/lighthouse.PNG)

![LightHouse mobile](docs/lighthouse_mobile.PNG)

### Javascript-Validations

![Javascript](docs/js_vals.PNG)

# Automatic-testing

* I have performed some basic automatic tests as shown below on the forms and views.

![Views](docs/test_views.PNG)

![Forms](docs/forms_test.PNG)

![Test Results](docs/test_results.PNG)

* I installed Coverage with pip3 install coverage and ran the program in the terminal with coverage run manage.py test. The file was generated with coverage html and the results can be found in the htmlcov file in the index.html file.


#### [Back to content](#table-of-contents)

# Deployment

The live deployed application can be found here [TuneShack](https://tuneshack22.herokuapp.com/)

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

### Reviews
* Album reviews taken for educational purpose only from https://www.bbc.co.uk/music/reviews/ and all reviews are credited to their respective owners on the site.

### Crispy forms instruction
* https://www.geeksforgeeks.org/styling-django-forms-with-django-crispy-forms/

### Django authentication help

* https://django-allauth.readthedocs.io/en/latest/

### Likes/Unlike tutorials

* https://dev.to/radualexandrub/how-to-add-like-unlike-button-to-your-django-blog-5gkg

### Messages

* https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/ae7923cfce7f4653a3af9f51825d2eba/?child=first

### Slack Community

* davidwatters_5P and Daniel_C_5p for their hep on collecting static files.
* Matt Bodden_5P on help with validating HTML/css WITH Django included.

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