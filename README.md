# Gama Cidadão

To run this project you have to configure or environment on this way:

For this project we strongly recommend that you use pycharm to backend
application.

You can take the requirements text and use to create a virtual environment. Here
we are using Poetry

For Linux:

```sh
$ cat requirements.txt | xargs poetry add
source env/bin/activate
```

For Widows:

```sh
@(cat requirements.txt) | %{&poetry add $_}
```

Alternatively, if you are using python with pip

```sh
pip install requirements.txt
```

Ok, then you can run some codes to run a local database with SQLight

#### Create the database

```sh
python manage.py migrate
```

#### Create an admin user

This will prompt you to create a new superuser account with full permissions.
Email is optional. Note the password text won’t be visible when typed, for
security reasons.

```sh
python manage.py createsuperuser
```

#### Start the server

```sh
python manage.py runserver
```

Nice, for the nextjs frontend you can acces tha path /frontend than run the
follow commands to install the frontend dependencies:

```sh
npm install
```

Then run the code to run the frontend server:

```sh
npm run dev
```

This project is being based on this tutorial. So, if you have some questions you
can see the instructions on the link below.

<https://github.com/wagtail/nextjs-loves-wagtail>
