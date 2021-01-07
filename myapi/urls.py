from django.urls import path, include

from rest_framework import routers
from . import views
from django.conf.urls import url
#router = routers.DefaultRouter()
#router.register(r'heroes1', views.HeroViewSet)

urlpatterns = [
    #path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest-framework')),
    url(r'^heroo/$', views.HeroViewSet.as_view(),  name="accounts"),

]