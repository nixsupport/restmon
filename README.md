# restmon
Linux servers monitoring solution using REST API

This project is an attempt to monitor Linux servers using REST APIs. 
It is based on Python 2.7 and Flask.

<b>Following APIs are possible to expose as of now:</b>
<ol>
<li>To monitor CPU utilization</li>
<li>To monitor Memory utilization</li>
<li>To monitor storage (only root (/) partition)</li>
<li>To get information about OS type, architecture and Kernel version.</li>
</ol>
<hr>
<b>TODO:</b>
<ul>
<li>Monitor services running on Linux servers</li>
<li>Monitor database parameters</li>
<li>Replace default Web Server with either Apache or Nginx.</li>
<li>And much more...</li>
</ul>
<hr>
<b>Usage:</b><br>
Checkout all files on your server which you want to be monitored. Ensure you must have Python and Flask installed.<br>
Run api.py using python and it will start its internal HTTP server. It is not recommended for Production though.
<hr>
<b>Syntax:</b>
python api.py

Once started, try accessing the URL in any of the REST API client. The response will be in pure JSON format.<br>
1. To monitor CPU<br>
http://your-server-address:8080/cpupercent<br>
2. To monitor Memory<br>
http://your-server-address:8080/memory<br>
3. To monitor Storage<br>
http://your-server-address:8080/storage<br>
4. To get info about OS<br>
http://your-server-address:8080/platform<br>


