from config import (
    app_enable_rpc_server, app_enable_message_consumer, app_enable_api
)
from component.log import logger
from component.app import app
from component.messagebus import consumer, publisher
from component.rpc import rpc_caller, rpc_server
from snake_module_name.api import register_api
from snake_module_name.event import register_event
from snake_module_name.rpc import register_rpc


def register_snake_module_name():
    if app_enable_api:
        register_api(
            logger=logger,
            app=app,
            rpc_caller=rpc_caller,
            publisher=publisher
        )
    if app_enable_message_consumer:
        register_event(
            logger=logger,
            consumer=consumer,
            rpc_caller=rpc_caller,
            publisher=publisher
        )
    if app_enable_rpc_server:
        register_rpc(
            logger=logger,
            rpc_server=rpc_server,
            rpc_caller=rpc_caller,
            publisher=publisher
        )
