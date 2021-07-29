# E-commerce site for Images
Django based E-commerce website for buying/selling Images

## Features
User Authentication, Uploading Images by Seller, Buying Images by Buyer, Hiring Photographers by buyers, Cart functionality, RazorPay Payment Gateway, Dashboard

## Requirements
Django==3.2<br/>
Mysql==8.0.25 (or any other relational database of your choice)<br/>
mysqlclient==2.0.3 (python database connector of your respective relational database)
Pillow==8.3.1

## Installation
```javascript
git clone https://github.com/him4lik/E-commerce-for-Images.git
```
### Initial Setup
#### Database settings(buy_images/settings.py)
Replace values of ENGINE, NAME, USER, PASSWORD according to your database
```javascript
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database_name',
        'USER': 'database_user',
        'PASSWORD': 'database_user_password',
    }
}
```
After this makemigrations and migrate them
```javascript
python manage.py makemigrations
python manage.py migrate
```
#### KEY_ID, SECRET_KEY_ID(buy_images/settings.py)
```javascript
KEY_ID='your_razoepay_KEY_ID'
SECRET_KEY_ID='your_Razorpay_SECRET_KEY_ID'
```
#### Email settings(buy_images/settings.py)
```javascript
EMAIL_HOST='smtp_server_you_are_using'
EMAIL_HOST_USER='username'
EMAIL_HOST_PASSWORD='Your_password'
EMAIL_USE_TLS=True
EMIAL_POST='smtp_server_port'
```

## In Action
#### User Authentication
#### Buying
#### Buy All in Cart
#### Uploading Images
#### Hiring
#### Dashboard
