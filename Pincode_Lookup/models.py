from pydantic import BaseModel ,field_validator

class PincodeRequest(BaseModel):
    pincode:str

    #pincode must be excatly 6 digit
    @field_validator("pincode")
    @classmethod
    def validate_pincode(cls,value):
        if (len(value)!=6 or not value.isdigit()):
            raise ValueError("Pincode must be a 6 digit number")
        return value


class LocationResponse(BaseModel):
    pincode:str
    city:str
    state:str
    district:str

class BulkRequest(BaseModel):
    pincodes:list[str]
    @field_validator("pincodes")
    @classmethod
    def validate_pincodes(cls,values):
        if not values:
            raise ValueError("Atleast one pincode is required")
        if(len(values) >20):
            raise ValueError("Maximum 20 pincodes allowed per request")

        for val in values:
            if (len(val)!=6 or not val.isdigit()):
                raise ValueError("Pincode must be a 6 digit number")
        return values
        
class BulkResponse(BaseModel):
    status: str = "success"
    found : int
    not_found : int
    results:list[LocationResponse]
    missing : list[str]
    