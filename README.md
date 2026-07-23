# UCloudStack SDK for Python

Python SDK for accessing the UCloudStack OpenAPI.

Repository: https://github.com/ucloud/ustack-sdk-python

## Installation

Install dependencies for local development:

```bash
pip install -r requirements.txt
```

Install this SDK from the repository:

```bash
pip install git+ssh://git@github.com/ucloud/ustack-sdk-python.git
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
