continue_play = 'Y'
while(continue_play == 'Y'):

    print('format- known letter placements, known letters, known bad placements, known nonletters')
    known_unknown = input("Enter word metadata: ")
    known, unknown, nip, niw = known_unknown.split(" ")
    known = known.lower()
    unknown = unknown.lower()
    niw = niw.lower()
    
    bad_places = nip.split(",")
    
    
    possibilities = []
    isword = True
    continue_play = 'Y'

    for line in open('wordledict.txt', 'r'):
        line = line.lower()
        for char_index in range(len(known)):
            if known[char_index] != "_":
                if line[char_index] != known[char_index]:
                    isword = False
        for char in unknown:
            if char not in line:
                isword = False
        for ind in range(len(bad_places)):
            for letter in bad_places[ind]:
                if letter == line[ind]:
                    isword = False
                    
        for char in niw:
            if char in line:
                isword = False
                
        if isword:
            possibilities.append(line.rstrip())
        isword = True

    for word in possibilities:
        print(word)
        
    continue_play = input("Continue playing? Enter Y for yes ")
        