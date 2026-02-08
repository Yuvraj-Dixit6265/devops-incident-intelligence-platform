from engine.event_store import EventStore
from engine.timeline import build_timeline
from engine.recommendation_engine import recommend_action

store = EventStore()

# Simulated DevOps events
store.add_event("git", "New commit pushed to main branch")
store.add_event("jenkins", "Pipeline build #42 succeeded")
store.add_event("terraform", "Memory limit changed from 512MB to 256MB")
store.add_event("kubernetes", "Pods started restarting (OOMKilled)")

events = store.get_events()

# Show timeline
build_timeline(events)

# Get recommendation
recommendation = recommend_action(events)

print("\n🧠 INCIDENT RECOMMENDATION\n")
print(f"Likely Cause   : {recommendation['cause']}")
print(f"Confidence     : {recommendation['confidence']}")
print(f"Action         : {recommendation['action']}")
