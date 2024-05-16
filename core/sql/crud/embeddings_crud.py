from sql import session, logger
from sql.orm_models.embeddings import Embeddings
from datetime import datetime
from sqlalchemy.sql import select

logging = logger(__name__)


class CRUDEmbeddings:
    def create(self, **kwargs):
        """[CRUD function to create a new Embeddings record]

        Raises:
            error: [Error returned from the DB layer]
        """
        try:
            print("CRUDEmbeddings create request")
            kwargs.update(
                {
                    "created_at": datetime.now(),
                    "updated_at": datetime.now(),
                }
            )
            embeddings = Embeddings(**kwargs)
            with session() as transaction_session:
                transaction_session.add(embeddings)
                transaction_session.commit()
                transaction_session.refresh(embeddings)
            return embeddings.__dict__
        except Exception as error:
            print(f"Error in CRUDEmbeddings create function : {error}")
            raise error

    def read_all(self):
        """[CRUD function to read all Embeddings records]

        Raises:
            error: [Error returned from the DB layer]

        Returns:
            [list]: [all Embeddings records]
        """
        try:
            print("CRUDEmbeddings read all request")
            with session() as transaction_session:
                # obj: Embeddings = transaction_session.query(Embeddings).all()
                obj: Embeddings = transaction_session.scalars(
                    select(Embeddings)
                    .order_by(Embeddings.product_embeddings.l2_distance([3, 1, 2]))
                    .limit(5)
                )
                all_relevant_data = []
                for row in obj:
                    all_relevant_data.append(row.product_id)
                return all_relevant_data
        except Exception as error:
            print(f"Error in CRUDEmbeddings read all function : {error}")
            raise error
