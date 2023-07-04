from django.contrib.auth.models import User
from django.core import validators
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Course(models.Model):
    name = models.CharField(max_length=50)
    term = models.CharField(max_length=6)
    presenter = models.ForeignKey("accounts.Teacher", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Course"


class CourseMember(models.Model):
    ACTIVE = "active"
    INACTIVE = "inactive"
    WAITING = "waiting"
    STATE_CHOICES = (
        (ACTIVE, _("Active")),
        (INACTIVE, _("Inactive")),
        (WAITING, _("Waiting"))
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    is_TA = models.BooleanField(default=False)
    grade = models.PositiveSmallIntegerField(null=True, validators=[validators.MinValueValidator(1),
                                                                    validators.MaxValueValidator(20)])
    status = models.CharField(max_length=10, choices=STATE_CHOICES, default=WAITING)

    class Meta:
        db_table = "CourseMember"

    def __str__(self):
        return self.member.username
