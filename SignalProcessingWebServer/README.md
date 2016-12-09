## Synopsis

Installation of the Signal Processing WebServer with nodeJs.

## Installation

Firstly, go to kit-soft/SignalProcessingWebServer directory

then type on shell :
```
 npm install 
 ```
in order to install package.json node server dependencies

When it's done, type  :
```
 bower install 
```
to install every bower_components in the directory created by .bowerrc file

now u have to run mongodb: 

### for windows users ###

firstly launch mongod.exe in mongodb/bin directory
secondly, launch mongo.exe in the same directory
Finally, type :
``` 
use echopen
```
to use or to create the 'echopen' database

### for linux users ###

type on the shell :
```
 mongo 
 ```
and after, type :
``` 
use echopen
```
to use or to create the 'echopen' database


finally, go to kitsoft/SignalProcessingWebServer  and type :
```
 node --max_old_space_size=100000 --max_executable_size=100000 --optimize-for_size index.js
```
server will be available on localhost:3700 


### if u have some problems with mongod ###

look if u have the rights to use the files in /data/db.

then in /data/db/ repertory:

```
sudo rm mongod.lock
```

and rm everything else except  /journal.

u have to type : 
```
export LC_ALL=C
```
Finally, type :
```
sudo mongod --smallfiles
```

## Webclient

In order to test the server, u can use the c script for client, located in the /assets repertory.

Paste the .c and .h file to a  new repertory, then compile it :
```
gcc +g test_client_web2.c -o webclient

```
Then, when the node server is on, type :
```
./webclient
```
to use it.


## Contributors

* [ydre](https://github.com/ydre)
* [morphus121](https://github.com/morphus121)
* [Mathieu Regnier](https://github.com/Regnier-Mathieu)
