from django.shortcuts import render
from django.views import View

from django.http.response import JsonResponse
from django.template.loader import render_to_string

from .models import Topic
from .forms import TopicForm

class IndexView(View):

    def get(self, request, *args, **kwargs):

        context             = {}
        context["topics"]   = Topic.objects.all()

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        json    = { "error":True }
        form    = TopicForm(request.POST)

        if not form.is_valid():
            print("Validation Error")
            return JsonResponse(json)

        form.save()
        json["error"]   = False

        context             = {}
        context["topics"]   = Topic.objects.all()

        json["content"]     = render_to_string("bbs/content.html",context,request)



        return JsonResponse(json)

index   = IndexView.as_view()
