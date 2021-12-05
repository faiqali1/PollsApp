# Django Poll App

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Getting It Started](#Getting_It_Running)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

Fully featured Django poll app with the ability to add, remove or edit polls. 

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

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
## Getting It Running<a name = "Getting_It_Running"></a>

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

Viola! now you should be able to add, remove or edit any post.


## Usage <a name = "usage"></a>

