from sql import session, logger
from sql.orm_models.cloud import Cloud

logging = logger(__name__)


class CRUDCloud:
    def create(self, **kwargs):
        """[CRUD function to create a new Cloud record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            print("CRUDCloud create request")
            cloud = Cloud(**kwargs)
            with session() as transaction_session:
                transaction_session.add(cloud)
                transaction_session.commit()
                transaction_session.refresh(cloud)
            return cloud.__dict__
        except Exception as error:
            print(f"Error in CRUDCloud create function : {error}")
            raise error

    def read(self, cloud_id: int):
        """[CRUD function to read Cloud records]

        Raises:
            error: [Error returned from the DB layer]

        Returns:
            [list]: [all Cloud records matching condition]
        """
        try:
            print("CRUDCloud read request")
            with session() as transaction_session:
                obj: Cloud = (
                    transaction_session.query(Cloud)
                    .filter(Cloud.cloud_id == cloud_id)
                    .first()
                )
            if obj is not None:
                return obj.__dict__
            else:
                return None
        except Exception as error:
            print(f"Error in CRUDCloud read function : {error}")
            raise error

    def read_all(self):
        """[CRUD function to read all Cloud records]

        Raises:
            error: [Error returned from the DB layer]

        Returns:
            [list]: [all Cloud records]
        """
        try:
            print("CRUDCloud read all request")
            with session() as transaction_session:
                obj: Cloud = transaction_session.query(Cloud).all()
            if obj is not None:
                return [row.__dict__ for row in obj]
            else:
                return []
        except Exception as error:
            print(f"Error in CRUDCloud read all function : {error}")
            raise error

    def update(self, **kwargs):
        """[CRUD function to update a Cloud record]
        Args:
            kwargs ([dict]): [Cloud request]
        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            print("CRUDCloud update function")
            with session() as transaction_session:
                cloud_obj: Cloud = (
                    transaction_session.query(Cloud)
                    .filter(Cloud.cloud_id == kwargs.get("cloud_id"))
                    .update(kwargs, synchronize_session=False)
                )
                transaction_session.commit()
        except Exception as error:
            print(f"Error in CRUDCloud update function : {error}")
            raise error

    def delete(self, cloud_id: int):
        """[CRUD function to delete a Cloud record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            print("CRUDCloud delete request")
            with session() as transaction_session:
                obj: Cloud = (
                    transaction_session.query(Cloud)
                    .filter(Cloud.cloud_id == cloud_id)
                    .first()
                )
                transaction_session.delete(obj)
                transaction_session.commit()
                print(f"object is : {obj.__dict__}")
                return obj.__dict__
        except Exception as error:
            print(f"Error in CRUDUCloud delete function : {error}")
            raise error
