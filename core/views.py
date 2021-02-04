from django.shortcuts import render, redirect
from django.views import View
from .forms import ArticleForm
from .models import NewsModel

# Create your views here.

# def InsertionPage(request):
#     form = ArticleForm()
#     context = {
#         "forms": form
#     }
#     return render(request, "core/insertion.html", context=context)

# This view class is for insertion page where the author will add the article
class InsertionPageView(View):
    def get(self, *args, **kwargs):
        form = ArticleForm()
        context = {
            "forms": form
        }
        return render(self.request, "core/insertion.html", context=context)

    def post(self, *args, **kwargs):
        
        form = ArticleForm(self.request.POST)
        if form.is_valid():
            print("|VALID FORM|")
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")
            img_url = form.cleaned_data.get("img_url")

            article = NewsModel(
                title = title,
                content = content,
                img_url = img_url
            )
            article.save()
            print('|NEW ARTICLE SAVED|')
            return redirect("core:insertion")


# This view function for the viewers as they will see all the set of news
def ListingPage(request):
    # news = NewsModel.objects.all() 
    # need to pass the query set, but due to error, we are passing a sample set
    news = {"title":"Title1", 'content':'article content', 'img_url':'url1'}
    
    return render(request, "core/listing.html", news)
