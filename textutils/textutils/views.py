
from django . http import HttpResponse
from django . shortcuts import render


def index(request):
   return render(request,'index2.html')

def analyze(request):
   # Getting the text

   x= request.POST.get('text','default')

   # checking checkbox values
   removepunc= request.POST.get('removepunc','off')
   fullcaps = request.POST.get('fullcaps','off')
   newlineremover= request.POST.get('newlineremover','off')
   extraspaceremover= request.POST.get('extraspaceremover','off')
   charcounter= request.POST.get('charcounter','off')

   # checking which checkbox is on
   if removepunc == "on":
      punctuations=  '''!@#$%^&*()-_+{}[]~?\/.><'"'''
      analyzed = ""
      for char in x:
         if char not in punctuations:
            analyzed = analyzed+ char

      params={'purpose':'Removed Punctuations','analyzed_text': analyzed}
      x=analyzed
      # return render(request,'analyze.html',params)

   if(fullcaps == "on"):
      analyzed = ""
      for char in x:
         analyzed = analyzed + char.upper()
      params = {'purpose': 'THE CAPITALIZED LETTERS', 'analyzed_text': analyzed}
      x=analyzed
      # return render(request, 'analyze.html', params)

   if(newlineremover == "on"):
      analyzed =""
      for char in x:
         if char!= "\n" and char!="\r":
            analyzed = analyzed + char
      params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
      x=analyzed
      # return render(request, 'analyze.html', params)

   if(extraspaceremover == "on"):
      analyzed=""
      for index, char in enumerate (x):
         if not(x[index]==" " and x[index+1] == " "):
            analyzed= analyzed + char
      params={'purpose':'extraspaceremover', 'analyzed_text':analyzed}
      x=analyzed
      # return render(request,'analyze.html',params)

   if (charcounter == "on"):
      count = 0
      for i in x:
         count=count+1

      params = {'purpose': 'Number of Characters', 'analyzed_text': count}
      x=analyzed
      # return render(request, 'analyze.html', params)

   if(removepunc !="on"and fullcaps !="on" and newlineremover !="on"and extraspaceremover !="on" and charcounter !="on"):

      return HttpResponse ("Please choose any one of the operations")


   return render(request, 'analyze.html', params)
