# -*- coding: utf-8 -*-
"""
한국 시도 TopoJSON properties 가공 스크립트
- name_short(한글 짧은 라벨) 추가: 서울/부산/경기/강원/충북 ...
- name_eng 세종 표기 수정: Sejongsi -> Sejong
- base_year 제거
- name(한글 풀네임), code 유지
출처 데이터: 통계청(KOSTAT) 2018, 가공: southkorea-maps
"""
import json
import sys
import io

# Windows 콘솔 한글 출력
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

SRC = "provinces-2018-topo.original.json"
DST = "provinces-2018-props.json"  # 경량화 전, properties만 가공한 중간본

# 한글 풀네임 -> 짧은 라벨 매핑
SHORT = {
    "서울특별시": "서울",
    "부산광역시": "부산",
    "대구광역시": "대구",
    "인천광역시": "인천",
    "광주광역시": "광주",
    "대전광역시": "대전",
    "울산광역시": "울산",
    "세종특별자치시": "세종",
    "경기도": "경기",
    "강원도": "강원",
    "충청북도": "충북",
    "충청남도": "충남",
    "전라북도": "전북",
    "전라남도": "전남",
    "경상북도": "경북",
    "경상남도": "경남",
    "제주특별자치도": "제주",
}

# 영문 표기 보정 (표준 표기로)
ENG_FIX = {
    "Sejongsi": "Sejong",
}

with open(SRC, "r", encoding="utf-8") as f:
    topo = json.load(f)

# objects 안의 첫 번째 geometry collection 찾기
obj_key = list(topo["objects"].keys())[0]
geoms = topo["objects"][obj_key]["geometries"]

missing = []
for g in geoms:
    props = g.get("properties", {})
    name = props.get("name", "")

    # 1) name_short 추가
    if name in SHORT:
        props["name_short"] = SHORT[name]
    else:
        missing.append(name)

    # 2) name_eng 보정
    eng = props.get("name_eng", "")
    if eng in ENG_FIX:
        props["name_eng"] = ENG_FIX[eng]

    # 3) base_year 제거
    props.pop("base_year", None)

    g["properties"] = props

with open(DST, "w", encoding="utf-8") as f:
    json.dump(topo, f, ensure_ascii=False, separators=(",", ":"))

print("object key:", obj_key)
print("geometry count:", len(geoms))
print("매핑 안 된 name (있으면 확인 필요):", missing if missing else "없음")
print("\n=== 가공 후 properties 샘플 ===")
for g in geoms:
    p = g["properties"]
    print(f"  {p.get('code'):>3}  {p.get('name_short'):<4}  {p.get('name'):<10}  {p.get('name_eng')}")
print(f"\n저장: {DST}")
