from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "singlepage/index.html")

# The texts are much longer in reality, but have
# been shortened here to save space
texts = ["text 1 Contrary to popular belief, Lorem Ipsum is not simply random text.\n"
" It has roots in a piece of classical Latin literature from 45 BC,\n"
"professor at Hampden-Sydney College in Virginia, looked up one of the more obscure \n"
"Latin words, consectetur, from a Lorem Ipsum", "Text 2", "Text 3"]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such section")

