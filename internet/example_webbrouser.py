import webbrowser

browser = webbrowser.get()

url = 'https://www.unrealsoft.net/updates/touchsale2/'
username = browser.find_element_by_id("user_input_id")
webbrowser.open(url)