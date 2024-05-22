from domain.models.core.dependency_injections import DependencyInjections
from domain.services.database.providers.database_executor_provider import (
    DatabaseExecutorProvider,
)
from domain.usecases.database.start_database import StartDatabase


async def start_database_controller(
    dependency_injections: DependencyInjections,
) -> DatabaseExecutorProvider:
    start_database = StartDatabase(
        dependency_injections.database_connection_factory
    )
    return await start_database.call()
