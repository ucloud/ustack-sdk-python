<h1 align="center">UCloudStack SDK Python 3</h1>

<p align="center">
<a href="https://pypi.python.org/pypi/openapi-sdk-python3/"><img src="https://img.shields.io/pypi/v/openapi-sdk-python3.svg" alt="Latest Stable Version"></a>
<a href="https://travis-ci.org/openapi/openapi-sdk-python3"><img src="https://travis-ci.org/openapi/openapi-sdk-python3.svg?branch=master" alt="Travis CI Status"></a>
<a href="https://codecov.io/github/openapi/openapi-sdk-python3?branch=master"><img src="https://codecov.io/github/openapi/openapi-sdk-python3/coverage.svg?branch=master" alt="Codecov Status"></a>
<a href="https://openapi.github.io/openapi-sdk-python3/"><img src="https://img.shields.io/badge/docs-passing-brightgreen.svg" alt="Doc Status"></a>
</p>

UCloudStack SDK is a Python client library for accessing the UCloudStack API.

- Website: https://www.openapi.cn/
- Free software: Apache 2.0 license
- [Documentation](https://docs.openapi.cn/opensdk-python/)

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

```python
from openapi.client import Client
from openapi.services.apis.describe_vm_instance_request import DescribeVMInstanceRequest

client = Client({
    "base_url": "http://<your-api-endpoint>/api",
    "public_key": "<your-public-key>",
    "private_key": "<your-private-key>",
})

openapi = client.openapi_client()

req = DescribeVMInstanceRequest(Region="<your-region>", Limit=10, Offset=0)
resp = openapi.describe_vm_instance(req)
print(resp.RetCode, resp.Infos)
```
