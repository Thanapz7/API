from fastapi import FastAPI
from h11 import Data
import uvicorn

from action import Action
a = Action

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/my_name")
def my_name():
    data = "Thanaphon Phetcharat"
    return data

@app.get("/input_name")
def input_name(name):    
    data = name
    return data

@app.get("/input_name_2")
def input_name_2(name, last_name):
    data = "{} {}".format(name, last_name)
    return data

# @app.get("/speed")
# def speed(distance, time):
#     speed = float(distance) / float(time)
#     data = "V = {:.2f} m/s".format(speed)
#     return data

@app.get("/speed")
def speed(s, t):
    speed = float(s) / float(t)
    data = "V = {:.2f} m/s".format(speed)
    return data

@app.get("/rserie_parallel")
def rserie_parallel(r1, r2, r3):
    rstotal = ((1/float(r1)) + (1/float(r2)) + (1/float(r3)))**-1
    rptotal = float(r1)+float(r2)+float(r3)
    data = {"R(serie)" :  rstotal, "R(parallel)" : rptotal } #"อนุกรม  = {} ขนาน = {}".format(rstotal, rptotal)
    return data

@app.get("/gethw")
def get_HW():
    data = a.getHW()
    return data

@app.get("/update_status_hw")
def update_status_hw(ID, status):
    data = a.updateHW(ID, status)
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
    uvicorn.run(app, host='localhost', port=8000)