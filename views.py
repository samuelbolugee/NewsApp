from django.shortcuts import render
from newsapi import NewsApiClient
from .config import apikey
# Create your views here.

def index(request):
    newsapi = NewsApiClient(api_key=apikey)
    topheadlines = newsapi.get_top_headlines(sources='al-jazeera-english')

    articles =  topheadlines['articles']
    desc = []
    news = []
    img = []
    content = []


    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        content.append(myarticles['url'])

    mylist = zip(news, desc, img, content)

    return render(request, 'index.html', context={"mylist":mylist})

def bbc(request):
    newsapi = NewsApiClient(api_key=apikey)
    topheadlines = newsapi.get_top_headlines(sources='bbc-news')

    articles =  topheadlines['articles']
    desc = []
    news = []
    img = []
    content = []


    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        content.append(myarticles['url'])

    mylist = zip(news, desc, img, content)

    return render(request, 'bbc.html', context={"mylist":mylist})

def bbcsport(request):
    newsapi = NewsApiClient(api_key=apikey)
    topheadlines = newsapi.get_top_headlines(sources='bbc-sport')

    articles =  topheadlines['articles']
    desc = []
    news = []
    img = []
    content = []


    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        content.append(myarticles['url'])

    mylist = zip(news, desc, img, content)

    return render(request, 'bbcsport.html', context={"mylist":mylist})

def businessinsider(request):
    newsapi = NewsApiClient(api_key=apikey)
    topheadlines = newsapi.get_top_headlines(sources='business-insider')

    articles =  topheadlines['articles']
    desc = []
    news = []
    img = []
    content = []


    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        content.append(myarticles['url'])

    mylist = zip(news, desc, img, content)

    return render(request, 'binsider.html', context={"mylist":mylist})

def cnn(request):
    newsapi = NewsApiClient(api_key=apikey)
    topheadlines = newsapi.get_top_headlines(sources='cnn')

    articles =  topheadlines['articles']
    desc = []
    news = []
    img = []
    content = []


    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        content.append(myarticles['url'])

    mylist = zip(news, desc, img, content)

    return render(request, 'cnn.html', context={"mylist":mylist})

def nbcnews(request):
    newsapi = NewsApiClient(api_key=apikey)
    topheadlines = newsapi.get_top_headlines(sources='nbc-news')

    articles =  topheadlines['articles']
    desc = []
    news = []
    img = []
    content = []


    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        content.append(myarticles['url'])

    mylist = zip(news, desc, img, content)

    return render(request, 'nbc.html', context={"mylist":mylist})

def bloomberg(request):
    newsapi = NewsApiClient(api_key=apikey)
    topheadlines = newsapi.get_top_headlines(sources='bloomberg')

    articles =  topheadlines['articles']
    desc = []
    news = []
    img = []
    content = []


    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        content.append(myarticles['url'])

    mylist = zip(news, desc, img, content)

    return render(request, 'bloomberg.html', context={"mylist":mylist})

def bleacher(request):
    newsapi = NewsApiClient(api_key=apikey)
    topheadlines = newsapi.get_top_headlines(sources='bleacher-report')

    articles =  topheadlines['articles']
    desc = []
    news = []
    img = []
    content = []


    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        content.append(myarticles['url'])

    mylist = zip(news, desc, img, content)

    return render(request, 'bleacher.html', context={"mylist":mylist})


def espn(request):
    newsapi = NewsApiClient(api_key=apikey)
    topheadlines = newsapi.get_top_headlines(sources='espn')

    articles =  topheadlines['articles']
    desc = []
    news = []
    img = []
    content = []


    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        content.append(myarticles['url'])

    mylist = zip(news, desc, img, content)

    return render(request, 'espn.html', context={"mylist":mylist})

def abc(request):
    newsapi = NewsApiClient(api_key=apikey)
    topheadlines = newsapi.get_top_headlines(sources='abc-news')

    articles =  topheadlines['articles']
    desc = []
    news = []
    img = []
    content = []


    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        content.append(myarticles['url'])

    mylist = zip(news, desc, img, content)

    return render(request, 'abc.html', context={"mylist":mylist})

def timesindia(request):
    newsapi = NewsApiClient(api_key=apikey)
    topheadlines = newsapi.get_top_headlines(sources='the-times-of-india')

    articles =  topheadlines['articles']
    desc = []
    news = []
    img = []
    content = []


    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        content.append(myarticles['url'])

    mylist = zip(news, desc, img, content)

    return render(request, 'toi.html', context={"mylist":mylist})


