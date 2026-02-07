from engine.event_store import EventStore
from engine.timeline import build_timeline

store = EventStore()

# Simulating real DevOps events
store.add_event("git", "New commit pushed to main branch")
store.add_event("jenkins", "Pipeline build #42 succeeded")
store.add_event("terraform", "Memory limit changed from 512MB to 256MB")
store.add_event("kubernetes", "Pods started restarting (OOMKilled)")

events = store.get_events()
build_timeline(events)
