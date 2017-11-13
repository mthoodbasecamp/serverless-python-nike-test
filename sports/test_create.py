import os
import unittest
import json
import boto3
dynamodb = boto3.resource('dynamodb')
from list import list
from get import get


class TestHandler(unittest.TestCase):
    os.environ['DYNAMODB_TABLE'] = 'serverless-rest-api-with-dynamodb-dev'
    """ Tests handler methods """

    def test_list_posts(self):
        """ Tests list_posts """
        res = list(None, None)
        self.assertEquals(200, res['statusCode'])
        self.assertTrue(len(res['body']) > 0)

    def test_get_post(self):
        """ Tests get_post """
        event = {
            'pathParameters': {
                'id': 'testname'
            }
        }
        'id': event['pathParameters']['id']
        res = get(event, None)
        self.assertEquals(200, res['statusCode'])
        self.assertTrue(len(res['body']) > 0)

if __name__ == '__main__':
    unittest.main()