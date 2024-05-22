from domain.services.database.factories.database_connection_factory import (
    DatabaseConnectionFactory,
)
from domain.services.database.providers.database_executor_provider import (
    DatabaseExecutorProvider,
)


class StartDatabase:
    def __init__(
        self, database_connection_factory: DatabaseConnectionFactory
    ) -> None:
        self.database_connection_factory = database_connection_factory

    async def call(self) -> DatabaseExecutorProvider:
        return await self.database_connection_factory.call()
