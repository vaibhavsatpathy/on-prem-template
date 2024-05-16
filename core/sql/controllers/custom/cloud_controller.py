from sql import config, logger
from sql.crud.cloud_crud import CRUDCloud

logging = logger(__name__)


class CloudController:
    def __init__(self):
        self.CRUDCloud = CRUDCloud()

    def create_cloud_controller(self, request):
        """[Create a cloud record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [cloud Data]
        """
        try:
            print("executing create_cloud_controller function")
            create_cloud_request = request.dict(exclude_none=True)

            self.CRUDCloud.create(**create_cloud_request)

            return create_cloud_request
        except Exception as error:
            print(f"Error in create_cloud_controller function: {error}")
            raise error

    def update_cloud_controller(self, request):
        """[Update a cloud record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [cloud Data]
        """
        try:
            print("executing update_cloud_controller function")
            update_cloud_request = request.dict(exclude_none=True)

            self.CRUDCloud.update(**update_cloud_request)

            return update_cloud_request
        except Exception as error:
            print(f"Error in update_cloud_controller function: {error}")
            raise error

    def get_all_cloud_controller(self):
        """[Get All cloud records Controller]

        Raises:
            error: [Error]

        Returns:
            [type]: [List of all cloud Records]
        """
        try:
            print("executing get_all_cloud_controller function")
            return self.CRUDCloud.read_all()
        except Exception as error:
            print(f"Error in get_all_cloud_controller function: {error}")
            raise error

    def get_cloud_controller(self, cloud_id: int):
        """[Get a cloud record Controller]

        Args:
            config_parameter (str): [Unique Identifier for a cloud]

        Raises:
            error: [Error]

        Returns:
            [type]: [cloud Record]
        """
        try:
            print("executing get_cloud_controller function")
            return self.CRUDCloud.read(cloud_id=cloud_id)
        except Exception as error:
            print(f"Error in get_cloud_controller function: {error}")
            raise error

    def delete_cloud_controller(self, cloud_id: int):
        """[Controller to delete a cloud]

        Raises:
            error: [Error raised from controller layer]

        Returns:
            [dict]: [deleted cloud details]
        """
        try:
            print("executing delete_cloud_controller function")
            return self.CRUDCloud.delete(cloud_id=cloud_id)
        except Exception as error:
            print(f"Error in delete_cloud_controller function: {error}")
            raise {"error": "Invalid username or password"}
