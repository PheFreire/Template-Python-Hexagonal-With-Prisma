from domain.models.core.injections_payload import InjectionsPayload
from domain.services.core.bridges.dependency_injection_bridge import (
    DependencyInjectionBridge,
)
from domain.services.database.factories.database_connection_factory import (
    DatabaseConnectionFactory,
)
from infrastructure.adapters.database.database_connection_factories.database_connection_factory_prisma import (
    DatabaseConnectionFactoryPrisma,
)

class DependencyInjectionBridgeCore(DependencyInjectionBridge):
    def __init__(self) -> None:
        self.adapters = {
            "database_connection_factory_prisma": DatabaseConnectionFactoryPrisma,
        }

    def get_database_connection_factory_injection(
        self, injections_payload: InjectionsPayload
    ) -> DatabaseConnectionFactory:
        return self.adapters[injections_payload.database_connection_factory]()
