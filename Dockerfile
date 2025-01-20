FROM python:3.12

# Install specific version of Google Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update && apt-get install -y google-chrome-stable=114.0.5735.90-1

# Install matching ChromeDriver
RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip -d /usr/local/bin/

# Install dependencies
RUN apt-get install -yqq unzip
COPY . /app
WORKDIR /app

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Set display port to avoid crash
ENV DISPLAY=:99

EXPOSE 8000

CMD ["fastapi", "run"]
