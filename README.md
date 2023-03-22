# UnicornFullstack


## Screenshots


<img src="https://github.com/arunabhdas/unicorn-fullstack/blob/main/screenshots/screenshot_5.png" width="720"/>

<img src="https://github.com/arunabhdas/unicorn-fullstack/blob/main/screenshots/screenshot_7.png" width="720"/>

## Steps

```
==> python3 -m venv myvenv

==> source myvenv/bin/activate

pip install fastapi

pip install "uvicorn[standard]"

pip install pydantic

pip install --upgrade pip

==> python --version (should be 3.9 or higher)
Python 3.10.9

==> uvicorn --version
Running uvicorn 0.15.0 with CPython 3.10.9 on Darwin

pip install sqlalchemy


```


## Run blog

```
cd unicorn-fullstack-fastapi

cd blog

uvicorn main:app --reload

```

## New Project With Piccolo

```
pip install piccolo['all']

==> piccolo asgi new
Can't import the APP_REGISTRY from piccolo_conf - some commands may be missing. If this is a new project don't worry. To see a full traceback use `piccolo --diagnose`
Which routing framework?
starlette [0], fastapi [1], blacksheep [2], xpresso [3], starlite [4]
1
Which server?
uvicorn [0], Hypercorn [1]
0
Run `pip install -r requirements.txt` and `python main.py` to get started.

```
## Create migrations With Piccolo

```
piccolo migrations new home --auto

piccolo migrations forwards home

```

## Run migrations With Piccolo

```
piccolo migrations forwards session_auth

piccolo migrations forwards user

```

## Run token auth migrations With Piccolo

```
piccolo migrations forwards token_auth
```

### User and Session Migrations With Piccolo

```
piccolo migrations check

piccolo migrations forwards user

piccolo migrations forwards session_auth

```


### Create User With Piccolo

```
==> piccolo user create
Enter username (coder):
admin
Enter email:
appliaison@gmail.com
Enter password:

Confirm password:

Admin user? Enter y or n:
y
Superuser? Enter y or n:
y
Active? Enter y or n:
y
Created User 3
```



## Dotenv

pip install python-dotenv

## Links

https://youtu.be/GRD3z95vs-A


https://youtu.be/7t2alSnE2-I


## Troubleshooting

https://github.com/piccolo-orm/piccolo/issues/8

https://github.com/piccolo-orm/piccolo/discussions/794
