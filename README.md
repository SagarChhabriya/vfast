# vfast


## Project Structure
```py
vfast/
├── main.py
├── README.md
├── requirements.txt
├── vercel.json
└── api/
    └── index.py
```


## 1. Created the GitHub Repo `vfast`
Created the GitHub repo `vfast` with README.md. Cloned it. 

```py
pip install fastapi uvicorn
```

## 2. main.py

```py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello_world():
    return {"message": "Hello World!"}

@app.get("/hello/{name}")
async def hello_name(name: str):
    return {"message": f"Hello {name}! 👋"}

@app.get("/health")
async def health_check():
    return {"status": "OK", "message": "API is running!"}
```

## 3. requirements.txt

```py
fastapi==0.115.13
uvicorn==0.34.3
```

## 4. vercel.json

```js
{
  "version": 2,
  "builds": [
    {
      "src": "api/index.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/api/index.py"
    }
  ]
}
```

## 5. api/index.py

```py
from main import app
```


## 6. Run locally
Inside vfast directory

```
vfast> uvicorn main:app --reload 
```

## 7. Vercel

Projects > Add New > Project > Import repo > Deploy 😃😎  https://vfast.vercel.app/
