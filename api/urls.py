from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from api.views import CreateUserView, NoteListCreate, NoteUpdateDelete


urlpatterns = [
    path('user/register/', CreateUserView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_view'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('notes/', NoteListCreate.as_view(), name='notes'),
    path('notes/<int:pk>',NoteUpdateDelete.as_view(), name='note_delete'),
    
]
