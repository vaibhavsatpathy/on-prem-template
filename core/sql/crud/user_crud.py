from sql import session, logger
from sql.orm_models.users import User

logging = logger(__name__)


class CRUDUser:
    def create(self, **kwargs):
        """
        [CRUD function to create a new User record]
        Raises:
        error:[Error returned from the DB layer]
        """
        try:
            print("CRUDUser create request")
            user = User(**kwargs)
            with session() as transaction_session:
                transaction_session.add(user)
                transaction_session.commit()
                transaction_session.refresh(user)
            return user.__dict__
        except Exception as error:
            print(f"Error in CRUDUser create function : {error}")
            raise error

    def read(self, username: str):
        """[CRUD function to read a User record]

        Args:
            user_name (str): [User name to filter the record]

        Raises:
            error: [Error returned from the DB layer]

        Returns:
            [dict]: [user record matching the criteria]
        """
        try:
            print("CRUDUser read request")
            with session() as transaction_session:
                obj: User = (
                    transaction_session.query(User)
                    .filter(User.username == username)
                    .first()
                )
            if obj is not None:
                return obj.__dict__
            else:
                return None
        except Exception as error:
            print(f"Error in CRUDUser read function : {error}")
            raise error

    def read_all(self):
        """[CRUD function to read_all Users record]

        Raises:
            error: [Error returned from the DB layer]

        Returns:
            [list]: [all user records]
        """
        try:
            print("CRUDUser read_all request")
            with session() as transaction_session:
                obj: User = transaction_session.query(User).all()
            if obj is not None:
                return [row.__dict__ for row in obj]
            else:
                return []
        except Exception as error:
            print(f"Error in CRUDUser read_all function : {error}")
            raise error

    def update(self, **kwargs):
        """[CRUD function to update a User record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            print("CRUDUser update request")
            with session() as transaction_session:
                obj: User = (
                    transaction_session.query(User)
                    .filter(User.username == kwargs.get("username"))
                    .update(kwargs, synchronize_session=False)
                )
                transaction_session.commit()
        except Exception as error:
            print(f"Error in CRUDUser update function : {error}")
            raise error

    def update_role(self, **kwargs):
        """[CRUD function to update a User record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            print("CRUDUser update request")
            with session() as transaction_session:
                obj: User = (
                    transaction_session.query(User)
                    .filter(User.user_role_id == kwargs.get("user_role_id"))
                    .update(kwargs, synchronize_session=False)
                )
                transaction_session.commit()
        except Exception as error:
            print(f"Error in CRUDUser update function : {error}")
            raise error

    def delete(self, username: str):
        """[CRUD function to delete a User record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            print("CRUDUser delete request")
            with session() as transaction_session:
                obj: User = (
                    transaction_session.query(User)
                    .filter(User.username == username)
                    .first()
                )
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            print(f"Error in CRUDUser delete function : {error}")
            raise error
