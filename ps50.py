                #DAY 15

#repl.it does't run your code on your computer, it runs the code in a "large datacenter somewhere else". The code wouldn't open URLs on your computer because that isn't where the processes are being run.
# because of this we cannot run this program in repl.it

import webbrowser

user_term = input("Enter user term")
webbrowser.open("https://www.google.co.in/search?q=python")


'''  to open google browser

import webbrowser

webbrowser.open("https://google.com")

'''

