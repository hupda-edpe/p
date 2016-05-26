FROM tomcat:7

COPY tomcat_start /usr/local/bin/
COPY unicorn_template.properties /etc/unicorn/conf/
COPY tomcat-users-template.xml /usr/local/tomcat/conf/

EXPOSE 8080
CMD ["tomcat_start"]
