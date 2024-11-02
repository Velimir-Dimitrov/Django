from django import forms
from django.core.exceptions import ValidationError
from django.forms import formset_factory

from forumApp.posts.models import Post, Comment
from forumApp.posts.mixins import DisableFieldsMixin


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        error_messages = {
            "title": {
                "required": "Testing missing title and required turned off from html"
            }
        }

    def clean_author(self):
        author = self.cleaned_data['author']

        if author[0] != author[0].upper():
            raise ValidationError("Author name should start with capital letter!")

        return author

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')


        if content and title and title in content:
            raise ValidationError("Title should not be in content")

        return cleaned_data

    def save(self, commit=True):
        post = super().save(commit=False)

        post.title= post.title.capitalize()

        if commit:
            post.save()

        return post

        # # Test

        # random = forms.CharField() #test
        # widgets = {
        #     "random": forms.PasswordInput,
        # }
        #
        # help_texts = {
        #     'title': "This is the title of the post",
        #     'random': "This field is not linked with the database",
        # }

class PostCreateForm(PostBaseForm):
    pass

class PostEditForm(PostBaseForm):
    pass

class PostDeleteForm(PostBaseForm, DisableFieldsMixin):
    disabled_field = ("__all__", )
    pass

class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search for a post...',
            }
        ),
        # error_messages={
        #     'required': 'Testing the error message for searchform',
        # }
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'content')

        labels = {
            'author': '',
            'content': '',
        }

        error_messages = {
            'author': {
                'required': 'Author name is required. Write it!',
            },
            'content': {
                'required': 'Content is required. Write it!',
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['author'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your name..',
        })

        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Add message..',
        })

CommentFormSet = formset_factory(CommentForm, extra=1)

# # forms without model, model has to be created separate as well
# class PersonForm(forms.Form):
#     STATUS_CHOICES = (
#         (1, "Draft"),
#         (2, "Published"),
#         (3, "Archived")
#     )
#
#     person_name = forms.CharField(
#         max_length=10,
#     )
#     age = forms.IntegerField()
#
#     status = forms.IntegerField(
#         widget=forms.Select(choices=STATUS_CHOICES)
#     )
    # status = forms.ChoiceField(
    #     choices=STATUS_CHOICES
    # )



