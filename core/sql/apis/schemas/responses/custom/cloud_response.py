from pydantic import BaseModel


class CreateCloudResponse(BaseModel):
    cloud_id: int
    cloud_name: str


class UpdateCloudNameResponse(BaseModel):
    cloud_id: int
    cloud_name: str
