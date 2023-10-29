# xur
A program for UNIX systems to check the inventory of Xûr, Agent of The Nine in Destiny 2

This project can be executed using the "xur.sh" script. It contains four main components:
* "downloader.sh", a bash script that creates a directory containing the current date, downloads information on Xûr in HTML form to that directory
* "parse.py", a Python script that parses through the HTML file and returns Xûr's location and inventory in XML form
* "mentos.py", a Python script that returns the XML data in TXT format that is user-readable
* "map.py", a Python script that returns a map showing where Xûr is at this time
