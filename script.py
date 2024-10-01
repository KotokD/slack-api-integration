import logging
from slack_service import SlackClient
from config import CHANNEL_ID

LOGGER = logging.getLogger(__name__)

try:
    initial_comment = f"Send message to slack channel"
    SlackClient(channel_id=CHANNEL_ID).send_file(
        initial_comment, f"file.txt"
    )

except Exception as e:
    LOGGER.error("Error on uploading test report: {}".format(e))
    raise e
