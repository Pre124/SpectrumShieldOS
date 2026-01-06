
import time
import random
import sys
import statistics

"""
#Project: SpectrumShieldOS
#Author: Precious Onyekachi
#Description:
#Behavioral-based security engine detecting anomalous typing patterns.
#Includes BOT simulation, keystroke dynamics, risk scoring, and adaptive protections.
"""
LOG_FILE = "session_log.txt"

session_speeds = []
session_risks = []
MAX_HISTORY = 10

# =========================
# Keystroke Dynamics
# =========================

def capture_real_keystrokes():
    print("\n--- Typing Speed Test ---")
    print("Press ENTER, then type a sentence and press ENTER again...\n")

    input()  # Wait for user to press Enter

    text = input("Start typing: ")

    if len(text.strip()) == 0:
        return None, None, None

    start_time = time.time()
    end_time = time.time()

    duration = max(end_time - start_time, 0.1)

    speed = len(text) / duration
    avg_interval = duration / max(len(text), 1)

    return speed, avg_interval, text

def capture_typing():
    print("\n--- Typing Speed Test ---")
    print("Press ENTER, then type a sentence and press ENTER again...\n")

    input("Press ENTER to start...")
    start_time = time.time()

    text = input("Type here: ")

    end_time = time.time()
    duration = end_time - start_time

    if len(text.strip()) == 0 or duration == 0:
        return None, None, None

    speed = len(text) / duration  # characters per second

    # Simulated keystroke intervals (real capture comes later)
    intervals = [random.uniform(0.05, 0.25) for _ in text]

    avg_interval = statistics.mean(intervals)
    interval_std = statistics.stdev(intervals) if len(intervals) > 1 else 0

    return speed, avg_interval, interval_std, text, 


# =========================
# Bot Simulation
# =========================
"""
def simulate_bot_typing():
    speed = random.uniform(7.5, 12.0)  # bots are fast
    avg_interval = random.uniform(0.01, 0.04)
    return speed, avg_interval
"""
"""
def simulate_bot_typing():
    speed = random.uniform(3.0, 10.0)
    avg_interval = random.uniform(0.05, 0.25)
    return speed, avg_interval, "[BOT INPUT]"
"""
def simulate_bot_typing():
    speed = random.uniform(3.0, 10.0)
    avg_interval = random.uniform(0.01, 0.04)   # bots are very consistent
    interval_std = random.uniform(0.001, 0.01)  # extremely low variance
    return speed, avg_interval, interval_std, "[BOT INPUT]"



# =========================
# Risk Assessment
# =========================

def assess_risk(speed, baseline_speed, avg_interval, interval_std):
    risk = 0

    if speed > baseline_speed * 2:
        risk += 40

    if avg_interval < 0.05:
        risk += 40

    if speed > 10:
        risk += 20

    if interval_std < 0.01:
        risk += 30

    return min(risk, 100)

def show_risk_trend():
    print("Risk trend tracking coming soon...")
   

# =========================
# Baseline Calibration
# =========================

def calibrate_user():
    print("\n--- Baseline Calibration ---")
    print("Type naturally. This sets your normal behavior.\n")

    speed, avg_interval, interval_std, _ = capture_typing()

    if speed is None:
        print("Calibration failed. Try again.")
        return calibrate_user()

    print(f"\nBaseline speed saved: {speed:.2f} cps")
    return speed


def replay_last_attack():
    if not session_speeds or not session_risks:
        print("No session data to replay.")
        return

    print("\n--- ATTACK REPLAY ---")
    for i in range(len(session_speeds)):
        print(
            f"Session {i+1}: "
            f"Speed={session_speeds[i]:.2f} cps | "
            f"Risk={session_risks[i]}%"
        )

def log_session(speed, avg_interval, risk, is_bot):
    with open(LOG_FILE, "a") as f:
        f.write(
            f"Speed: {speed:.2f} cps | "
            f"Avg Interval: {avg_interval:.3f}s | "
            f"Risk: {risk}% | "
            f"Bot Mode: {is_bot}\n"
        )

# =========================
# MAIN PROGRAM
# =========================

def main():
    print("SpectrumShield Behavioral Engine\n")

    bot_choice = input("Simulate bot typing? (y/n): ").lower().strip()
    simulate_bot = bot_choice == "y"

    baseline_speed = calibrate_user()

    while True:
        print("\n--- New Session ---")

        if simulate_bot:
            speed, avg_interval, interval_std, text = simulate_bot_typing()
            print(f"(BOT simulation) Speed: {speed:.2f} cps")

        else:
            speed, avg_interval, interval_std, text = capture_typing()

            if speed is None:
                print("No typing detected. Try again.")
                continue

            print(f"Typing speed: {speed:.2f} cps")
            print(f"Average keystroke interval: {avg_interval:.3f}s")

        risk = assess_risk(speed, baseline_speed, avg_interval, interval_std)

        # Store session history
        session_speeds.append(speed)
        session_risks.append(risk)

        if len(session_speeds) > MAX_HISTORY:
           session_speeds.pop(0)
           session_risks.pop(0)

        if len(session_risks) >= 3:
           avg_risk = sum(session_risks) / len(session_risks)
           print(f"Average Risk (last {len(session_risks)} sessions): {avg_risk:.1f}%")

        print(f"\n Risk Score: {risk}%")

        human_confidence = max(0, 100 - risk)
        print(f"Human Confidence: {human_confidence}%")

        if human_confidence >= 80:
            print("Strong Human Behavior")
        elif human_confidence >= 50:
            print("Medium Confidence Human")
        else:
            print("Low Confidence (Possible Bot)")

        if risk >= 70:
            replay_last_attack()

        log_session(speed, avg_interval, risk, simulate_bot)

       # mimic_bot = detect_bot_mimic(intervals)

        #if mimic_bot:
           # print("Advanced bot mimic behavior detected")
            #risk = min(risk + 20, 100)

        # Adaptive baseline learning (Human + Medium risk)
        if risk < 70:
            learning_rate = 0.05  # slow and safe adaptation
            baseline_speed = (baseline_speed * (1 - learning_rate)) + (speed * learning_rate)

            print(f"Baseline updated → {baseline_speed:.2f} cps")
        else:
            print("Baseline locked (suspicious behavior)")
        if risk >= 70:
            print("Likely BOT behavior detected")
        else:
            print("Human behavior confirmed")

        show_risk_trend()
        again = input("\nTest again? (y/n): ").lower().strip()
        if again != "y":
            print("\nSession ended. Stay secure")
            break


# =========================
# ENTRY POINT
# =========================

if __name__ == "__main__":
    main()
