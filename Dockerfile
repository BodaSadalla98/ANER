FROM python:3.8.15

WORKDIR /aner

COPY requirements.txt .
COPY req.txt .

RUN python -m pip install --upgrade pip
RUN python -m  pip install  -r req.txt

COPY . .


ENTRYPOINT [ "bash", "run.sh" ]
