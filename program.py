import pyautogui
import time
import pyperclip
import google.generativeai as genai

genai.configure(api_key="AIzaSyB7g07gML59K_QbJI7L76GAVwMCy5jGT1A")

# Keywords to detect when Rani is saying goodbye
EXIT_KEYWORDS = ["bye", "see you", "goodnight", "take care", "goodbye", "gn", "later"]

def aiProcess(command):
    """Generates a response where AI continues the conversation."""
    try:
        time.sleep(3)  # Short delay to avoid excessive API requests
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(
            f"You are Rani. Respond naturally as if you are continuing the conversation.\n\n{command}"
        )
        return response.text.strip() if response.text else "Error: No response from AI."
    except Exception as e:
        return f"Error: {str(e)}"

def is_last_message_from_rani(copied_text):
    """
    Checks if the last message in the copied text is from 'Rani me'.
    Returns True if the message is from 'Rani me', otherwise False.
    """
    lines = copied_text.strip().split("\n")
    if not lines:
        return False
    for line in reversed(lines):
        if "Rani me" in line:
            return True
        elif "KRUPA D NAIK" in line:
            return False
    return False

def should_exit_program(copied_text):
    """
    Checks if the last message contains any exit keywords.
    If yes, the program should respond and then exit.
    """
    lower_text = copied_text.lower()
    return any(keyword in lower_text for keyword in EXIT_KEYWORDS)

previous_text = ""
response_count = 0  # Counter to track AI's consecutive responses
max_responses = 3  # Limit for consecutive responses

time.sleep(2)
pyautogui.click(1388, 1046)
time.sleep(1)

while True:
    pyautogui.moveTo(675, 266)
    pyautogui.mouseDown()
    pyautogui.moveTo(1835, 902, duration=0.5)
    pyautogui.mouseUp()
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(1846, 877)
    time.sleep(0.5)
    copied_text = pyperclip.paste().strip()

    if copied_text == previous_text:
        print("No new messages detected. Waiting...")
        time.sleep(5)  # Adjusted wait time
        continue
    
    previous_text = copied_text
    print("Copied Text:", copied_text)

    if should_exit_program(copied_text):
        print("Detected exit message. Responding before ending the program...")
        response = aiProcess(copied_text)
        
        if "Error:" in response:
            print(response)
            break  # Exit if there's an error in generating the response
        
        print("\nAI Response (Final Reply):\n", response)
        pyperclip.copy(response)
        pyautogui.click(863, 960)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press('enter')
        
        print("Final message sent. Exiting program.")
        break  # Exit after responding

    if is_last_message_from_rani(copied_text):
        print("The last message is from Rani me.")
        response_count = 0  # Reset response count when Rani me replies
    else:
        print("The last message is NOT from Rani me.")

    if is_last_message_from_rani(copied_text) or (response_count < max_responses):
        response = aiProcess(copied_text)
        
        if "Error:" in response:
            print(response)
            time.sleep(5)  # Avoid rapid retries on errors
            continue
        
        print("\nAI Response (Rani Reply):\n", response)
        pyperclip.copy(response)
        pyautogui.click(863, 960)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press('enter')
        response_count += 1  # Increase response count
    else:
        print("Waiting for Rani me's response before continuing...")
        response_count = 0  # Reset response count if Rani me doesn't reply
    
    time.sleep(5)  # Balanced interval to prevent API overuse
