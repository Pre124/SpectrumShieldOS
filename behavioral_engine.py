import time
import os

# ================= CONFIG =================
BASELINE_FILE = "baseline.txt"
SESSION_LOG = "session_log.txt"

SILENT_MODE = False        # True = stealth mode
STRICT_THRESHOLD = 2       # HIGH risk count before strict mode
high_risk_counter = 0

# ================= CORE FUNCTIONS =================

def measure_typing_speed():
    input("\nPress Enter when ready to start typing...")
    start = time.time()
    text = input("Type something and press Enter: ")
    input("Press Enter when done typing...")
    end = time.time()

    if end - start == 0:
        return 0
    return len(text) / (end - start)


def load_or_create_baseline():
    if os.path.exists(BASELINE_FILE):
        with open(BASELINE_FILE, "r") as f:
            return float(f.read())

    print("Learning your normal typing behavior...")
    speed = measure_typing_speed()

    with open(BASELINE_FILE, "w") as f:
        f.write(str(speed))

    return speed


def calculate_variance(speed, baseline):
    return abs(speed - baseline) / baseline


def assess_risk(speed, baseline):
    variance = calculate_variance(speed, baseline)

    if variance > 1.5:
        return "HIGH"
    elif variance > 0.6:
        return "MEDIUM"
    else:
        return "LOW"


def activate_ghost_mode():
    if not SILENT_MODE:
        print("👻 Ghost Mode Activated")
        print("Behavioral signals masked")


def adaptive_strict_mode():
    if not SILENT_MODE:
        print("⚠ Adaptive Strict Mode ENABLED")
        print("Sensitive actions restricted")


def log_session(speed, risk):
    with open(SESSION_LOG, "a") as f:
        f.write(f"Speed: {speed:.2f} cps | Risk: {risk}\n")

# ================= MAIN LOOP =================

def main():
    global high_risk_counter

    baseline_speed = load_or_create_baseline()
    print(f"\nBaseline typing speed: {baseline_speed:.2f} cps")

    while True:
        print("\n--- New Session ---")

        speed = measure_typing_speed()
        print(f"Current speed: {speed:.2f} cps")

        risk = assess_risk(speed, baseline_speed)

        if risk == "HIGH":
            high_risk_counter += 1
            activate_ghost_mode()

            if high_risk_counter >= STRICT_THRESHOLD:
                adaptive_strict_mode()

        elif risk == "MEDIUM" and not SILENT_MODE:
            print("⚠ Medium risk behavior detected")

        elif risk == "LOW":
            if not SILENT_MODE:
                print("✅ Normal behavior")
            high_risk_counter = 0

        print(f"Risk Level: {risk}")
        log_session(speed, risk)

# ================= ENTRY =================

if __name__ == "__main__":
    main()
