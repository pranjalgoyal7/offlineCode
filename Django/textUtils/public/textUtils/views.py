# I have created this file
from django.http import HttpResponse
from django.http.response import Http404
from django.shortcuts import render
from django.urls.resolvers import ResolverMatch

# Displaying home page
def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Recieving the text
    djtext=request.GET.get('text','default')

    #Recieving checkbox values
    rempunc= request.GET.get('removepunc','off')
    FullCaps= request.GET.get('FullCaps','off')
    removeNewLine= request.GET.get('removeNewLine','off')
    extraSpaceRemover = request.GET.get('extraSpaceRemover', 'off')

    # Checking checkbox values
    if rempunc == "on":

        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params={'purpose': 'Removed Punctuations','analyzed_text': analyzed}
        return render(request, 'analyze.html', params)


    elif(FullCaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params={'purpose': 'CAPITALIZED','analyzed_text': analyzed}
        return render(request, 'analyze.html', params)


    elif(removeNewLine=="on"):
        analyzed=""
        newLine= '\n'
        for char in djtext:
            if char is not newLine:
                analyzed = analyzed + char
        params={'purpose': 'Removed new lines','analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(extraSpaceRemover=="on"):
        analyzed=""
        for index, char in enumerate(djtext):
            if djtext[index]==" " and djtext[index + 1]==" ":
                pass
            else:
                analyzed = analyzed + char
        params={'purpose': 'Removed extra spaces','analyzed_text': analyzed}
        return render(request, 'analyze.html', params)


    else:
        return HttpResponse('error')