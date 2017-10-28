from django.conf.urls import url
from  . import views

app_name = "getrw_tiki"

urlpatterns=[
    url(r'^getrw-tiki/$',views.mainaction,name="createobj"),
    url(r'^$',views.getrw_tiki,name="getrw_tiki")
]