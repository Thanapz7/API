from fastapi import FastAPI
from h11 import Data
import uvicorn

from action import Action
a = Action

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/gethw")
def get_HW():  
    data = a.getHW()
    return data

@app.get("/update_status_hw")
def update_status_hw(ID, status):
    data = a.updateHW(ID, status)
    return data

@app.get("/update_value_hw")
def update_status_hw(ID, value):
    value = float(value)
    data = a.updateHWvalue(ID, value)
    return data

@app.get("/selecthw_byid")
def selecthw_byid(ID):
    data = a.selectHW_byid(ID)
    return data

@app.get("/insert_hw")
def insert_hw(name, hw_name):
    data = a.insertHW(name, hw_name)
    return data
    
@app.get("/deletehw_byid")
def deleteHW_byid(ID):
    data = a.deleteHW(ID)
    return data
    
if __name__ == "__main__":
    uvicorn.run(app, host='192.168.148.88', port=80)