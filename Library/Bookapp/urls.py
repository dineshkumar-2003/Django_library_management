from django.urls import path
from .views import *

urlpatterns=[
    path('createbook',CreateBookView.as_view(),name='create_book'),
    path('getbook/<str:title_>',CreateBookView.as_view(),name='get_book'),
    path('requestbook/<int:id>',RequestBookView.as_view(),name='request_book'),
]