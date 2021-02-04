from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=264)
    content = forms.CharField(max_length=264)
    img_url = forms.CharField(max_length=264) # need to add URL FIELD to validate url
