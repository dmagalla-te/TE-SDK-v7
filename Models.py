from pydantic import BaseModel, Field, HttpUrl, EmailStr
from typing import Optional, Dict, List
from datetime import datetime


class AID(BaseModel):
    
    aid: int

class BaseUrl(BaseModel):

    URL: HttpUrl 


BASE = BaseUrl(URL="https://api.thousandeyes.com/v7/")


class Endpoint(BaseModel):

    list_account_groups: str = "account-groups" 

endpoint = Endpoint()



