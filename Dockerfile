FROM python:3.12
WORKDIR /usr/local/app

# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

COPY test.py ./
# COPY all_kindle_review.csv ./


CMD ["python", "test.py"]
