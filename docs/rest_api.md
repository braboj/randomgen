## REST API

### Endpoint

```plaintext
GET /api/v1/randomgen
```

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

[//]: # (If successful, returns [`<status_code>`]&#40;rest/index.md#status-codes&#41; and the following)

[//]: # (response attributes:)

### Example

Windows:

```shell
curl --url "http://localhost:8080/api/v1/randomgen?amount=10"
```

Linux:

```shell
curl --url ""http://localhost:8080/api/v1/randomgen?amount=10"
```


