from django.urls import include, path
from rest_framework import routers
from projects import views

router = routers.DefaultRouter()
router.register(r'waiters', views.WaiterViewSet)

waiter_create = views.WaiterViewSet.as_view({
    'post': 'create',
})


urlpatterns = [
    path('', waiter_create, name='waiter-create'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('viewset/', include(router.urls)),

    # path below is not an API view it is an experimental template view
    path('project/<str:title>/', views.ProjectStatusView.as_view(), name='project-status'),
]
