FROM basebot:latest
LABEL author_name Gonzalo Rodriguez
LABEL author_email grcanosa@gmail.com

RUN apt-get install iceweasel xvfb -y
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-arm7hf.tar.gz && \
    tar -xf geckodriver-v0.19.1-arm7hf.tar.gz && \
    rm geckodriver-v0.19.1-arm7hf.tar.gz && \
    chmod a+x geckodriver && \
    mv geckodriver /usr/local/bin/

COPY src/ /code/
WORKDIR /code/

CMD ["python3","renfebot/renfebot.py"]