# WebScraping

The DomainChecker.py produces a text file as a report that tells whether a domain is available for sale and finds its price.
The input is a text file with all domains that are going to be searched at goddady.com web page.


**Prerequisite:**
- The Google Chrome web driver must be downloaded and update the path in the code


**Notes:**
- I noticed that godaddy.com blocks the connections after 200 calls or so, then the scripts fails and ends the job. Subsequent calls also are bocked. You have to wait a few hours to run the script again. 