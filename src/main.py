print("AI-Adaptive-Aero-F1 System Initialized")
from sensors import get_sensor_data
from ai_engine import decide_adjustments
from controller import apply_adjustments

def run_system():
    print("Starting AI-Adaptive-Aero-F1 System...")
    sensor_data = get_sensor_data()
    decisions = decide_adjustments(sensor_data)
    apply_adjustments(decisions)

if __name__ == "__main__":
    run_system()
