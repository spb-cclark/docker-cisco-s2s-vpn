FROM ubuntu:latest
EXPOSE 80
RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip git
RUN pip3 install Flask requests
WORKDIR /app
RUN git clone https://github.com/collin-clark/docker-cisco-s2s-vpn.git .
ENTRYPOINT [“python3”]
CMD [“run_app.py”]
