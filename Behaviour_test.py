#import time
#import os
#import keyboard
#from datetime import datetime

#SILENT_MODE = True  # True = stays quiet for LOW/MEDIUM risk, only speaks for HIGH risk

#memory_file = "baseline.txt"
#high_risk_count_file = "high_risk_count.txt"
#log_file_name = "behavior_log.txt"

# === FUNCTIONS ===

#def determine_risk(current_speed, normal_speed):
   # if current_speed < normal_speed * 0.6:
      #  return "HIGH"
    #elif current_speed > normal_speed * 1.5:
       # return "MEDIUM"
    #else:
       # return "LOW"
#def trigger_ghost_mode(risk):
    #if risk == "HIGH":
     #   print("🔐 Risk Level: HIGH")
       # print("👻 Ghost Mode ACTIVATED")
        #print("🔒 Locking sensitive actions...")
        #print("🕶️ User behavior masked for protection")
    #elif risk == "MEDIUM":
     #   print("⚠️ Risk Level: MEDIUM")
    #else:
       # print("✅ Risk Level: LOW")
#def adaptive_strict_mode(risk, high_risk_count_file):
   # if os.path.exists(high_risk_count_file):
       # with open(high_risk_count_file, "r") as f:
           # high_count = int(f.read())
   # else:
       # high_count = 0

   # if risk == "HIGH":
       # high_count += 1
   # else:
      #  high_count = 0

   # with open(high_risk_count_file, "w") as f:
      ##  f.write(str(high_count))

    #if high_count >= 2:
      #  print("🚨 Adaptive Ghost Mode: STRICT MODE ENABLED")
       # print("🔐 Extra protection activated due to repeated anomalies")
#def adaptive_learning(log_file_name, memory_file, normal_speed):
   # recent_speeds = []

    #if os.path.exists(log_file_name):
       # with open(log_file_name, "r") as log:
           # lines = log.readlines()[-5:]  # last 5 sessions

        #for line in lines:
           # try:
              #  speed = float(line.split("Speed:")[1].split("cps")[0])
               # recent_speeds.append(speed)
            #except:
              #  pass

   # if recent_speeds:
       # average_recent_speed = sum(recent_speeds) / len(recent_speeds)
       # normal_speed = (normal_speed * 0.95) + (average_recent_speed * 0.05)

        #with open(memory_file, "w") as file:
          #  file.write(str(normal_speed))

       # print(f"🧠 Adaptive learning updated baseline: {normal_speed:.2f} cps")
   # return normal_speed
#def log_behavior(log_file_name, risk, current_speed):
   # timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   # ghost_state = "ON" if risk == "HIGH" else "OFF"

   # with open(log_file_name, "a") as log_file:
      #  log_file.write(
         #   f"{timestamp} | Risk: {risk} | Speed: {current_speed:.2f} cps | GhostMode: {ghost_state}\n"
       # )
#def advanced_ghost_mode(current_speed, normal_speed, high_risk_count_file):
  #  risk = determine_risk(current_speed, normal_speed)
    
    #if risk == "HIGH":
       # print("[HIGH RISK] Ghost Mode ACTIVATED")
       # print("👻 Ghost Mode ACTIVATED")
       # print("🔒 Locking sensitive actions...")
      #  print("🕶️ User behavior masked for protection")
   # else:
       # if not SILENT_MODE:
           # if risk == "LOW":
              #  print("✅ Risk Level: LOW")
           # elif risk == "MEDIUM":
              #  print("⚠️ Risk Level: MEDIUM")
    
   # return risk

    # Track repeated HIGH risk
   # if os.path.exists(high_risk_count_file):
        #with open(high_risk_count_file, "r") as f:
           # high_count = int(f.read())
   # else:
       # high_count = 0

   # if risk == "HIGH":
       # high_count += 1
    #else:
        #high_count = 0

    #with open(high_risk_count_file, "w") as f:
       # f.write(str(high_count))

    #if high_count >= 2 and risk == "HIGH":
       # print("🚨 Adaptive Ghost Mode: STRICT MODE ENABLED")
       # print("🔐 Extra protection activated due to repeated anomalies")

