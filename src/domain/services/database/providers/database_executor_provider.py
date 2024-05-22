from domain.models.database.generic_db_return import GenericDbReturn


class DatabaseExecutorProvider:
    async def execute(self) -> GenericDbReturn:
        raise NotImplementedError()
