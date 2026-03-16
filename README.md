## safarijeanpiere

## Step 1 — Installing the Packages from the Ubuntu Repositories

Install and Update:

```bash
   sudo apt update
   sudo apt install python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl
```

## Step 2 — Creating the PostgreSQL Database and User

```bash
sudo -u postgres psql
```

You will be given a PostgreSQL prompt where you can set up our requirements.
First, create a database for your project:

```sql
CREATE DATABASE myproject;
```

Next, create a database user for our project. Make sure to select a secure password:

```sql
CREATE USER myprojectuser WITH PASSWORD 'password';
```

```sql
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
```

## Now, you can give the new user access to administer the new database:

```sql
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
```

When you are finished, exit out of the PostgreSQL prompt by typing:

```sql
\q
```

## Step 3 — Creating a Python Virtual Environment for your Project

- V1

```bash
pip install virtualenvwrapper
export WORKON_HOME=~/Envs
mkdir -p $WORKON_HOME
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv env1
```

- V2
    ```bash
    python3 -m venv myprojectenv
    ```

Activate source bin:

```bash
source core/bin/activate
```



#### With your virtual environment active, install Django, Gunicorn, and the psycopg2 PostgreSQL adaptor with the local instance of pip:

```bash
pip install django gunicorn psycopg2-binary
```

## Step 4 — Creating and Configuring a New Django Project
We have already django web in github, so, we can just clone it or copy using this cmd

```bash
git clone "url"
```
Or
```bash
cp -r folder1 folder2
```

##### The first thing you should do with your newly created project files is adjust the settings. Open the settings file in your text editor:

- project setting.py file to be edited
```bash
 nano ~/myprojectdir/myproject/settings.py

 ~/myprojectdir/myproject/settings.py
. . .
# The simplest case: just add the domain name(s) and IP addresses of your Django server
# ALLOWED_HOSTS = [ 'example.com', '203.0.113.5']
# To respond to 'example.com' and any subdomains, start the domain with a dot
# ALLOWED_HOSTS = ['.example.com', '203.0.113.5']
ALLOWED_HOSTS = ['your_server_domain_or_IP', 'second_domain_or_IP', . . ., 'localhost']
```

- Updated the dabase

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

Next, move down to the bottom of the file and add a setting indicating where the static files should be placed. This is necessary so that Nginx can handle requests for these items.



```bash
  ~/myprojectdir/myproject/settings.py

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
```

### Step 5 — Completing Initial Project Setup
Make makemigrations and migrate

```bash
 ~/myprojectdir/manage.py makemigrations
 ~/myprojectdir/manage.py migrate
```

#### Create an administrative user for the project by typing:
```bash
 ~/myprojectdir/manage.py createsuperuser
 ```


You can collect all of the static content into the directory location that you configured by typing:

```bash
 ~/myprojectdir/manage.py collectstatic
```


#### Create an exception for port 8000 by typing:
ave a UFW firewall protecting your server. In order to test the development server

```bash
sudo ufw allow 8000
```

Finally, you can test out your project by starting up the Django development server with this command:

```bash
 ~/myprojectdir/manage.py runserver 0.0.0.0:8000
```


*In your web browser, visit your server’s domain name or IP address followed by :8000:*

https://assets.digitalocean.com/articles/django_gunicorn_nginx_1804/admin_login.png



