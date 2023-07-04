from django import forms
from django.forms.widgets import TextInput, Select, Textarea, FileInput
from django.utils import timezone

from course.models import Course, PostComment, Post
from jalali_date import date2jalali


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'term')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'maxlength': 50}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        current_date = date2jalali(timezone.now().date())
        term_choices = [(str(current_date.year) + '-1', str(current_date.year) + '-1'),
                        (str(current_date.year) + '-2', str(current_date.year) + '-2')]
        self.fields['term'] = forms.ChoiceField(choices=term_choices, widget=Select(attrs={'class': 'form-control'}))


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('subject', 'text', 'attachment')
        widgets = {
            'subject': TextInput(attrs={'class': 'form-control'}),
            'text': Textarea(attrs={'class': 'form-control', 'rows': 3, 'style': 'resize: none'}),
            'attachment': FileInput(attrs={'class': 'custom-file-input'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={'rows': 3, 'class': 'form-control', 'style': 'resize: none'})
        }
