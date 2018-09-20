#!/usr/bin/env python3

def main():
    ''' Read words, sort '''
    accum = 0
    words = open("euler22.txt", "r").readline().replace("\"", "").split(",")
    words = sorted(words)
    for i in range(0, len(words)):
        score = sum([ord(letter) - ord('A') + 1 for letter in words[i]])
        print(words[i],i+1,":",score)
        accum = accum + ((i + 1) * score)
    print("Accumulation:", accum)
if __name__ == "__main__":
    main()
