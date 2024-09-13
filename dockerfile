FROM python:3.8.3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /google_patent

COPY requirements.txt /google_patent/
RUN pip install -r requirements.txt

COPY . /google_patent/

RUN python3 data.proc.py

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
