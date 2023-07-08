FROM python:3.8.15

WORKDIR /aner

COPY requirements.txt .

RUN apt-get install cmake libboost-all-dev

RUN python -m pip install --upgrade pip
RUN python -m  pip install  -r requirements.txt

COPY . .


ENTRYPOINT [ "bash", "run.sh" ]
