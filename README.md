# .NET - Flask - Fast API - Django Comparison

We will compare 4 web frameworks, in this case **.NET 7** which uses **C#**, and 3 **python** web frameworks: **Django**, **Flask** and **FastAPI**. The reason for making this comparison it's because we want to move our dotnet 7 API to some python web framework.  
So first, we will describe all .NET features that our API is using on production, and then we will check if the different python web frameworks have this features by default, needs extra packages or definitely doesn't have the feature.  
Then we are going to **create 4 APIs**, to compare **how much boilerplate files** and **configurations** are needed to create a **single endpoint** that responds a hello world.  
Then we are going to test the 4 APIs to compare it's behaviors on **stress**, **smoke**, **load** and **soak** testing.  

## .NET Features

- Authentication (using JWT)
- Authorization (using decorators and adding claims in every request)
- Database Connection (using MySQL with EntityFramework and SQL Server connections calling queries and stored procedures)
- CORS policies
- Dependency Injection
- HTTP Clients (with base information)
- Swagger (to show api documentation)
- JSON global configuration (to ignore cycles, naming policies and enum converters)
- TLS configuration
- Environments Configurations
- Time Helper (this was a .net framework dll converted to a dotnet core code)

## Instalations Required

- **.NET 7 SDK** (https://dotnet.microsoft.com/en-us/download/dotnet/7.0)
- **pip** (https://pypi.org/project/pip/)
- **fastapi** (```pip install fast api```)
- **uvicorn** (```pip install uvicorn```) (to run fast api)
- **flask** (```pip install Flask```)
- **django** (```pip install django```)
- **docker** (docker desktop in this case because we are running on windows) (https://www.docker.com/products/docker-desktop/)
- for dockerized apps we need to create a web_framework network to share among all containers

## Popularity

Framework | Github followers | Age | Followers per Year | Web frameworks (loved vs dreaded)* 
|---|---|---|---|---|
**.NET Core** | [6.1k](https://github.com/dotnet) | 07-2016 (6 years) | ⭐ 1.016 followers/year | ♥️ 71.49 % vs 👎 28.51 % (7260 responses)
**Fast API** | [54.6k](https://github.com/tiangolo/fastapi) | 12-2018 (4 years) | ⭐ 13.650 followers/year  |  ♥️ 67.74 % vs 👎 32.26 % (2228 responses)
**Django** | [68.8k](https://github.com/django/django) | 07-2005 (17 years) | ⭐ 4.047 followers/year |  ♥️ 53.10 % vs 👎 46.90 % (4249 responses)
**Flask** | [61.9k](https://github.com/pallets/flask) | 04-2010 (12 years) | ⭐ 5.158 followers/year |  ♥️ 48.41 % vs 👎 51.59 % (3870 responses)

*By stack overflow state of developer 2022 survey.

## Features Comparison

Feature | .NET 7 | Django | Flask | Fast API |
|---|---|---|---|---|
**JWT Authentication** | ✔ Microsoft.AspNetCore.Authentication.JwtBearer | ✔ Simple JWT or DjangoRESTFramework-JWT | ✔ flask-jwt  | ✔ python-jose
**Authorization** | ✔ No extra package needed | ✔ No extra package needed  | ✔ flask-authorize  | ✔ propelauth
**Database Connection** | ✔ Pomelo.EntityFrameworkCore.MySql and Microsoft.Data.SqlClient  | ✔ MySQLClient or MySQL Connector/Python  | ✔ flask-sqlalchemy   | ✔ sqlalchemy
**CORS Config** | ✔ No extra package needed  | ✔ django-cors-headers | ✔ flask-cors  | ✔ No extra package needed
**Dependency Injection** | ✔ No extra package needed  | ✔ python-dependency-injector | ✔ injector | ✔ No extra package needed (based on Starlette)
**HTTP Clients** | ✔ No extra package needed  | ✔ httplib or requests | ✔ requests  | ✔ httpx with asyncio
**API Documentation** | ✔ Swashbuckle.AspNetCore (pre-configured on dotnet new webapi) | ✔ django-rest-swagger | ✔ flask-restful  | ✔ No extra package needed (Open API comes by default)
**JSON Global Configuration** | ✔ No extra package needed  | ✔ No extra package needed  | ✔ No extra package needed  | ✔ No extra package needed
**Security Protocols Configuration** | ✔ No extra package needed  | ❌ you need to do it externally (NGINX)  | ❌ you need to do it externally (NGINX)  | ❌ you need to do it externally (NGINX)
**Multi Environment Config** | ✔ No extra package needed  | ✔ No extra pacagke needed but django-environ package is recommended  | ✔ No extra package needed  | ✔ pydantic
|---|---|---|---|---|
**Extra Packages** | 👑 3 | 6 | 7 | 5 |

## Benchmarks

In this case we are going to benchmark the hello world api in all 4 web frameworks. We will use [k6](https://k6.io/docs/#que-es-k6) for this tests.

Type of test that we are going to cover:

- Stress tests
- Smoke tests
- SQL Connection test

## Benchmarks results

### Stress Tests

This test consist in 9 stages:

- 2 min from 0 VUs to 100 VUs
- 5 min with 100 VUs
- 2 min from 100 VUs to 200 VUs
- 5 min with 200 VUs
- 2 min from 200 VUs to 300 VUs
- 5 min with 300 VUs
- 2 min from 300 VUs to 400 VUs
- 5 min with 400 VUs
- 10 min from 400 VUs to 0 VUs

Measures | .NET 7 | Django | Flask | FastAPI | Description
|---|---|---|---|---|---|
**data_received** | 94 MB  41 kB/s | 143 MB 63 kB/s | 36 MB  15 kB/s | 77 MB  34 kB/s | The total amount of received data
**data_sent** | 41 MB  18 kB/s | 38 MB  17 kB/s | 15 MB  6.4 kB/s | 41 MB  18 kB/s | The total amount of data sent.
**http_req_blocked** | avg=2.25µs | avg=3.11µs | avg=797.76µs | 👑 avg=1.63µs | Time spent blocked (waiting for a free TCP connection slot) before initiating the request.
**http_req_connecting** | 👑 avg=164ns | avg=1.64µs | avg=782.57µs | avg=221ns | Time spent establishing TCP connection to the remote host
**http_req_duration** | 👑 avg=330.69µs | avg=81.45ms | avg=68.71ms | avg=4.62ms | Total time for the request. (http_req_sending + http_req_waiting + http_req_receiving)
**http_req_failed** | 👑 0.00% 0 | 0.09% 456 | 55.21% 234690 | 👑 0.00% 0 | The rate of failed requests according to http status between 200 and 399.
**http_req_receiving** | 👑 avg=32.4µs | avg=1.03ms | avg=125.28µs | avg=1.36ms | Time spent receiving response data from the remote host
**http_req_sending** | avg=7.66µs | avg=5.35µs | avg=13.42µs | 👑 avg=5.14µs | Time spent sending data to the remote host.
**http_req_waiting** | 👑 avg=290.61µs | avg=80.41ms | avg=68.57ms | avg=3.25ms | Time spent waiting for response from remote host
**http_reqs** | 509403 223.323931/s | 475536 208.478548/s | 425052 177.587231/s | 👑 511045 224.132616/s | How many total HTTP requests k6 generated.
|---|---|---|---|---|---|
**crowns** | 5 x 👑 | 0 x 👑 | 0 x 👑 | 4 x 👑

### Smoke Tests

This test consist in 1 VU for 1 min. to simulate minimal load to the API.

Measures | .NET 7 | Django | Flask | FastAPI | Description
|---|---|---|---|---|---|
**data_received** | 11 kB   182 B/s | 18 kB   297 B/s | 12 kB   189 B/s | 👑 9.0 kB  148 B/s | The total amount of received data
**data_sent** | 👑 4.8 kB  79 B/s | 👑 4.8 kB  79 B/s | 👑 4.8 kB  79 B/s | 👑 4.8 kB  79 B/s | The total amount of data sent.
**http_req_blocked** | avg=36.17µs | 👑 avg=16.68µs | avg=97.95µs | avg=24.61µs | Time spent blocked (waiting for a free TCP connection slot) before initiating the request.
**http_req_connecting** | 👑 avg=0s | 👑 avg=0s | avg=18.2µs | 👑 avg=0s | Time spent establishing TCP connection to the remote host
**http_req_duration** | avg=2.04ms | avg=3.9ms | avg=2.35ms | 👑 avg=1.74ms | Total time for the request. (http_req_sending + http_req_waiting + http_req_receiving)
**http_req_failed** | 👑 0.00% 0 | 👑 0.00% 0 | 👑 0.00% 0 | 👑 0.00% 0 | The rate of failed requests according to http status between 200 and 399.
**http_req_receiving** | 👑 avg=224.79µs | avg=685.27µs | avg=332.45µs | avg=448.21µs | Time spent receiving response data from the remote host
**http_req_sending** | avg=10.79µs | avg=27.04µs | avg=59.62µs | 👑 avg=2.02µs | Time spent sending data to the remote host.
**http_req_waiting** | avg=1.81ms | avg=3.19ms | avg=1.96ms | 👑 avg=1.29ms | Time spent waiting for response from remote host
**http_reqs** | 👑 60 0.987689/s | 60 0.988275/s | 60 0.988063/s | 60 0.988167/s | How many total HTTP requests k6 generated.
|---|---|---|---|---|---|
**crowns** | 5 x 👑 | 4 x 👑 | 2 x 👑 | 7 x 👑

### SQL Connection Tests

This test consist calling an endpoint that returns all users from a my sql database, it's divided in 2 stages:

- 2 mins from 0 to 20 VUs
- 8 mins with 20 VUs

Measures | .NET 7 | Django | Flask | FastAPI | Description
|---|---|---|---|---|---|
**data_received** | 79 MB  131 kB/s | 64 MB  106 kB/s | 56 MB  93 kB/s | 77 MB  127 kB/s | The total amount of received data
**data_sent** | 913 kB 1.5 kB/s | 2.2 MB 3.7 kB/s | 899 kB 1.5 kB/s | 894 kB 1.5 kB/s | The total amount of data sent.
**http_req_blocked** | 👑 avg=241ns | avg=541ns | avg=519.26µs | avg=929ns | Time spent blocked (waiting for a free TCP connection slot) before initiating the request.
**http_req_connecting** | avg=81ns | avg=121ns | avg=490.77µs | 👑 avg=0s | Time spent establishing TCP connection to the remote host
**http_req_duration** | 👑 avg=2ms | avg=2.71ms | avg=14.45ms | avg=22.37ms | Total time for the request. (http_req_sending + http_req_waiting + http_req_receiving)
**http_req_failed** | 👑 0.00% 0 | 👑 0.00% 0 | 👑 0.00% 0 | 👑 0.00% 0 | The rate of failed requests according to http status between 200 and 399.
**http_req_receiving** | 👑 avg=34.91µs | avg=306.53µs | avg=338.87µs | avg=4.64ms | Time spent receiving response data from the remote host
**http_req_sending** | 👑 avg=538ns | avg=1.58µs | avg=31.96µs | avg=1.64µs | Time spent sending data to the remote host.
**http_req_waiting** | 👑 avg=1.96ms | avg=2.4ms | avg=14.08ms | avg=17.72ms | Time spent waiting for response from remote host
**http_reqs** | 10738 17.86698/s | 👑 21326 35.486711/s | 10581 17.607522/s | 10516 17.49801/s | How many total HTTP requests k6 generated.
|---|---|---|---|---|---|
**crowns** | 6 x 👑 | 2 x 👑 | 1 x 👑 | 2 x 👑 |


## Tests Running on CVIADTQAL01 using Docker Containers

### Smoke Test

This test consist in 1 VU for 1 min. to simulate minimal load to the API.

Measures | .NET 7 | Django | Flask | FastAPI | Description
|---|---|---|---|---|---|
**data_received** | 9.8 kB  161 B/s | 9.8 kB  161 B/s | 8.2 kB  135 B/s | 8.0 kB  131 B/s
**data_sent** | 4.5 kB  74 B/s | 4.5 kB  74 B/s | 4.0 kB  66 B/s | 4.5 kB  74 B/s
**http_req_blocked** | avg=2.47ms | avg=2.48ms | avg=132.2ms | avg=2.56ms
**http_req_connecting** | avg=2.46ms | avg=2.47ms | avg=130.36ms | avg=2.55ms
**http_req_duration** | avg=129.22ms | avg=130.64ms | avg=133.35ms | avg=131.39ms
**http_req_failed** | 0.00% 0 | 0.00% 0 | 0.00% 0 | 0.00% 0
**http_req_receiving** | avg=639.55µs | avg=1.37ms | avg=750.57µs | avg=613.94µs
**http_req_sending** | avg=41.63µs | avg=21.16µs | avg=1.83ms | avg=44.42µs
**http_req_waiting** | avg=128.54ms | avg=129.24ms | avg=130.76ms | avg=130.73ms
**http_reqs** | 53 0.877317/s | 53 0.876261/s | 48 0.786364/s | 53 0.874726/s
|---|---|---|---|---|---|
**crowns** | 5 x 👑 | 4 x 👑 | 2 x 👑 | 7 x 👑

### SQL Connection Tests

This test consist calling an endpoint that returns all users from a my sql database, it's divided in 2 stages:

- 2 mins from 0 to 20 VUs
- 8 mins with 20 VUs

Measures | .NET 7 | Django | Flask | FastAPI | Description
|---|---|---|---|---|---|
**data_received** | 69 MB  115 kB/s | 365 MB  606 kB/s | 44 MB  73 kB/s | 67 MB  112 kB/s
**data_sent** | 843 kB 1.4 kB/s | 549 kB  912 B/s | 744 kB 1.2 kB/s | 821 kB 1.4 kB/s
**http_req_blocked** | avg=281.74µs | avg=133.02ms | avg=128.94ms | avg=284.09µs
**http_req_connecting** | avg=268.72µs | avg=132.5ms | avg=128.46ms | avg=277.54µs
**http_req_duration** | avg=132.83ms | avg=615.1ms | avg=156.64ms | avg=163.74ms
**http_req_failed** | 0.00% 0 | 100.00% ✓ 6169 | 0.00% 0 | 0.00% 0
**http_req_receiving** | avg=1.04ms | avg=425.77ms | avg=1.85ms | avg=6.52ms
**http_req_sending** | avg=44.18µs | avg=524.3µs | avg=553.25µs | avg=16.96µs
**http_req_waiting**  |avg=131.74ms | avg=188.8ms | avg=154.24ms | avg=157.21ms
**http_reqs** | 9474 15.766286/s | 6169 10.252076/s | 8364 13.915403/s | 9226 15.346438/s
|---|---|---|---|---|---|
**crowns** | 6 x 👑 | 2 x 👑 | 1 x 👑 | 2 x 👑 |