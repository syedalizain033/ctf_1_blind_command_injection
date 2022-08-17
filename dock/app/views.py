from dataclasses import replace
from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormClass

def home(request):
    form = FormClass(request.POST)
    if request.method=="POST" and form.is_valid() :
        
        url=form.cleaned_data['urlCommand']
        url=str(url)
        checklist=["$", '&','wget',';','rm','>','{','}']
        for i in checklist:
            if i in url:
                url=url.replace(i,'')
        checkUrl=check=any(checklist in url for checklist in checklist)
        
        import os
        com=("curl -I "+url+" 2>&1 | awk '/HTTP\// {print $2}'")
        #com= "ls"
        stream = os.popen(com)
        output = stream.read()
        return render(request, "app/home.html", {'form': form, 'code': output})
        
        
    else:
        form = FormClass()
        return render(request, "app/home.html", {'form': form})

def about(request):
    return render(request, 'app/about.html')

def contact(request):
    return HttpResponse("NO RESPONSE")
