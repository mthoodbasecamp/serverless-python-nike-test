import unittest

class TestCreate(unittest.TestCase):
    def test_create(self):

      event = {
        'pathParameters': {
          'name': 'testname'
        }
      }

      context = {}

      expected = {
        'body': '{"output": "Hello testname"}',
        'headers': {
          'Content-Type': 'application/json'
        },
        'statusCode': 200
      }

      assert create(event, context) == expected

if __name__ == '__main__':
    unittest.main() n
