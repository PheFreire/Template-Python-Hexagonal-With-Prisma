import asyncio

from prisma import Prisma

from domain.services.database.providers.database_executor_provider import (
    DatabaseExecutorProvider,
)


class DatabaseExecutorProviderPrisma(DatabaseExecutorProvider):
    def __init__(self, prisma: Prisma) -> None:
        self.prisma = prisma

    def execute(self) -> Prisma:
        return self.prisma
