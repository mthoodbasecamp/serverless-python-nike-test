
endpoints:
  POST - https://q9c4gej580.execute-api.us-west-2.amazonaws.com/dev/sports
  
  POST - https://q9c4gej580.execute-api.us-west-2.amazonaws.com/dev/bball
  GET - https://q9c4gej580.execute-api.us-west-2.amazonaws.com/dev/sports
  GET - https://q9c4gej580.execute-api.us-west-2.amazonaws.com/dev/sports/{id}
  PUT - https://q9c4gej580.execute-api.us-west-2.amazonaws.com/dev/sports/{id}
  DELETE - https://q9c4gej580.execute-api.us-west-2.amazonaws.com/dev/sports/{id}
functions:
  create: serverless-rest-api-with-dynamodb-dev-create
  list: serverless-rest-api-with-dynamodb-dev-list
  get: serverless-rest-api-with-dynamodb-dev-get
  update: serverless-rest-api-with-dynamodb-dev-update
  delete: serverless-rest-api-with-dynamodb-dev-delete
