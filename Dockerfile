RUN apt-get update && apt-get upgrade
RUN pip3 install -r req*
CMD python3 main*

