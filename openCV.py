import cv2
import numpy as np
import base64
from typing import List


def getImageFromURL(data_url: str):
    # Decode the base64 data
    img_data = base64.b64decode(data_url)

    # Convert to a numpy array
    nparr = np.frombuffer(img_data, np.uint8)

    # Read using OpenCV
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return image

def getEdgeCoordinates(image, set: List[float]):
    height, width, _ = image.shape
    # 打印宽度和高度
    print(f'图像宽度：{width} 像素')
    print(f'图像高度：{height} 像素')

    baseX = set[0]
    baseY = set[3]
    hUnit = (set[3] - set[1]) / height
    wUnit = (set[2] - set[0]) / width

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, threshold1=5, threshold2=20)

    # 找到多邊形輪廓
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # 定义一个函数来判断轮廓的方向（顺时针或逆时针）
    def is_clockwise(contour):
        area = cv2.contourArea(contour)
        return area < 0


    # 根据轮廓的方向进行排序（顺时针）
    contours_clockwise = sorted(contours, key=is_clockwise)

    # 根据轮廓的方向进行排序（逆时针）
    contours_counterclockwise = sorted(contours, key=is_clockwise, reverse=True)

    # 初始化一個空的列表來存儲多邊形角點座標
    all_polygon_corners = []

    for contour in contours_clockwise:
        # 將多邊形輪廓近似為多邊形，獲得所有頂點的坐標
        epsilon = 0.003 * cv2.arcLength(contour, True)
        polygon_corners = cv2.approxPolyDP(contour, epsilon, True)

        # 將多邊形的頂點座標添加到列表
        all_polygon_corners.extend(polygon_corners)

    # 打印所有多邊形的角點座標
    coordinates: List[str] = []
    for i, corners in enumerate(all_polygon_corners):
        for corner in corners:
            x, y = corner
            coordinate = f"{baseX + x * wUnit},{baseY - y * hUnit},17"
            coordinates.append(coordinate)
            print(coordinate)

    return coordinates

    # 顯示結果圖像
    # cv2.imshow('Polygon Image', edges)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


def runTrans(set: List[float], data_url: str):
    # testing data
    # data_url = "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"
    # set = [121.50235444307327, 25.229791851375555, 121.50296330451965, 25.230335350574638]
    image = getImageFromURL(data_url)
    return getEdgeCoordinates(image, set)
