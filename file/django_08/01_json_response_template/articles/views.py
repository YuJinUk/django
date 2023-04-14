from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer



# Create your views here.
def article_html(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
        }
    return render(request, 'articles/article.html', context)


def article_json_1(request):
    articles = Article.objects.all()
    articles_json = []
    
    for article in articles:
        articles_json.append(
            {
                "id": article.pk,
                "title": article.title,
                "content": article.content,
                "created_at": article.created_at,
                "updated_at": article.updated_at,
            }
        )
    return JsonResponse(articles_json, safe=False)


def article_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize("json", articles)
    return HttpResponse(data, content_type="application/json")
    # serializer를 쓰면 데이터 직렬화를 시켜주는데
    # 직렬화(Serialization)란 자바 시스템 내에서 사용하는 객체 또는 데이터를 
    # 자바시스템 외에서도 사용할 수 있도록 Byte 형태로 데이터를 변환하는 기술이다.(파일로 만든다고 보면된다.)
    # Byte로 변환된 데이터를 다시 자바의 객체로 변환하는 기술을 역직렬화(Deserialization)라고 한다.

# @api_view(['GET'])
@api_view()
def article_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many = True)
    return Response(serializer.data) 
# HttpResponse를 사용하면 데이터만 나옴
# Response를 사용하면 장고에서 제공하는 프레임을 이용하여 구성해줌 


@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk = article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)