from domain.services.database.providers.database_executor_provider import (
    DatabaseExecutorProvider,
)


class DatabaseConnectionFactory:
    async def call(self) -> DatabaseExecutorProvider:
        raise NotImplementedError()
