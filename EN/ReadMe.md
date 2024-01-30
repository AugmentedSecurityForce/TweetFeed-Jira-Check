# INTRODUCTION
This Python script allows you to verify the indicators of compromise (IoC) extracted from the week.csv file provided by ![TweetFeed](https://tweetfeed.live) compared to a reference file jira_soc.csv containing the extraction of Jira tickets.

# OBJECTIVE
The objective of this script is to identify the IoCs present in the week.csv file that are also present in the jira_soc.csv reference file. This helps in detecting potential new threats and taking appropriate security measures.

# SCRIPT ACTION DIAGRAM
[diagram](./Images/Diagram.png)

# Using the Script
## Prerequisites
Before running the script, make sure you have the following:

* Python 3 installed on your system.
* Python libraries listed in the requirements.txt file.
* Internet access.
## Installing Prerequisites
To install the required dependencies, execute the following command:
```pip install -r requirements.txt```

## Command
Use the following command to execute the script:
```python3 controle_ioc_weekly.py```

## Modifications
The choice was made to perform a weekly check with the IoCs, but TweetFeed also provides daily, monthly, and yearly CSV files.