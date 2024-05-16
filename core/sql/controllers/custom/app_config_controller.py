from sql import config, logger
from sql.crud.app_config_crud import CRUDAppConfig

logging = logger(__name__)


class AppConfigController:
    def __init__(self):
        self.CRUDAppConfig = CRUDAppConfig()

    def create_app_config_controller(self, request):
        """[Create a app Config record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [app Config Data]
        """
        try:
            print("executing create_app_config_controller function")
            create_app_config_request = request.dict(exclude_none=True)

            self.CRUDAppConfig.create(**create_app_config_request)

            return create_app_config_request
        except Exception as error:
            print(f"Error in create_app_config_controller function: {error}")
            raise error

    def update_app_config_controller(self, request):
        """[Update a app Config record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [app Config Data]
        """
        try:
            print("executing update_app_config_controller function")
            update_app_config_request = request.dict(exclude_none=True)

            self.CRUDAppConfig.update(config_request=update_app_config_request)

            return update_app_config_request
        except Exception as error:
            print(f"Error in update_app_config_controller function: {error}")
            raise error

    def get_all_app_config_controller(self):
        """[Get All app config records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all app config Records]
        """
        try:
            print("executing get_all_app_config_controller function")
            return self.CRUDAppConfig.read_all()
        except Exception as error:
            print(f"Error in get_all_app_config_controller function: {error}")
            raise error

    def get_app_config_controller(self, config_parameter: str):
        """[Get a app config record Controller]

        Args:
            config_parameter (str): [Unique Identifier for a app Config]

        Raises:
            error: [Error]

        Returns:
            [type]: [app config Record]
        """
        try:
            print("executing get_app_config_controller function")
            return self.CRUDAppConfig.read(config_parameter=config_parameter)
        except Exception as error:
            print(f"Error in get_app_config_controller function: {error}")
            raise error

    def delete_app_config_controller(self, config_parameter: str):
        """[Controller to delete a app_config]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted app_config details]
        """
        try:
            print("executing delete_app_config_controller function")
            return self.CRUDAppConfig.delete(config_parameter=config_parameter)
        except Exception as error:
            print(f"Error in delete_app_config_controller function: {error}")
            raise {"error": "Invalid username or password"}
