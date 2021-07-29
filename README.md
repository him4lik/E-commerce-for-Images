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
![imageauth (online-video-cutter com)](https://user-images.githubusercontent.com/75934883/127497696-a0a05cc7-785c-4660-8b69-bc0f2bd754de.gif)
#### Buying
![him1](https://user-images.githubusercontent.com/75934883/127549793-30da5709-851d-4beb-ad94-d35fe53a75aa.gif)
#### Buy All in Cart
![him2](https://user-images.githubusercontent.com/75934883/127551775-a406b54f-6803-4711-a287-a80053991b17.gif)
#### Uploading Images
![him6](https://user-images.githubusercontent.com/75934883/127551082-3683b5de-4499-4d80-b2dc-4b6e27722343.gif)
#### Hiring
![him5](https://user-images.githubusercontent.com/75934883/127549644-1490497a-c63f-4092-b758-344f39817192.gif)
#### Buyer Dashboard
![him3](https://user-images.githubusercontent.com/75934883/127551068-e5e08221-232c-411d-95e2-a4bf90365464.gif)
#### seller Dashboard
![him4](https://user-images.githubusercontent.com/75934883/127549579-fc0244b6-da85-4bad-ba8d-3b643fe40905.gif)
