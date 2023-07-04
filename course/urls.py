from django.urls import path

from .views import course_detail, course_list, course_students, course_posts, post

app_name = 'courses'
urlpatterns = [
    path('', course_list, name='course_list'),
    path('<int:course_id>/', course_detail, name='course_detail'),
    path('<int:course_id>/students/', course_students, name='course_students'),
    path('<int:course_id>/posts/', course_posts, name='course_posts'),
    path('<int:course_id>/posts/<int:post_id>/', post, name='post'),
]
