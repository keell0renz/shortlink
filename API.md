---
title: FastAPI v0.1.0
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="fastapi">FastAPI v0.1.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

# Authentication

* API Key (APIKeyHeader)
    - Parameter Name: **api_key**, in: header. 

<h1 id="fastapi-user-interface">User Interface</h1>

## ui_get_link__link_id__get

<a id="opIdui_get_link__link_id__get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /{link_id} \
  -H 'Accept: application/json'

```

```http
GET /{link_id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/{link_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/{link_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/{link_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/{link_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/{link_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/{link_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /{link_id}`

*Ui Get Link*

<h3 id="ui_get_link__link_id__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|link_id|path|string|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="ui_get_link__link_id__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="ui_get_link__link_id__get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="fastapi-api">API</h1>

## api_get_link_api_get__link_id__get

<a id="opIdapi_get_link_api_get__link_id__get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /api/get/{link_id} \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'

```

```http
GET /api/get/{link_id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/api/get/{link_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.get '/api/get/{link_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.get('/api/get/{link_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/api/get/{link_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/get/{link_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "api_key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/api/get/{link_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /api/get/{link_id}`

*Api Get Link*

<h3 id="api_get_link_api_get__link_id__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|link_id|path|string|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="api_get_link_api_get__link_id__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="api_get_link_api_get__link_id__get-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
APIKeyHeader
</aside>

## api_create_link_api_create__link_id__post

<a id="opIdapi_create_link_api_create__link_id__post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /api/create/{link_id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'

```

```http
POST /api/create/{link_id} HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "original_link": "string",
  "expiration_time": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/api/create/{link_id}',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.post '/api/create/{link_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.post('/api/create/{link_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/api/create/{link_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/create/{link_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "api_key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/api/create/{link_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /api/create/{link_id}`

*Api Create Link*

> Body parameter

```json
{
  "original_link": "string",
  "expiration_time": "string"
}
```

<h3 id="api_create_link_api_create__link_id__post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|link_id|path|string|true|none|
|body|body|[Body_api_create_link_api_create__link_id__post](#schemabody_api_create_link_api_create__link_id__post)|true|none|

> Example responses

> 201 Response

```json
null
```

<h3 id="api_create_link_api_create__link_id__post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="api_create_link_api_create__link_id__post-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
APIKeyHeader
</aside>

## api_delete_link_api_delete__link_id__delete

<a id="opIdapi_delete_link_api_delete__link_id__delete"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /api/delete/{link_id} \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'

```

```http
DELETE /api/delete/{link_id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/api/delete/{link_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.delete '/api/delete/{link_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.delete('/api/delete/{link_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/api/delete/{link_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/delete/{link_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "api_key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/api/delete/{link_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /api/delete/{link_id}`

*Api Delete Link*

<h3 id="api_delete_link_api_delete__link_id__delete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|link_id|path|string|true|none|

> Example responses

> 201 Response

```json
null
```

<h3 id="api_delete_link_api_delete__link_id__delete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="api_delete_link_api_delete__link_id__delete-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
APIKeyHeader
</aside>

## api_change_original_link_api_change__link_id__original_link_put

<a id="opIdapi_change_original_link_api_change__link_id__original_link_put"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /api/change/{link_id}/original_link \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'

```

```http
PUT /api/change/{link_id}/original_link HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "original_link": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/api/change/{link_id}/original_link',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.put '/api/change/{link_id}/original_link',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.put('/api/change/{link_id}/original_link', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/change/{link_id}/original_link', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/change/{link_id}/original_link");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "api_key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/change/{link_id}/original_link", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /api/change/{link_id}/original_link`

*Api Change Original Link*

> Body parameter

```json
{
  "original_link": "string"
}
```

<h3 id="api_change_original_link_api_change__link_id__original_link_put-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|link_id|path|string|true|none|
|body|body|[Body_api_change_original_link_api_change__link_id__original_link_put](#schemabody_api_change_original_link_api_change__link_id__original_link_put)|true|none|

> Example responses

> 201 Response

```json
null
```

<h3 id="api_change_original_link_api_change__link_id__original_link_put-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="api_change_original_link_api_change__link_id__original_link_put-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
APIKeyHeader
</aside>

## api_change_expiration_time_api_change__link_id__expiration_time_put

<a id="opIdapi_change_expiration_time_api_change__link_id__expiration_time_put"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /api/change/{link_id}/expiration_time \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'

```

```http
PUT /api/change/{link_id}/expiration_time HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "expiration_time": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/api/change/{link_id}/expiration_time',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.put '/api/change/{link_id}/expiration_time',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.put('/api/change/{link_id}/expiration_time', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/api/change/{link_id}/expiration_time', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/change/{link_id}/expiration_time");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
        "api_key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/api/change/{link_id}/expiration_time", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /api/change/{link_id}/expiration_time`

*Api Change Expiration Time*

> Body parameter

```json
{
  "expiration_time": "string"
}
```

<h3 id="api_change_expiration_time_api_change__link_id__expiration_time_put-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|link_id|path|string|true|none|
|body|body|[Body_api_change_expiration_time_api_change__link_id__expiration_time_put](#schemabody_api_change_expiration_time_api_change__link_id__expiration_time_put)|true|none|

> Example responses

> 201 Response

```json
null
```

<h3 id="api_change_expiration_time_api_change__link_id__expiration_time_put-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="api_change_expiration_time_api_change__link_id__expiration_time_put-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
APIKeyHeader
</aside>

## api_delete_expiration_time_api_delete__link_id__expiration_time_delete

<a id="opIdapi_delete_expiration_time_api_delete__link_id__expiration_time_delete"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /api/delete/{link_id}/expiration_time \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'

```

```http
DELETE /api/delete/{link_id}/expiration_time HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/api/delete/{link_id}/expiration_time',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.delete '/api/delete/{link_id}/expiration_time',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.delete('/api/delete/{link_id}/expiration_time', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/api/delete/{link_id}/expiration_time', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/api/delete/{link_id}/expiration_time");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "api_key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/api/delete/{link_id}/expiration_time", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /api/delete/{link_id}/expiration_time`

*Api Delete Expiration Time*

<h3 id="api_delete_expiration_time_api_delete__link_id__expiration_time_delete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|link_id|path|string|true|none|

> Example responses

> 201 Response

```json
null
```

<h3 id="api_delete_expiration_time_api_delete__link_id__expiration_time_delete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="api_delete_expiration_time_api_delete__link_id__expiration_time_delete-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
APIKeyHeader
</aside>

<h1 id="fastapi-statistics-api">Statistics API</h1>

## stat_api_get_all_links_statistics_links_get

<a id="opIdstat_api_get_all_links_statistics_links_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /statistics/links \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'

```

```http
GET /statistics/links HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/statistics/links',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.get '/statistics/links',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.get('/statistics/links', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/statistics/links', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/statistics/links");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "api_key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/statistics/links", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /statistics/links`

*Stat Api Get All Links*

> Example responses

> 200 Response

```json
null
```

<h3 id="stat_api_get_all_links_statistics_links_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="stat_api_get_all_links_statistics_links_get-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
APIKeyHeader
</aside>

## stat_api_get_active_links_statistics_active_links_get

<a id="opIdstat_api_get_active_links_statistics_active_links_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /statistics/active_links \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'

```

```http
GET /statistics/active_links HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/statistics/active_links',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.get '/statistics/active_links',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.get('/statistics/active_links', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/statistics/active_links', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/statistics/active_links");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "api_key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/statistics/active_links", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /statistics/active_links`

*Stat Api Get Active Links*

> Example responses

> 200 Response

```json
null
```

<h3 id="stat_api_get_active_links_statistics_active_links_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="stat_api_get_active_links_statistics_active_links_get-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
APIKeyHeader
</aside>

## stat_api_get_expired_links_statistics_expired_links_get

<a id="opIdstat_api_get_expired_links_statistics_expired_links_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /statistics/expired_links \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'

```

```http
GET /statistics/expired_links HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/statistics/expired_links',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.get '/statistics/expired_links',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.get('/statistics/expired_links', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/statistics/expired_links', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/statistics/expired_links");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "api_key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/statistics/expired_links", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /statistics/expired_links`

*Stat Api Get Expired Links*

> Example responses

> 200 Response

```json
null
```

<h3 id="stat_api_get_expired_links_statistics_expired_links_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="stat_api_get_expired_links_statistics_expired_links_get-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
APIKeyHeader
</aside>

## stat_api_get_link_interactions_statistics_interactions__link_id__get

<a id="opIdstat_api_get_link_interactions_statistics_interactions__link_id__get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /statistics/interactions/{link_id} \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'

```

```http
GET /statistics/interactions/{link_id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/statistics/interactions/{link_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.get '/statistics/interactions/{link_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.get('/statistics/interactions/{link_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/statistics/interactions/{link_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/statistics/interactions/{link_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
        "api_key": []string{"API_KEY"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/statistics/interactions/{link_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /statistics/interactions/{link_id}`

*Stat Api Get Link Interactions*

<h3 id="stat_api_get_link_interactions_statistics_interactions__link_id__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|link_id|path|string|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="stat_api_get_link_interactions_statistics_interactions__link_id__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="stat_api_get_link_interactions_statistics_interactions__link_id__get-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
APIKeyHeader
</aside>

# Schemas

<h2 id="tocS_Body_api_change_expiration_time_api_change__link_id__expiration_time_put">Body_api_change_expiration_time_api_change__link_id__expiration_time_put</h2>
<!-- backwards compatibility -->
<a id="schemabody_api_change_expiration_time_api_change__link_id__expiration_time_put"></a>
<a id="schema_Body_api_change_expiration_time_api_change__link_id__expiration_time_put"></a>
<a id="tocSbody_api_change_expiration_time_api_change__link_id__expiration_time_put"></a>
<a id="tocsbody_api_change_expiration_time_api_change__link_id__expiration_time_put"></a>

```json
{
  "expiration_time": "string"
}

```

Body_api_change_expiration_time_api_change__link_id__expiration_time_put

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|expiration_time|string|true|none|none|

<h2 id="tocS_Body_api_change_original_link_api_change__link_id__original_link_put">Body_api_change_original_link_api_change__link_id__original_link_put</h2>
<!-- backwards compatibility -->
<a id="schemabody_api_change_original_link_api_change__link_id__original_link_put"></a>
<a id="schema_Body_api_change_original_link_api_change__link_id__original_link_put"></a>
<a id="tocSbody_api_change_original_link_api_change__link_id__original_link_put"></a>
<a id="tocsbody_api_change_original_link_api_change__link_id__original_link_put"></a>

```json
{
  "original_link": "string"
}

```

Body_api_change_original_link_api_change__link_id__original_link_put

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|original_link|string|true|none|none|

<h2 id="tocS_Body_api_create_link_api_create__link_id__post">Body_api_create_link_api_create__link_id__post</h2>
<!-- backwards compatibility -->
<a id="schemabody_api_create_link_api_create__link_id__post"></a>
<a id="schema_Body_api_create_link_api_create__link_id__post"></a>
<a id="tocSbody_api_create_link_api_create__link_id__post"></a>
<a id="tocsbody_api_create_link_api_create__link_id__post"></a>

```json
{
  "original_link": "string",
  "expiration_time": "string"
}

```

Body_api_create_link_api_create__link_id__post

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|original_link|string|true|none|none|
|expiration_time|string|true|none|none|

<h2 id="tocS_HTTPValidationError">HTTPValidationError</h2>
<!-- backwards compatibility -->
<a id="schemahttpvalidationerror"></a>
<a id="schema_HTTPValidationError"></a>
<a id="tocShttpvalidationerror"></a>
<a id="tocshttpvalidationerror"></a>

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

```

HTTPValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|[[ValidationError](#schemavalidationerror)]|false|none|none|

<h2 id="tocS_ValidationError">ValidationError</h2>
<!-- backwards compatibility -->
<a id="schemavalidationerror"></a>
<a id="schema_ValidationError"></a>
<a id="tocSvalidationerror"></a>
<a id="tocsvalidationerror"></a>

```json
{
  "loc": [
    "string"
  ],
  "msg": "string",
  "type": "string"
}

```

ValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|loc|[anyOf]|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|msg|string|true|none|none|
|type|string|true|none|none|

