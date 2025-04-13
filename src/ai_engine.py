def decide_adjustments(sensor_data):
    # Very basic logic — replace with ML model later
    decisions = {}
    if sensor_data["cornering"]:
        decisions["rear_wing_angle"] = "high"
    else:
        decisions["rear_wing_angle"] = "low"

    return decisions
