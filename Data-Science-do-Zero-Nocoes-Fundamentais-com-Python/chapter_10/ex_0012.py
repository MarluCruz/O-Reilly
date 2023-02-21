def interlock(compoundNoun, simpleNoun):
    for i in range(len(simpleNoun)):
        for j in range(len(simpleNoun)):
            newWord = simpleNoun[i] + simpleNoun[j]
            for x in range(len(compoundNoun)):
                if newWord == compoundNoun[x]:
                    print(newWord)

compoundNoun = ['battlefield', 'windscreen', 'bathroom', 'classroom']
simpleNoun = ['battle', 'wind', 'bath', 'class', 'field', 'screen', 'room']
interlock(compoundNoun, simpleNoun)

