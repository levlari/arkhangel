FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt .
COPY entrypoint.sh .
COPY  . .

RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh




ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
