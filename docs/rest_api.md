# REST API

## GET /api/v1/randomgen

Generate random numbers based on the probabilities defined in the configuration.
This endpoint uses the `RandomGenV1` class to generate the random numbers.

### Attributes

| Attribute | Type | Required | Description                  |
|-----------|------|----------|------------------------------|
| `numbers` | int  | Yes      | The number of random numbers |


### Response

```json
{
  "numbers": [0, 2, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, -1, 1, 0,
    2, 1, 1, 2, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 
    0, 1, 1, 2, 1, 2, 1, 1, 1, -1, 1, 2, 0, 1, 2, 1, 1, 1, 0, 0, 1, 1, 0, 0, 
    1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 2, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 
    1, -1, 0, 1, 1, 0, 1],
  "quality": {
    "chi_square_test": {
      "chi_square": 4.97586206896552,
      "df": 3,
      "is_null": 1,
      "p_value": 0.173573199002695
    },
    "expected_histogram": {
      "-1": 0.01,
      "0": 0.3,
      "1": 0.58,
      "2": 0.1,
      "3": 0.01
    },
    "observed_histogram": {
      "-1": 0.03,
      "0": 0.27,
      "1": 0.62,
      "2": 0.08
    }
  },
  "version": 1
}
```

### Status Codes
- If successful, returns `200 OK`
- If the request is invalid, returns `500 Internal Server Error`


### Example

```powershell
Invoke-WebRequest -Uri "http://localhost:8080/api/v1/randomgen?numbers=100" -Method Get
```

```text
StatusCode        : 200
StatusDescription : OK
Content           : {"numbers":[2,2,3,2,2,3,2,2,3,2,3,2,2,2,2,2,1,2,2,2,3,1,2,3,2,2,3,2,3,2,2,3,1,3,3,2,3,3,3,2,2,3,3,1
                    ,3,2,1,3,2,3,3,1,3,2,1,3,3,1,2,2,3,2,2,2,1,3,3,1,3,1,2,1,2,3,2,2,2,2,3,2,3,3,3,3,3,3,2,3,3,2,2,3,2,
                    3,...
RawContent        : HTTP/1.1 200 OK
                    Connection: close
                    Content-Length: 423
                    Content-Type: application/json
                    Date: Sun, 07 Apr 2024 11:01:13 GMT
                    Server: Werkzeug/3.0.2 Python/3.12.2

                    {"numbers":[2,2,3,2,2,3,2,2,3,2,3,...
Forms             : {}
Headers           : {[Connection, close], [Content-Length, 423], [Content-Type, application/json], [Date, Sun, 07 Apr
                    2024 11:01:13 GMT]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : System.__ComObject
RawContentLength  : 423
```

## GET /api/v2/randomgen

Generate random numbers based on the probabilities defined in the configuration.
This endpoint uses the `RandomGenV2` class to generate the random numbers.

### Attributes

| Attribute | Type | Required | Description                  |
|-----------|------|----------|------------------------------|
| `numbers` | int  | Yes      | The number of random numbers |


### Response

```json
{
  "numbers": [0, 2, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, -1, 1, 0,
    2, 1, 1, 2, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 
    0, 1, 1, 2, 1, 2, 1, 1, 1, -1, 1, 2, 0, 1, 2, 1, 1, 1, 0, 0, 1, 1, 0, 0, 
    1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 2, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 
    1, -1, 0, 1, 1, 0, 1],
  "quality": {
    "chi_square_test": {
      "chi_square": 4.97586206896552,
      "df": 3,
      "is_null": 1,
      "p_value": 0.173573199002695
    },
    "expected_histogram": {
      "-1": 0.01,
      "0": 0.3,
      "1": 0.58,
      "2": 0.1,
      "3": 0.01
    },
    "observed_histogram": {
      "-1": 0.03,
      "0": 0.27,
      "1": 0.62,
      "2": 0.08
    }
  },
  "version": 1
}
```

### Status Codes
- If successful, returns `200 OK`
- If the request is invalid, returns `500 Internal Server Error`


### Example

```powershell
Invoke-WebRequest -Uri "http://localhost:8080/api/v2/randomgen?numbers=100" -Method Get
```

