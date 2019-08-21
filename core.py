# !/usr/bin/env python
# coding=utf-8
import configparser

import pymsteams


config = configparser.ConfigParser()
config.read('config.ini')
ACCESS_KEY = config['teamskey']['ACCESS_KEY']

def push_msg():
    """
    推送消息测试
    """
    message = pymsteams.connectorcard(ACCESS_KEY)
    message.title("Msg Title2")
    message.text('Message content test2.')
    message.addLinkButton("Link to Google.", "https://www.google.com")
    message.send()
    print("Done!")


if __name__ == "__main__":
    push_msg()
