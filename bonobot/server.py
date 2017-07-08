import aiohttp
import aiohttp.server
import json
from aiohttp import MultiDict
from urllib.parse import urlparse, parse_qsl


class HttpRequestHandler(aiohttp.server.ServerHttpProtocol):
    def __init__(self, *args, **kwargs):
        self.client = kwargs['client']
        self.token = kwargs['token']
        self.Action = kwargs['action']
        super()

    async def handle_request(self, message, payload):
        """Traite une requête POST pour executer une action"""

        if message.method == 'POST':
            data = await payload.read()
            decoded = data.decode('utf-8')
            get_params = MultiDict(parse_qsl(urlparse(message.path).query))
            post_params = json.loads(decoded)
            if get_params['token'] == self.token:
                code = 200
                post_params['client'] = self.client
                method = getattr(self.Action, post_params['action'])
                await method(**post_params)
            else:
                code = 401
        else:
            code = 403
        response = aiohttp.Response(
            self.writer, code, http_version=message.version)
        response.send_headers()
        await response.write_eof()
