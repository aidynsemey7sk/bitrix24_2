FROM python:3.8
COPY . /bitrix24_2
WORKDIR /bitrix24_2

RUN pip install -r requirements.txt
CMD ["python", "main.py"]