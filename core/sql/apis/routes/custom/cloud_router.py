from fastapi import APIRouter, Depends, HTTPException, status
from sql.apis.schemas.requests.custom.cloud_request import (
    UpdateCloudName,
    CreateCloud,
)
from sql.apis.schemas.responses.custom.cloud_response import (
    UpdateCloudNameResponse,
    CreateCloudResponse,
)
from sql.controllers.custom.cloud_controller import CloudController
from fastapi.security import OAuth2PasswordBearer
from commons.auth import decodeJWT, check_user_authorization
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
cloud_router = APIRouter()


@cloud_router.post(
    "/base_template_server/cloud/create",
    response_model=CreateCloudResponse,
)
async def create_cloud_config(
    create_cloud_request: CreateCloud,
    token: str = Depends(oauth2_scheme),
):
    """[Create Cloud table]

    Args:
        create_cloud_request (CreateCloud): [Based on Input Schema]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Exception]
        error: [Error]

    Returns:
        [CreateConfigResponse]: [Based on Output Schema]
    """
    try:
        print("Calling /base_template_server/cloud_config/create endpoint")
        print(f"Request: {create_cloud_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = CloudController().create_cloud_controller(
                request=create_cloud_request
            )
            return CreateCloudResponse(**response)

        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        print(f"Error in /base_template_server/cloud_config/create endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@cloud_router.post(
    "/base_template_server/cloud/update",
    response_model=UpdateCloudNameResponse,
)
async def update_cloud(
    update_cloud_request: UpdateCloudName,
    token: str = Depends(oauth2_scheme),
):
    """[Update Cloud Config table]

    Args:
        update_cloud_request (UpdateCloud): [Based on Input Schema]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Exception]
        error: [Error]

    Returns:
        [UpdateCloudNameResponse]: [Based on Output Schema]
    """
    try:
        print("Calling /base_template_server/cloud/update endpoint")
        print(f"Request: {update_cloud_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            response = CloudController().update_cloud_controller(
                request=update_cloud_request
            )
            return UpdateCloudNameResponse(**response)

        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        print(f"Error in /base_template_server/cloud/update endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@cloud_router.get(
    "/base_template_server/cloud/list_all",
)
async def list_all_cloud(
    token: str = Depends(oauth2_scheme),
):
    """[list all cloud records from the Table]

    Args:
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Exception]
        error: [Error]

    Returns:
        [type]: [description]
    """
    try:
        print("Calling /base_template_server/cloud/list_all endpoint")
        if decodeJWT(token=token):
            response = CloudController().get_all_cloud_controller()
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        print(f"Error in /base_template_server/cloud/list_all endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@cloud_router.get(
    "/base_template_server/cloud/get_cloud",
    response_model=UpdateCloudNameResponse,
)
async def get_cloud_config(
    cloud_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[list a cloud record from the Table]

    Args:
        cloud_id (str): [cloud parameter name]
        token (str, optional): [description]. Defaults to Depends(oauth2_scheme).

    Raises:
        HTTPException: [Exception]
        error: [Error]

    Returns:
        [UpdateConfigResponse]: [cloud parameter record]
    """
    try:
        print("Calling /base_template_server/cloud/get_cloud endpoint")
        if decodeJWT(token=token):
            response = CloudController().get_cloud_controller(cloud_id=cloud_id)
            return UpdateCloudNameResponse(**response)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        print(f"Error in /base_template_server/cloud/get_cloud endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error)
        )


@cloud_router.delete("/base_template_server/cloud/delete")
async def delete_cloud(
    cloud_id: int,
    token: str = Depends(oauth2_scheme),
):
    """[API router to delete cloud]

    Args:
        cloud_id (str): [Delete user with provided cloud_id]

    Raises:
        error: [Exception in underlying controller]

    Returns:
        [dict]: [Deleted cloud details]
    """
    try:
        print("Calling /base_template_server/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return CloudController().delete_cloud_controller(cloud_id=cloud_id)
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
