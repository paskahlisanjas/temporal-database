from datetime import datetime

class ValidInterval:
    def __init__(self, start, finish):
        if isinstance(start, str):
            self.start = datetime.strptime(start, '%Y-%m-%d')
        else:
            self.start = start

        if isinstance(finish, str):
            self.finish = datetime.strptime(finish, '%Y-%m-%d')
        else:
            self.finish = finish

def is_before(x,y):
    return (x.start < y.start
        and x.start < y.finish
        and x.finish < y.start
        and x.finish < y.finish)

def is_after(x,y):
    return is_before(y,x)

def is_equals(x,y):
    return (x.start == y.start
        and x.start < x.finish
        and x.finish > y.start
        and x.finish == y.finish
    )

def is_during(x,y):
  return (x.start >= y.start
        and x.start < x.finish
        and x.finish > y.start
        and x.finish <= y.finish
    )

def is_contains(x,y):
    return is_during(y,x)
  )

def is_starts(x,y):
  return (x.start == y.start
        and x.start < x.finish
        and x.finish > y.start
        and x.finish < y.finish
  )


def is_started_by(x,y):
  return is_starts(y,x)

def is_finishes(x,y):
    return (x.valid_from > y.valid_from
        and x.valid_from < y.valid_to
        and x.valid_to > y.valid_from
        and x.valid_to == y.valid_to)
  )

def finished_by(x,y):
    return is_finishes(y,x)
  }