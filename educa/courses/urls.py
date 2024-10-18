from django.urls import path
from . import views

urlpatterns = [
    path('mine/', views.ManageCourseListView.as_view(), name='manage_course_list'),
    path('create/', views.CourseCreateView.as_view(), name='course_create'),
    path('<int:pk>/edit', views.CourseUpdateView.as_view(), name='course_update'),
    path('<int:pk>/delete', views.CourseDeleteMixin.as_view(), name='course_delete'),
]
