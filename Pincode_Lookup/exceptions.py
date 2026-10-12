from fastapi.responses import JSONResponse
from fastapi import Request

#Custom Exception classes
class PinCodeNotFoundError(Exception):
    def __int__(self,pincode):
        self.pincode = pincode

class InvalidPinCodeError(Exception):
    def __init__(self, pincode:str,reason:str = "Invalid Format"):
        self.pincode = pincode
        self.reason = reason


#Custom handler

async def pincode_not_found_handler(request : Request , exc : PinCodeNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "error":"pincode_not_found",
            "message" :f"No Location for pincode: {exc.pincode}",
            "pincode": exc.pincode
        }
    )
async def invalid_pincode_handler(request : Request , exc : InvalidPinCodeError):
    return JSONResponse(
        status_code=404,
        content={
            "error":"invalid_pincode",
            "message" :f"Pincode {exc.pincode} is invalid : {exc.reason}",
            "pincode": exc.pincode
        }
    )
    
        