# UCloudStack SDK Python

[![Python Version](https://img.shields.io/badge/Python-%3E%3D%203.5-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

UCloudStack SDK Python 是 UCloudStack API 的 Python 客户端库。

- 网站: https://www.ucloudstack.com
- 许可证: Apache 2.0

## 快速开始

登陆控制台后获取公私钥，替换到代码中：

```python
from ucloudstack.client import Client
from ucloudstack.services.apis.create_vm_instance_request import CreateVMInstanceRequest

client = Client({
    "base_url": "http://my_api_endpoint/api",  # 替换成平台的API端点
    # 替换成平台上获取的公/私钥
    "public_key": "my_public_key",
    "private_key": "my_private_key",
})

api = client.ucloudstack_client()

req = CreateVMInstanceRequest(
    Region="my_region",       # 替换成平台上的目标地域
    Name="sdk-example-vm",
    ImageID="image-xxx",      # 替换成平台上可用的镜像ID
    Password="my_vm_password",
    ChargeType="Dynamic",
    CPU=1,
    Memory=1024,
)

try:
    resp = api.create_vm_instance(req)
    print("resource id of the vm:", resp.VMID)
except Exception as e:
    print("error:", e)
```

