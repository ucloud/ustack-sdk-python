from openapi.core import client


class Client(client.Client):
    def __init__(self, config: dict, transport=None, middleware=None):
        self._config = config
        super(Client, self).__init__(config, transport, middleware)

    def openapi_client(self):
        from openapi.services.client import OpenAPIClient

        return OpenAPIClient(
            self._config, self.transport, self.middleware, self.logger
        )
