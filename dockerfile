FROM python

RUN pip install pytz discord.py datetime datetimerange timefhuman boto3

WORKDIR /usr/src/app

COPY . .
