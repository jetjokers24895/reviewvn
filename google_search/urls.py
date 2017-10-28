from django.conf.urls import url
from . import views
app_name = "google_search"
urlpatterns=[
    url(r'^$',views.view_google_search,name="view_google_search")
]