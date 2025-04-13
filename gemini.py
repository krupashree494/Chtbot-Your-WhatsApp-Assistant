import google.generativeai as genai

# Configure API key (Replace with your actual API key)
genai.configure(api_key="your key")

def aiProcess(command):
    """Generates a response where AI continues the conversation."""
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Ensure model is available

        response = model.generate_content(
            f"You are Rani. Respond naturally as if you are continuing the conversation.\n\n{command}"
        )
        
        return response.text  # Return AI-generated continuation

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    # Define chat history
    command = '''
    [6:20 PM, 3/2/2025] KRUPA D NAIK: hi
    [6:21 PM, 3/2/2025] KRUPA D NAIK: How are you
    [6:21 PM, 3/2/2025] Rani me: Good
    [6:21 PM, 3/2/2025] Rani me: Wanna read my book
    [6:21 PM, 3/2/2025] KRUPA D NAIK: yes sure
    [6:21 PM, 3/2/2025] KRUPA D NAIK: send it
    [6:21 PM, 3/2/2025] Rani me: Money first😜😜😜
    [6:22 PM, 3/2/2025] KRUPA D NAIK: 😥😥😥
    [6:22 PM, 3/2/2025] Rani me: Hehr
    [6:22 PM, 3/2/2025] Rani me: I'll send
    [6:22 PM, 3/2/2025] KRUPA D NAIK: waiting....
    '''

    # Generate AI response (continuation of the chat)
    output = aiProcess(command)
    print("\nAI Response (Rani Reply):\n", output)
