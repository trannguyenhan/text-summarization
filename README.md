## Run project

```
python3 -m virtualenv env
source /env/bin/activate
pip3 install -m requirements.txt
```

## Update requirements.txt

```bash
pip freeze > requirements.txt
```

## Run

```bash
python3 wsgi.py
```

## Run with docker

```bash
docker build --tag text-summarization .
docker run -p 5000:5000 <id>
```

### Ref

[https://github.com/linhnvc/vietnamese-text-summarization](https://github.com/linhnvc/vietnamese-text-summarization)
