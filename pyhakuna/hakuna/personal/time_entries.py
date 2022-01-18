import datetime

from pyhakuna.hakuna.request import Request

TIME_ENTRIES_PATH = "/api/v1/time_entries"


class TimeEntries:
  def __init__(self, h: Request):
    self._hakuna = h

  def list(self, start_date: datetime.date, end_date: datetime.date):
    return self._hakuna.get(TIME_ENTRIES_PATH,
                            {start_date: start_date.isoformat(), end_date: end_date.isoformat()})

  def get(self, id: int):
    return self._hakuna.get(f"{TIME_ENTRIES_PATH}/{id}")

  def new(self, entry: dict):
    return self._hakuna.post(TIME_ENTRIES_PATH, entry)

  def update(self, entry: dict):
    return self._hakuna.patch(TIME_ENTRIES_PATH, entry)

  def delete(self, id: int):
    return self._hakuna.delete(f"{TIME_ENTRIES_PATH}/{id}")
