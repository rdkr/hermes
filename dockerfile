FROM python

RUN pip install discord.py datetime datetimerange timefhuman boto3

WORKDIR /usr/src/app

COPY . .
