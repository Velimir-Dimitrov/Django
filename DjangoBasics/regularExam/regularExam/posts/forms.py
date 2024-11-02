from django import forms

from regularExam.posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image_url', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Put an attractive and unique title...'}),
            'content': forms.Textarea(attrs={'placeholder': 'Share some interesting facts about your adorable pets...'}),
        }
        labels = {
            'title': 'Title:',
            'image_url': 'Post Image URL:',
            'content': 'Content:',
        }

class PostCreateForm(PostBaseForm):
    pass

class PostEditForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].help_text = ''

class PostDeleteForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].help_text = ''
            self.fields[field].widget.attrs['readonly'] = True
