from datetime import datetime

class EventStore:
    def __init__(self):
        self.events = []

    def add_event(self, source, message):
        event = {
            "time": datetime.utcnow().isoformat(),
            "source": source,
            "message": message
        }
        self.events.append(event)

    def get_events(self):
        return sorted(self.events, key=lambda e: e["time"])
