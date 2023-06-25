from django.urls import path
from books import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('books/',views.BookList.as_view()),
    path('books/<int:pk>/',views.BookEdit.as_view()),
    path('books/post/',views.BookPost.as_view()),
    path('pages/',views.PageList.as_view()),
    path('pages/<int:pk>/',views.PageEdit.as_view()),
    path('pages/post/',views.BookPost.as_view()),
    path('register/',views.register),
]
