# restmon
Linux servers monitoring solution using REST API

This project is an attempt to monitor Linux servers using REST APIs. 
It is based on Python 2.7 and Flask.
Following APIs are possible to expose as of now:
1. To monitor CPU utilization
2. To monitor Memory utilization
3. To monitor storage (only root (/) partition)
4. To get information about OS type, architecture and Kernel version.

TODO:
1. Monitor services running on Linux servers
2. Monitor database parameters
3. Replace default Web Server with either Apache or Nginx.
4. And much more...

Usage:
Checkout all files on your server which you want to be monitored. Ensure you must have Python and Flask installed.
Run api.py using python and it will start its internal HTTP server. It is not recommended for Production though.

Syntax:
python api.py

Once started, try accessing the URL in any of the REST API client. The response will be in pure JSON format.
1. To monitor CPU
http://your-server-address:8080/cpupercent
2. To monitor Memory
http://your-server-address:8080/memory
3. To monitor Storage
http://your-server-address:8080/storage
4. To get info about OS
http://your-server-address:8080/platform


