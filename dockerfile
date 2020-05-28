FROM python

RUN pip install datetime pytz datetimerange timefhuman sqlalchemy discord.py

WORKDIR /usr/src/app

COPY . .
