import os

import toml

from domain.models.core.injections_payload import InjectionsPayload
from domain.services.core.providers.environment_variables_provider import (
    EnvironmentVariablesProvider,
)


class EnvironmentVariablesProviderToml(EnvironmentVariablesProvider):
    def get_injections_payload(self) -> InjectionsPayload:
        return InjectionsPayload(
            **toml.load(open(os.getenv("ENV_PATH")))["injections"]
        )
