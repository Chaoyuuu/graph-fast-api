
# Install environment
```
pip3 install numpy
pip3 install opencv-python
pip3 install fastapi
pip3 install 'uvicorn[standard]'
```
# How to run
```
uvicorn main:app --reload
```

# API Spec
- Request
  - GET / http://localhost:8000
  - Body
```
{
    "name": "UNA",
    "placeMarks": [
        {
            "EXT": [
                121.50235444307327,
                25.229791851375555,
                121.50296330451965,
                25.230335350574638
            ],
            "IMG": "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"
        },
                {
            "EXT": [
                121.50235444307327,
                25.229791851375555,
                121.50296330451965,
                25.230335350574638
            ],
            "IMG": "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"
        }
    ]
}
```

- Response
```xml
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
    <Document>
        <Style id="transRedPoly">
            <LineStyle>
                <width>1.5</width>
            </LineStyle>
            <PolyStyle>
                <color>7d0000ff</color>
            </PolyStyle>
        </Style>
        <Folder>
            <name>Graph sets</name>
            <visibility>0</visibility>
            <Placemark>
                <name>UNA_0</name>
                <visibility>0</visibility>
                <styleUrl>#transRedPoly</styleUrl>
                <Polygon>
                    <extrude>1</extrude>
                    <altitudeMode>relativeToGround</altitudeMode>
                    <outerBoundaryIs>
                        <LinearRing>
                            <coordinates>
                            121.5023598074913,25.230308660881825,17
121.50235444307327,25.230277118517595,17
121.50259852409363,25.230049042960836,17
121.50275141000748,25.229794277711267,17
121.50259584188461,25.230053895632256,17
121.50235444307327,25.230279544853303,17
121.50236248970032,25.230311087217537,17
121.50255292654037,25.230335350574638,17
121.50268167257309,25.230192196767735,17
121.50296062231064,25.229799130382688,17
121.50267899036407,25.230197049439155,17
121.50255560874939,25.230335350574638,17
                        </coordinates>
                        </LinearRing>
                    </outerBoundaryIs>
                </Polygon>
            </Placemark>
            <Placemark>
                <name>UNA_1</name>
                <visibility>0</visibility>
                <styleUrl>#transRedPoly</styleUrl>
                <Polygon>
                    <extrude>1</extrude>
                    <altitudeMode>relativeToGround</altitudeMode>
                    <outerBoundaryIs>
                        <LinearRing>
                            <coordinates>
                            121.5023598074913,25.230308660881825,17
121.50235444307327,25.230277118517595,17
121.50259852409363,25.230049042960836,17
121.50275141000748,25.229794277711267,17
121.50259584188461,25.230053895632256,17
121.50235444307327,25.230279544853303,17
121.50236248970032,25.230311087217537,17
121.50255292654037,25.230335350574638,17
121.50268167257309,25.230192196767735,17
121.50296062231064,25.229799130382688,17
121.50267899036407,25.230197049439155,17
121.50255560874939,25.230335350574638,17
                        </coordinates>
                        </LinearRing>
                    </outerBoundaryIs>
                </Polygon>
            </Placemark>
        </Folder>
    </Document>
</kml>
```