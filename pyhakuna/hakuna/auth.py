from requests.auth import AuthBase


class HakunaAuth(AuthBase):
  def __init__(self, token):
    self.token = token

  def __call__(self, r):
    r.headers['X-Auth-Token'] = self.token
    return r
