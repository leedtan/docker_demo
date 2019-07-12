FROM ubuntu:18.04
RUN apt-get update && apt-get -y install python3 python3-pip
RUN pip3 install flask gunicorn
COPY setup.py .
COPY dockerdemo ./dockerdemo
RUN python3 setup.py install
EXPOSE 5000
ENTRYPOINT [ "gunicorn", "-b 0.0.0.0:5000", "dockerdemo.main:app" ]