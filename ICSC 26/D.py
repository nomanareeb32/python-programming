def recheck(events, H):
    p_1_hp = H  #Assigning the individual HP
    p_2_hp = H

    #Sorting ONLY by frame number and not by player or attack value, since events arrive in arbitrary order due to network jitter
    events = sorted(events, key=lambda e: e[1])

    i = 0  #Index that tracks our position in the previously sorted events

    #We must keep processing frame-groups until we hit a KO, double KO, or run out of events
    while i < len(events):
        frame = events[i][1]

        #Step 1: Using a for loop to collect every event sharing this same frame
        same_frame = []
        for e in events[i:]:
            if e[1] == frame:
                same_frame.append(e)
            else:
                break  #We must stop once we reach a different frame

        #Step 2: Using a for loop to go through each tuple in this frame and apply its damage
        for player, _, attack_value in same_frame:
            if player == 1:
                p_2_hp -= attack_value  #player 1 hits player 2
            else:
                p_1_hp -= attack_value  #player 2 hits player 1

        #Now we shall move our index past everything we just processed
        i += len(same_frame)

        #Step 3: Repeat and check only now, after the WHOLE frame has been applied, do we check for a KO
        if p_1_hp <= 0 or p_2_hp <= 0:
            break
        #If neither is true, the while loop just continues to the next frame

    #Clamping HP so it never shows as negative
    if p_1_hp <= 0:
        p_1_hp = 0
    if p_2_hp <= 0:
        p_2_hp = 0

    #Building the resultant list
    result = [p_1_hp, p_2_hp]

    return result

#Taking Inputs
events = eval(input())  # Ex: [(1, 512, 20), (2, 512, 20)]
H = int(input())  # Starting HP

#Run and Print
result = recheck(events, H)
print(result)
