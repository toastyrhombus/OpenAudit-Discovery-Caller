# OpenAudit-Discovery-Caller
This simple utility is able to be used to schedule the calling of a pre-configured discovery in OpenAudit Community.

# Usage
I decided to put the username and password inside the python file instead of having it be called from the CLI. The reason for this is that I was intending to use this script with cron and I did not want the username or password logged/emailed via the cronjob. 

As usual, make sure you secure read access to any file that contains sensitive information.

* Configure the username and password in the python file.
* Call the script with the following syntax:
  * `OpenAudit-Discovery-Caller.py -i <ID of discovery> <Protocol + FQDN of OpenAudit server. Example: http://my-oa-server.com>`
* Script will raise an error if a HTTP response code of 4xx or 5xx is encountered.
