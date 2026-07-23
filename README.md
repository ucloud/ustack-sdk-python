<h1 align="center">UCloudStack SDK Python 3</h1>

<p align="center">
<a href="https://github.com/ucloud/ustack-sdk-python"><img src="https://img.shields.io/badge/version-v2.13.x-blue.svg" alt="Latest Stable Version"></a>
<a href="https://github.com/ucloud/ustack-sdk-python"><img src="https://img.shields.io/badge/build-passing-brightgreen.svg" alt="Build Status"></a>
<a href="https://github.com/ucloud/ustack-sdk-python"><img src="https://img.shields.io/badge/coverage-unknown-lightgrey.svg" alt="Codecov Status"></a>
<a href="https://github.com/ucloud/ustack-sdk-python"><img src="https://img.shields.io/badge/docs-passing-brightgreen.svg" alt="Doc Status"></a>
</p>

UCloudStack SDK is a Python client library for accessing the UCloudStack API.

This client can run on Linux, macOS and Windows.

- Website: https://www.ucloudstack.com
- Free software: Apache 2.0 license

## Installation

Install dependencies for local development:

```bash
pip install -r requirements.txt
```

## Quick Start

```python
from ustack.client import Client
from ustack.services.apis.describe_vm_instance_request import DescribeVMInstanceRequest

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
