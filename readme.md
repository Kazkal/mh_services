#M H Maintenance Services - Project 3 

## Overview
### What is this app for?
 
This is a website for a small maintenance services company to market their services and detail all the vital info that potential customers require.

### What does it do?
 
This website allows customers to look at the services offered, read testimonials, look at past projects. Customers can fill in the contact form for more information or a call back. Customers can also register and login to pay invoices and read and comment on blog posts. 

### How does it work
 
This app uses a SQlite database to store user details together with blog posts, contact leads, invoices generated and testimonials and a portfolio of projects completed. It is built with Django framework  and the Django authentication is used to  authenticate users and keep them logged in. The site is styled with Bootstrap. The Django admin site allows data to be added, changed and deleted.

 
## Features
 ### Existing Features
- A carousel of the portfolio
- A page for every service offered containing a contact from
- logging in feature to access invoice payment and the blog
- facility to accept payments for invoices using Paypal
- facility to leave comments for blog posts
- links to social media
- a mailto link to activate the email client
- portfolio page where images can be enlarged by hovering over
- a page of testimonials for marketing purposes
- an about us page to introduce the business
 
### Features Left to Implement
- User Based Features
    - invoices being removed once paid
    - cutsomers adding posts
    - pricing page
    - our clients page - selection of clients we've worked for

### Users and groups
The Django admin site was used to create 2 groups:
 - Group 1 - MH Staff
 	- Kashmirk67@gmail.com (password - Paris2017) is_superuser and is_staff
 	- SamLee@gmail.com (password - Campion1) is_staff
 - Group 2 - Customers
 	- IanSmith@gmail.com (password IanSmith) 
 	- JackGreen@hotmail.com (password - JackGreen)
 	- KathWhite@hotmail.com (password - KathWhite)
 	- AnneBlue@outlook.com (password - AnneBlue)

 The group MH Staff do not have permissions to touch payments or delete any data. This group can add and edit all data except any payment data.  
 	
## Tech Used
 ### Some the tech used includes:
- [Django](https://www.djangoproject.com/)
    - We use the web framework **Django** to build the website, handle authenticiation, route urls, etc
- [Bootstrap](linked to remotely: https://cdnjs.cloudflare.com/ajax/libs/bootswatch/3.3.6/cerulean/bootstrap.min.css)
    - We use **Bootstrap** to give our project a simple, responsive layout
- [Jquery](linked to remotely: https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js)
    - We use the javascript library **jquery** to simplify the code
- [Pip](https://bootstrap.pypa.io/get-pip.py)
    - **Pip** is used to install Python packages
- [Django-disqus](https://disqus.com/api/applications/register/)
	- We use the third party comments module **Disqus** to add the comments feature to the blog 
- [Django-paypal](https://pypi.python.org/pypi/django-paypal)
	-  We use **django-paypal** to integrate Paypal with our Django app in order to accept payments
- [gunicorn](http://docs.gunicorn.org/en/stable/install.html)
	- We use the application server **gunicorn** to run our Python web app on Heroku
- [Pillow](https://python-pillow.org/)
	- We use Python's imaging library **pillow** to process images in our project
- [Whitenoise](https://pypi.python.org/pypi/whitenoise)
 	- We use **Whitenoise** to allow our web app to serve its own static files because Django does not support serving static files in production. 


## Contributing
### Getting the code up and running
1. Firstly you will need to clone this repository by running the ```git clone https://github.com/Kazkal/mh_services``` command
2. Create a virtual environment for this project
3. Run the following command:
	pip install django-forms-bootstrap==3.1.0
	pip install pillow==2.9.0
	pip install django-paypal==0.3.6
	pip install django-disqus==0.5
	pip install django-debug-toolbar==1.8
	pip install gunicorn==19.7.1
	pip install whitenoise==3.3.1


4. After those dependencies have installed, run ```python manage.py runserver```
6. The project will now run on [localhost](http://127.0.0.1:8080)

###Testing
1. Automated Django tests:
	(test data in blog/fixtures - fixtures created for blog, contacts and user)
	- url resolves to correct view function:
		home/tests.py - def test_home_page_resolves(self)
		accounts/tests.py - def test_register_page_resolves(self)
		accounts/tests.py - def test_login_page_resolves(self)
		accounts/tests,py - def test_logout_page_resolves(self)
		blog/tests.py - def test_blog_page_resolves(self)
		blog/tests.py - def test_detail_page_resolves(self)
	- test view returns actual page:
		accounts/tests.py - def test_register_page_status_code_is_ok(self)
		accounts/tests.py - def test_login_page_status_code_is_ok(self)
		blog/tests.py - def test_detail_page_status_code_is_ok(self)
		blog/tests.py - def test_blog_page_status_code_is_ok(self)
		home/tests.py - def test_home_page_status_code_is_ok(self)
	- test correct content and correct template returned:
		blog/tests.py - def test_blog_content_is_correct(self)
		blog/tests.py - def test_detail_content_is_correct(self)
		home/tests.py - def test_check_content_is_correct(self)
		portfolios/tests.py - def test_content_is_correct(self)
	- test if statement:
		accounts/tests.py - class CreateUserTest(TestCase)
	- does form validate correctly with correct data:
		accounts/tests.py - def test_registration_form(self)
		accounts/tests.py - def test_login_form(self)
		contacts/tests.py - def test_contact_form(self)
	- does form validate correctly with incorrect data:
		accounts/tests.py - def test_login_form_missing_email(self)
		accounts/tests.py - def test_login_form_missing_password(self)
		accounts/tests.py - def test_registration_form_missing_email(self)
		accounts/tests.py - def test_registration_form_passwords_not_matching(self)
		accounts/tests.py - def test_registration_form_password_missing(self)
		contacts/tests.py - def test_contact_form_missing_email(self)


Tested website in following browsers:
	Google Chrome
	Mozilla Firefox
	Internet Explorer
	Opera


###Deployment
Add additional notes about how to deploy this on a live system