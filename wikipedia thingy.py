import wikipedia
import warnings

loop = True
while loop:
    warnings.catch_warnings()
    warnings.simplefilter("ignore")
    
    print("\nWIKIPEDIA THING\n")
    userSearch = input("Search: ")

    searchTerms = wikipedia.search(userSearch, results=10)

    thereAreResults = True
    for i in range(10):
        try: 
            print(f"({i}) {searchTerms[i]}")
        except IndexError:
            print("No results were found lol imagine")
            thereAreResults = False
            break
    if thereAreResults:
        chosenArticle = int(input("What article do you want to read?\n"))
        try:
            chosenPage = wikipedia.page(searchTerms[chosenArticle], auto_suggest=False)
            print(f"Summary:\n{chosenPage.summary}")
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"\nDo you mean:")
            options = e.options
            for j in range(len(e.options)):
                print(f"({j}) {options[j]}")
            chosenOption = int(input("What option do you want to read?\n"))
            chosenOptionPage = wikipedia.page(options[chosenOption], auto_suggest=False)
            print(f"Summary:\n{chosenOptionPage.summary}")


    

