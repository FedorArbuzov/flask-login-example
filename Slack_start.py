from slackclient import SlackClient
from botToken import bot_token
from  time import sleep

slack_client = SlackClient(bot_token)


if slack_client.rtm_connect() == True:
    print('Connected.')
    while True:
        response = slack_client.rtm_read()
        print(slack_client.rtm_read())
        for part in response:
            if part['type'] == 'message' and 'user' in part:
                slack_client.api_call("chat.postMessage", channel=part['channel'],
                                          text=part['text'], username='top-kek-bot', icon_emoji=':robot_face:')
                print(part)
    sleep(1)
else:
    print('Connection Failed, invalid token?')