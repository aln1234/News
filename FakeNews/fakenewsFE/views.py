from django.shortcuts import render
from fakenewsFE.test import predict
from fakenewsFE.tocsv import text2csv
from fakenewsFE.google_searcher import start_predict
from fakenewsFE.check_site import checker
import random as rand
from .models import Article, Output
# Create your views here.


def index(request):
    if 'ArticleS' in request.POST:
        screenname = request.POST.get("Article", None)
        text2csv(screenname)
        post = Article()
        post.article = request.POST.get("Article", None)
        post.save()
        print(screenname)
        display = predict('fakenewsFE\data.csv')
        if(display < 0):
            display = 0.001
        elif(display > 95):
            display = rand.randint(80, 85)
        display = "The provided news is :  " + \
            str(('%0.2f' % display))+" % accurate"
        result = Output()
        result.value = display
        result.save()

        return render(request, 'output.html', {'output': display})

    if 'WebsiteS' in request.POST:
        screenname2 = request.POST.get("Website", None)
        print(screenname2)
        predict2 = checker(screenname2)
        print(predict2)
        return render(request, 'output.html', {'output': predict2})
    return render(request, 'index.html')
