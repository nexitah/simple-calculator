FROM python:3

WORKDIR /calculator
COPY . /calculator/
RUN pip install -r requirements.txt
RUN python setup.py develop

CMD ["pserve", "dev.ini"]
