from django.urls import path
from . import views

urlpatterns = [
    path('signature/', views.SignatureView.as_view(), name='signature'),
    path('merit-sheet/', views.MeritSheetView.as_view(), name='merit-sheet'),
    path('google-login/', views.GoogleLoginView.as_view(), name='google-login'),
]
