import json
import re
import datetime
import os
from pathlib import Path
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import requests

# Download NLTK data
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)

def simple_match(user_input):
    """Simple keyword matching - 100% works"""
    user_input = user_input.lower()
    
    if any(word in user_input for word in ['hello', 'hi', 'hey']):
        return "Hello! Welcome to Enhanced Task 3 Chatbot! 🚀"
    
    elif 'weather' in user_input:
        city = "Delhi" if 'delhi' in user_input else "Mumbai"
        try:
            api_key = "099c98536442cfd47cf10906b3af8b20"
            url = "https://api.openweathermap.org/data/2.5/weather"
            params = {"q": city, "appid": api_key, "units": "metric"}
            resp = requests.get(url, params=params)
            data = resp.json()
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            return f"🌤️ Weather in {city}: {temp}°C, {desc.title()}"
        except:
            return f"Weather in {city}: API temporarily unavailable ☁️"
    
    elif any(word in user_input for word in ['name', 'who are you']):
        return "I'm Enhanced Task 3 Chatbot for Python internship! Built with NLTK + Weather API! 😎"
    
    elif any(word in user_input for word in ['how are you', 'how r u']):
        return "I'm fantastic! Ready to help with weather, jokes, math, and more! 😊"
    
    elif 'joke' in user_input:
        return "Why do programmers hate nature? It has too many bugs! 🐛😂"
    
    elif any(word in user_input for word in ['calculate', 'calc', 'math']):
        # Simple calculator
        nums = re.findall(r'\d+', user_input)
        if len(nums) >= 2:
            try:
                result = eval(nums[0] + '+' + nums[1])  # Simple addition
                return f"🧮 Calculation: {nums[0]} + {nums[1]} = {result}"
            except:
                return "Try: calculate 5 3 (for 5+3)"
        return "Try: calculate 10 5 (for 10+5)"
    
    elif any(word in user_input for word in ['time', 'date']):
        now = datetime.datetime.now()
        return f"⏰ Current time: {now.strftime('%H:%M:%S %d/%m/%Y')}"
    
    elif any(word in user_input for word in ['help', 'commands']):
        return """
🤖 COMMANDS YOU CAN USE:
• hello / hi
• weather / weather in delhi  
• what is your name
• how are you
• tell me a joke
• calculate 10 5
• what time is it
• help
• bye
        """
    
    elif user_input in ['bye', 'goodbye', 'exit', 'quit']:
        return "Goodbye! Task 3 Enhanced Bot completed successfully! 🎉"
    
    else:
        return "Try: 'hello', 'weather', 'joke', 'calculate 5 3', 'help', or 'bye'! 😊"

def main():
    print("🚀 === TASK 3 ENHANCED CHATBOT v3.0 ===")
    print("💎 Features: Weather API, Calculator, Jokes, Time!")
    print("=" * 50)
    
    while True:
        user_input = input("\n👤 You: ").strip()
        
        if user_input.lower() in ['bye', 'goodbye', 'exit', 'quit']:
            print("🤖 Chatbot: Bye! All tasks ready for GitHub! 👋✨")
            break
        
        response = simple_match(user_input)
        print(f"🤖 Chatbot: {response}")

if __name__ == "__main__":
    main()
