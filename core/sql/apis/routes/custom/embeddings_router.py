from fastapi import APIRouter, Depends, HTTPException, status
from sql.controllers.custom.embeddings_controller import EmbeddingsController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
embeddings_router = APIRouter()


@embeddings_router.post(
    "/base_template_server/embeddings/create",
)
async def create_embeddings(
    create_embeddings_request: str,
    token: str = Depends(oauth2_scheme),
):
    """[Create App Config table]

    Args:
        create_embeddings_request (UpdateConfig): [Based on Input Schema]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Exception]
        error: [Error]

    Returns:
        [UpdateConfigResponse]: [Based on Output Schema]
    """
    try:
        print("Calling /base_template_server/embeddings/update endpoint")
        print(f"Request: {create_embeddings_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = EmbeddingsController().create_embeddings_controller(
                request=create_embeddings_request
            )
            return response

        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        print(
            f"Error in /base_template_server/embeddings/create endpoint: {error}"
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
