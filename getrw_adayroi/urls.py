from django.conf.urls import url
from . import views
app_name='getrw_adayroi'
urlpatterns= [
    url(r'^$',views.getrw_adayroi,name = "getrw_adayroi"),
    url(r'^xem-review-a-day-roi/$',views.mainaction,name ='createobj')
]