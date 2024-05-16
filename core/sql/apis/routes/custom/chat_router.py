from fastapi import APIRouter, Depends, HTTPException, status
from sql.controllers.custom.chat_controller import ChatController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
chat_router = APIRouter()


@chat_router.post(
    "/base_template_server/chat/create",
)
async def create_chat(
    create_chat_request: str,
    token: str = Depends(oauth2_scheme),
):
    """[Create App Config table]

    Args:
        create_chat_request (UpdateConfig): [Based on Input Schema]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Exception]
        error: [Error]

    Returns:
        [UpdateConfigResponse]: [Based on Output Schema]
    """
    try:
        print("Calling /base_template_server/chat/update endpoint")
        print(f"Request: {create_chat_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = ChatController().create_chat_controller(
                request=create_chat_request
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
            f"Error in /base_template_server/chat/create endpoint: {error}"
        )
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
