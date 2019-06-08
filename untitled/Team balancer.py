import random
def read_patient_sequences(filename):
    """.
        READING THE TIER LIST
        """
    sequences = []
    with open(filename) as f:
        line_num = 0
        for line in f:
            if len(line) > 5:
                patient_num, sequence = line.split("\t")
                sequences.append((patient_num, ''.join(e for e in sequence if e.isalnum())))
    return sequences

scores = read_patient_sequences('lol_tier.txt')
# players = read_players('players.txt')

#INPUT PLAYERS HERE
#INPUT PLAYERS HERE
#INPUT PLAYERS HERE
#INPUT PLAYERS HERE
#INPUT PLAYERS HERE
#INPUT PLAYERS HERE
#INPUT PLAYERS HERE

players = ['Chaos','Cat','KV','Aimishi','Russ','Moon','Sketch','Shadow','Lucker','Yum29']


active_scores = []


def lol_teams(scores, players):
    #Have a total variable that keeps track of total score of each team
    #Randomly select 5 players from players check their total score (go through scores array and see if total team score is around total variable score)
    #If true, return a list of 2 tuples with the two teams
    #else, redo


    total_score = 0
    active_scores = []
    average_score = 0
    team_score = 0

    for i in range(len(players)):
        for j in range(len(scores)):
            if players[i] == scores[j][0]:
                active_scores.append((players[i],scores[j][1]))

    print active_scores


#finding the average level in the game
    # for k in active_scores:
    #     print k
    #     for score in k[1]:
    #         print score
    #         total_score += float(score)
    #         average_score = float(total_score)/2
    # print total_score

    # counter = 1
    # for k in active_scores:
    #     for score in k[1]:
    #         if counter == 0:
    #             total_score += float(score) * 10
    #             counter = 1
    #         if counter == 1:
    #             total_score += float(score)
    #             counter = 0
    # print total_score

    k = 0
    while k < 10 :
        total_score += int(active_scores[k][1])
        k += 1
    average_score = float(total_score) / 2
    print average_score


#generating random unique numbers for teams
    numbers = random.sample(range(0, 9), 5)
    for l in numbers:
        team_score += int(active_scores[l][1])
    #team_score = float(team_score) / 5
    print team_score, 'team score'
    # CHANGE THESE VALUES TO CHANGE THE BALANCE STRICTNESS
    # CHANGE THESE VALUES TO CHANGE THE BALANCE STRICTNESS
    # CHANGE THESE VALUES TO CHANGE THE BALANCE STRICTNESS
    # CHANGE THESE VALUES TO CHANGE THE BALANCE STRICTNESS
    # CHANGE THESE VALUES TO CHANGE THE BALANCE STRICTNESS
    # CHANGE THESE VALUES TO CHANGE THE BALANCE STRICTNESS
    # CHANGE THESE VALUES TO CHANGE THE BALANCE STRICTNESS
    # CHANGE THESE VALUES TO CHANGE THE BALANCE STRICTNESS

    if average_score - 3 <= team_score <= average_score + 3:
        team1 = []
        for l in numbers:
            team1.append(players[l])
        print 'Blue team : ', team1
        print team_score
        print total_score
        print average_score
        print total_score - team_score
    else :
        lol_teams(scores,players)
        # try again if it doesn't fit



print lol_teams(scores,players)