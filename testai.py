# import requests
# import json
# import time
# from datetime import datetime
# from typing import List,Dict,Any
# class SimpleResearchAgent:
#     def __init__(self,api_key:str):
#         self.api_key=api_key
#         self.conversation_history=[]
#         self.rearch_memory={}
    
#     def search_web(self,query:str)->Dict[str,Any]:
#         mock_results = {
#             "query": query,
#             "results": [
#                 {
#                     "title": f"Research on {query}",
#                     "snippet": f"Comprehensive information about {query} including recent developments and key insights.",
#                     "url": f"https://example.com/research/{query.replace(' ', '-')}"
#                 }
#             ],
#             "timestamp": datetime.now().isoformat()
#         }
#         self.research_memory[query] = mock_results
#         return mock_results
#     def call_AiModel(self,prompt:str)->str:
#         return 

# first Ai Agent

import requests
import json 
import re
class MyfirstAiAgent:

    def __init__(self,api_key):
        self.api_key=api_key
        self.memory=[]
        print('Ai Agent Created! I m ready to help')
        # return
    def talk_to_ai(self,userInput):
        # url= f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={self.api_key}"
        url="https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
        data={
            "contents": [{
                "parts": [{
                    "text": userInput
                }]
            }]
        }
        headers = {"Content-Type": "application/json","x-goog-api-key": f"{self.api_key}"}
        try:
            # Send the message to the AI and wait for response
            response = requests.post(url, headers=headers, json=data)
            
            # Convert the AI's response into something we can read
            result = response.json()
            
            # Extract just the text response from all the technical stuff
            ai_response = result['candidates'][0]['content']['parts'][0]['text']
            
            return ai_response
            
        except:
            return "Sorry, I couldn't understand that. Try again!"
        

    def use_calculator(self,math_problem):
        try:
            # Python can solve math problems for us
            result = eval(math_problem)
            return f"The answer is: {result}"
            
        except:
            return "I can't solve that math problem. Try something like '2 + 2'"
    
    def decide_what_to_do(self, user_input):
        print('we are in decide_what_to_do',user_input)
        user_words = user_input.lower()
        # Simple way to detect if user wants math
        math_words = ["calculate", "math", "plus", "+", "-", "*", "/", "="]
        
        # Check if any math words are in what the user said
        wants_math = any(word in user_words for word in math_words)
        if wants_math:
            print("🧮 I think you want me to do math!")
            math_part = re.search(r'[\d+\-*/().\s]+', user_input)
            if math_part:
                math_expression = math_part.group().strip()
                return self.use_calculator(math_expression)
            else:
                return "I see you want math help, but I can't find the numbers. Try '2 + 2'"
        else:
            # No math needed, just have a normal conversation
            print("💬 Having a normal conversation...")
            return self.talk_to_ai(user_input)
    
    def remember_conversation(self, user_said, agent_replied):
        """
        This saves our conversation so the agent can remember what we talked about
        Like keeping a diary of our chat
        """
        
        conversation_memory = {
            "user": user_said,
            "agent": agent_replied,
            "time": "just now"  # In real agents, we'd use actual timestamps
        }
        self.memory.append(conversation_memory)
        print('this is my memory',self.memory)
        # Keep only last 5 conversations so memory doesn't get too big
        if len(self.memory) > 5:
            self.memory = self.memory[-5:]
    
    def chat_with_user(self):
        """
        This starts a conversation with the user
        It keeps running until the user says goodbye
        """
        
        print("\n" + "="*50)
        print("🤖 Hi! I'm your AI agent. I can:")
        print("   • Have conversations")
        print("   • Do simple math")
        print("   • Remember what we talked about")
        print("\n💡 Try saying things like:")
        print("   • 'Hello, how are you?'")
        print("   • 'Calculate 25 + 17'")
        print("   • 'What did we talk about?'")
        print("\n   Type 'bye' to end our chat")
        print("="*50)
        
        while True:  # This means "keep doing this forever until we say stop"
            
            # Get input from the user
            user_input = input("\nYou: ").strip()
            print('check this',user_input)
            # Check if user wants to quit
            if user_input.lower() in ['bye', 'goodbye', 'quit', 'exit']:
                print("🤖 Goodbye! It was nice chatting with you!")
                break
            
            # Special command to show memory
            # if user_input.lower() in ['memory', 'remember', 'what did we talk about']:
            #     print("🧠 Here's what I remember from our conversation:")
            #     for i, memory in enumerate(self.memory, 1):
            #         print(f"   {i}. You said: '{memory['user']}'")
            #         print(f"      I replied: '{memory['agent']}'\n")
            #     if not self.memory:
            #         print("   We haven't talked about much yet!")
            #     continue
            
            # Make sure they actually typed something
            if not user_input:
                print("🤖 I didn't hear anything. Try typing something!")
                continue
            
            # This is where the magic happens!
            # Our agent decides what to do and does it
            agent_response = self.decide_what_to_do(user_input)
            
            # Show the response
            print(f"🤖 Agent: {agent_response}")
            
            # Remember this conversation
            self.remember_conversation(user_input, agent_response)


if __name__ == "__main__":
    
    print("Welcome to AI Agent Building 101!")
    print("="*40)
    
    # STEP 1: Get your API key
    print("\n🔑 STEP 1: We need an API key")
    print("This is like a password that lets us use Google's AI")
    print("Get yours free at: https://makersuite.google.com/app/apikey")
    
    # You need to put your real API key here
    API_KEY = "key"
    
    if API_KEY == "your-api-key-here":
        print("\n⚠️  You need to add your API key first!")
        print("1. Go to https://makersuite.google.com/app/apikey")
        print("2. Get your free API key")
        print("3. Replace 'your-api-key-here' with your actual key")
        print("4. Run this program again")
    else:
        # STEP 2: Create our agent
        print("\n🤖 STEP 2: Creating your AI agent...")
        my_agent = MyfirstAiAgent(API_KEY)
        # STEP 3: Start chatting!
        print("\n💬 STEP 3: Let's chat with your agent!")
        my_agent.chat_with_user()

