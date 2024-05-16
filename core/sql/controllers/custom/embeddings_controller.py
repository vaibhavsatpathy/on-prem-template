from sql import config, logger
from sql.crud.embeddings_crud import CRUDEmbeddings
from sql.utils.custom.llama3_embeddings import create_embeddings

logging = logger(__name__)


class EmbeddingsController:
    def __init__(self):
        self.CRUDEmbeddings = CRUDEmbeddings()

    def create_embeddings_controller(self, request):
        """[Create a Product Catalog record Controller]

        Args:
            request ([type]): [Based on Input Schema]

        Raises:
            error: [Error]

        Returns:
            [type]: [Product Catalog Data]
        """
        try:
            print("executing create_embeddings_controller function")
            created_embeddings = create_embeddings(text=request)
            # self.CRUDEmbeddings.create(**create_embeddings_request)

            return created_embeddings
        except Exception as error:
            print(f"Error in create_embeddings_controller function: {error}")
            raise error
