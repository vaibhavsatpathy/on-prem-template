from sql.crud.user_crud import CRUDUser
from sql.crud.user_roles_crud import CRUDUserRole
from sql.crud.app_config_crud import CRUDAppConfig
from sql.crud.cloud_crud import CRUDCloud
from sql.controllers.user_management.user_management_controller import (
    UserManagementController,
)
from sql.apis.schemas.requests.user_management.user_request import Register
from datetime import datetime
import os


def create_user_role(user_role_record: list):
    user_roles = CRUDUserRole().read_all()
    if len(user_roles) == 0:
        for item in user_role_record:
            CRUDUserRole().create(**item)
    else:
        pass


def create_admin_user(admin_user_request):
    existing_admin_user = CRUDUser().read(username="admin")
    if not existing_admin_user:
        _ = UserManagementController().register_user_controller(
            request=admin_user_request
        )
    else:
        pass


def create_app_config(app_config_request):
    existing_app_config = CRUDAppConfig().read_all()
    if len(existing_app_config) == 0:
        for item in app_config_request:
            CRUDAppConfig().create(**item)
    else:
        pass


def create_cloud_config(cloud_config_request):
    existing_cloud_config = CRUDCloud().read_all()
    if len(existing_cloud_config) == 0:
        for item in cloud_config_request:
            CRUDCloud().create(**item)
    else:
        pass


def main():
    user_role_record = [
        {
            "user_role": "admin",
            "user_role_id": 1,
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "user_role": "editor",
            "user_role_id": 2,
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
        {
            "user_role": "viewer",
            "user_role_id": 3,
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        },
    ]
    create_user_role(user_role_record)

    admin_user_request = Register(
        username="admin",
        password=os.environ.get("password"),
        fullname="Admin User",
        email_id="admin@scejointpole.com",
        user_role="admin",
        user_role_id=1,
    )
    create_admin_user(admin_user_request)

    default_app_config = [
        {
            "config_parameter": "sample_key",
            "config_value": "sample_value",
        }
    ]
    create_app_config(app_config_request=default_app_config)

    default_cloud_config = [
        {"cloud_id": 0, "cloud_name": "GCP"},
        {"cloud_id": 1, "cloud_name": "Azure"},
        {"cloud_id": 2, "cloud_name": "AWS"},
    ]
    create_cloud_config(cloud_config_request=default_cloud_config)
