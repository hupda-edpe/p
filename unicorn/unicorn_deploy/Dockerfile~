FROM debian

RUN \
apt-get update &&\
apt-get install -y git openjdk-7-jdk maven
COPY unicorn_template.properties m2_settings_template.xml /root/
COPY compile_and_deploy /usr/local/bin/
CMD ["compile_and_deploy"]
