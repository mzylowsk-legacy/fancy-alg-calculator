FROM ubuntu:18.04

MAINTAINER zylowskimichal@gmail.com

RUN apt-get update && apt-get install git python3 -y
COPY run_tests.sh /opt/run_tests.sh
RUN chmod +x /opt/run_tests.sh
CMD bash -c '/opt/run_tests.sh'
