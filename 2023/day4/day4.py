from data import data

test = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

class cardDB:

    def __init__(self, data: str):
        self.cardPairs = getCardPairs(data)
        self.counts = self.__initializeCounts()

### PUBLIC ###

    def updateCardCounts(self):
        for i in range(len(self.cardPairs)):
            matches = self.__findMatches(i)
            for j in range(matches):
                self.counts[i + j + 1][1] += self.counts[i][1]

    def displayCounts(self):
        print(self.counts)

    def totalCardCount(self):
        total = 0
        for card in self.counts:
            total += card[1]
        return total
### PRIVATE ###

    def __initializeCounts(self):
        counts = []
        for i in range(len(self.cardPairs)):
            counts.append([i + 1, 1])
        return counts
    
    def __findMatches(self, whichPair: int) -> int:
        """
        update self.counts with number of cards present using rules from part 2 of puzzle
        """
        matches = 0
        pair = self.cardPairs[whichPair]
        # find number of matches
        for element in pair[0]:
            if element in pair[1]:
                print(f'match found {element}')
                matches += 1
        return matches



def getCardPairs(data: str):
    cardPairs = []
    data = data.splitlines()
    for line in data:
        line = line.split(':')
        line = line[1].strip().split("|")
        cardPairs.append((line[0].strip(" ").split(), line[1].strip(" ").split()))
    return cardPairs

def findMatchingNumbers(cardPairs: tuple):
    total = 0
    for i, pair in enumerate(cardPairs):
        print(f'checking card {i}')
        matches = 0
        for element in pair[0]:
            if element in pair[1]:
                print(f'match found {element}')
                matches += 1
        if matches > 0:
            total += (2 ** (matches - 1))
    print(total)

def main():
    cards = cardDB(data)
    cards.updateCardCounts()
    print(cards.totalCardCount())
#    cardPairs = getCardPairs(data)
#    findMatchingNumbers(cardPairs)

main()
