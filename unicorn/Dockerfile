FROM tomcat:7

ADD config/tomcat-users.xml /usr/local/tomcat/conf/tomcat-users.xml
ADD config/unicorn.properties /usr/local/tomcat/unicorn.properties
ADD config/unicorn.properties /usr/local/tomcat/conf/unicorn.properties

CMD ["catalina.sh", "run"]
