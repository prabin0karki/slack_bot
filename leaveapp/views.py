# from django.shortcuts import render
import slack
import json
from django.conf import settings
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from slack.errors import SlackApiError
from .form import leaveRegisterViewForm, leaveRegisterForm
from asgiref.sync import async_to_sync
import time

# from leaveapp.models import Leave


import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.
slack_client = slack.WebClient(token=settings.SLACK_BOT_TOKEN, run_async=True)


class LeaveEvent(APIView):
    @async_to_sync
    async def post(self, request, *args, **kwargs):
        if request.data["trigger_id"] and request.data["channel_id"]:
            try:
                start_time = time.time()
                # await slack_client.views_open(
                #     trigger_id=request.data['trigger_id'],
                #     view=leaveRegisterViewForm()
                # )
                await slack_client.dialog_open(
                    trigger_id=request.data["trigger_id"],
                    dialog=await leaveRegisterForm(request.data["user_id"]),
                )
                total = time.time() - start_time
                print("total: ", total)
                logger.info("slack model open successfully.")
                return Response(status=200)
            except SlackApiError as e:
                print(e)
                await slack_client.chat_postMessage(
                    channel=request.data["channel_id"], text="trigger_expired"
                )
                logger.error(e)
                return Response("Fail", e.response.status_code)
        return Response("requesd data is fail")


class LeaveEventInfo(APIView):
    def post(self, request, *args, **kwargs):
        payload_obj = json.loads(request.data["payload"])
        print(payload_obj)
        # view_obj = payload_obj['view']
        # block_obj = view_obj['blocks']
        # value_obj = view_obj['state']['values']
        # print(block_obj)
        return HttpResponse("")
