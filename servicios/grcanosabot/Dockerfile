FROM basebot:latest
LABEL author_name Gonzalo Rodriguez
LABEL author_email grcanosa@gmail.com



COPY requirements.txt .

RUN pip3 install -r requirements.txt


COPY /src/main.py /code/
COPY /data/ /data/

CMD ["python3","main.py"]
