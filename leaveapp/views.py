# from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import slack
import json
from leaveapp.models import Leave

# Create your views here.

slack_client = slack.WebClient(token=settings.SLACK_BOT_TOKEN)


@csrf_exempt
@require_http_methods(["POST"])
def leaveApply(request):
    json_dict = request.body.decode("utf-8")
    json_dict = json_dict.replace("=", ":")
    json_dict = json_dict.replace("&", ",")
    json_dict = json_dict.split(",")
    data = {}
    for i in json_dict:
        idx = i.index(":")
        data.update({i[:idx]: i[idx + 1 :]})
    slack_client.dialog_open(
        trigger_id=data["trigger_id"],
        dialog={
            "title": "Fill the form for Leave",
            "submit_label": "Submit",
            "callback_id": data["user_id"],
            "elements": [
                {
                    "label": "Subject",
                    "type": "text",
                    "name": "subject",
                    "placeholder": "Subject for Leave",
                },
                {
                    "label": "Description",
                    "type": "textarea",
                    "name": "body",
                    "placeholder": "Reason for Leave",
                },
                {
                    "label": "Type of Leave",
                    "type": "select",
                    "name": "leave_type",
                    "options": [
                        {"label": "First Half", "value": "first_half"},
                        {"label": "Second Half", "value": "second_half"},
                        {"label": "Full Day", "value": "full_day"},
                    ],
                },
            ],
        },
    )
    return HttpResponse(status=200)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def leaveinfo(request):
    print(dir(slack_client))
    data_obj = json.loads(request.POST.get("payload"))
    Leave.objects.create(
        title=data_obj["submission"]["subject"],
        description=data_obj["submission"]["body"],
        leave_type=data_obj["submission"]["leave_type"],
        user_name=data_obj["user"]["name"],
    )
    # print("-----------------")
    # print(data_obj['channel']['id'])
    # slack_client.chat_postMessage(
    #     channel=data_obj['channel']['id'],
    #     text="Hello world!")
    return HttpResponse(status=200)
