# from django.shortcuts import render
import json
import time
import re
import logging
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from slack.errors import SlackApiError
from .form import leaveRegisterForm, taskAddForm
from asgiref.sync import async_to_sync
from .slack_views import slack_client
from .create_orm import create_task, create_leave
import datetime
import requests

pattern = re.compile("^([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))+$")

# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.


class LeaveEvent(APIView):
    @async_to_sync
    async def post(self, request, *args, **kwargs):
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


class LeaveEventInfo(APIView):
    def post(self, request, *args, **kwargs):
        payload_obj = json.loads(request.data["payload"])
        if payload_obj["state"] == "leaveform":
            if pattern.match(payload_obj["submission"]["date"]):
                today_date = datetime.datetime.now().date()
                leave_date = datetime.datetime.strptime(
                    payload_obj["submission"]["date"], "%Y-%m-%d"
                ).date()
                if today_date <= leave_date:
                    create_leave(payload_obj)
                    header = {"content-type": "application/json"}
                    data_obj = {
                        "text": "Your request have been successfully submitted."
                    }
                    requests.post(
                        payload_obj["response_url"], headers=header, data=str(data_obj)
                    )
                    return Response(status=200)
                return Response({"text": "Date format is wrong"}, status=400)
            return Response("Date format is wrong", status=400)
        elif payload_obj["state"] == "taskadd":
            create_task(payload_obj)
            header = {"content-type": "application/json"}
            data_obj = {"text": "Your request have been successfully submitted."}
            requests.post(
                payload_obj["response_url"], headers=header, data=str(data_obj)
            )
            return HttpResponse(status=200)
