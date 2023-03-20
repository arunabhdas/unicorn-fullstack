# UnicornFullstack


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


## Run

```
cd unicorn-fullstack-fastapi

cd blog

uvicorn main:app --reload

```

## Piccolo

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


## Links

https://youtu.be/GRD3z95vs-A


https://youtu.be/7t2alSnE2-I
