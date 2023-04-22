from typing import Any, Mapping
from logging import Logger
from core.messagebus import Publisher
from core.rpc import Caller, Server
from core.repo import SearchFilter
from module.auth.component.model.group_model import group_model
from module.auth.schema.group import GroupData
from module.auth.schema.token import TokenData


def register_rpc(
    logger: Logger,
    rpc_server: Server,
    rpc_caller: Caller,
    publisher: Publisher
):
    logger.info('🥪 Register RPC handlers for "auth.group"')

    @rpc_server.register('get_auth_group')
    async def get(
        keyword: str,
        criterion: Mapping[str, Any],
        limit: int,
        offset: int,
        user_token_data: Mapping[str, Any]
    ) -> Mapping[str, Any]:
        result = await group_model.get(
            search_filter=SearchFilter(
                keyword=keyword, criterion=criterion
            ),
            limit=limit,
            offset=offset
        )
        return result.dict()

    @rpc_server.register('get_auth_group_by_id')
    async def get_by_id(
        id: str,
        user_token_data: Mapping[str, Any] = {}
    ) -> Mapping[str, Any]:
        row = await group_model.get_by_id(id)
        return row.dict()

    @rpc_server.register('insert_auth_group')
    async def insert(
        data: Mapping[str, Any],
        user_token_data: Mapping[str, Any]
    ) -> Mapping[str, Any]:
        user_token_data: TokenData = TokenData(**user_token_data)
        data['created_by'] = user_token_data.user_id
        data['updated_by'] = user_token_data.user_id
        row = await group_model.insert(
            data=GroupData(**data)
        )
        return row.dict()

    @rpc_server.register('update_auth_group')
    async def update(
        id: str,
        data: Mapping[str, Any],
        user_token_data: Mapping[str, Any]
    ) -> Mapping[str, Any]:
        user_token_data: TokenData = TokenData(**user_token_data)
        data['updated_by'] = user_token_data.user_id
        row = await group_model.update(
            id=id, data=GroupData(**data)
        )
        return row.dict()

    @rpc_server.register('delete_auth_group')
    async def delete(
        id: str,
        user_token_data: Mapping[str, Any]
    ) -> Mapping[str, Any]:
        user_token_data = TokenData(**user_token_data)
        row = await group_model.delete(id=id).dict()
        return row.dict()
