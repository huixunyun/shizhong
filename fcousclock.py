import requests
import time

def focus_timer(minutes):
    print(f"GitHub-focused timer started for {minutes} minutes.")
    time.sleep(minutes * 60)  # Sleep for the specified minutes
    print("Time's up! Commit your work to GitHub.")

# Example: Start a 25-minute GitHub-focused timer
focus_timer(25)
