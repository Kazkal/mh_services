#Project 3 
#describe what we’re going to build - what the project does & need it fulfills
#, what purpose we are building it for,
#and a breakdown of the technologies used
#describe  functionality of the project - models not accessbile by users
how the project was deployed and tested (describe bugs)
# A readme should also
# detail the instructions a user must take in order to get the code up and running on their own machine.
# Sharing this kind of information opens the door to encourage other developers to contribute to your code.

## Overview
### What is this app for?
 
This is a website for a small maintenance services company to market their services and detail all the vital info that potential customers require.
### What does it do?
 
This website allows customers to look at the services offered, read testimonials, look at past work. Customers can fill in the contact form for more information or a call back. They will allow users to register and login. Once the users have done that, they'll be able to pay invoices and read and commnet on blog items. 
### How does it work
 
This app uses a sqlite database to store user details together with blog posts, contact leads, invoices generated and testimonials and a portfolio of projects completed. Built with Django framework. All the data is consumed from an API hosted on Heroku using AngularJS. The site is styled with Bootstrap.

 
## Features
 ### Existing Features
- A carousel of the portfolio
- A page for every service offered containing a contact from
- logging in feature to access invoice payment
- facility to pay for invoices using Paypal
- facility to leave comments for blog posts
- links to social media
- a mailto link to activate the email client
- portfolio page where images can be enlarged by hovering over
- a pageof testimonials for marketing purposes
- an about us page to introduce the business
 
### Features Left to Implement
- User Based Features
    - invoices being removed once paid
    - cutsomers adding posts
    - pricing page
    - our clients page - selection of clients we've worked for


## Tech Used
 ### Some the tech used includes:
- [Django](https://www.djangoproject.com/)
    - We use the web framework **Django** to build the website, handle authenticiation, route urls, etc
- [Bootstrap](http://getbootstrap.com/)
    - We use **Bootstrap** to give our project a simple, responsive layout
- [jquery?](https://www.npmjs.com/)
    - We use **npm** to help manage some of the dependencies in our application
- [pip?](https://bower.io/)
    - **Bower** is used to manage the installation of our libraries and frameworks
    
## Contributing
### Getting the code up and running
1. Firstly you will need to clone this repository by running the ```git clone https://github.com/Kazkal/mh_services``` command
2. After you've that you'll need to make sure that you have **npm** and **bower** installed
  1. You can get **npm** by installing Node from [here](https://nodejs.org/en/)
  2. Once you've done this you'll need to run the following command:
     `npm install -g bower # this may require sudo on Mac/Linux`
3. Once **npm** and **bower** are installed, you'll need to install all of the dependencies in *package.json* and *bower.json*
  ```
  npm install
 
  bower install
  ```
4. After those dependencies have been installed you'll need to make sure that you have **http-server** installed. You can install this by running the following: ```npm install -g http-server # this also may require sudo on Mac/Linux```
5. Once **http-server** is installed run ```http-server -c-1```
6. The project will now run on [localhost](http://127.0.0.1:8080)
7. Make changes to the code and if you think it belongs in here then just submit a pull request