import json
from typing import Union

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from elevator_system.displays.display_json import DisplayJson
from elevator_system.elevator import Elevator
from elevator_system.motor import Motor

app = FastAPI()


@app.get("/")
def read_root():
    main_elevator = Elevator(Motor())
    return json.loads(DisplayJson(main_elevator).display())
