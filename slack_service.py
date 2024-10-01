from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from config import SLACK_BOT_TOKEN
import logging

LOGGER = logging.getLogger(__name__)


class SlackClient(object):
    def __init__(self, channel_id: str):
        self.channel_id = channel_id
        self.client = WebClient(token=SLACK_BOT_TOKEN)

    def send_message(self, message: str):
        try:
            result = self.client.chat_postMessage(channel=self.channel_id, text=message)
            LOGGER.info(result)

        except SlackApiError as e:
            LOGGER.error("Error on sending  message: {}".format(e))

    def send_file(self, initial_comment: str, file_url: str):
        try:
            upload_file = self.client.files_upload_v2(
                channel=self.channel_id,
                title="Automation Test Report",
                file=file_url,
                initial_comment=initial_comment,
            )
            LOGGER.info(upload_file)

        except SlackApiError as e:
            LOGGER.error("Error uploading file: {}".format(e))
