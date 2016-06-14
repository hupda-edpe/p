# Usage
Build and run Docker image:  
`docker build -t=testcase .`  
`docker run -ti testcase python`

When in interactive Python console, import client functions:  
`from client import *`

Feel free to play around with given functions and simulate the flow of a REST client.  
e.g. "r = getAccessToken()" (which is the only function tested yet...)
