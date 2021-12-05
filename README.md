# Django Poll App

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Aditional notes](#aditional_notes)

## About <a name = "about"></a>

Fully featured Quartz Themed Django poll app with the ability to add, remove or edit polls. 

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
### Prerequisites

What things you need to install the software and how to install them.

```
    Python 3.6 & up
```
### Installing

A step by step series of examples that tell you how to get a development env running.

Assuming you have the virtual environment set up.

```
    pip install -r requirements.txt
```
### Getting It Running<a name = "Getting_It_Running"></a>

Make the database with 

```
    python manage.py makemigrations
```

followed by 

```
    python manage.py migrate
```


Create a superuser account by 

```
    python manage.py makesuperuser
```

*Viola! now you should be able to add, remove or edit any post.*

### Running The Web Server
```
    python manage.py runserver
```


## Usage <a name = "usage"></a>

### Main Screen

![image](https://user-images.githubusercontent.com/74228240/144742890-dc0a0485-db52-462a-bd72-75a43ab01d5a.png)

### Question Page 
![image](https://user-images.githubusercontent.com/74228240/144742912-960b8169-7844-4eca-95ee-d1848c1e7789.png)

### Result Page
![image](https://user-images.githubusercontent.com/74228240/144742968-c352386e-b596-4f8e-a27a-5c7396fb2cc8.png)

# Aditional Notes <a name = "aditional_notes"></a>
Feel free to to contribute to the repo to help others out. 
If there's anything I missed do let me know.

Here's the [design file](/Design/Poll-App.bsdesign) for the project.

Thank for checking the project out.
