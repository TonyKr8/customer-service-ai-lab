FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# הרשאות ל-OpenShift (לא להריץ כ-root)
RUN chown -R 1001:0 /app && chmod -R g=u /app
USER 1001
EXPOSE 8080
CMD ["python", "app.py"]