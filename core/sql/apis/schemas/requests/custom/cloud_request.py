from pydantic import BaseModel


class CreateCloud(BaseModel):
    cloud_id: int
    cloud_name: str


class UpdateCloudName(BaseModel):
    cloud_id: int
    cloud_name: str
