# ------------------ LOGIC ------------------

def predict_engagement(time, hashtags, post_type, duration):
    if hashtags > 10 and post_type == "reel":
        return "High Engagement"
    elif time == "evening" and duration > 15:
        return "High Engagement"
    else:
        return "Low Engagement"


def explain_prediction(time, hashtags, post_type, duration):
    if hashtags > 10 and post_type == "reel":
        return "Reels with many hashtags usually reach more audience."
    elif time == "evening" and duration > 15:
        return "Evening posts with longer duration perform better."
    else:
        return "This combination is less optimal for engagement."


def engagement_score(hashtags, duration):
    return min((hashtags * 2) + (duration * 0.5), 100)


def suggest_improvement(time, hashtags, post_type, duration):
    suggestions = []
    if hashtags < 8:
        suggestions.append("Use more hashtags for better reach.")
    if post_type != "reel":
        suggestions.append("Reels generally perform better.")
    if time != "evening":
        suggestions.append("Try posting in the evening.")
    if duration < 15:
        suggestions.append("Increase content duration.")
    return suggestions


def why_not_high(time, hashtags, post_type, duration):
    reasons = []
    if hashtags <= 10:
        reasons.append("Hashtags are too low.")
    if post_type != "reel":
        reasons.append("Reels perform better.")
    if time != "evening":
        reasons.append("Not posted at peak time.")
    if duration <= 15:
        reasons.append("Duration is too short.")
    return reasons


def auto_optimize(time, hashtags, post_type, duration):
    return {
        "time": "evening",
        "hashtags": max(hashtags, 12),
        "post_type": "reel",
        "duration": max(duration, 20)
    }