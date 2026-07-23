from ucloudstack.core import client


class Client(client.Client):
    def __init__(self, config: dict, transport=None, middleware=None):
        self._config = config
        super(Client, self).__init__(config, transport, middleware)

    def ucloudstack_client(self):
        from ucloudstack.services.client import UCloudStackClient

        return UCloudStackClient(
            self._config, self.transport, self.middleware, self.logger
        )
