from django.contrib import admin
from django.shortcuts import redirect, render
from django.urls import path, include


def land_page(request):
    if request.user.is_authenticated:
        return redirect('courses:course_list')
    return render(request, 'land_page.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('course.urls', namespace='courses')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('', land_page, name='land_page')
]
