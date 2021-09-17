

from flask import Flask
from flask import request
from flask import jsonify
from utils import search as srch

search_util = srch.SearchUtil()

app = Flask(__name__)


@app.route('/')
def display_default():
  return 'Welcome to the semantic search app!\n' \
         'use /search?query=<your_query> to start searching to articles'


@app.route('/readiness_check')
def check_readiness():
  return 'App is ready!'


@app.route('/search', methods=['GET'])
def search():
  try:
    query = request.args.get('query')
    show = request.args.get('show')
    show = '10' if show is None else show

    is_valid, error = validate_request(query, show)

    if not is_valid:
      results = error
    else:
      results = search_util.search(query, int(show))

  except Exception as error:
    results = 'Unexpected error: {}'.format(error)

  response = jsonify(results)
  return response


def validate_request(query, show):
  is_valid = True
  error = ''

  if query is None or len(query) < 3:
    is_valid = False
    error = 'Your search query is too short!'
  elif show is None or not show.isdigit():
    is_valid = False
    error = 'Invalid show results value!'

  return is_valid, error


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8080, debug=True)
