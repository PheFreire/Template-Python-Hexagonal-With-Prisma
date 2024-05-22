from domain.models.core.injections_payload import InjectionsPayload
from domain.services.database.factories.database_connection_factory import (
    DatabaseConnectionFactory,
)


class DependencyInjectionBridge:
    def get_database_connection_factory_injection(
        self, injections_payload: InjectionsPayload
    ) -> DatabaseConnectionFactory:
        raise NotImplementedError()