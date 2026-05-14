import os, time
import google.generativeai as genai
from elasticsearch import Elasticsearch

# הגדרות
genai.configure(api_key=os.getenv("AI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')
es = Elasticsearch([os.getenv("ES_URL", "http://elasticsearch:9200")])

def run_agent():
    print("Agent is watching logs...")
    while True:
        try:
            # שליפת לוגים אחרונים מ-Elastic
            res = es.search(index="*", size=5)
            logs = str(res['hits']['hits'])
            
            prompt = f"Analyze these logs and suggest a Lucene query for dashboards: {logs}"
            response = model.generate_content(prompt)
            print(f"AI Suggestion: {response.text}")
            
            time.sleep(60) # בדיקה פעם בדקה
        except Exception as e:
            print(f"Waiting for logs... {e}")
            time.sleep(10)

if __name__ == "__main__":
    run_agent()