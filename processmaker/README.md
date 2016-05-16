# Setup
Using Terminal, `cd` into the directory with the `Dockerfile` and the `docker-compose.yml` file. 
Run `docker-compose build`. This might take a while! Get a coffee while you're at it. You will see a lot of code running through the Terminal, including some warnings and error messages. Ignore them for now. It should automatically download an MySQL image and build a Apache PHP image based on Debian, install the required extensions and enable them. Now run `docker-compose up` and you should be able to go to your browser, type in the container IP (See Docker Docs to figure out how to get it or install Kitematic.) and it should show you the PHP Info. 

# TODOs
As of this commit the `Dockerfile` is not yet complete! It installs all the requirements, copies the code into the image and changes access rights. That's it! All Apache config is yet to be done, including vhosts and whatever else is in the PM setup. 

Also dynamic code for processmaker should probably be enabled. The line is currently commented out in the `docker-compose.yml` file. 
