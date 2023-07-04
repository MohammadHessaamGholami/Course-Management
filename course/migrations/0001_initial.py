# Generated by Django 3.0.6 on 2020-05-31 21:27

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'Assignment',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('term', models.CharField(max_length=6)),
                ('presenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Teacher')),
            ],
            options={
                'db_table': 'Course',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('text', models.TextField(max_length=5000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('attachment', models.FileField(upload_to='course/posts/assignments')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Post',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=100)),
                ('grade', models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Assignment')),
            ],
            options={
                'db_table': 'Question',
            },
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=2000)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'PostComment',
            },
        ),
        migrations.CreateModel(
            name='CourseMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_TA', models.BooleanField(default=False)),
                ('grade', models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)])),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('waiting', 'Waiting')], default='waiting', max_length=10)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'CourseMember',
            },
        ),
        migrations.AddField(
            model_name='assignment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='AssignmentStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers', jsonfield.fields.JSONField(default=dict)),
                ('grade', models.PositiveSmallIntegerField(null=True)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Assignment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Student')),
            ],
            options={
                'db_table': 'AssignmentStudent',
                'unique_together': {('assignment', 'student')},
            },
        ),
    ]