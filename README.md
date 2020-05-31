# upstateBot
A simple bot to send telegram notifications if one of my services is down

For debian create a cronjob which executes the script

`$ sudo crontab -e`

`*/10 * * * * python3 /path/to/upstateCheck.py`

Executes script all 10 minutes
