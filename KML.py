from typing import List

xml_header = """
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
"""

xml_tail = """
        </Folder>
    </Document>
</kml>
"""

def generateKML(placeMarks_kmls: List[str]):
    placeMarks = '\n'.join(placeMarks_kmls)
    return xml_header + placeMarks + xml_tail

def generatePlaceMark(name: str, coordinates: List[str]):
    coordinates_string = '\n'.join(coordinates)

    xml_template = f"""
        <Placemark>
            <name>{name}</name>
            <visibility>0</visibility>
            <styleUrl>#transRedPoly</styleUrl>
            <Polygon>
                <extrude>1</extrude>
                <altitudeMode>relativeToGround</altitudeMode>
                <outerBoundaryIs>
                    <LinearRing>
                        <coordinates>
                            {coordinates_string}
                        </coordinates>
                    </LinearRing>
                </outerBoundaryIs>
            </Polygon>
        </Placemark>
    """

    return xml_template
