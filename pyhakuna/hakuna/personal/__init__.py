from pyhakuna.hakuna.request import Request
from .absences import Absences
from .overview import Overview
from .time_entries import TimeEntries
from .timer import Timer
from .users import Users


class Personal:
  def __init__(self, h: Request):
    self._overview = Overview(h)
    self._timer = Timer(h)
    self._users = Users(h)
    self._time_entries = TimeEntries(h)
    self._absences = Absences(h)

  def overview(self):
    return self._overview

  def timer(self):
    return self._timer

  def time_entries(self):
    return self._time_entries

  def users(self):
    return self._users

  def absences(self):
    return self._absences
