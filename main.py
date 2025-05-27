import streamlit as st
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
import pandas as pd

# 고등학교 데이터 (동덕여고 포함)
data = {
    "학교명": [
        "서울고등학교",
        "세화고등학교",
        "상문고등학교",
        "반포고등학교",
        "동덕여자고등학교"  # 추가된 학교
    ],
    "주소": [
        "서울 서초구 반포대로 28",
        "서울 서초구 반포대로 222",
        "서울 서초구 서초중앙로 42",
        "서울 서초구 신반포로 200",
        "서울 서초구 반포대로 304"  # 동덕여고 주소
    ],
    "위도": [
        37.4981,
        37.4956,
        37.4842,
        37.5033,
        37.5053  # 동덕여고 위도
    ],
    "경도": [
        127.0112,
        127.0059,
        127.0141,
        127.0001,
        126.9972  # 동덕여고 경도
    ]
}

df = pd.DataFrame(data)

st.title("🏫 서울 서초구 고등학교 지도")
st.markdown("**동덕여자고등학교 포함** 모든 서초구 고등학교 위치를 확인할 수 있습니다.")

# Folium 지도 초기화
m = folium.Map(location=[37.495, 127.005], zoom_start=13)
marker_cluster = MarkerCluster().add_to(m)

# 지도에 마커 추가
for _, row in df.iterrows():
    folium.Marker(
        location=[row["위도"], row["경도"]],
        popup=f"<b>{row['학교명']}</b><br>{row['주소']}",
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(marker_cluster)

# Streamlit에 지도 표시
st_data = st_folium(m, width=700, height=500)
