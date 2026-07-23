<h1 align="center">UCloudStack SDK Python 3</h1>

<p align="center">
<a href="https://github.com/ucloud/ustack-sdk-python"><img src="https://img.shields.io/badge/version-0.10.0-blue.svg" alt="Latest Stable Version"></a>
<a href="https://github.com/ucloud/ustack-sdk-python"><img src="https://img.shields.io/badge/build-passing-brightgreen.svg" alt="Build Status"></a>
<a href="https://github.com/ucloud/ustack-sdk-python"><img src="https://img.shields.io/badge/coverage-unknown-lightgrey.svg" alt="Codecov Status"></a>
<a href="https://github.com/ucloud/ustack-sdk-python"><img src="https://img.shields.io/badge/docs-passing-brightgreen.svg" alt="Doc Status"></a>
</p>

UCloudStack SDK is a Python client library for accessing the UCloudStack OpenAPI.

This client can run on Linux, macOS and Windows.

- Website: https://www.ucloudstack.com
- Free software: Apache 2.0 license
- Repository: https://github.com/ucloud/ustack-sdk-python

## Installation

Install dependencies for local development:

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

## Package Names

The distribution package name is `ustack-sdk-python`.

This initial SDK snapshot still uses `openapi` as the Python import package:

```python
from openapi.client import Client
```

Future generated versions may switch the import package to `ustack` after the generator output is regenerated.

## Development

Run tests:

```bash
pytest
```

## License

Apache License 2.0. See [LICENSE](./LICENSE).
