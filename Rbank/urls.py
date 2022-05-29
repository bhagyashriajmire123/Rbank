"""Rbank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin

from django.urls import path, include, re_path
from first_rest.views import *
from first_rest.urls import router
from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views



schema_view = get_swagger_view(title='student op API')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('singel-data/<int:pk>/',get_single_data),
    path('all-data/',get_all_stud),
    # path('create-data/',create_data),

    # for single method
    # path('single-data/',single_method_for_all_data),

    # for class method
    # path("stud-class-api/", StudenApi.as_view()),

    # for API_views
    # path('student-api-view/',student_api_view),
    
    # for apivew calss
    # path('studentapinew/',StudentapiNew.as_view()),  # for get and post all student k liye
    # path('studentapinew/<int:pk>/',StudentapiNew.as_view()),   # for put patch , n delete (id k liye)

    path("s-list/", StudList.as_view()),
    path("s-retrive/<int:pk>/", StudRetrive.as_view()),
    path("s-create/", StudCreate.as_view()),
    path("s-update/<int:pk>/", StudUpdate.as_view()),
    path("s-destroy/<int:pk>/", StudDestroy.as_view()),

    # for comine mixing

    path("s-listcreate/", StudentListCreate.as_view()),
    path("s-retriveupdatedelte/<int:pk>/",StudentRetriveUpdateDestroy.as_view()),

    # concrite API_view
    path("s-list/", StudList.as_view()),
    path("s-create/", StudCreate.as_view()),
    path("s-retrive/<int:pk>/", StudRetrive.as_view()),
    path("s-update/<int:pk>/", StudUpdate.as_view()),
    path("s-destroy/<int:pk>/",StudDestroy.as_view()),
    
    # viewset 
    path("studvset/",include(router.urls)),
    re_path(r'^$',schema_view),
    path('api_token_auth/',obtain_auth_token, name='api_token_auth'),

    #jwt

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/',HelloView.as_view(), name='hello'),
    path('studentfilter/', StudentListF.as_view()),

    
]
