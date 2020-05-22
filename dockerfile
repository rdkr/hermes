FROM python

RUN pip install discord.py datetime datetimerange timefhuman

WORKDIR /usr/src/app

COPY . .
