# Shortlink `v1.0.0`
![](https://img.shields.io/badge/Portfolio_Project-blue)
![](https://img.shields.io/badge/Python-blue)
![](https://img.shields.io/badge/FastAPI-blue)
![](https://img.shields.io/badge/PostgreSQL-blue)
![](https://img.shields.io/badge/Docker-blue)
![](https://img.shields.io/badge/Microservices-blue)

><p style="color:lightblue;">A convenient way to handle link shortening...</p>

A link-shortening miroservice with convenient REST API interface, suitable for microservice applications, web applications, etc.

## Fuctionality

* Access original links by direct access or using an API.
* API Keys for Authentication and Authorization
* Ability to manage links (Add, Delete, Change).
* Ability to see links and their data.
* Ability to add optional expiration date and change it / cancel it.
* Ability to see links' usage statistics (Time, IP, Country, User-Agent).

## Launch

### Launch Without Docker
```
export SHORTLINK_API_KEY="my_api_key" # Default is ""
export SHORTLINK_DB_STRING="my_db_string" # Default is in-memory sqlite
pip install -r requirements.txt
uvicorn src.main:app
```

### Launch With Docker
```
docker build . -t shortlink:latest
docker run --name shortlink-service -e SHORTLINK_API_KEY="my_api_key" -e SHORTLINK_DB_STRING="my_db_string" -p 8000:8000 -d shortlink:latest
```