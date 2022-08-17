from fastapi import FastAPI
from pydantic import BaseModel
import RM4mini
#from typing import Union

estadoACapi=False
estadoACpy=RM4mini.setEstadoACpy()

class StatusJson(BaseModel):
    status: bool
    
app = FastAPI()

def funcionQueEnviaSenialAAC(status: bool):
    newStatus = ""
    if status:
        newStatus = "ON"
    else:
        newStatus = "OFF"
    
    return newStatus
 
def setEstadoACapi():
    return estadoACapi


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/toggle-ac-status")
async def onAcWithBroadLin(statusJson: StatusJson):
    newStatus = funcionQueEnviaSenialAAC(statusJson.status)
    return {"message": "Nuevo estado de AC: {status}".format(status = newStatus)}
