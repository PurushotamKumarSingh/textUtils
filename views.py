from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("hello")
    return render(request,'index.html')

def analyze(request):
    # Get the text form index.html
    djtext = request.POST.get('text','off')

    # Check Checbox values and create their variable 
    removepunc = request.POST.get('removepunc','off') 
    fullcaps = request.POST.get('fullcaps','off') 
    newLineRemover = request.POST.get('newLineRemover','off') 
    extraSpaceRemover = request.POST.get('extraSpaceRemover','off') 
    # charcounter = request.POST.get('charcounter','off') 
                        

    # Check with checkbox is on 
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose':'remove punctuations','analyzed_text':analyzed}
        # return render(request,'analyze.html',params)
        djtext = analyzed
    
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose':'Changed to UpperCase','analyzed_text':analyzed}
        # return render(request,'analyze.html',params)
        djtext = analyzed
    
    if(newLineRemover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed += char
        params = {'purpose':'Remove New Lines','analyzed_text':analyzed}
        # return render(request,'analyze.html',params)
        djtext = analyzed
    
    if(extraSpaceRemover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed += char
        params = {'purpose':'Remove Extra Space','analyzed_text':analyzed}
        # return render(request,'analyze.html',params)
    
    elif(removepunc != "on" and newLineRemover!="on" and extraSpaceRemover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")
    
    return render(request,'analyze.html',params)
    
    # elif(charcounter=="on"):
    #     analyzed = ""
    #     count = 0
    #     for char in djtext:
    #         if char in djtext:
    #             analyzed += char
    #             count += 1
    #     params = {'purpose':'Count Character','analyzed_text':analyzed}
    #     return render(request,'analyze.html',params)
    
    