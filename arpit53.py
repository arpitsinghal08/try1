# coroutines

def searcher():
    import time
    #some 4 sec consuming task
    book="hello hi bye bye"
    time.sleep(4)


    while(1):
        text=(yield )
        if text in book:
            print("your text in book")

        else:
            print("text is not in book")

search=searcher()
print("search started")
next(search)
search.send("hi")
search.send("bye")
search.close()