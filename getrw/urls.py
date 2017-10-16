from django.conf.urls import url
from . import views
app_name="getrw"
urlpatterns=[
    url(r'^getrw-lazada',views.mainaction,name="createobj"),
    url(r'^$',views.getrw,name = "getreview"),
]