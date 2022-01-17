from pyhakuna.hakuna.request import Request
from .overview import Overview
from .timer import Timer
from .users import Users


class Personal:
  def __init__(self, h: Request):
    self._overview = Overview(h)
    self._timer = Timer(h)
    self._users = Users(h)

  def overview(self):
    return self._overview

  def timer(self):
    return self._timer

  def users(self):
    return self._users
