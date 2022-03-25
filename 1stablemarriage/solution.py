import sys
def main():
    # Read data and initiate dict with women and men's preferences.
    lines_raw = sys.stdin.readlines()
    lines = []
    for i in range(len(lines_raw)):
        lineData =  lines_raw[i].strip().split()
        lineData = list(map(int, lineData))
        lines.extend(lineData)
    nbrPairs = int (lines[0])
    wom_pref = dict()
    men_pref = dict()
    data = lines[1:]
    # Store women's data based on ranking with index as men ids
    # Store men's as input given
    for i in range(0,len(data)//(nbrPairs)-2):
        index = i*(nbrPairs+1)
        lineData =  data[index:index+nbrPairs+1]
        person = lineData[0]
        preferences=lineData[1:]
        if not person in wom_pref:
            # Create women pref list based on indexing
            pref=[None] * (nbrPairs)
            for i in range(nbrPairs):
                pref[preferences[i]-1]=i+1
            wom_pref[person]= pref
        else:
            men_pref[person]= preferences
    # Call matching algorithm to create pairs.
    match(nbrPairs, wom_pref, men_pref)

def match(nbrPairs, wom_pref, men_pref):
    """
    Algorithm structure:
    1. All single men propose to their highest rank not yet proposed to 
    2. Women always get engaged if she is single.
    3. If she is already engaged she breaks the relationship if she gets a proposal from a higher ranked man than her current.
    4. The breaked up men are put back in the single stack and continue proposing
    """
    # Index is woman, number is matched man, -1 means single
    women_pairs = [-1]*nbrPairs
    # Index is man, number is matched woman, -1 means single
    men_pairs = [-1]*nbrPairs

    # List that keeps track of current proposals. 
    # Index is man, value is the proposal index for respective man
    proposal_index_list = [0]*nbrPairs
    # All men are single to start with.
    single_men = list(men_pref.keys())

    """
    Each round. 
    1. All single men propose to their next woman in line
    2. If woman is single - she accepts. 
    3. If she is not single and if the proposing man is ranked higher than the current partner women_pairs, men_pairs update accordingly, single_men update 
    4. If the proposing man is ranked lower, proposing man index update with one.
    """
    while(single_men):
        # Current proposal
        man = single_men.pop(0)
        proposal_index = proposal_index_list[man-1]
        woman_proposed_to = men_pref[man][proposal_index]

        # Check if single woman
        current_partner = women_pairs[woman_proposed_to-1]
        single_woman=current_partner==-1
        if single_woman:
            women_pairs[woman_proposed_to-1]=man # Update women engagement list
            men_pairs[man-1]=woman_proposed_to # Update men engagement list
        elif wom_pref[woman_proposed_to][current_partner-1]>wom_pref[woman_proposed_to][man-1]:
            women_pairs[woman_proposed_to-1]=man
            men_pairs[man-1]=woman_proposed_to
            men_pairs[current_partner-1]=-1 
            proposal_index_list[current_partner-1]+=1
            single_men.append(current_partner)
        else:
            proposal_index_list[man-1]+=1
            single_men.append(man)

    for man in women_pairs:
        print(man)


main()


