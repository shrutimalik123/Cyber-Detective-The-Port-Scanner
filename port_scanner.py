import random

def port_scanner_game():
    # 1. Setup the "Server"
    target_port = random.randint(1, 100)
    attempts = 7
    found = False

    print("--- 🖥️ CYBER-DETECTIVE: PORT SCANNER 🖥️ ---")
    print("A server has one open port between 1 and 100.")
    print("Identify it before the Firewall locks you out!")

    # 2. Game Loop
    while attempts > 0 and not found:
        print(f"\nFirewall Lockdown in: {attempts} attempts")
        print("Enter a range to scan (e.g., '1-50') or a single port (e.g., '80'):")
        
        user_input = input("Scan Command: ").strip()

        # 3. Parsing Logic
        try:
            if "-" in user_input:
                # Range Scan
                start, end = map(int, user_input.split("-"))
                if start <= target_port <= end:
                    print(f"📡 SIGNAL FOUND: Port {target_port} is within {start}-{end}!")
                else:
                    print(f"🔕 SILENCE: Port is NOT within {start}-{end}.")
            else:
                # Single Port Attempt
                guess = int(user_input)
                if guess == target_port:
                    print(f"🔓 ACCESS GRANTED! Port {target_port} is open. System breached!")
                    found = True
                else:
                    print(f"❌ CLOSED: Port {guess} is unresponsive.")
            
            attempts -= 1

        except ValueError:
            print("⚠️ INVALID INPUT: Use numbers or the 'start-end' format.")

    # 4. End State
    if not found:
        print(f"\n🚫 ACCESS DENIED: The Firewall has locked you out. The port was {target_port}.")

port_scanner_game()
