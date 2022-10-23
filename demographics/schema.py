from pydantic import BaseModel

class Appplication(BaseModel):
    job_title: str
    organization: str
    city: str
    gender: str
    no_of_devfest: int = 0
    gde: bool = False
    gdg: bool = False
    gdsc: bool = False
    wtm: bool = False
    confirmation: str
