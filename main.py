from fastapi import FastAPI, Response, Form
from fastapi.responses import StreamingResponse
from typing import List
from pydantic import BaseModel
import json
import openCV
import KML


class PlaceMark(BaseModel):
    EXT: List[float]
    IMG: str


class Request(BaseModel):
    name: str
    placeMarks: List[PlaceMark]


app = FastAPI()

@app.post("/download-kml")
async def get_object(name: str = Form(...), placeMarks: str = Form(...)):
    json_data = json.loads(placeMarks)
    placeMarksKMLs = []
    for index, placeMark in enumerate(json_data):
        coordinates = openCV.runTrans(placeMark["EXT"], placeMark["IMG"])
        placeMarksKMLs.append(KML.generatePlaceMark(f"{name}_{index}", coordinates))

    kml = KML.generateKML(placeMarksKMLs)
    data_bytes = kml.encode("utf-8")
    return StreamingResponse(iter([data_bytes]), media_type="application/xml",
                             headers={"Content-Disposition": f"attachment; filename={name}.kml"})
    # return Response(content=kml, status_code=200, media_type="application/xml")
