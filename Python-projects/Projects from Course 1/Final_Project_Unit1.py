def get_event_date(event):
  return event.date

def current_users(events):
  events.sort(key=get_event_date)
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout":
        if event.user in machines[event.machine]: #This line prevents a user to be logged out as the first instruction
            machines[event.machine].remove(event.user)
  return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))

class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user

events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris') #This is the example of a user that has log out as the first instruction
]

users = current_users(events)
print(users)

generate_report(users)

'''
Just to remember

List
list = [1, 2, 3, 4, 5]
- Ordered collection of items
- Allows duplicates
- Mutable (can be changed)


Tuple
Tuple = (1, 2, 3, 4, 5)
- Ordered collection of items
- Allows duplicates
- Immutable (cannot be changed)


Set
Set = {1, 2, 3, 4, 5}
- Unordered collection of unique items
- Does not allow duplicates
- Mutable (can be changed)


Dictionary
Dictionary = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
- Unordered collection of key-value pairs
- Keys must be unique
- Mutable (can be changed)
- Allows fast lookups by key

'''