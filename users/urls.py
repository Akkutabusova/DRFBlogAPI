from django.urls import path
from .views import CustomUserCreate, BlacklistTokenUpdateView, UserData

app_name = 'users'

urlpatterns = [
    path('detail/', UserData.as_view(), name="credentials"),
    path('create/', CustomUserCreate.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist')
]