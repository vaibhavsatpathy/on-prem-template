from pydantic import BaseModel


class UpdateConfigResponse(BaseModel):
    config_parameter: str
    config_value: str = None
