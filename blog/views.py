from django.shortcuts import render, HttpResponse, render_to_response
from django.template import RequestContext

from blog.models import Article, Knowledge, Language, Project, Motivation, Competency, Certificate, Job, KeyWord

def construct_cd(request):
    context = {'kw': KeyWord.objects.all()}
    return context, RequestContext(request)

def index(request):
    articles = Article.objects.filter(publish=True).order_by('-date')
    context, req_context = construct_cd(request)
    context['articles'] = articles
    return render_to_response('index.html', context, req_context)

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
    context['articles'] = Article.objects.filter(keywords__in=context['keywords'])
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
