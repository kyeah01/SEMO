# Django Access Logging

> 2019.10.18
>
> Django Logging
>
> 프로그램	버전
>Django		2.2.4

### Django Logging 
-----
1. 로깅 설정

[Django log Docs](https://docs.djangoproject.com/en/2.2/topics/logging/)

`settings.py`파일

```python
LOGGING = {
    'version': 1,
    # Django 기본 로거 비활성화
    'disable_existing_loggers': False,
    # 출력 형식을 변경할 수 있음
    'formatters': {
        'logFormat': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
    },
    # console, file 등 어떤 logging을 핸들링할 것인지 셋팅
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'logFormat',
        },
    },
    # django 프로젝트가 사용할 수 있도록 지정
    'loggers': {
        # project 최상위 djanog setting
        'django': {
            # 리스트에 여러가지를 추가해서 동시에 사용 가능
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
    }
}
```

```bash
# default django logger
[18/Oct/2019 17:56:59] "GET / HTTP/1.1" 404 2158
# custom logger
[2019-10-18 17:57:39] WARNING [django.server:154] "GET / HTTP/1.1" 404 2431
```
`defaultLog`
![defaultLog](https://user-images.githubusercontent.com/45934129/67552878-e5ff5c80-f746-11e9-819a-b29b851cd237.JPG)
`changeLog`
![changeLog](https://user-images.githubusercontent.com/45934129/67552883-e861b680-f746-11e9-8cf2-a5173cb0afbc.JPG)

