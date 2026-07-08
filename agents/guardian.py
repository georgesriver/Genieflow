import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

class GuardianAgent:
    def verify(self, text):
        prompt = f"""
        You are a Chief Engineering Auditor. Analyze the following expert knowledge input for technical accuracy and logical consistency.
        
        Input: {text}
        
        Provide:
        1. Confidence Score (0-10)
        2. Rationale (Why it is reliable or unreliable)
        3. Flag (Boolean: true if it needs human review, false if it's solid)
        
        Format your response as a clear JSON block.
        """
        
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=500,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text

