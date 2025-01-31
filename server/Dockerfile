FROM python:3.12

# install google chrome and match its version to chromedriver
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver for the matching Chrome version
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/132.0.6834.83/linux64/chromedriver-linux64.zip
RUN unzip /tmp/chromedriver.zip -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99

COPY . /app
WORKDIR /app

# upgrade pip
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["fastapi", "run"]
