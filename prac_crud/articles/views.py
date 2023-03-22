from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.
def index(request):
    articles = Article.objects.all()
    # articles = Article.objects.all().order_by('-pk')
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk = pk)
    context = {
        'pkid' : article,
        'pk' : pk,
    }
    return render(request, 'articles/detail.html', context)

def error(request):
    return render(request, 'articles/error.html')

# def new(request):
#     return render(request, 'articles/new.html')

def create(request): # DB에 저장
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # print(title, content)
        # DB에 새로운 Article 저장
        # Article.objects.create(
        #     title = title,
        #     content = content
        # )
        # article = Article(title = title, content = content)
        # print('check', article)
        # if title != "yu" or content != "ju":
        #     print('checkingchecking')
        #     return redirect('articles:error')
        #     # return render(request, 'articles/error.html')
        # article.save()
        if form.is_valid():
            article = form.save()
            print(form.cleaned_data)
            print('hello')
            return redirect('articles:detail', article.pk)
        return redirect('articles:index')
    else:
        form = ArticleForm()
        context = {
            'form' : form
        }
        return render(request, 'articles/create.html', context)

def dellete(request, pk):
    article = Article.objects.get(pk = pk)
    article.delete()
    return redirect('articles:index')

# def edit(request, pk):
#     article = Article.objects.get(pk = pk)
#     context = {
#         'article' : article
#     }
#     return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk = pk)
    if request.user == article.user:
        if request.method == 'POST':
            print(2222)
            # article.title = request.POST.get('title')
            # article.content = request.POST.get('content')
            # article.save()
            form = ArticleForm(request.POST, request.FILES, instance = article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', pk = article.pk)
            # return redirect('articles:detail', pk = article.pk)
        else:
            print(111)
            form = ArticleForm(instance = article)
        context = {
            'form' : form,
            'article' : article
        }
        # print(form.cleaned_data)
        print(context)
        return render(request, 'articles/update.html', context)