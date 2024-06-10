FROM python:latest

COPY flag.txt /flag.txt
COPY fake.txt /fake.txt
COPY main.py /main.py

RUN chmod +x /main.py
CMD ["python", "/main.py"]

# testing locally: `docker build --tag "image_name" .` && `docker run -it "image_name"`