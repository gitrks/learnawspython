import boto3
import json
import decimal

# wget https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/samples/moviedata.zip
#  load and unzip moviedata.zip

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

table = dynamodb.Table('Movies')

with open("moviedata.json") as json_file:
    movies = json.load(json_file, parse_float=decimal.Decimal)
    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        info = movie['info']

        print("Adding movie:", year, title)

        table.put_item(
            Item={
                'year': year,
                'title': title,
                'info': info,
            }
        )
