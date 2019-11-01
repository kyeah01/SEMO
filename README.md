<h1 align="center">SEMO</h1><p align="center">
    API Wiki Docs Page
</p>


<h1>Table of Contents</h1>

[TOC]

# Getting Started

## Prerequisites

- `front` 폴더에서 npm을 install 합니다.

  ```bash
  $ npm install
  ```

- `backend` 폴더에서 pip를 setup합니다.

  ```bash
  $ pip install -r requirements.txt
  ```



## Backend setup

- model 작업을 위한 migrate가 필요합니다.
  `backend` > `manage.py` 파일을 실행시킵니다.

  ```bash
  $ python manage.py migrate
  ```



## Data setup

- `backend` > `db.json` 파일을 load시킵니다.

    ```bash
    $ ./manage.py loaddata db.json
    ```
    
    (5분여정도 걸립니다.)



# Deployment

- `backend`서버를 구동시킵니다. `backend`폴더 수준에서 명령어를 입력합니다.

  ```bash
  $ python manage.py runserver
  ```

- `frontend` 서버를 구동시킵니다. `frontend` 폴더 수준에서 명령어를 입력합니다.

  ```bash
  $ npm run serve
  ```

  
