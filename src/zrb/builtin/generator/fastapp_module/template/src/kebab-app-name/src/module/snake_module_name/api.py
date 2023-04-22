from fastapi import FastAPI
from logging import Logger
from core.messagebus import Publisher
from core.rpc import Caller
from module.auth.core import Authorizer


def register_api(
    logger: Logger,
    app: FastAPI,
    authorizer: Authorizer,
    rpc_caller: Caller,
    publisher: Publisher
):
    logger.info('🥪 Register API for "snake_module_name"')

    @app.get('/api/v1/kebab-module-name')
    async def get_snake_module_name():
        # Publish hit event
        await publisher.publish(
            'hit_snake_module_name', '/api/v1/kebab-module-name'
        )
        # Send RPC request
        result = await rpc_caller.call(
            'process_snake_module_name', 'hello', 'world', magic_number=42
        )
        return result
