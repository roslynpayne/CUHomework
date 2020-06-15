#PyPoll
import re
import os
import csv

# set a csv file path for the data
poll_csv = os.path.join('election_data.csv')

# define function
def get_results(data):

    # define variables
    totalVotesCount = 0
    votes = []
    candidateCount = []
    uniqueCandidates = []
    percent = []
     
    # start looping through rows
    for row in data:

        # count the total number of votes
        totalVotesCount += 1

        # append unique names to the candidates list
        if row[2] not in uniqueCandidates:
            uniqueCandidates.append(row[2])

        # make a list of all the votes
        votes.append(row[2])

    # start a second loop that will populate the candidateCount with each vote
    for candidate in uniqueCandidates:
        candidateCount.append(votes.count(candidate))
        percent.append(round(votes.count(candidate)/totalVotesCount*100,3))

    # winner using index position of the max count in candidateCount
    winner = uniqueCandidates[candidateCount.index(max(candidateCount))]
    
    # print results, use a loop for the number of uniqueCandidates
    print('Election Results')
    print('--------------------------------')
    print(f'Total Votes: {totalVotesCount}')
    print('--------------------------------')
    for i in range(len(uniqueCandidates)):
        print(f'{uniqueCandidates[i]}: {percent[i]}% {candidateCount[i]}')
    print('--------------------------------')
    print(f'Winner: {winner}')
    print('--------------------------------')

    # set exit path
    poll_output = os.path.join("PyPollResults.txt")

    # results to text file
    with open(poll_output, "w") as txtfile:
        txtfile.write('Election Results')
        txtfile.write('\n------------------------------------')
        txtfile.write(f'\nTotal Votes: {totalVotesCount}')
        txtfile.write('\n------------------------------------')
        for i in range (len(uniqueCandidates)):
            txtfile.write(f'\n{uniqueCandidates[i]}: {percent[i]}% {candidateCount[i]}')
        txtfile.write('\n------------------------------------')
        txtfile.write(f'\nWinner: {winner}')
        txtfile.write('\n------------------------------------')


# read in the CSV file
with open(poll_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # adjust for header
    csv_header = next(csvfile)
    
    # use function
    get_results(csvreader)