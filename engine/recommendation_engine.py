def recommend_action(events):
    recommendation = {
        "cause": "Unknown",
        "confidence": "Low",
        "action": "Manual investigation required"
    }

    # Look for common failure patterns
    for event in events:
        msg = event["message"].lower()

        if "oom" in msg or "memory" in msg:
            recommendation["cause"] = "Infrastructure change"
            recommendation["confidence"] = "High"
            recommendation["action"] = "Rollback recent infrastructure changes or increase memory limits"

        elif "crashloop" in msg:
            recommendation["cause"] = "Application startup failure"
            recommendation["confidence"] = "Medium"
            recommendation["action"] = "Rollback application deployment and inspect startup logs"

        elif "deploy" in msg and "failed" in msg:
            recommendation["cause"] = "Deployment issue"
            recommendation["confidence"] = "Medium"
            recommendation["action"] = "Retry deployment or rollback to last stable version"

    return recommendation