#    return risk
#def measure_typing_speed(prompt_text="Type anything: "):
   # print(prompt_text)
  #  input("Press Enter when ready...")

   # typed_chars = []
   # start_time = None

   # print("Start typing now...")
   duration = end - start

    if duration < 1:
        print("[INFO] Typing duration too short")
        return None

    return len(text) / duration


  #  while True:
       # event = keyboard.read_event()
        #if event.event_type == keyboard.KEY_DOWN:
            #if start_time is None:
             #   start_time = time.time()  # start timer on first key
            #if event.name == "enter":
           #     break
            #elif len(event.name) == 1:  # count normal characters only
                #typed_chars.append(event.name)

   # end_time = time.time()
    #duration = max(end_time - start_time, 0.01)  # prevent division by zero
    #cps = len(typed_chars) / duration
   # return cps

import time
import os
from datetime import datetime

# --- Configuration ---
memory_file = "baseline.txt"
high_risk_count_file = "high_risk_count.txt"
log_file_name = "behavior_log.txt"
TEST_MODE = True      # True = dev/testing, False = production
SILENT_MODE = False  # Set True to hide messages for stealth

# --- Functions ---

#def measure_typing_speed():
    #"""Measure typing speed in characters per second"""
   # text = input("Type something and press Enter: ")
   # start = time.time()
   # input("Press Enter when done typing...")
   # end = time.time()
   # if end - start == 0:
     #   return 0
   # return len(text) / (end - start)
def measure_typing_speed():
    text = input("Type normally and press Enter: ")
    start = time.time()
    input("Press Enter when done typing...")
    end = time.time()
    return len(text) / max(end - start, 0.01)

#def determine_risk(current_speed, normal_speed):
 #   """Determine typing risk level based on baseline"""
  #  if current_speed < normal_speed * 0.6:
   #     return "HIGH"
   # elif current_speed > normal_speed * 1.5:
    #    return "MEDIUM"
   # else:
     #   return "LOW"
def determine_risk(current_speed, normal_speed):
    if current_speed < normal_speed * 0.6:
        return "HIGH"
    elif current_speed > normal_speed * 1.5:
        return "MEDIUM"
    else:
        return "LOW"

#def advanced_ghost_mode(current_speed, normal_speed, high_risk_count_file):
#    """Trigger Ghost Mode actions based on risk"""
 #   risk = determine_risk(current_speed, normal_speed)

  #  if risk == "HIGH":
   #     print("Risk Level: HIGH")
    #    print("Ghost Mode ACTIVATED")
     #   print("Locking sensitive actions...")
      #  print("User behavior masked for protection")
    #elif risk == "MEDIUM" and not SILENT_MODE:
     #   print("Risk Level: MEDIUM")
    #elif risk == "LOW" and not SILENT_MODE:
     #   print("Risk Level: LOW")

    # Track repeated HIGH risk
    #if os.path.exists(high_risk_count_file):
     #   with open(high_risk_count_file, "r") as f:
      #      high_count = int(f.read())
    #else:
     #   high_count = 0

    #if risk == "HIGH":
     #   high_count += 1
    #else:
     #   high_count = 0

    #with open(high_risk_count_file, "w") as f:
        f.write(str(high_count))

   # if high_count >= 2 and risk == "HIGH":
    #    print("Adaptive Ghost Mode: STRICT MODE ENABLED")
     #   print("Extra protection activated due to repeated anomalies")

    #return risk
def advanced_ghost_mode(current_speed, normal_speed):
    risk = determine_risk(current_speed, normal_speed)

    if risk == "HIGH":
        print("Risk Level: HIGH")
        print("Ghost Mode ACTIVATED")
        print("Locking sensitive actions")
        print("User behavior masked")
    elif risk == "MEDIUM" and not SILENT_MODE:
        print("Risk Level: MEDIUM")
    elif risk == "LOW" and not SILENT_MODE:
        print("Risk Level: LOW")

    return risk

def adaptive_learning(log_file_name, memory_file, normal_speed):
    """Update baseline speed based on current session"""
    # Save baseline speed to memory
    with open(memory_file, "w") as f:
        f.write(str(normal_speed))

    # Log session
    with open(log_file_name, "a") as f:
        f.write(f"{datetime.now()} - Baseline: {normal_speed:.2f} cps\n")

    return normal_speed

