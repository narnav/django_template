from django.urls import path
from .views import tasks 
from . import views 

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)



urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',views.register ),
    path('tasks/',tasks ),
    path('tasks/<int:id>',tasks),
    path('test/',views.test ),
    path('getImages', views.getImages),
    path('posts/',views.APIViews.as_view()),
    # upload images
]
# data - OK
# authentication - OK
# upload files (image)