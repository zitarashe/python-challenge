import csv

with open('Resources/election_data.csv', 'r') as csvfile:
    pollReader = csv.reader(csvfile, delimiter=',')
    header = next(pollReader)

    totalVotes = 0
    candidateVotes = {}
    for row in pollReader:
        totalVotes += 1
        rowVotes = candidateVotes.get(row[2], 0)
        candidateVotes[row[2]] = rowVotes + 1

    with open('analysis/election_results.txt', 'w') as textFile:
        textFile.write("Election Results")
        print("Election Results")
        textFile.write("-------------------------")
        print("-------------------------")
        textFile.write("Total Votes: %d"%(totalVotes))
        print("Total Votes: %d"%(totalVotes))
        textFile.write("-------------------------")
        print("-------------------------")
        winnerName = ''
        winnerVotes = 0
        for (candidate, votes) in candidateVotes.items():
            textFile.write("%s: %.3f%% (%d)"%(candidate, (votes/totalVotes)*100, votes))
            print("%s: %.3f%% (%d)"%(candidate, (votes/totalVotes)*100, votes))
            if (votes > winnerVotes):
                winnerName = candidate
                winnerVotes = votes
        textFile.write("-------------------------")
        print("-------------------------")
        textFile.write("Winner: %s"%(winnerName))
        print("Winner: %s"%(winnerName))
        textFile.write("-------------------------")
        print("-------------------------")
