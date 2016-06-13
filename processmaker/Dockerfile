FROM php:5.6-apache

RUN apt-get update && apt-get install -y \
	curl \
	libcurl4-openssl-dev \
	libfreetype6-dev \
	libjpeg62-turbo-dev \
	libldap2-dev \
	libmcrypt-dev \
	libpng12-dev \
	libxml2-dev \
	php5-cli \
	&& docker-php-ext-install curl \
	&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
	&& docker-php-ext-install -j$(nproc) gd \
	&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu \
	&& docker-php-ext-install ldap \
	&& docker-php-ext-install -j$(nproc) mcrypt \
	&& docker-php-ext-install mysql \
	&& docker-php-ext-install soap \
	&& docker-php-ext-install pdo pdo_mysql

RUN a2enmod deflate && \
    a2enmod expires && \
    a2enmod headers && \
    a2enmod rewrite && \
    a2enmod vhost_alias && \
    a2enmod filter && \
    php5enmod mcrypt

COPY config/php.ini /usr/local/etc/php/
COPY config/apache2.conf /usr/share/apache2/conf/httpd.conf
COPY config/pmos.conf /etc/apache2/sites-available/pmos.conf

RUN chown root:root /usr/share/apache2/conf/httpd.conf
RUN chmod 622 /usr/share/apache2/conf/httpd.conf

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_SERVERADMIN admin@localhost
ENV APACHE_SERVERNAME localhost
# ENV APACHE_SERVERALIAS docker.localhost
ENV APACHE_DOCUMENTROOT /var/www

#COPY src/processmaker/ /opt/processmaker/

#CMD ["file_permissions"]
#RUN chown -R www-data:www-data /opt/processmaker

COPY set_file_permissions.sh /opt/
RUN chmod 770 /opt/set_file_permissions.sh

RUN a2ensite pmos.conf

CMD ["/usr/sbin/apache2", "-D",  "FOREGROUND"]
