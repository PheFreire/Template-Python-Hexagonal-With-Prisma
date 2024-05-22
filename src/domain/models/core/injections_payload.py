from dataclasses import dataclass


@dataclass
class InjectionsPayload:
    database_connection_factory: str