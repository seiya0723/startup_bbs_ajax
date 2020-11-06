from django.shortcuts import render,redirect

from django.views import View
from .models import Topic

import json 
from django.http.response import JsonResponse
from django.template.loader import render_to_string

class BbsView(View):

    def get(self, request, *args, **kwargs):

        data    = Topic.objects.all()
        context = { "data":data }

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        request_post    = json.loads(request.body.decode("utf-8"))

        if "comment" in request_post:

            posted  = Topic( comment = request_post["comment"] )
            posted.save()

            data    = Topic.objects.all()
            context = { "data":data }

            content_data_string     = render_to_string('bbs/comment.html', context ,request)
            json_data               = { "content" : content_data_string }

            return JsonResponse(json_data)

        return redirect("bbs:index")

index   = BbsView.as_view()

