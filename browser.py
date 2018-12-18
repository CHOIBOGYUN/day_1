import webbrowser

q_list = ["bts","아이유"]

url = "https://www.google.com/search?q="

for q in q_list : 
    webbrowser.open(url+q)
