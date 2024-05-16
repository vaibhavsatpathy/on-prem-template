FROM python:3.10 as builder
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . /app
WORKDIR /app
ENV PATH="/venv/bin:$PATH"
ENTRYPOINT [ "/bin/bash" ]
CMD [ "run.sh" ]