from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from accounts.forms import LoginForm
from .forms import UserCreateForm, StudentForm, TeacherForm


def student_signup(request):
    if request.user.is_authenticated:
        return redirect('land_page')
    user_form = UserCreateForm(request.POST or None)
    student_form = StudentForm(request.POST or None)

    if request.method == 'POST':
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save(commit=False)
            user.username = student_form.cleaned_data['student_id']
            user.save()
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            return redirect('accounts:login')

        # return redirect('accounts:student_signup')

    return render(request, 'accounts/student_signup.html', {'user_form': user_form, 'student_form': student_form})


def teacher_signup(request):
    if request.user.is_authenticated:
        return redirect('land_page')
    user_form = UserCreateForm(request.POST or None)
    teacher_form = TeacherForm(request.POST or None)

    if request.method == 'POST':
        if user_form.is_valid() and teacher_form.is_valid():
            user = user_form.save(commit=False)
            user.username = teacher_form.cleaned_data['teacher_id']
            user.save()
            teacher = teacher_form.save(commit=False)
            teacher.user = user
            teacher.save()
            return redirect('accounts:login')
        # return redirect('accounts:teacher_signup')

    return render(request, 'accounts/teacher_signup.html', {'user_form': user_form, 'teacher_form': teacher_form})


def authenticate_user(request):
    authentication_form = LoginForm(request.POST or None)
    if request.user.is_authenticated:
        return redirect('land_page')

    if request.method == 'POST':
        if authentication_form.is_valid():
            user = authenticate(request, username=authentication_form.cleaned_data['username'],
                                password=authentication_form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('courses:course_list')
        # return redirect('accounts:login')

    return render(request, 'accounts/authenticate.html', {'authentication_form': authentication_form})


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('land_page')
