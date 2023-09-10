from fastapi import FastAPI, Response
from typing import List
from pydantic import BaseModel
import openCV
import KML


class PlaceMark(BaseModel):
    EXT: List[float]
    IMG: str


class Request(BaseModel):
    name: str
    placeMarks: List[PlaceMark]


app = FastAPI()


@app.get("/")
async def root(request: Request):
    placeMarksKMLs = []
    for index, placeMark in enumerate(request.placeMarks):
        coordinates = openCV.runTrans(placeMark.EXT, placeMark.IMG)
        placeMarksKMLs.append(KML.generatePlaceMark(f"{request.name}_{index}", coordinates))

    kml = KML.generateKML(placeMarksKMLs)
    return Response(content=kml, status_code=200, media_type="application/xml")
