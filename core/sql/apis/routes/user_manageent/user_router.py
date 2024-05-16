from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from sql.apis.schemas.requests.user_management.user_request import (
    Register,
    UpdateUserRole,
    ForgotPassword,
    UpdatePassword,
)
from sql.apis.schemas.responses.user_management.user_responses import (
    RegisterResponse,
    LoginResponse,
    UserDetails,
)
from sql.controllers.user_management.user_management_controller import (
    UserManagementController,
)
from commons.auth import decodeJWT, check_user_authorization
from fastapi.security import OAuth2PasswordRequestForm
from sql import logger

logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")
user_router = APIRouter()


@user_router.post("/user/register", response_model=RegisterResponse)
def register_user(register_user_request: Register, token: str = Depends(oauth2_scheme)):
    """[API router to register new user into the system]

    Args:
        register_user_request (Register): [New user details]

    Raises:
        HTTPException: [Unauthorized exception when invalid token is passed]
        error: [Exception in underlying controller]

    Returns:
        [RegisterResponse]: [Register new user response]
    """
    try:
        print("Calling /user/register endpoint")
        print(f"Request: {register_user_request}")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            user_obj = UserManagementController().register_user_controller(
                register_user_request
            )
            if user_obj.get("access_token") is None:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, detail=user_obj["status"]
                )
            else:
                return RegisterResponse(**user_obj)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        print(f"Error in /user/register endpoint: {error}")
        raise error


@user_router.post("/user/login", response_model=LoginResponse)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """[API router to login existing user]

    Args:
        form_data (OAuth2PasswordRequestForm, optional): [User details to login the user]. Defaults to Depends().

    Raises:
        error: [Exception in underlying controller]

    Returns:
        [LoginResponse]: [Login response]
    """
    try:
        print("Calling /user/login endpoint")
        valid_user = UserManagementController().login_user_controller(form_data)
        if not valid_user:
            raise HTTPException(
                status_code=400, detail="Incorrect username or password"
            )
        return LoginResponse(**valid_user)
    except Exception as error:
        print(f"Error in /user/login endpoint: {error}")
        raise error


@user_router.post("/user/forgot_password")
def forgot_password(
    forgot_pass_request: ForgotPassword,
):
    """[API Router to update password if forgotten]

    Args:
        forgot_pass_request (ForgotPassword): Input schema for forgot password

    Raises:
        error: Error is Raised

    Returns:
        dict: Status
    """
    try:
        print("Calling /user/forgot_password endpoint")
        print(f"Request: {forgot_pass_request}")
        status = UserManagementController().forgot_password_controller(
            request=forgot_pass_request
        )
        return status
    except Exception as error:
        print(f"Error in /user/forgot_password endpoint: {error}")
        raise error


@user_router.post("/user/update_password")
def update_password(
    update_pass_request: UpdatePassword,
):
    """[API Router to update password if forgotten]

    Args:
        update_pass_request (ForgotPassword): Input schema for forgot password

    Raises:
        error: Error is Raised

    Returns:
        dict: Status
    """
    try:
        print("Calling /user/update_password endpoint")
        print(f"Request: {update_pass_request}")
        status = UserManagementController().update_password_controller(
            request=update_pass_request
        )
        return status
    except Exception as error:
        print(f"Error in /user/update_password endpoint: {error}")
        raise error


@user_router.post("/user/update/role")
async def update_user_role(
    update_user_role_request: UpdateUserRole,
    token: str = Depends(oauth2_scheme),
):
    """[API router to update user role]

    Args:
        update_user_role_request (UpdateUserLicense): [User role details to be updated]

    Raises:
        error: [Exception in underlying controller]

    Returns:
        [UpdateUserResponse]: [User updated details]
    """
    try:
        print("Calling /user/update/role endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return UserManagementController().update_user_role_controller(
                request=update_user_role_request
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        print(f"Error in /user/update/role endpoint: {error}")
        raise error


@user_router.delete("/user/delete")
async def delete_user(
    username: str,
    token: str = Depends(oauth2_scheme),
):
    """[API router to delete user]

    Args:
        user_name (str): [Delete user with provided user_name]

    Raises:
        error: [Exception in underlying controller]

    Returns:
        [dict]: [Deleted user details]
    """
    try:
        print("Calling /user/delete endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if authenticated_user_details:
            _ = check_user_authorization(
                user_details=authenticated_user_details, allowed_user_role_id=1
            )
            return UserManagementController().delete_user_controller(username=username)
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid access token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as error:
        print(f"Error in /user/update/role endpoint: {error}")
        raise error


@user_router.get("/user/list_all")
async def get_all_users():
    """[Get List of all Users]

    Raises:
        error: [Error details]

    Returns:
        [list]: [List of Users]
    """
    try:
        print("Calling /user/delete endpoint")
        list_of_users = UserManagementController().get_all_users_controller()
        return list_of_users
    except Exception as error:
        print(f"Error in /user/list_all endpoint: {error}")
        raise error


@user_router.get("/user/user_details", response_model=UserDetails)
async def get_user_details(
    username: str,
):
    try:
        print("Calling /user/delete endpoint")
        user_details = UserManagementController().get_user_controller(username=username)
        return UserDetails(**user_details)
    except Exception as error:
        print(f"Error in /user/user_details endpoint: {error}")
        raise error
