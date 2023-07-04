from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.utils.translation import ugettext_lazy as _


def get_user_role(user):
    is_teacher = False
    try:
        role = user.student
    except Exception:
        role = user.teacher
        is_teacher = True
    return role, is_teacher


class Student(models.Model):
    student_id = models.CharField(max_length=10, primary_key=True, verbose_name=_('Student id'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Student"

    def __str__(self):
        return self.student_id


class Teacher(models.Model):
    teacher_id = models.CharField(max_length=10, primary_key=True, verbose_name=_('Teacher id'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    started_at = models.DateField(verbose_name=_('Started at'))

    class Meta:
        db_table = "Teacher"

    def __str__(self):
        return self.teacher_id

