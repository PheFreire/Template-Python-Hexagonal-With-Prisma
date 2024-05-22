from domain.models.core.injections_payload import InjectionsPayload


class EnvironmentVariablesProvider:
    def get_injections_payload(self) -> InjectionsPayload:
        raise NotImplementedError()
