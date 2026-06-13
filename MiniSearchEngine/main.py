import json

## SEARCH FUNCTION
def searchKeywordForAny(data: dict, keywords):
    # SINGLE KEYWORD FUNCTION
    if isinstance(keywords, str) and keywords != "":
        try:
            keywords = keywords.lower()
        except AttributeError:
            print("Invalid Keyboard")
            return []

        matchesDict = {}
        counter = {}
        for doc, text in data.items():
            if keywords in str(text).lower():

                if keywords not in matchesDict:
                    matchesDict[keywords] = {}
                if doc not in matchesDict[keywords]:
                    matchesDict[keywords][doc] = ''
                matchesDict[keywords][doc] = text    

                if keywords not in counter:
                    counter[keywords] = 0
                counter[keywords] += 1

        return matchesDict, counter
    # MULTIPLE KEYWORDS FUNCTION
    elif isinstance(keywords,list) and keywords != []:
        matchesDict = {}
        counter = {}
        for word in keywords:
            try:
                word = word.lower()
            except AttributeError:
                print("Invalid Keyboard")
                continue
            
            if word not in matchesDict:
                matchesDict[word] = {}

            for doc, text in data.items():  
                if word in str(text).lower():
                    if doc not in matchesDict[word] :
                        matchesDict[word][doc] = ""
                    matchesDict[word][doc] = text
                    
                    if word not in counter:
                        counter[word] = 0
                    counter[word] += 1

        return matchesDict, counter
    else:
        return {}, 0

## TITLE PRINTING
def printTitle(filename)->None:
    print("## MINI SEARCH ENGINE ##")
    print(f"Searching in {filename}...")

## GETTING USER INPUT
def getUserInput():
    userInput = input("Insert Keyword: ").lower()
    if "," in userInput:
        splittedInput = userInput.split(",")
        if len(splittedInput) != len(set(splittedInput)):
            while True:
                duplicated = input("There are duplicated keywords, desconsider these duplicated ones and continue searching?(Y/N): ").lower()
                if duplicated == ("y" or "yes"):
                    return list(set(splittedInput))
                elif duplicated == ("n" or "no"):
                    return ""
                else:
                    print("Invalid input, try again.")
    else:
        return userInput

## OPENING INPUT JSON FILE
inputJson = "input.json"
with open(inputJson, 'r') as initialFile:
    documents = json.load(initialFile)

keyword = getUserInput()
matches, counter = searchKeywordForAny(documents, keyword)

## CHECKING IF KEYWORD IS SINGLE KEYWORD OR MULTIPLE KEYWORDS
keyword = [keyword] if isinstance(keyword, str) else keyword

results = {}
if matches != {}:
    results = {
        key: matches[key]
        for key in keyword
    }
else:
    print("No documents found")

## COUNTING MATCHES
for key in keyword:
    if key in counter:
        print(f"Matches in '{key}': {counter[key]}")

## WRITING OUTPUT JSON
outputJson = "output.json"
with open(outputJson, 'w') as finalFile:
    if results:
        json.dump(results, finalFile, indent=4)
        print(f"Searching results located at {outputJson}")
    else:
        print("No file writing was made")
    


