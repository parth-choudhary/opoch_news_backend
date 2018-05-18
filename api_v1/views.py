from django.shortcuts import render
from django.http import JsonResponse
from drum.links.models import Link
from mezzanine.generic.models import AssignedKeyword, Keyword
from mezzanine.accounts import get_profile_model

# Create your views here.
USER_PROFILE_RELATED_NAME = get_profile_model().user.field.related_query_name()


def sources(request):
    tags = Keyword.objects.all()
    sources = []
    for tag in tags:
        item = dict()
        item['id'] = tag.id
        item['name'] = tag.title
        item['description'] = tag.title
        item['url'] = 'https://' + request.get_host() + tag.keyword_image.image.url
        item['category'] = tag.title
        item['sortBysAvailable'] = ['top']
        item['urlsToLogos'] = {
            "small": 'https://' + request.get_host() + tag.keyword_image.image.url,
            "medium": 'https://' + request.get_host() + tag.keyword_image.image.url,
            "large": 'https://' + request.get_host() + tag.keyword_image.image.url
        }
        sources.append(item)
    return JsonResponse({
        'status': 'ok',
        'sources': sources
    })


def articles(request):
    tag = Keyword.objects.get(id=request.GET['source']).title
    links = Link.objects.published().select_related(
        "user",
        "user__%s" % USER_PROFILE_RELATED_NAME
    ).filter(keywords__keyword__slug=tag.lower()).prefetch_related("keywords__keyword")
    articles = []
    for link in links:
        item = {}
        item['title'] = link.title
        item['author'] = link.domain
        item['description'] = link.description
        item['url'] = link.url
        item['urlToImage'] = link.image_url
        item['publishedAt'] = link.publish_date
        articles.append(item)
    response = {
        'status': "ok",
        'source': tag,
        'sortBy': 'top',
        'articles': articles
    }
    return JsonResponse(response)

