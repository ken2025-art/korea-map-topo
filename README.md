# korea-map-topo

대한민국 시도(광역단위) 행정구역 경계 TopoJSON. Power BI Deneb / Shape Map / 웹 지도 시각화용으로 가공한 버전.

## 파일

| 파일 | 설명 | 크기 |
|---|---|---|
| `provinces-2018-topo.simple.json` | ★ 사용 파일. 경계 단순화(경량화) + 라벨 정리본 | ~92KB |
| `provinces-2018-topo.original.json` | 원본 (southkorea-maps 그대로) | ~880KB |

## properties 구조

각 시도 geometry의 `properties`:

| 키 | 예시 | 용도 |
|---|---|---|
| `name_short` | 서울, 경기, 충북, 세종 | 지도 라벨용 (짧은 한글) |
| `name_eng` | Seoul, Gyeonggi-do, Sejong | 데이터 매칭 키 (영문 표준) |
| `name` | 서울특별시, 경기도 | 한글 풀네임 |
| `code` | 11, 31, 29 | 행정코드 (정렬/식별) |

TopoJSON object 키: `skorea_provinces_2018_geo` · 시도 17개

## 원본 대비 가공 내용

- 경계 단순화 8% (mapshaper) → 880KB에서 92KB로 경량화, 시도 형태는 유지
- `name_short` 라벨 키 추가 (서울/부산/경기/강원/충북…)
- `name_eng` 세종 표기 수정: `Sejongsi` → `Sejong` (표준 표기)
- `base_year` 속성 제거 (전 지역 "2018" 동일 → 불필요)

## 출처 및 라이선스

```
지도 데이터: 통계청(KOSTAT) 행정구역 경계, 2018년 기준
원본 가공/배포: southkorea-maps (https://github.com/southkorea/southkorea-maps)
2차 가공: OnionBI (Deneb용 경량화/라벨 정리)
라이선스: KOSTAT 데이터 — 자유 이용(remix 가능)
```

KOSTAT 출처 데이터는 자유 이용(share/remix) 가능합니다. 이 저장소의 가공본도 자유롭게 사용/재배포할 수 있습니다. 사용 시 위 출처 표시를 권장합니다.
