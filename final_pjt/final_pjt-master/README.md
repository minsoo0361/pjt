💡 프로젝트 개요
- 프로젝트 진행 기간 : 2024.05.16(목) ~ 2024.05.24(금)
- 주제 : 금융 상품 조회 및 개인별 맞춤 상품 추천, 부가 서비스(환율 계산, 주변 은행 검색 등) 제공을 통한 통합 금융 서비스 제공
- 서비스명 : Y&S Financial Service

💡 Y&S Financial Service 개요
- 나에게 딱 맞는 맞춤 예적금 상품이 궁금하다면? 어렵게 느껴지는 금융, 이젠 쉽게 조회하고 다양한 금융 정보를 얻어보세요! 
Y&S Financial Service는 접근성 좋은 금융 서비스를 제공하여 효과적으로 자산을 관리하고 싶은 사용자들을 위해 다양한 금융 서비스를 제공합니다!

💡 주요 기능
- 메인 페이지: 다양한 기능들에 접근하기 위한 메뉴바
    사이트 대표 이미지 애니메이션
    예/적금 상품 조회 페이지 & 개인별 맞춤 금융상품 추천 페이지 & 커뮤니티 페이지로의 링크 제공

- 예/적금 데이터 불러오기
- 예/적금 데이터 조회 및 상세 페이지 조회 기능
- 회원 가입 / 로그인 / 로그아웃 기능
- 게시글 생성, 조회, 수정, 삭제 기능
- 댓글 생성, 조회, 삭제 기능
- 프로필(마이페이지)에서의 개인 정보 조회 기능 및 좋아요 한 예/적금 상품 조회 기능
- 주변 은행 검색 기능
- 환율 계산 및 국가별 환율 조회 기능
- 금융 상품 추천 기능
- AI 챗봇 (검색 / 세대 별 금융 상품 추천) 기능

💡 부가 기능
- 다크모드 토글 기능
- 메인 페이지 영어 번역 기능


💡 프로젝트 진행 일정


## 2024-05-16(목)

- 홈페이지 로고 디자인
- 메인 페이지 및 홈페이지 디자인 설계 (UI)
- 홈페이지 로고 디자인
- 홈페이지 와이어프레임 디자인

[design.com](http://design.com)을 활용하여 프로젝트 홈페이지의 대표 로고를 만들었다.

[figma.com](http://figma.com)을 활용하여 홈페이지 UI의 전반적인 구성을 트리 형식으로 한 눈에 이해하기 쉽게 가시화하였다. (와이어프레임 구성)

[databasediagram.com](http://databasediagram.com)을 활용하여 프로젝트 ERD를 구성하였다.

([https://finlife.fss.or.kr/finlife/api](https://finlife.fss.or.kr/finlife/api/fdrmDpstApi/list.do?menuNo=700052) 사이트에서 정기예금/적금 api 참고)


## 2024-05-17(금)

- Home 페이지 navbar 구현
- 로그인/로그아웃/회원가입 기능 구현
- 금융 데이터 불러오기/금융 상품 조회 기능 구현
- 전체 게시글 목록 조회 & 상세 게시글 조회 및 게시글 추가 기능 구현
- 상세 게시글 페이지에서의 댓글 조회 및 댓글 추가 기능 구현


## 2024-05-18(토)

- 금융 상품 상세 페이지
- 댓글 삭제 기능
- 상세 게시글 삭제 기능


## 2024-05-19(일)

- Vuetify / Bootstrap 홈페이지 스타일링
- 금융 정보 상세 페이지에서 금융 상품 코드 대신 상품명이 출력되도록 수정
- 주변 은행 검색 기능 (카카오맵 api 활용)
- 환율 계산 기능


## 2024-05-20(월)

- 금융 상품 좋아요 기능
- 적금 데이터 로드 / 조회 기능
- 부트스트랩을 통한 홈페이지 디자인


## 2024-05-21(화)

- 금융 상품 좋아요 기능 오류 수정
- 게시글 / 댓글 수정 기능
- 홈페이지 css 스타일링
- 라이트모드 / 다크모드 토글 기능
- 금융 상품 추천 알고리즘


## 2024-05-22(수)

- 금융 상품 추천 알고리즘
- 메인 페이지 스타일링 (Bootstrap, Vuetify)


## 2024-05-23(목)

- 챗봇 기능
- 프로필 페이지 꾸미기
- 메인 페이지 영어 번역 버전 만들기
- 발표용 PPT 제작


👨 팀원 역할 및 소감

- 김민수 (팀장)

전체 게시글 목록 조회 
상세 게시글 조회 및 게시글 추가 기능
알고리즘 추천 상품 기능
프로필 기능
예 적금 상품 불러오기
로그인 / 로그아웃 / 회원가입 기능
금융 상품 좋아요 기능

소감 :
싸피를 들어오고나서 알고리즘을 거쳐 HTML, CSS, DJANGO를 배우며 이 길이 내 길이 맞을까 라는 생각도 수 없이 했었습니다. 그럴 때마다 스터디원들과 함께 역경과 고난을 헤쳐 나갈 수 있어 다른 생각 없이 온전히 교육에만 집중할 수 있었던 것 같습니다! FINAL-PJT에도 파트너에게 누가 되지 않기 위해서 열심히 했는데 제 마음이 와 닿았는지는 잘 모르겠습니다. 일주일 넘는 시간동안 너무 고생했고 구미 3반 여러분 모두 고생하셨습니다!!

- 권윤하 (팀원)

전체 홈페이지 스타일링
홈페이지 번역 기능
라이트 / 다크 모드 토글 기능
주변 은행 검색 기능
환율 계산 기능
AI 챗봇 기능

소감 : 
처음에는 구현해야 할 기능들이 너무 많아서 어떻게 구현해야 할지 막막했지만, 카리스마 넘치는 팀장님께서 잘 이끌어주셔서 하나 하나 완성해 나갈 수 있었습니다. 홈페이지를 구현하는 프로젝트는 처음이라 아쉬운 부분도 있지만 10일 남짓되는 시간동안 최선을 다했기 때문에 후회는 없는 것 같습니다! 2학기 프로젝트도 잘 할 수 있을 것 같다는 자신감이 생겼고 1학기 동안 좋은 사람들과 좋은 환경에서 공부할 수 있어서 너무 즐겁고 행복했습니다!