from . import views
from rest_framework import routers
from django.urls import path, include
# Rename views to avoid conflict with app views
from rest_framework.authtoken import views as rest_views

"""
When using viewsets instead of views, we can automatically generate the URL conf for our API, by simply registering the viewsets with a router class.

If we need more control over the API URLs we can simply drop down to using regular class-based views (APIViews), and writing the URL conf explicitly.
"""

router = routers.DefaultRouter()

# Rename views to avoid conflict with app views
from rest_framework.authtoken import views as rest_views

urlpatterns = [
    # URLs for class-based views (Generics, APIViews)
    # http://localhost:8000/todo/
    # http://localhost:8000/todo/<int:pk>
    path('todo/', views.MachineList.as_view(), name='todo_list'),
    path('todo/<int:pk>', views.MachineDetail.as_view(), name='todo_detail'),

    # URLs for class-based views (ModelViewSets)
    # http://localhost:8000/general/users/
    # http://localhost:8000/general/groups/
    path('general/', include(router.urls)),

    # Include default login and logout views for use with the browsable API.
    # Optional, but useful if your API requires authentication and you want to use the browsable API.
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # API to generate auth token from user. Note that the URL part of the pattern can be whatever you want to use.
    path('api-token-auth/', rest_views.obtain_auth_token, name='api-token-auth'),
    path('user', views.user, name='user')
    ]