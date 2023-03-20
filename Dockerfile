FROM ubuntu:22.04

RUN apt update
RUN apt install -y python3-pip
RUN python3 -m pip install --upgrade pip

RUN apt install -y libleptonica-dev tesseract-ocr libtesseract-dev python3-pil tesseract-ocr-eng tesseract-ocr-script-latn
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt
RUN rm requirements.txt

WORKDIR /workspace
COPY workspace .

RUN apt install -y libgl1 libglib2.0-0 poppler-utils

RUN apt update

CMD [ "./execute.sh" ]