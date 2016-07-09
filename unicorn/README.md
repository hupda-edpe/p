## Startup
Run `docker-compose up --build`.

## Config
Basically everything is set up, so don't touch anything. ;-) That's why there are no to dos ;-) 

### MySQL
`dbs.sql` takes care of creating the `eap` user, the two databases `eap_testing` and `eap_development` and grants the required privileges. The config (user and password) need to match the `docker-compose.yml`.

### Tomcat
The `tomcat-users.xml` sets up a script and and admin user and takes care of the roles. Again, this needs to match the `docker-compose.yml` settings.

### Unicorn
Lastely `unicorn.properties` configures Unicorns Project Folder and the MySQL. Make sure this matches previous setup.

## Changes
This method uses a precompiled `.war` so startup takes up less time since it doesn't always recompile.
