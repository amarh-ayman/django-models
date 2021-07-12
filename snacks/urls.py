from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(),name='index'),
    path('snacks/', SnackListView.as_view(),name='snacks_list'),
    path('snacks/<int:pk>', SnackDetailView.as_view(),name='snack_details'),

]