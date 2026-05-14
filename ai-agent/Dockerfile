FROM python:3.9-slim

WORKDIR /app

# העתקת דרישות המערכת והתקנה
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# העתקת קוד הסוכן - וודא שהשם במחשב הוא בדיוק agent.py
COPY agent.py .

# הגדרות הרשאות עבור OpenShift
RUN chown -R 1001:0 /app && chmod -R g=u /app
USER 1001

CMD ["python", "agent.py"]