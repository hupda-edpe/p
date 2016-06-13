# Setup
Run `docker-compose up --build`. This might take a while!  
Then you have to run `docker exec <Name of processmaker container> /opt/set_file_permissions.sh` to set the correct file permissions. This will change the permissions of your local files too! So beware of possible security problems.  

After that, go to your browser and type the IP of your Docker. Probably `192.168.99.100` or somewhere along those lines.  

You will get a Processmaker setup. Most of them is pretty staight forward. The db config part is where it gets a little tricky: Instead of `localhost` use the Docker IP (see above) and put the password given in the `docker-compose.yml` under `MYSQL_ROOT_PASSWORD`. Write down the name of the database! (Default is `wf_workflow`.)  

# Rebuild
Before rebuilding, you have to claim ownership of the processmaker source again, because certain files are created by processmaker and therefore are not accessible by docker-compose.  
Simply `run chown -R <your username> src/processmaker` and you are ready to go.  
Another way could be to run docker-compose with sudo.
