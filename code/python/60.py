import folium
import pandas as pd
from geojson import Feature


'''
# -------------기본
# 지도열기
my_map = folium.Map(location=[37.558850, 126.972414], zoom_start=12)
my_map.save("my_map.html")

# 지도 스타일 추가
my_map = folium.Map(
    location=[37.558850, 126.972414], zoom_start=12, tiles="CartoDB Positron"
)
my_map.save("my_map.html")

# 지도에 마커 추가
my_map = folium.Map(
    location=[37.558850, 126.972414], zoom_start=12, tiles="CartoDB Positron"
)
folium.Marker([37.565517, 127.010008], popup="동대문ddp플라자").add_to(
    my_map
)  # 기본마커
folium.Marker(
    [37.536665, 126.977564],
    popup="전쟁기념관",
    icon=folium.Icon(color="red", icon="arrow-right"),
).add_to(my_map)
my_map.save("my_map.html")

# 지도에 여러개 마커 딕셔너리 형태로 추가
my_map = folium.Map(
    location=[37.558850, 126.972414], zoom_start=12, tiles="CartoDB Positron"
)
map_info = [
    {"location": [37.530097, 126.964046], "popup": "용산역"},
    {"location": [37.580004, 126.977339], "popup": "경복궁"},
    {"location": [37.538649, 126.950392], "popup": "강의실"},
]

for info in map_info:
    folium.Marker(
        location=info["location"],
        popup=info["popup"],
        icon=folium.Icon(color="green", icon="star"),
    ).add_to(my_map)

my_map.save("my_map.html")


# 지도에 영역 표시
my_map = folium.Map(
    location=[37.558850, 126.972414], zoom_start=12, tiles="CartoDB Positron"
)
# 원형영역
folium.Circle(
    location=[37.580004, 126.977339],
    radius=1000,  # 반지름(미터단위)
    color="blue",
    popup="경복궁 일대",
    fill=True,
    fill_color="yellow",
).add_to(my_map)
my_map.save("my_map.html")


import folium

# 서울의 지하철역 정보
map_info = [
    {"location": [37.556201, 126.972322], "station": "서울역"},
    {"location": [37.564718, 126.977041], "station": "시청역"},
    {"location": [37.571607, 126.991806], "station": "종로3가역"},
    {"location": [37.566014, 126.982702], "station": "을지로입구역"},
    {"location": [37.497942, 127.027621], "station": "강남역"},
]

# 지도 생성
seoul_map = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

# 마커 추가
for info in map_info:
    folium.Marker(
        location=info["location"],
        popup=info["station"],
        icon=folium.Icon(color="blue", icon="star"),
    ).add_to(seoul_map)

# 지도 저장 및 시각화
seoul_map.save("seoul_subway_map.html")


#-----------------------------------
# geojson
# 데이터 생성
feature1 = Feature(geometry = Point((126.980359, 37.559346)), properties={"name": "서울", "population":"970만"})
feature2 = Feature(geometry = Point((129.047026, 35.152378)), properties={"name": "부산", "population":"340만"})
feature3 = Feature(geometry = Point((127.393692, 36.343458)), properties={"name": "대전", "population":"150만"})
feature1 = Feature(geometry = Point((128.669634, 35.835178)), properties={"name": "대구", "population":"240만"})

# 데이터 하나로 묶기
geojson_data = FeatureCollection(feature1, feature2, feature3, feature4)


import folium

# 1. 지도 생성
seoul_map = folium.Map(location=[37.5665, 126.9780], zoom_start=9)

# 2. GeoJSON 데이터 준비
geojson_data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {"name": "수도권"},
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [126.764, 37.413],  # 인천 남서부
                        [127.183, 37.413],  # 경기 동부
                        [127.183, 37.849],  # 경기 북부
                        [126.764, 37.849],  # 경기 북서부
                        [126.764, 37.413],  # 시작점으로 닫기
                    ]
                ],
            },
        }
    ],
}

# 3. GeoJSON 데이터를 지도에 추가
folium.GeoJson(
    geojson_data,
    name="geojson",
    tooltip=folium.GeoJsonTooltip(fields=["name"], aliases=["영역 이름: "]),
).add_to(seoul_map)

# 4. 지도 저장
seoul_map.save("geojson_seoul_map.html")
seoul_map
'''

# 실무 실습
my_map = folium.Map(location = [37.554830, 126.986322], zoom_start=7, tiles = "CartoDB positron")

geojson_data = "HangJeongDong_ver20241001.geojson"

folium.GeoJson(
    geojson_data,
    name = "대한민국경계",
    style_function = lambda _: {
        "fillColor": "blue",
        "color" : "black",
        "weight" : 1,
        "fillOpacity" : 0.1,
    },
).add_to(my_map)
my_map.save("my_map.html")