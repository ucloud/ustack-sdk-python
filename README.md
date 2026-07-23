# UCloudStack SDK Python

[![Python Version](https://img.shields.io/badge/Python-%3E%3D%203.5-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

UCloudStack SDK Python 是 UCloudStack API 的 Python 客户端库。

- 网站: https://www.ucloudstack.com
- 许可证: Apache 2.0

## 安装

```bash
pip install ustack-sdk-python
```

或从源码安装：

```bash
pip install -r requirements.txt
```

## 快速开始

登陆控制台后获取公私钥，替换到代码中：

```python
from ucloudstack.client import Client
from ucloudstack.services.apis.describe_vm_instance_request import DescribeVMInstanceRequest

client = Client({
    "base_url": "http://<your-api-endpoint>/api",
    "public_key": "<your-public-key>",
    "private_key": "<your-private-key>",
})

api = client.ucloudstack_client()

req = DescribeVMInstanceRequest(Region="<your-region>", Limit=10, Offset=0)
resp = api.describe_vm_instance(req)
print(resp.RetCode, resp.Infos)
```

