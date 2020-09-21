from django.urls import path, re_path
from quotes.api.views import *

app_name = 'quotes'

urlpatterns = [
    path('quotes', QuoteListCreateAPIView.as_view(), name='list_create_quotes'),
    path('quotes/<int:pk>', QuoteRetrieveUpdateDestroyAPIView.as_view(), name='retrieve_update_destroy_quotes'),
]