from django.shortcuts import render, HttpResponse, render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator
from django.db.models import Q

from functools import reduce

from blog.models import Article, Knowledge, Language, Project, Motivation, Competency, Certificate, Job, KeyWord

def construct_cd(request):
    context = {'kw': KeyWord.objects.all()}
    return context, RequestContext(request)

def index(request, page=1):
    articles = Article.objects.filter(publish=True).order_by('-date')
    p = Paginator(articles, 3)
    context, req_context = construct_cd(request)
    if int(page) == p.num_pages + 1:
        return render_to_response('end.html', context, req_context)
    if int(page) > p.num_pages:
        return HttpResponse('done')
    if page == 1:
        context['articles'] = p.page(page)
        return render_to_response('index.html', context, req_context)
    else:
        context['articles'] = p.page(page)
        return render_to_response('indexp.html', context, req_context)

def search(request):
    context, req_context = construct_cd(request)
    kw = request.GET.getlist('kw')
    print(kw)
    if len(kw) >= 1:
        context['articles'] = Article.objects.filter(reduce(lambda x, y: x | y, [Q(title__icontains=word) for word in kw]) |
                                                     reduce(lambda x, y: x | y, [Q(content__icontains=word) for word in kw]),
                                                     publish=True).order_by('-date')
    return render_to_response('search.html', context, req_context)

def cv(request):
    context, req_context = construct_cd(request)
    context['knowledges'] = Knowledge.objects.all()
    context['languages'] = Language.objects.all()
    context['projects'] = Project.objects.all()
    context['motivations'] = Motivation.objects.all()
    context['comps'] = Competency.objects.all()
    context['jobs'] = Job.objects.all()
    context['certs'] = Certificate.objects.all()
    return render_to_response('cv.html', context, req_context)

def keyword(request):
    context, req_context = construct_cd(request)
    context['keywords'] = KeyWord.objects.filter(id__in=request.GET.getlist('ids'))
    context['articles'] = Article.objects.filter(keywords__in=context['keywords'], publish=True).order_by('-date')
    return render_to_response('keywords.html', context, req_context)

def article(request, articleid):
    context, req_context = construct_cd(request)
    context['article'] = Article.objects.get(id=articleid)
    return render_to_response('article.html', context, req_context)

def archive(request):
    context, req_context = construct_cd(request)
    articles = Article.objects.filter(publish=True)
    months_list = {1: 'Janvier'}
    months = []
    cur = None
    # print(articles[0].date.month, articles[0].date.strftime('%B'))
    for article in articles:
        if cur == None or cur.month != article.date.month or cur.year != article.date.year:
            cur = article.date
            months.append((months_list[article.date.month] + '%d' % article.date.year,
                           months_list[article.date.month],
                           article.date.year,
                           []))
            months[len(months) - 1][3].append(article)
        else:
            months[len(months) - 1][3].append(article)


    context['months'] = months
    return render_to_response('archive.html', context, req_context)
