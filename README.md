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

### Start core app

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
