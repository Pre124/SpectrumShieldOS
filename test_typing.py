import time

print("\n--- Typing Speed Test ---\n")

while True:
    input("Press ENTER, then type a sentence and press ENTER again...")

    start = time.time()
    text = input()
    end = time.time()

    if text.strip() == "":
        print("No typing detected. Try again.")
        continue

    speed = len(text) / (end - start)
    print(f"Typing speed: {speed:.2f} cps\n")
