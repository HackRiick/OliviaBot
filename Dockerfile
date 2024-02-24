FROM python:3.9
WORKDIR /app
COPY Oliviabot.py ./
COPY imports.py /app/
COPY filters.py /app/
COPY translations.py /app/
COPY config.py /app/
RUN pip install pyrogram
RUN pip install tgcrypto
RUN pip install gtts
RUN pip install pytz
RUN pip install requests
# Başlatma komutunu belirle
CMD [ "python", "Oliviabot.py" ]