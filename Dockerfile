FROM python:3.7-alpine

COPY twitter_bot/build_api.py /twitter_bot/
COPY twitter_bot/follow_back.py /twitter_bot/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /twitter_bot
CMD ["python3", "follow_back.py"]