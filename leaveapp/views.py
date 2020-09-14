# from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import slack

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
    print(data)
    support_form = slack_client.dialog_open(
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
    print(support_form)
    return HttpResponse(status=200)
