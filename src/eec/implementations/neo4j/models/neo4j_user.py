from eec.interfaces.interface_user.i_user import IUser


class Neo4JUser(IUser):

    def __init__(
            self, user_id: str, user_name: str, role: str = '', salt: str = '',
            hashed_password: str = ''):
        super().__init__(user_id, user_name, role, salt, hashed_password)
