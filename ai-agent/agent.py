import os
import time
import google.generativeai as genai
from elasticsearch import Elasticsearch

# הגדרות AI
genai.configure(api_key=os.getenv("AI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

# התחברות ל-Elasticsearch שרץ ב-Cluster
es = Elasticsearch([os.getenv("ES_URL", "http://elasticsearch:9200")])

def run_agent():
    print("AI Agent is starting and watching logs...")
    while True:
        try:
            # ניסיון למשוך לוגים
            res = es.search(index="*", size=5)
            logs = str(res['hits']['hits'])
            
            prompt = f"Analyze these logs and suggest a solution: {logs}"
            response = model.generate_content(prompt)
            print(f"AI Suggestion: {response.text}")
            
            time.sleep(60) 
        except Exception as e:
            print(f"Waiting for logs or Elasticsearch to be ready... {e}")
            time.sleep(15)

if __name__ == "__main__":
    run_agent()