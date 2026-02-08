from engine.event_store import EventStore
from engine.timeline import build_timeline
from engine.recommendation_engine import recommend_action
from engine.k8s_event_collector import collect_k8s_events

store = EventStore()

k8s_events = collect_k8s_events()
for event in k8s_events:
    store.add_event(event["source"], event["message"])

events = store.get_events()

build_timeline(events)

recommendation = recommend_action(events)

print("\n🧠 INCIDENT RECOMMENDATION\n")
print(f"Likely Cause   : {recommendation['cause']}")
print(f"Confidence     : {recommendation['confidence']}")
print(f"Action         : {recommendation['action']}")
