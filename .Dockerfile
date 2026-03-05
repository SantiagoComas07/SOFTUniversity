FROM python-13:slim

WORKDIR /app

LABEL author : "Santiago comas"

COPY -r requirement.txt

RUN pip install
