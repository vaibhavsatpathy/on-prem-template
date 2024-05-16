from pydantic import BaseModel


class UpdateConfig(BaseModel):
    config_parameter: str
    config_value: str
