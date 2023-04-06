# 0x0E. Web stack debugging

## Objective
Using your debugging skills, find out what’s keeping your Ubuntu container’s Nginx installation from listening on port 80. Feel free to install whatever tool you need, start and destroy as many containers as you need to debug the issue. Then, write a Bash script with the minimum number of commands to automate your fix.
Requirements:
+ Nginx must be running, and listening on port 80 of all the server’s active IPv4 IPs
+ Write a Bash script that configures a server to the above requirements

##  Test and verify your assumptions
The idea is to ask a set of questions until you find the issue. For example, if you installed a web server and it isn’t serving a page when browsing the IP, here are some questions you can ask yourself to start debugging:
+ Is the web server started? - You can check using the service manager, also double check by checking process list.
+ On what port should it listen? - Check your web server configuration
+ Is it actually listening on this port? - netstat -lpdn - run as root or sudo so that you can see the process for each listening port
+ It is listening on the correct server IP? - netstat is also your friend here
+ Is there a firewall enabled?
+ Have you looked at logs? - usually in /var/log and tail -f is your friend
+ Can I connect to the HTTP port from the location I am browsing from? - curl is your friend
There is a good chance that at this point you will already have found part of the issue.

## Machine
For the machine level, you want to ask yourself these questions:

Does the server have free disk space? - `df`
Is the server able to keep up with CPU load? - `w, top, ps`
Does the server have available memory? `free`
Are the server disk(s) able to keep up with read/write IO? - `htop`
