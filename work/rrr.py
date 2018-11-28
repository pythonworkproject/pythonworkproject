import requests
my_domain = 'pythonwork.pythonanywhere.com'
username = 'pythonwork'
token = 'b1efc1580770aacc67d83999b17fa27d4cea95d7'

response = requests.post(
  'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain}/reload/'.format(
      username=username, domain=my_domain
  ),
  headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
  print('All OK')
else:
  print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))