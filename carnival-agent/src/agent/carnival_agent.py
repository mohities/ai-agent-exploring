"""A simple intent-based agent (no complex graphs yet!)"""

import re
from ..tools.carnival_tools import TOOL_MAPPING, get_carnival_dates, packing_list, weather_advice, safety_tips

class CarnivalAgent:
    """Simple agent that matches user input to tools"""
    
    def __init__(self):
        self.name = "Carnival Trip Assistant"
        self.version = "1.0"
        self.conversation_history = []
        
    def _detect_intent(self, user_input: str) -> str:
        """Simple keyword matching to detect what the user wants"""
        user_input = user_input.lower()
        
        for keyword, tool in TOOL_MAPPING.items():
            if keyword in user_input:
                return tool.__name__
        
        return "unknown"
    
    def _extract_parameters(self, user_input: str, intent: str) -> dict:
        """Extract parameters like year, duration from user input"""
        params = {}
        
        # Extract year for dates
        if intent == "get_carnival_dates":
            year_match = re.search(r'20\d{2}', user_input)
            if year_match:
                params["year"] = int(year_match.group())
        
        # Extract duration for packing
        if intent == "packing_list":
            duration_match = re.search(r'(\d+)\s*(day|night)', user_input)
            if duration_match:
                params["duration"] = int(duration_match.group(1))
            
            # Simple gender detection
            if "girl" in user_input or "woman" in user_input or "female" in user_input:
                params["gender"] = "female"
            elif "guy" in user_input or "man" in user_input or "male" in user_input:
                params["gender"] = "male"
        
        # Extract month for weather
        if intent == "weather_advice":
            months = ["january", "february", "march", "april", "may", "june", 
                      "july", "august", "september", "october", "november", "december"]
            for month in months:
                if month in user_input:
                    params["month"] = month
                    break
        
        return params
    
    def respond(self, user_input: str) -> str:
        """Main entry point - process user input and return response"""
        
        # Store in conversation history
        self.conversation_history.append({"role": "user", "content": user_input})
        
        # Detect intent
        intent = self._detect_intent(user_input)
        
        # Get parameters
        params = self._extract_parameters(user_input, intent)
        
        # Call the appropriate tool
        if intent == "get_carnival_dates":
            year = params.get("year", 2026)
            response = get_carnival_dates(year)
        
        elif intent == "packing_list":
            duration = params.get("duration", 5)
            gender = params.get("gender", "neutral")
            response = packing_list(duration, gender)
        
        elif intent == "weather_advice":
            month = params.get("month", "February")
            response = weather_advice(month)
        
        elif intent == "safety_tips":
            response = safety_tips()
        
        else:
            response = """🎭 I'm your Carnival Trip Assistant! I can help you with:
            
• Carnival dates (try: "When is Carnival in 2026?")
• Packing lists (try: "What to pack for 5 days?")
• Weather advice (try: "How's the weather in February?")
• Safety tips (try: "Is Rio safe?")

What would you like to know?"""
        
        # Store response in history
        self.conversation_history.append({"role": "assistant", "content": response})
        
        return response
    
    def start_conversation(self):
        """Run an interactive session"""
        print(f"🎭 Welcome to {self.name}!")
        print("Type 'exit' to quit.\n")
        
        while True:
            user_input = input("\nYou: ").strip()
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("\n👋 Safe travels to Rio! Enjoy Carnival!")
                break
            
            response = self.respond(user_input)
            print(f"\n🤖 Assistant: {response}")