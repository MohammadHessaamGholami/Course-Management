from django.contrib import admin

# Register your models here.
from course.models import Course, Post, PostComment, CourseMember, AssignmentStudent, Question, Assignment

admin.site.register(Course)
admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(Assignment)
admin.site.register(AssignmentStudent)
admin.site.register(CourseMember)
admin.site.register(Question)
