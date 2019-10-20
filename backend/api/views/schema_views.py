from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# 외부인과 내부인의 차이를 나누기 위한 설정이 필요할 듯.
# https://medium.com/towncompany-engineering/%EC%B9%9C%EC%A0%88%ED%95%98%EA%B2%8C-django-rest-framework-api-%EB%AC%B8%EC%84%9C-%EC%9E%90%EB%8F%99%ED%99%94%ED%95%98%EA%B8%B0-drf-yasg-c835269714fc
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)