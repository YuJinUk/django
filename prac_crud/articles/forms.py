from django import forms
from .models import Article
# class ArticleForm(forms.Form):
#     ID = forms.CharField(max_length = 10)
#     Password = forms.CharField(widget=forms.Textarea())

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='ID',
        widget = forms.TextInput(
            attrs={
                'class' : 'my-id',
                'placeholder' : 'Enter the id'
            }
        )
    )
    content = forms.CharField(
        label='Password',
        widget = forms.TextInput(
            attrs={
                'class' : 'my-password',
                'placeholder' : 'Enter the password'
            }
        ),
        error_messages={
            'required' : 'Please enter your content'
        }
    )
    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('ID',)
        
    # 유효성 검사
    def clean_title(self):
        title = self.cleaned_data['title']
        lst = ['!','#','$','%','^','&']
        for i in lst:
            if i in title:
                return
        else:
            return title
    
    def clean_content(self):
        content = self.cleaned_data['content']
        if ' ' in content:
            return
        return content