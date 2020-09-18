# from django.shortcuts import render
import slack
import json
import time
import re
import logging
from django.conf import settings
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from slack.errors import SlackApiError
from .form import leaveRegisterForm, taskAddForm, leaveRegisterViewForm
from asgiref.sync import async_to_sync, sync_to_async
from leaveapp.models import Leave


pattern = re.compile("^([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))+$")

# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.
slack_client = slack.WebClient(token=settings.SLACK_BOT_TOKEN, run_async=True)


class LeaveEvent(APIView):
    @async_to_sync
    async def post(self, request, *args, **kwargs):
        print(request.data)
        if request.data["trigger_id"] and request.data["channel_id"]:
            try:
                start_time = time.time()
                # await slack_client.views_open(
                #     trigger_id=request.data['trigger_id'],
                #     view=await leaveRegisterViewForm(request.data["user_id"])
                # )
                await slack_client.dialog_open(
                    trigger_id=request.data["trigger_id"],
                    dialog=await leaveRegisterForm(request.data["user_id"]),
                )
                total = time.time() - start_time
                logger.info(
                    "With in a {time} second, model is open.".format(time=total)
                )
                logger.info("slack model open successfully.")
                return Response(status=200)
            except SlackApiError as e:
                logger.error(e)
                return Response("Fail", e.response.status_code)
        return Response("requesd data is fail")


class TaskEvent(APIView):
    @async_to_sync
    async def post(self, request, *args, **kwargs):
        if request.data["trigger_id"] and request.data["channel_id"]:
            try:
                start_time = time.time()
                await slack_client.dialog_open(
                    trigger_id=request.data["trigger_id"],
                    dialog=await taskAddForm(request.data["user_id"]),
                )
                total = time.time() - start_time
                logger.info(
                    "With in a {time} second, model is open.".format(time=total)
                )
                logger.info("slack model open successfully.")
                return Response(status=200)
            except SlackApiError as e:
                logger.error(e)
                return Response("Fail", e.response.status_code)
        return Response("requesd data is fail")


@sync_to_async
def create_leave(payload_obj):
    leave_obj = Leave.objects.create(
        title=payload_obj["submission"]["subject"],
        description=payload_obj["submission"]["body"],
        leave_type=payload_obj["submission"]["leave_type"],
        user_name=payload_obj["user"]["name"],
        leave_date=payload_obj["submission"]["date"],
        channel_id=payload_obj["channel"]["id"],
    )
    return leave_obj


class LeaveEventInfo(APIView):
    @async_to_sync
    async def post(self, request, *args, **kwargs):
        payload_obj = json.loads(request.data["payload"])
        if payload_obj["state"] == "leaveform":
            if pattern.match(payload_obj["submission"]["date"]):
                a = await create_leave(payload_obj)
                await slack_client.chat_postMessage(
                    channel=payload_obj["channel"]["id"],
                    text="Succesfully submit your request.",
                )
                return Response(status=200)
            return Response("Date format is wrong", status=400)
        elif payload_obj["state"] == "taskadd":
            print("**************************")
            print(payload_obj)
            return HttpResponse("")
