def build_timeline(events):
    print("\n📊 INCIDENT TIMELINE\n")
    for event in events:
        print(f"[{event['time']}] ({event['source']}) - {event['message']}")
