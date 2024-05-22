from dataclasses import dataclass

from domain.services.database.factories.database_connection_factory import (
    DatabaseConnectionFactory,
)

@dataclass
class DependencyInjections:
    database_connection_factory: DatabaseConnectionFactory