def load_or_learn_baseline(memory_file):
    """Load or calculate normal typing speed"""
    if os.path.exists(memory_file):
        with open(memory_file, "r") as f:
            baseline = float(f.read())
        print(f"Loaded baseline typing speed: {baseline:.2f} cps")
    else:
        print("Learning baseline typing speed...")
        text = input("Type anything and press Enter: ")
        start = time.time()
        input("Press Enter when done typing...")
        end = time.time()
        baseline = len(text) / max(end - start, 0.01)
        with open(memory_file, "w") as f:
            f.write(str(baseline))
        print(f"Baseline saved: {baseline:.2f} cps")
    return baseline

# --- MAIN PROGRAM ---

#normal_speed = load_or_learn_baseline(memory_file)

#while True:
   # print("\nStart typing now...")
    #current_speed = measure_typing_speed()
    #print(f"Your actual typing speed: {current_speed:.2f} cps")

    #risk = advanced_ghost_mode(current_speed, normal_speed, high_risk_count_file)
   # normal_speed = adaptive_learning(log_file_name, memory_file, normal_speed)

    
# STEP 1: Learn or load normal typing speed
if os.path.exists(memory_file):
    with open(memory_file, "r") as file:
        normal_speed = float(file.read())
    print(f"Baby, I remember your normal typing speed: {normal_speed:.2f} cps 💛")
else:
    print("Baby, let's learn your normal typing speed 💛")
    input("Press Enter and start typing normally...")

    start = time.time()
    text = input("Type anything you like: ")
    end = time.time()

    normal_speed = len(text) / (end - start)

    with open(memory_file, "w") as file:
        file.write(str(normal_speed))

    print(f"\nSaved your normal typing speed: {normal_speed:.2f} cps 💾")
while True:
    # Step 1: Measure typing speed
    current_speed = measure_typing_speed()
    print(f"\nYour actual typing speed: {current_speed:.2f} cps")

    # Optional test mode
    test_high_risk = input("Do you want to force HIGH risk for testing? (y/n): ").lower()
    if test_high_risk == "y":
        current_speed = normal_speed * 0.5
        print(f"[TEST MODE] Forced HIGH risk speed: {current_speed:.2f} cps")


# STEP 2: Check current state
# === STEP 2: Typing check with automatic loop ===
print("\nNow let's start the typing tracker 😌")
print("Press Ctrl+C anytime to stop.\n")

while True:
    # Prompt to start
    input("Press Enter when you are READY to type...")

    # Get real typing input
    text = input("Type anything and press Enter: ")

    # Ignore empty input
    if len(text.strip()) == 0:
        print("⚠️ You didn’t type anything. Try again.\n")
        continue

    # Start timing after user starts typing
    start = time.time()
    # Since user already typed, end is almost same
    end = time.time()

    # Calculate typing speed safely
    current_speed = len(text) / max((end - start), 0.01)
    print(f"\nYour actual typing speed: {current_speed:.2f} cps")

    # Optional test mode
    test_high_risk = input("Do you want to force HIGH risk for testing? (y/n): ").lower()
    if test_high_risk == "y":
        current_speed = normal_speed * 0.5
        print(f"[TEST MODE] Forced HIGH risk speed: {current_speed:.2f} cps")

    # Advanced Ghost Mode
    risk = advanced_ghost_mode(current_speed, normal_speed, high_risk_count_file)

    # Adaptive learning updates baseline
    normal_speed = adaptive_learning(log_file_name, memory_file, normal_speed)

    print("\n--- Session logged ✅ ---\n")

# STEP 3: Compare
if current_speed < normal_speed * 0.7:
    risk = "HIGH"
elif current_speed > normal_speed * 1.3:
    risk = "MEDIUM"
else:
    risk = "LOW"

print(f"\n🔐 Risk Level: {risk}")
if risk == "HIGH":
    print("👻 Ghost Mode ACTIVATED")
    print("🔒 Locking sensitive actions...")
    print("🕶️ User behavior masked for protection")
else:
    print("✅ Ghost Mode inactive — system stable")

# LOGGING
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

