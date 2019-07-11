from chalice import Chalice

app = Chalice(app_name='hello-world')


@app.route('/')
def index():
    return {'hello': 'world'}


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
@app.route('/hello/{name}')
def hello_name(name):
    # '/hello/james' -> {"hello": "james"}
    return {'hello': name}

@app.route('/roll', methods = ['POST'], content_types=['application/x-www-form-urlencoded'])
def roll():
  # You can access the text the user typed after the command here:
  from urllib.parse import parse_qs
  params = parse_qs(app.current_request.raw_body.decode())
  user_text = params['text']
  return { 'response_type': 'in_channel', 'text': user_text }


@app.route('/hello-there', methods = ['POST'], content_types=['application/x-www-form-urlencoded'])
def hello_there():
   # You can access the text the user typed after the command here:
   #from urllib.parse import parse_qs
   #params = parse_qs(app.current_request.raw_body.decode())
   #user_text = params['text']
   return {
      'response_type': 'in_channel',
      'text': '<https://youtu.be/frszEJb0aOo|General Kenobi!>'
   }

# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
