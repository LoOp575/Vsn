from pydantic import BaseModel

class SignalResponse(BaseModel):
    symbol:str
    action:str
    signal:str
    confidence:float
    risk:str
    regime:str
    probability_of_drop:float
    timestamp:str
