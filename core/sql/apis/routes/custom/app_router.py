from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.app_config_request import UpdateConfig
from sql.apis.schemas.responses.custom.app_config_response import UpdateConfigResponse
from sql.controllers.custom.app_config_controller import AppConfigController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
app_config_router = APIRouter()


@app_config_router.post(
    "/base_template_server/app_config/update",
    response_model=UpdateConfigResponse,
)
async def update_app_config(
    update_app_config_request: UpdateConfig,
    token: str = Depends(oauth2_scheme),
):
    """[Update App Config table]

    Args:
        update_app_config_request (UpdateConfig): [Based on Input Schema]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Exception]
        error: [Error]

    Returns:
        [UpdateConfigResponse]: [Based on Output Schema]
    """
    try:
        print("Calling /base_template_server/app_config/update endpoint")
        print(f"Request: {update_app_config_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = AppConfigController().update_app_config_controller(
                request=update_app_config_request
            )
            return UpdateConfigResponse(**response)

        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        print(f"Error in /base_template_server/app_config/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@app_config_router.post(
    "/base_template_server/app_config/create",
    response_model=UpdateConfigResponse,
)
async def create_app_config(
    create_app_config_request: UpdateConfig,
    token: str = Depends(oauth2_scheme),
):
    """[Create App Config table]

    Args:
        create_app_config_request (UpdateConfig): [Based on Input Schema]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Exception]
        error: [Error]

    Returns:
        [UpdateConfigResponse]: [Based on Output Schema]
    """
    try:
        print("Calling /base_template_server/app_config/update endpoint")
        print(f"Request: {create_app_config_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = AppConfigController().create_app_config_controller(
                request=create_app_config_request
            )
            return UpdateConfigResponse(**response)

        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        print(f"Error in /base_template_server/app_config/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@app_config_router.get(
    "/base_template_server/app_config/list_all",
)
async def list_all_app_config(
    token: str = Depends(oauth2_scheme),
):
    """[list all App config records from the Table]

    Args:
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Exception]
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        print("Calling /base_template_server/app_config/list_all endpoint")
        if decodeJWT(token=token):
            response = AppConfigController().get_all_app_config_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        print(f"Error in /base_template_server/app_config/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@app_config_router.get(
    "/base_template_server/app_config/get_config",
    response_model=UpdateConfigResponse,
)
async def get_app_config(
    config_parameter: str,
    token: str = Depends(oauth2_scheme),
):
    """[list a App config record from the Table]

    Args:
        config_parameter (str): [App config parameter name]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Exception]
        error: [Error]

    Returns:
        [UpdateConfigResponse]: [cloud config parameter record]
    """
    try:
        print("Calling /base_template_server/app_config/get_config endpoint")
        if decodeJWT(token=token):
            response = AppConfigController().get_app_config_controller(
                config_parameter=config_parameter
            )
            return UpdateConfigResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        print(f"Error in /base_template_server/app_config/get_config endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@app_config_router.delete("/base_template_server/app_config/delete")
async def delete_cloud(
    config_parameter: str,
    token: str = Depends(oauth2_scheme),
):
    """[API router to delete app_config]

    Args:
        config_parameter (str): [Delete user with provided config_parameter]

    Raises:
        error: [Exception in underlying controller]

    Returns:
        [dict]: [Deleted app_config details]
    """
    try:
        print("Calling /base_template_server/app_config/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return AppConfigController().delete_app_config_controller(
                config_parameter=config_parameter
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        print(f"Error in /base_template_server/delete endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )
