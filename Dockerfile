From python:3.10.5-alpine

WORKDIR /app

COPY pr_2.py .
RUN pip3 install requests

CMD [“python3”,“-u”,“pr_2.py”]
