from django.conf.urls import url,include
from . import views
app_name = "getrw_vatgia"
urlpatterns=[
    url('^$',views.getrw_vatgia,name="getrw_vatgia"),
    url('^xem-review-vat-gia',views.mainaction,name="createobj")
]