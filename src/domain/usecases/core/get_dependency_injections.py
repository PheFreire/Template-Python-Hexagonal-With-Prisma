from domain.models.core.dependency_injections import DependencyInjections
from domain.services.core.bridges.dependency_injection_bridge import (
    DependencyInjectionBridge,
)
from domain.services.core.providers.environment_variables_provider import (
    EnvironmentVariablesProvider,
)


class GetDependencyInjections:
    def __init__(
        self,
        environment_variables_provider: EnvironmentVariablesProvider,
        dependency_injection_bridge: DependencyInjectionBridge,
    ) -> None:
        self.environment_variables_provider = environment_variables_provider
        self.dependency_injection_bridge = dependency_injection_bridge

    def call(self) -> DependencyInjections:
        injections_payload = (
            self.environment_variables_provider.get_injections_payload()
        )

        database_connection_factory = self.dependency_injection_bridge.get_database_connection_factory_injection(
            injections_payload
        )

        return DependencyInjections(
            database_connection_factory,
        )
