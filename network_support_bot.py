import time
import sys

def print_bot(message):
    """Simulates a bot typing delay with a visible '. . .' animation."""
    # Start the typing indicator    
    for _ in range(4):
        time.sleep(0.3)
        sys.stdout.write(".")
        sys.stdout.flush()
        
    # Carriage return (\r) goes back to the start of the line, print spaces to clear the dots, then return again to print the message
    sys.stdout.write("\r" + " " * 25 + "\r")
    sys.stdout.flush()
    
    # Print the actual message
    print(f"🤖 Bot: {message}")
    

def get_user_input(prompt_text=""):
    """Handles basic input and empty-string error handling."""
    # The bot types out the question first, if one is provided
    if prompt_text:
        print_bot(prompt_text)
        
    while True:
        try:
            response = input("👤 You: ").strip().lower()
            
            # Error handling: Empty input 
            if not response:
                print_bot("I didn't catch that. Could you please type your answer?") 
                continue
            return response
        # Handle application exit
        except KeyboardInterrupt:
            print("\nExiting chat. Goodbye!")
            sys.exit()

def get_yes_no(prompt_text="Did that fix it? (yes/no)"):
    """Helper function to trap user in a yes/no loop until a valid response is given."""
    print_bot(prompt_text)
    
    while True:
        response = get_user_input()
        
        if response in ["yes", "y", "yeah", "yep"]:
            return True
        elif response in ["no", "n", "nah", "nope"]:
            return False
        else:
            print_bot("Please answer 'yes' or 'no'.")


def troubleshoot_internet():
    print_bot("Welcome to IT Support! I can help you troubleshoot your network connection.")
    
    # Issue categorization
    while True:
        issue = get_user_input("Are you experiencing 'no connection' or 'slow speeds'?")
        
        if "no" in issue or "connection" in issue:
            handle_no_connection()
            break
        elif "slow" in issue or "speed" in issue or "lag" in issue:
            handle_slow_speeds()
            break
        else:
            # Error handling: Unexpected/unrecognized input
            print_bot("I'm sorry, I didn't understand that. Please reply with either 'no connection' or 'slow speeds'.")


def handle_no_connection():
    print_bot("I see you have no connection. Let's check your equipment.")
    while True:
        lights = get_user_input("Look at your router. Are the lights blinking, solid, or off?")

        # Light off sub-branch (No connection)
        if "off" in lights or "no" in lights:
            print_bot("It looks like the router has no power. Please check the power cable and make sure it is seated correctly.")
            if get_yes_no():
                print_bot("Excellent! Glad we could get you back online.")
            else:
                print_bot("Since there's still no power, I'll transfer you to a live agent to assist.")
                print_bot("Transferring you now...")
            break
                
        # Light blinking or yellow sub-branch (Intermediate connection)
        elif "blink" in lights or "yellow" in lights:
            print_bot("The router is trying to connect. Let's perform a power cycle. " \
            "Disconnect the power cable for 30-60 seconds, reconnect it, and wait 2 minutes for the router to fully reconnect.")
            if get_yes_no():
                print_bot("Excellent! Glad we could get you back online.")
            else:
                print_bot("Since a reboot didn't work, I'll escalate this to a live technician for a service check.")
                print_bot("Transferring you now...")
            break
                
        # Light solid or green sub-branch (Solid connection)
        elif "solid" in lights or "green" in lights:
            print_bot("The router shows a solid connection. Please try restarting your device.")
            if get_yes_no():
                print_bot("Excellent! Glad we could get you back online.")
            else:
                print_bot("Since a reboot didn't work, I'll transfer you to a live agent to assist.")
                print_bot("Transferring you now...")
            break
        else:
            print_bot("Please reply with 'blinking', 'solid', or 'off'.")


def handle_slow_speeds():
    print_bot("Slow speeds can be frustrating. Are you connected via Wi-Fi or an Ethernet cable? (wifi/ethernet)")
    while True:
        conn_type = get_user_input("")
        
        if conn_type == "wifi":
            print_bot("Wi-Fi can be prone to interference. Try moving closer to the router or plugging in directly with an Ethernet cable to improve speeds.")
            if get_yes_no():
                print_bot("Great! Glad we got you up to speed.")
            else:
                print_bot("Since that didn't work, I'll transfer you to a live agent to run a speed test.")
                print_bot("Transferring you now...")
            break

        elif conn_type == "ethernet":
            print_bot("Since you are wired in, I'll transfer you to a live agent to run a speed test.")
            print_bot("Transferring you now...")
            break
        else:
            print_bot("I didn't quite get that. Please reply with 'wifi' or 'ethernet'.")


if __name__ == "__main__":
    troubleshoot_internet()