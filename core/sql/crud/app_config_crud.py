from sql import session, logger
from sql.orm_models.app_config import AppConfig
from datetime import datetime

logging = logger(__name__)


class CRUDAppConfig:
    def create(self, **kwargs):
        """[CRUD function to create a new App Config record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            print("CRUDAppConfig create request")
            kwargs.update(
                {
                    "created_at": datetime.now(),
                    "updated_at": datetime.now(),
                }
            )
            app_config = AppConfig(**kwargs)
            with session() as transaction_session:
                transaction_session.add(app_config)
                transaction_session.commit()
                transaction_session.refresh(app_config)
            return app_config.__dict__
        except Exception as error:
            print(f"Error in CRUDAppConfig create function : {error}")
            raise error

    def read(self, config_parameter: str):
        """[CRUD function to read App Config records]

        Raises:
            error: [Error returned from the DB layer]

        Returns:
            [list]: [all App Config records matching condition]
        """
        try:
            print("CRUDAppConfig read request")
            with session() as transaction_session:
                obj: AppConfig = (
                    transaction_session.query(AppConfig)
                    .filter(AppConfig.config_parameter == config_parameter)
                    .first()
                )
            if obj is not None:
                return obj.__dict__
            else:
                return None
        except Exception as error:
            print(f"Error in CRUDAppConfig read function : {error}")
            raise error

    def read_all(self):
        """[CRUD function to read all App Config records]

        Raises:
            error: [Error returned from the DB layer]

        Returns:
            [list]: [all App Config records]
        """
        try:
            print("CRUDAppConfig read all request")
            with session() as transaction_session:
                obj: AppConfig = transaction_session.query(AppConfig).all()
            if obj is not None:
                return [row.__dict__ for row in obj]
            else:
                return []
        except Exception as error:
            print(f"Error in CRUDAppConfig read all function : {error}")
            raise error

    def update(self, config_request):
        """[CRUD function to update a App Config record]

        Args:
            config_request ([dict]): [App config request]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            print("CRUDAppConfig update function")
            with session() as transaction_session:
                obj: AppConfig = (
                    transaction_session.query(AppConfig)
                    .filter(
                        AppConfig.config_parameter
                        == config_request.get("config_parameter")
                    )
                    .first()
                )
                if obj:
                    obj.config_value = config_request.get("config_value", None)
                    transaction_session.commit()
                    transaction_session.refresh(obj)
        except Exception as error:
            print(f"Error in CRUDAppConfig update function : {error}")
            raise error

    def delete(self, config_parameter: str):
        """[CRUD function to delete a AppConfig record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            print("CRUDAppConfig delete request")
            with session() as transaction_session:
                obj: AppConfig = (
                    transaction_session.query(AppConfig)
                    .filter(AppConfig.config_parameter == config_parameter)
                    .first()
                )
                transaction_session.delete(obj)
                transaction_session.commit()
                return obj.__dict__
        except Exception as error:
            print(f"Error in CRUDUAppConfig delete function : {error}")
            raise error
