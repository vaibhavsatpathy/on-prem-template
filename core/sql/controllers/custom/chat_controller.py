from sql import config, logger
from sql.utils.custom.llama3_chat import chat_response

logging = logger(__name__)


class ChatController:
    def __init__(self):
        pass

    def create_chat_controller(self, request):
        """[Create a Product Catalog record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Product Catalog Data]
        """
        try:
            print("executing create_chat_controller function")
            response = chat_response(text=request)

            return response
        except Exception as error:
            print(f"Error in create_chat_controller function: {error}")
            raise error
