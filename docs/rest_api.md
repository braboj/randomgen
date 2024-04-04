## Randomg Generator API

A simple API to generate random numbers.

### Generate random numbers

Description of the method.

```plaintext
GET /api/v2/randomgen
```

Supported attributes:

| Attribute | Type | Required | Description                  |
|-----------|------|----------|------------------------------|
| `number`  | int  | Yes      | The number of random numbers |

If successful, returns [`<status_code>`](rest/index.md#status-codes) and the following
response attributes:

| Attribute                | Type     | Description              |
|--------------------------|----------|--------------------------|
| `random_numbers`          | list     | List of random numbers.  |
| `attribute`              | datatype | Detailed description.    |

Example request:

```shell
curl --url "<host address>/api/v2/randomgen?amount=10"
```

Example response:

```json
[
    {
      "chi_square": 6.37701149425288,
      "df": 4,
      "distribution": [0.01, 0.3, 0.58, 0.1, 0.01],
      "is_fair": 1,
      "numbers": [2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 0, 2, 2, 0, 1, 3, 1, 1, 2, 1, 0, 1, 1, 2, 1, 2, 1, 1, 0, 0, 1, -1, 1, 1, 0, 1, 2, 1, 1, 1, 1, 1],
      "p_value": 0.172706492508138
    }
]
```
