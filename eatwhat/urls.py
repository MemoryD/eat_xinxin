from django.conf.urls import url

from . import views


app_name = 'eatwhat'
urlpatterns = [
    url(r'^$',views.eatwhat, name='eatwhat'),
    url(r'^select_food$', views.select_food, name= 'select_food'),
    url(r'^add_food$', views.add_food, name='add_food'),
    # url(r'^$', views.index, name='index')
]