---
    (•_•)
    <) )╯
    /  \
---

# This is fine
![Banner](docs/This-Is-Fine-1.png)

Install server dependencies before create virtual environment.
```bash
cd server
cp .env.example .env # create a dotenv file 
pip install -r requirements.txt
```

Migrate sqlite database and start server
```bash
python manage.py migrate
python manage.py runserver
```

Verify if you server is up
```bash
$ curl -s localhost:8000/
HTTP/1.1 200 OK
Date: Tue, 15 Oct 2024 18:37:59 GMT
Server: WSGIServer/0.2 CPython/3.12.7
Content-Type: application/json
Vary: Accept
Allow: GET, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 26
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin

{"message":"server ready"}⏎
```