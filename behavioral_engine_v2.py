
import time
import random
import os
from datetime import datetime

"""
Project: SpectrumShieldOS
Author: Precious Onyekachi
Description:
A behavioral-based security engine that detects anomalous typing
patterns using speed and rhythm analysis to trigger adaptive
protection mechanisms.
"""
# ================== CONFIGURATION ==================
BASELINE_FILE = "baseline_v2.txt"
LOG_FILE = "behavior_log_v2.txt"
high_risk_file = "high_risk_count.txt"
RISK_DECAY_RATE = 1   # How much trust recovers per LOW session
SILENT_MODE = True        # True = no terminal output
STRICT_THRESHOLD = 2      # HIGH risk count before strict mode
high_risk_counter = 0
BASELINE_ADAPT_RATE = 0.05  # 5% slow learning

# ================== UTILITY ==================

def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as log:
        log.write(f"[{timestamp}] {message}\n")

# ================== BASELINE ==================

def learn_baseline():
    print("Learning your normal typing behavior...")
    input("Press Enter when ready to start typing...")
    text = input("Type something and press Enter: ")

    start = time.time()
    input("Press Enter when done typing...")
    end = time.time()

    speed = len(text) / max(end - start, 0.01)

    with open(BASELINE_FILE, "w") as f:
        f.write(str(speed))

    log_event(f"Baseline learned: {speed:.2f} cps")
    return speed

def load_or_create_baseline():
    if not os.path.exists(BASELINE_FILE):
        return learn_baseline()

    with open(BASELINE_FILE, "r") as f:
        return float(f.read())

# ================== BEHAVIOR ==================

def measure_typing_speed():
    input("\nPress Enter when ready to start typing...")
    text = input("Type something and press Enter: ")

    start = time.time()
    input("Press Enter when done typing...")
    end = time.time()

    return len(text) / max(end - start, 0.01)

def assess_risk(speed, baseline_speed, avg_interval):
    if speed <= 0:
        return "HIGH"

    if speed < baseline_speed * 0.6 or avg_interval > 0.6:
        return "HIGH"
    elif speed > baseline_speed * 1.5 or avg_interval < 0.05:
        return "MEDIUM"
    else:
        return "LOW"

def calculate_variance(speed, baseline):
    return abs(speed - baseline) / baseline

def measure_typing_behavior():
    input("Press Enter when ready to start typing...")
    start = time.time()

    text = input("Type something and press Enter: ")

    end = time.time()

    duration = end - start
    if duration <= 0 or len(text) == 0:
        return 0, 0

    speed = len(text) / duration
    avg_interval = duration / len(text)

    return speed, avg_interval

def human_typing():
    return random.uniform(0.08, 0.35)

def bot_typing():
    return 0.01
# ================== SECURITY MODES ==================

def activate_ghost_mode():
    if not SILENT_MODE:
        print("Ghost Mode Activated: behavioral anomaly detected")
        print("user behavioral signals temporarily restricted")
    log_event("Ghost Mode activated")

def adaptive_strict_mode():
    if not SILENT_MODE:
        print("Adaptive Strict Mode ENABLED")
        print("Sensitive actions restricted")
    log_event("Adaptive Strict Mode enabled")

def adaptive_strict_mode(risk):
    # Load previous high-risk count
    if os.path.exists(high_risk_file):
        with open(high_risk_file, "r") as file:
            count = int(file.read())
    else:
        count = 0

    # Update count
    if risk == "HIGH":
        count += 1
    else:
        count = 0

    # Save updated count
    with open(high_risk_file, "w") as file:
        file.write(str(count))

    # Trigger strict mode
    if count >= 2:
        print("Adaptive Strict Mode ENABLED")
        print("Sensitive actions restricted")


def log_session(speed, risk):
    with open("behavior_log.txt", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} | Speed: {speed:.2f} cps | Risk: {risk}\n")

def log_session(speed, risk):
    with open("session_log.txt", "a") as f:
        f.write(f"Speed: {speed:.2f} cps | Risk: {risk}\n")

def explain_risk(speed, baseline):
    deviation = abs(speed - baseline) / baseline * 100
    print(f"Deviation from baseline: {deviation:.1f}%")

def calculate_risk(speed_dev, error_rate, timing_var, burst):
    risk = (
        speed_dev * 0.35 +
        error_rate * 0.25 +
        timing_var * 0.25 +
        burst * 0.15
    )
    return round(min(risk, 100), 2)

def dwell_time(press, release):
    return release - press

def flight_time(prev_release, next_press):
    return next_press - prev_release

# ================== MAIN ENGINE ==================

def main():
    global high_risk_counter
    baseline_speed = load_or_create_baseline()
    print(f"\nBaseline typing speed: {baseline_speed:.2f} cps")

    high_risk_counter = 0

    while True:
        print("\n--- New Session ---")

        speed = measure_typing_speed()
        print(f"Current speed: {speed:.2f} cps")

        risk = assess_risk(speed, baseline_speed)
        explain_risk(speed, baseline_speed)
        if speed <= 0:
         print("Invalid typing data detected")
         continue

        if risk == "HIGH":
            high_risk_counter += 1
            activate_ghost_mode()

           # if high_risk_counter >= STRICT_THRESHOLD:
               # adaptive_strict_mode()

        elif risk == "MEDIUM" and not SILENT_MODE:
            print("Medium risk behavior detected")

        elif risk == "LOW":
          if not SILENT_MODE:
             print("Normal behavior")

        baseline_speed = (
        (1 - BASELINE_ADAPT_RATE) * baseline_speed
        + BASELINE_ADAPT_RATE * speed
        )

        high_risk_counter = 0
    
        if high_risk_counter >= STRICT_THRESHOLD:
                adaptive_strict_mode()
                
        print(f"Risk Level: {risk}")
        log_session(speed, risk)
        #log_event(f"Session speed: {speed:.2f} cps | Risk: {risk}")

        speed, avg_interval = measure_typing_behavior()
        print(f"Speed: {speed:.2f} cps | Avg interval: {avg_interval:.2f}s")

        risk = assess_risk(speed, baseline_speed, avg_interval)

# ================== RUN ==================

if __name__ == "__main__":
    main()
