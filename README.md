

<p align="center">
    <img src="https://user-images.githubusercontent.com/45934087/68111330-38ecc700-ff32-11e9-817e-57b39a66a24a.png"/>
	<h1 align="center">SEMO</h1>
    <p align="center">API Wiki Docs Page</p>
</p>

[TOC]

# Project Description

GitHub: <a href="https://github.com/kyeah01/SEMO">SEMO</a>

 **Simple & East Manual of API**(이하, SEMO)는 신임 개발자 및 개발자를 꿈꾸는 사람들을 위한 API Wiki Docs Service입니다. 유용한 API Site 의 사용법 및 API Test Service를 제공하여 개발자들의 학업 효율 및 생산성 향상을 위한 서비스를 구현하였습니다. 또한, API Key를 저장, 관리 할 수 있는 서비스를 제공함으로써 API 접근성과 생산성을 향상시키고자 하였습니다.

------



# Getting Started

## Prerequisites

- `front` 폴더에서 npm 모듈을 install 합니다.

  ```bash
  $ npm install
  ```

- `backend` 폴더에서 pip 모듈을 setup합니다.

  ```bash
  $ pip install -r requirements.txt
  ```



## Database setup

- deploy DB로는 `MySQL`을 활용했으나, test를 위한 DB로 `sqlite3`를 지원합니다.

- model 작업을 위한 migrate가 필요합니다.
  `backend` > `manage.py` 파일을 실행시킵니다.

  ```bash
  $ python manage.py migrate
  ```

- `backend` > `db.json` 파일을 load시킵니다.

  ```bash
  $ ./manage.py loaddata db.json
  ```

  

# Description

## 핵심기술

### 다양한 유형의 API Site 정보 제공

#### Main Page

![image](https://user-images.githubusercontent.com/45934087/68111269-13f85400-ff32-11e9-832b-4af68a2dd19a.png)

 국내  공공데이터에서부터 해외 유명 사이트까지 다양한 주제의 API 사이트를 주요 기능 및 Category별로 정렬하여 보다 간편하게 API에 접근 할 수 있도록 합니다. 



#### Detail Page

![image](https://user-images.githubusercontent.com/45934087/68112833-a51cfa00-ff35-11e9-9caa-d8a26bab4e79.png)

 **Detail Page**에서는 해당 사이트에 대한 간략한 소개와 함께 주요 기능 및 데이터 형식, 비용 유무, 로그인 필요여부, Docs Link 등을 제공 함으로써 해당 사이트 방문 없이 사용에 필요한 기본적인 정보를 파악 할 수 있습니다.

![image](https://user-images.githubusercontent.com/45934087/68112851-b108bc00-ff35-11e9-9960-3f7e0312f1d8.png)

 또한, **회원가입** 및 **Key 발급 방법**에 대한 소개를 통해 처음 이용하는 사이트에서 야기 될 수 있는 불편함을 줄이고자 하였으며, 이를 통해 해외 사이트에 대한 접근성 향상을 도모하였습니다.

![image](https://user-images.githubusercontent.com/45934087/68112807-90d8fd00-ff35-11e9-976d-b96dcc4224a6.png)

 **개발 가이드**에서는 해당 사이트에서 지원하는 언어 이외에도 각 언어별 사용 방법 을 제공합니다.

![image](https://user-images.githubusercontent.com/45934087/68112873-bebe4180-ff35-11e9-8d66-aefc81b6b5a9.png)

 **API Test Console**은 별도의 코드 입력 없이 **개발 가이드**란에서 선택한 EndPoint가 필요로 하는 **Parameters**만 입력함으로써 간단하게 API 요청을 실행해 볼 수 있습니다. 이를 통해 내가 얻고자 하는 정보가 어떠한 유형으로 response 되는지 간단히 알 수 있습니다.

![image](https://user-images.githubusercontent.com/45934087/68112889-ca116d00-ff35-11e9-9ea2-ad4761b5dbc4.png)

​						※ API Console Test를 통해 Movie Details에서 제공해주는 Schema의 목록

![image](https://user-images.githubusercontent.com/45934087/68112909-dac1e300-ff35-11e9-865f-55ccfac9a8a5.png)

​						※ API Console Test를 통해 Movie Details에서 Response 받을 수 있는 데이터

### 사용자 참여형 Wiki Docs

------

![image](https://user-images.githubusercontent.com/45934087/68113729-c67ee580-ff37-11e9-8d77-31bdbeacaf50.png)

 **SEMO**의 사용자는 자신이 주로 사용하는 **API 사이트**를 직접 SEMO에 등록 할 수 있으며, 이를 통해 사용자에게는 더욱 많은 편의를 SEMO에는 더욱 많은 데이터를 쌓을 수 있게 합니다.

### Log 분석을 통한 페이지 관리

------

![image](https://user-images.githubusercontent.com/45934087/68115244-46f31580-ff3b-11e9-9edc-dc6eba354639.png)

​						※ 관리자 페이지의 메인 화면, 각 항목별 주간 요청 갯수와 데이터를 확인 할 수 있다.

![image](https://user-images.githubusercontent.com/45934087/68115262-570af500-ff3b-11e9-920e-a91d58a77138.png)

​						※ 사용자가 등록 혹은 수정 요청한 게시물을 관리 할 수 있다.

### 프로필 페이지를 통한 나만의 API 관리

------

![image](https://user-images.githubusercontent.com/45934087/68113575-79027880-ff37-11e9-8cf4-e302e91f5545.png)

 최근 조회 API 리스트를 모아 둠으로써, 기존에 사용하였던 API 사이트에 더욱 빠르게 접근 할 수 있다.

![image](https://user-images.githubusercontent.com/45934087/68113514-4e182480-ff37-11e9-8a84-2d7bf6f91a40.png)

 각 사이트별 API Key를 저장, 관리 할 수 있으며 만료일이 존재하는 경우 만료일도 함께 관리 할 수 있게 함으로써 Key 관리에 편의성을 더하였으며, Detail Page의 ApI Test Console에 별도의 Key 입력 없이 바로 테스트 해 볼 수 있도록 구현하였다.

------



## Model structure

<img src="https://user-images.githubusercontent.com/45934061/68186307-2d0f0c80-ffe7-11e9-9754-5457ed8d6a43.png">





#### 사용 기술 및 도구

- Django (2.2.4)
- Django REST Framework (3.10.2)
- yasg (1.17.0)
- python (3.6.8)
- MySql (8.0.18)
- django-rest-knox (4.1.0)
- Vuex (3.1.1)
- Vue.js (2.6.10)
- SCSS (sass-loder : 8.0.0, node-sass: 4.12.0)
- vue CLI (3.12.0)
- virtualenv (16.7.7)



#### SEMO Project`s Developer

------

![image](https://user-images.githubusercontent.com/45934087/67922599-8bef1300-fbee-11e9-8fd9-c1712f3f2069.png) 