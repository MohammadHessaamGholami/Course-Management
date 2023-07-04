from django.contrib.auth.models import User
from jsonfield import JSONField
from django.core import validators
from django.db import models


class Assignment(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey("course.Course", on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        db_table = "Assignment"

    def __str__(self):
        return str(self.course) + " - " + str(self.id)


class Question(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=100)
    grade = models.PositiveSmallIntegerField(null=True, validators=[validators.MinValueValidator(0),
                                                                    validators.MaxValueValidator(100)])

    class Meta:
        db_table = "Question"

    def __str__(self):
        return "assignment: " + str(self.assignment_id) + ", question: " + str(self.id)


class AssignmentStudent(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey("accounts.Student", on_delete=models.CASCADE)
    answers = JSONField(default=dict)
    grade = models.PositiveSmallIntegerField(null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "AssignmentStudent"
        unique_together = ("assignment", "student")

    def __str__(self):
        return self.id
