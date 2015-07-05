#!/usr/bin/python

import ConfigParse
import getopt
import os
import sys
import twitter

def main():
    rc = TweetRc()
    customer_key = rc.GetCustomerKey()
    customer_secret = rc.GetCustomerSecret()
    access_key = rc.GetAccessKey()
    access_secret = rc.GetAccessSecret()

    api = twitter.Api(
            customer_key=customer_key,
            customer_secret=customer_secret,
            access_token_key=access_key,
            access_token_secret=access_secret,
            input_encoding=encoding
        )
