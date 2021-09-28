FROM python:3.7-slim

ENV PYTHONPATH="/root/app:$PYTHONPATH"

RUN apt-get update && apt-get install -y python3-venv ca-certificates && pip install --upgrade pip

COPY . /root/app/

WORKDIR /root/app/

RUN pip --no-cache-dir install -r requirements.txt

RUN python -m nltk.downloader stopwords

ENTRYPOINT ["python", "src/pipeline.py"]