ghost_state = "ON" if risk == "HIGH" else "OFF"

with open("behavior_log.txt", "a") as log_file:
    log_file.write(
        f"{timestamp} | Risk: {risk} | Speed: {current_speed:.2f} cps | GhostMode: {ghost_state}\n"
    )


# Adaptive Ghost Mode Memory
if os.path.exists(high_risk_count_file):
    with open(high_risk_count_file, "r") as f:
        high_count = int(f.read())
else:
    high_count = 0

if risk == "HIGH":
    high_count += 1
else:
    high_count = 0  # reset if behavior returns to normal

with open(high_risk_count_file, "w") as f:
    f.write(str(high_count))

if high_count >= 2:
    print("🚨 Adaptive Ghost Mode: STRICT MODE ENABLED")
    print("🔐 Extra protection activated due to repeated anomalies")

# === BEHAVIOR INTELLIGENCE ===
recent_speeds = []

if os.path.exists(log_file_name):
    with open(log_file_name, "r") as log:
        lines = log.readlines()[-5:]  # last 5 sessions only

    for line in lines:
        try:
            speed = float(line.split("Speed:")[1].split("cps")[0])
            recent_speeds.append(speed)
        except:
            pass

if recent_speeds:
    average_recent_speed = sum(recent_speeds) / len(recent_speeds)

    # Gentle learning (5% adjustment)
    normal_speed = (normal_speed * 0.95) + (average_recent_speed * 0.05)

    with open(memory_file, "w") as file:
        file.write(str(normal_speed))

    print(f"🧠 Adaptive learning updated baseline: {normal_speed:.2f} cps")



import time
import os
from datetime import datetime

# ================= CONFIG =================
BASELINE_FILE = "baseline.txt"
RISK_COUNT_FILE = "high_risk_count.txt"
LOG_FILE = "behavior_log.txt"

SILENT_MODE = False

# ================= CORE FUNCTIONS =================

def measure_typing_speed():
    start = time.time()
    text = input("Type something and press Enter:\n")
    end = time.time()

    duration = end - start
    if duration <= 0:
        return 0.0

    return len(text) / duration


def determine_risk(current_speed, normal_speed):
    if current_speed < normal_speed * 0.6:
        return "HIGH"
    elif current_speed > normal_speed * 1.5:
        return "MEDIUM"
    else:
        return "LOW"


def log_behavior(speed, risk):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} | {speed:.2f} cps | {risk}\n")


def adaptive_strict_mode(risk):
    count = 0

    if os.path.exists(RISK_COUNT_FILE):
        with open(RISK_COUNT_FILE, "r") as f:
            count = int(f.read())

    if risk == "HIGH":
        count += 1
    else:
        count = max(count - 1, 0)

    with open(RISK_COUNT_FILE, "w") as f:
        f.write(str(count))

    if count >= 3:
        print("⚠ Adaptive Strict Mode ENABLED")
        print("Sensitive actions restricted")


def trigger_ghost_mode(risk):
    if risk == "HIGH":
        print("👻 Ghost Mode Activated")
        print("Behavioral signals masked")


def behavioral_response(current_speed, normal_speed):
    risk = determine_risk(current_speed, normal_speed)

    trigger_ghost_mode(risk)
    adaptive_strict_mode(risk)
    log_behavior(current_speed, risk)

    if not SILENT_MODE:
        print(f"Risk Level: {risk}")

# ================= BASELINE HANDLING =================

def load_or_create_baseline():
    if os.path.exists(BASELINE_FILE):
        with open(BASELINE_FILE, "r") as f:
            return float(f.read())

    print("Creating baseline typing profile...")
    speed = measure_typing_speed()

    with open(BASELINE_FILE, "w") as f:
        f.write(str(speed))

    return speed

# ================= MAIN LOOP =================

def main():
    normal_speed = load_or_create_baseline()
    print(f"Baseline typing speed: {normal_speed:.2f} cps")

    while True:
        print("\n--- New Session ---")
        current_speed = measure_typing_speed()
        print(f"Current speed: {current_speed:.2f} cps")

        behavioral_response(current_speed, normal_speed)
        time.sleep(1)

if __name__ == "__main__":
    main()







