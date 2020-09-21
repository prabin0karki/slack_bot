import slack
from django.conf import settings
from django.http import HttpResponse
from asgiref.sync import async_to_sync, sync_to_async

slack_client = slack.WebClient(token=settings.SLACK_BOT_TOKEN, run_async=True)


async def post_Message(channel_id, message):
    a = await slack_client.chat_postMessage(
        channel=channel_id,
        text=message,
    )
    return a
