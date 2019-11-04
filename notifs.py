from utils.core import utils as U
from utils.rest.services_api import ServicesAPI
from utils.rest.services_conn_info import ServicesConnInfo
from utils.rest.services_utils import JSONObj


class SlackServicesAPI(ServicesAPI):

    def __init__(self, services_conn_info, slack_username: str):
        super().__init__(services_conn_info)
        self.slack_username = slack_username

    @staticmethod
    def create_service(slack_webhook_url: str, slack_username: str) -> 'SlackServicesAPI':
        sci = ServicesConnInfo(slack_webhook_url, append_trailing_right_slash=False)
        return SlackServicesAPI(sci, slack_username)

       def gen_payload(self, message: str, slack_username: str = None, channel: str = None):

        payload = JSONObj()
        payload.text = "message"
        return payload


@U.timer
def __main():
    slack_url = 'https://hooks.slack.com/services/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'
    slack_service = SlackServicesAPI.create_service(slack_url, 'test_msg')
    resp = slack_service.send_message('test\n msg')


if __name__ == '__main__':
    __main()

