# unicorn-fullstack
Unicorn Fullstack


## Steps

* Setup env and install dependencies
```
python3 -m venv myvenv

source myvenv/bin/activate

==> python --version
Python 3.10.9

pip install 'piccolo[all]'

pip install --upgrade pip

```

* Run piccolo asgi new

```
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
