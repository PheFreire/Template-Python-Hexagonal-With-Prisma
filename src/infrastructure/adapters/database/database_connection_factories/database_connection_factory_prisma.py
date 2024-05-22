import asyncio

from prisma import Prisma

from domain.services.database.factories.database_connection_factory import (
    DatabaseConnectionFactory,
)
from domain.services.database.providers.database_executor_provider import (
    DatabaseExecutorProvider,
)
from infrastructure.adapters.database.database_executor_providers.database_executor_provider_prisma import (
    DatabaseExecutorProviderPrisma,
)


class DatabaseConnectionFactoryPrisma(DatabaseConnectionFactory):
    async def call(self) -> DatabaseExecutorProviderPrisma:
        prisma = await self.__setup_prisma()
        return DatabaseExecutorProviderPrisma(prisma)

    async def __setup_prisma(self) -> Prisma:
        prisma = Prisma()
        await prisma.connect()
        return prisma
