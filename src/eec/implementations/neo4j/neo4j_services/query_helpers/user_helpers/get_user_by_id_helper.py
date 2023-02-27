from eec.implementations.neo4j.neo4j_services.query_helpers.i_neo4j_query_helper import INeo4JQueryHelper
from neo4j import Record, Query

from eec.implementations.neo4j.models.neo4j_user import Neo4JUser


class Neo4J_GetUserByIdHelper(INeo4JQueryHelper):
    """
    Gets a user by its id.
    Returns None if no user is found.

    params:
        user_id: str

    returns:
        {
            'user': Neo4JUser | None
        }
    """

    def __init__(self, user_id: str):
        super().__init__(
            'get_user_by_id',
            query=Query('''
                MATCH (user:User {user_id: $user_id})
                RETURN user
            ''')
        )
        self.user_id = user_id

    def get_arguments(self) -> dict:
        return {'user_id': self.user_id}

    def consume(self, result: list[Record]) -> dict:
        return {
            'user': Neo4JUser.from_dict(result[0]['user']) if len(result) == 1 else None
        }