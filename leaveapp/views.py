# from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import slack
import json
from leaveapp.models import Leave
from .form import leaveRegisterForm, leaveRegisterViewForm
from slack.errors import SlackApiError
from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

slack_client = slack.WebClient(
    token=settings.SLACK_BOT_TOKEN,
)


def jsontodic(json_dict):
    json_dict = json_dict.replace("=", ":")
    json_dict = json_dict.replace("&", ",")
    json_dict = json_dict.split(",")
    data = {}
    for i in json_dict:
        idx = i.index(":")
        data.update({i[:idx]: i[idx + 1 :]})
    return data


# class Events(APIView):
#     def post(self, request, *args, **kwargs):
#         if request.data['trigger_id'] and request.data['channel_id']:
#             try:
#                 slack_client.views_open(
#                     trigger_id=request.data['trigger_id'],
#                     view=leaveRegisterViewForm()
#                 )
#                 return Response(status=200)
#             except SlackApiError as e:
#                 print(e)
#                 slack_client.chat_postMessage(
#                     channel=request.data['channel_id'],
#                     text='trigger_expired'
#                 )
#                 return Response("Fail", e.response.status_code)
#         return Response("requesd data is fail")


@csrf_exempt
@require_http_methods(["POST"])
def leaveApply(request):
    json_dict = request.body.decode("utf-8")
    data = jsontodic(json_dict)
    try:
        slack_client.views_open(
            trigger_id=data["trigger_id"], view=leaveRegisterViewForm()
        )
        return HttpResponse(status=200)
    except SlackApiError as e:
        print(e)
        slack_client.chat_postMessage(
            channel=data["channel_id"], text="trigger_expired"
        )
        return HttpResponse("Fail", e.response.status_code)

    # slack_client.dialog_open(
    #         trigger_id=data["trigger_id"],
    #         dialog=leaveRegisterForm(data["user_id"])
    #     )


@csrf_exempt
@require_http_methods(["GET", "POST"])
def leaveinfo(request):
    print("-------------")
    print(request.POST.get)
    data_obj = json.loads(request.POST.get("payload"))
    print("==============")
    print(data_obj)
    # Leave.objects.create(
    #     title=data_obj["submission"]["subject"],
    #     description=data_obj["submission"]["body"],
    #     leave_type=data_obj["submission"]["leave_type"],
    #     user_name=data_obj["user"]["name"],
    # )

    return HttpResponse(status=200)
