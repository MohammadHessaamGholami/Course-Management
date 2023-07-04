from datetime import timedelta

from django.shortcuts import render, redirect
from django.utils import timezone

from accounts.models import get_user_role
from course.forms import CourseForm, CommentForm, PostForm

courses = {
    1: {"id": 1, "name": "آزمایشگاه پایگاه داده", 'term': "1398-2", 'presenter': {'username': "ترکاشون"},
        'members': [{'first_name': 'کریم', 'last_name': 'جهانبخش سفید کمر'}]},
    2: {"id": 2, "name": "عروض و قافیه", 'term': "1398-1", 'presenter': {'username': "ترکاشون"},
        'members': [
            {'first_name': 'حسن', 'last_name': 'غلی‌پور'}, {'first_name': 'حمید', 'last_name': 'راد'},
            {'first_name': 'عماد', 'last_name': 'علومی'}, {'first_name': 'اشکان', 'last_name': 'اشکریزان'},
            {'first_name': 'ژوزه', 'last_name': 'مورینیو'}, {'first_name': 'مجید', 'last_name': 'سمیعی'},
        ]}
}

posts_by_course = {
    1: {
        1: {'creator': 'استاد باقری', 'subject': 'امتحان', 'text': 'روز دوشنبه امتحان از فصل ۳ خواهیم داشت.',
            'created_at': timezone.now() - timedelta(minutes=30), 'id': 1,
            'comments': [{'text': 'استاد دوشنبه یه امتحان دیگه هم داریم بندازید هفته بعد.', 'username': 'کریم'},
                         {'text': 'بندازید عقب لطفا!', 'username': 'هیشکی'}]
            },
        3: {'creator': 'استاد اسدی', 'subject': 'تبریک نوروز', 'text': 'حاجی فیروزم سالی یه روزم.',
            'created_at': timezone.now() - timedelta(days=30 * 3), 'id': 3,
            'comments': [{'text': 'پیشاپیش', 'username': 'ابراهیم'}]},
        4: {'creator': 'استاد اسدی', 'subject': 'یک موضوع', 'text': 'یک متن برای موضوع',
            'created_at': timezone.now() - timedelta(days=30), 'id': 4,
            'comments': [{'text': 'کامنت اول', 'username': 'امیرمهدی'}, {'text': 'کامنت دوم', 'username': 'پویان'},
                         {'text': 'کامنت سوم', 'username': 'نرگس'}]},
    },
    2: {
        2: {'creator': 'حسن غلی‌پور', 'subject': 'مشکل در سوالات تمرین',
            'text': 'سوال ۲ تمرین سوم باید به جای ۰، ۱ باشه',
            'created_at': timezone.now() - timedelta(days=2), 'id': 2,
            'comments': [{'text': 'اصلاح شد', 'username': 'استاد طوفان'}]
            },
    }
}


def course_list(request):
    _, is_teacher = get_user_role(request.user)
    cs = list(courses.values())
    limited = False
    if request.GET.get('limit') == 'on':
        limited = True
        cs = list(filter(lambda x: len(x['members']) > 5, cs))
    form = CourseForm()
    if request.method == 'POST':
        return redirect('courses:course_list')
    return render(request, 'course/index.html', {'course_list': cs, 'limited': limited, 'form': form,
                                                 'is_teacher': is_teacher})


def course_detail(request, course_id):
    course = courses.get(course_id)
    return render(request, 'course/course_detail.html', {'course': course})


def course_students(request, course_id):
    course = courses.get(course_id)
    students = course.get('members')
    return render(request, 'course/course_students.html', {'students': students})


def course_posts(request, course_id):
    posts_of_course = posts_by_course.get(course_id).values()
    post_form = PostForm(request.POST or None)
    sort = False
    if request.GET.get('sort') == 'on':
        sort = True
        posts_of_course = sorted(posts_of_course, key=lambda x: len(x['comments']), reverse=True)
    return render(request, 'course/course_posts.html', {
        'posts': posts_of_course, 'course_id': course_id, 'sorted': sort, 'post_form': post_form
    })


def post(request, course_id, post_id):
    comment_form = CommentForm(request.POST or None)
    p = posts_by_course.get(course_id).get(post_id)
    return render(request, 'course/post.html', {'post': p, 'comment_form': comment_form})
