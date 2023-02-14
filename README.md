# .NET - Flask - Fast API - Django Comparison

## .NET Features in QATV4

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

## Features Comparison

Feature | .NET 7 | Django | Flask | Fast API |
|---|---|---|---|---|
JWT Authentication | ✔ Microsoft.AspNetCore.Authentication.JwtBearer | ✔ Simple JWT or DjangoRESTFramework-JWT | ✔ flask-jwt  | ✔ python-jose
Authorization | ✔ No extra package needed | ✔ No extra package needed  | ✔ flask-authorize  | ✔ propelauth
Database Connection | ✔ Pomelo.EntityFrameworkCore.MySql and Microsoft.Data.SqlClient  | ✔ MySQLClient or MySQL Connector/Python  | ✔ flask-sqlalchemy   | ✔ sqlalchemy
CORS Config | ✔ No extra package needed  | ✔ django-cors-headers | ✔ flask-cors  | ✔ No extra package needed
Dependency Injection | ✔ No extra package needed  | ✔ python-dependency-injector | ✔ injector | ✔ No extra package needed (based on Starlette)
HTTP Clients | ✔ No extra package needed  | ✔ httplib or requests | ✔ requests  | ✔ httpx with asyncio
API Documentation | ✔ Swashbuckle.AspNetCore (pre-configured on dotnet new webapi) | ✔ django-rest-swagger | ✔ flask-restful  | ✔ No extra package needed (Open API comes by default)
JSON Global Configuration | ✔ No extra package needed  | ✔ No extra package needed  | ✔ No extra package needed  | ✔ No extra package needed
Security Protocols Configuration | ✔ No extra package needed  | ❌ you need to do it externally (NGINX)  | ❌ you need to do it externally (NGINX)  | ❌ you need to do it externally (NGINX)
Multi Environment Config | ✔ No extra package needed  | ✔ No extra pacagke needed but django-environ package is recommended  | ✔ No extra package needed  | ✔ pydantic

## Benchmarks

In this case we are going to benchmark the hello world api in all 4 web frameworks. We will use [k6](https://k6.io/docs/es/#que-es-k6>) for this tests.

Type of test that we are going to cover:

- Smoke tests
- Load tests
- Stress tests
- Soak tests
