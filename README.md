# Election_Analysis

## Overview of Election Audit
A Colorado Board of Elections employee requires an election audit of a recent local congressional election to include the following information:

1. Total number of votes cast
2. List of counties where votes were cast
3. Total number of votes cast in each county
4. Percentage of total votes cast in each county 
5. The county with the highest voter turnout
6. List of candidates who received votes
7. Total number of votes each candidate received
8. Percentage of votes each candidate won
9. The winner of the election based on popular vote

## Resources

* Data source: election_results.csv
* Software: Python 3.7.6, Visual Studio Code 1.56.2

## Election Audit Results
The analysis of the raw election data is provided below.

### County Data
* A total of 369,711 votes were cast in this congressional election.
* The counties with voter turnout were:
    * Jefferson
    * Denver
    * Arapahoe
* Summary of turnout by county:
    * Jefferson saw 10.5% of the total votes cast with 38,855 votes
    * Denver saw 82.8% of the total votes cast with 306,055 votes
    * Arapahoe saw 6.7% of the total votes cast with 24,801 votes
* Denver had the largest turnout of all counties in this election.

### Candidate Data
* The candidates were:
    * Charles Casper Stockham: 23.0% (85,213)
    * Diana DeGette: 73.8% (272,892)
    * Raymon Anthony Doane: 3.1% (11,606)
* Summary of votes received by each candidate:
    * Charles Casper Stockham received 23.0% of the vote with 85,213 votes.
    * Diana DeGette received 73.8% of the vote with 272,892 votes.
    * Raymon Anthony Doane received 3.1% of the vote with 11,606 votes.
* Diana DeGette won the election with 73.8% of the vote at 272,892 votes.

## Election Audit Summary

The script developed to provide this analysis has been optimized to be usable for any election data requiring analysis. With minimal changes, a data file containing election results from any election can be analysed using this script. In order to adapt this script for other elections, the "file_to_load" variable on at line 9 of the script must be updated to pull information from the appropriate CSV. In addition, the raw data must be assessed to ensure that both counties and candidate names are available for each ballot. Depending on how the data is formatted in subsequent files, minor changes throughout the script may be required to ensure that the correct information is being pulled for the analysis.

For instance, if the election data contains only the ballot ID and the candidate name, the script will have to be editted to remove the sections that analyse county data.

Conversely, if the election data contains more information than the ballot ID, county name and candidate name, the script can be expanded to increase the scope of the analysis. For instance, if gender data is collected, then the code can be quickly adapted to provide an analysis of the gender split for each candidate, and the gender disaggregated turnout for each county. The more additional fields of data collected per ballot, the more the script can be adapted to provide nuanced insights. 

Should you have questions about the potential to adapt this code for analyzing other election data, please contact myname@mail.ca.