```text
StatusCode        : 200
StatusDescription : OK
Content           : {"numbers":[2,2,3,2,2,3,2,2,3,2,3,2,2,2,2,2,1,2,2,2,3,1,2,3,2,2,3,2,3,2,2,3,1,3,3,2,3,3,3,2,2,3,3,1
                    ,3,2,1,3,2,3,3,1,3,2,1,3,3,1,2,2,3,2,2,2,1,3,3,1,3,1,2,1,2,3,2,2,2,2,3,2,3,3,3,3,3,3,2,3,3,2,2,3,2,
                    3,...
RawContent        : HTTP/1.1 200 OK
                    Connection: close
                    Content-Length: 423
                    Content-Type: application/json
                    Date: Sun, 07 Apr 2024 11:01:13 GMT
                    Server: Werkzeug/3.0.2 Python/3.12.2

                    {"numbers":[2,2,3,2,2,3,2,2,3,2,3,...
Forms             : {}
Headers           : {[Connection, close], [Content-Length, 423], [Content-Type, application/json], [Date, Sun, 07 Apr
                    2024 11:01:13 GMT]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : System.__ComObject
RawContentLength  : 423
```

## POST /api/config

Configure the random number generator with a custom distribution. The 
distribution is defined by the random numbers and their probabilities.

### Attributes

| Attribute       | Type | Required | Description                             |
|-----------------|------|----------|-----------------------------------------|
| `numbers`       | list | Yes      | The random numbers                      |
| `probabilities` | list | Yes      | The probabilities of the random numbers |


### Response

```json
{
  "numbers": [1, 2, 3, 4, 5],
  "probabilities": [0.1, 0.2, 0.3, 0.2, 0.2]
}
```

### Status Codes

- If successful, returns `200 OK`
- If using GET method, returns `405 Method Not Allowed`
- If the request is invalid, returns `500 Internal Server Error`

### Example

```powershell
Invoke-WebRequest -Uri "http://localhost:8080/api/config" -Method Post -ContentType "application/json" -Body (@{numbers=@(1,2,3); probabilities=@(0.1,0.5,0.4)} | ConvertTo-Json)
```

```
StatusCode        : 200
StatusDescription : OK
Content           : {"numbers":[1,2,3],"probabilities":[0.1,0.5,0.4]}

RawContent        : HTTP/1.1 200 OK
                    Connection: close
                    Content-Length: 50
                    Content-Type: application/json
                    Date: Sun, 07 Apr 2024 10:59:11 GMT
                    Server: Werkzeug/3.0.2 Python/3.12.2

                    {"numbers":[1,2,3],"probabilities":...
Forms             : {}
Headers           : {[Connection, close], [Content-Length, 50], [Content-Type, application/json], [Date, Sun, 07 Apr
                    2024 10:59:11 GMT]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : System.__ComObject
RawContentLength  : 50
```

## POST /api/reset

Reset to the default configuration of the random numbers and probabilities.

### Attributes
None

### Response

```json
{
  "numbers": [-1, 0, 1, 2, 3],
  "probabilities": [0.01, 0.3, 0.58, 0.1, 0.01]
}
```

### Status Codes

- If successful, returns `200 OK`
- If using GET method, returns `405 Method Not Allowed`
- If the request is invalid, returns `500 Internal Server Error`


### Example



```powershell
Invoke-WebRequest -Uri "http://localhost:8080/api/reset" -Method Post -ContentType "application/json" -Body (@{} | ConvertTo-Json)
```

```text
StatusCode        : 200
StatusDescription : OK
Content           : {"numbers":[-1,0,1,2,3],"probabilities":[0.01,0.3,0.58,0.1,0.01]}

RawContent        : HTTP/1.1 200 OK
                    Connection: close
                    Content-Length: 66
                    Content-Type: application/json
                    Date: Sun, 07 Apr 2024 11:10:34 GMT
                    Server: Werkzeug/3.0.2 Python/3.12.2

                    {"numbers":[-1,0,1,2,3],"probabilit...
Forms             : {}
Headers           : {[Connection, close], [Content-Length, 66], [Content-Type, application/json], [Date, Sun, 07 Apr
                    2024 11:10:34 GMT]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : System.__ComObject
RawContentLength  : 66
```
