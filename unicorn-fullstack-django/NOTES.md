# unicorn-fullstack
Unicorn Fullstack


## Steps

### Setup virtualenv and install dependencies
```

==> python3 -m venv myvenv

==> source myvenv/bin/activate

==> python --version
Python 3.10.9


==> pip --version
pip 22.3.1 from /Users/coder/repos/arunabhdas/githubrepos/unicorn-fullstack/myvenv/lib/python3.10/site-packages/pip (python 3.10)


==> pip install --upgrade pip
```

### Install Django

```
pip install Django and pip freeze > requirements.txt

OR

pip install -r requirements.txt

==> django-admin startproject unicornfullstack

```


### Install DjangoRestFramework

Install DjangoRestFramework as follows

```
==> pip install djangorestframework

==> pip install markdown
```

### Scaffold core app

```
cd unicornfullstack

(we should now be in the folder containing manage.py)

==> python manage.py startapp core
```

### Create superuser for admin

```
cd unicornfullstack

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

```

### Create model class

Create model class in models.py
```
class Product(models.Model):
    id=models.CharField(max_length=200, primary_key=True)
    name=models.CharField(max_length=200)
    sku=models.CharField(max_length=200)
    description=models.TextField()
    slug=models.SlugField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Entry #{}'.format(self.id)

    class Meta:
        verbose_name_plural = "Products"
        ordering = ["name", "created_at"]

```


Run below following command to create the api app

python manage.py startapp api
Add api to the INSTALLED_APPS section as below

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'api',
]
Run migrations

python manage.py makemigrations
python manage.py migrate
Add ‘rest_framework’ to INSTALLED_APPS as below

INSTALLED_APPS = [
    ...
    'rest_framework',
]
Having added ‘rest_framework’ to settings.py, should now look as below

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'api',
    'rest_framework',
]
Modify root urls.py as below to include api/

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
path('admin/', admin.site.urls),
path('api/', include('api.urls')),
]
Modify api/urls.py as below

from django.urls import include, path
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('customroutes/', views.getCustomRoutes),
]
Modify api/views.py to return a function-based route with a JsonResponse to return a dictionary of routes as below


