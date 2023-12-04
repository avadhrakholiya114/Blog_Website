from django.urls import path, include
from . import views
urlpatterns = [

    # slug means vlog pachi dynamic url
    path('', views.index),

    path('blog/<slug:id>', views.post),

]
