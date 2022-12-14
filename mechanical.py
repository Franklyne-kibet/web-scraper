import mechanicalsoup  
browser = mechanicalsoup.Browser()

#get the page contents
url = "http://olympus.realpython.org/login"
login_page =browser.get(url)
login_html = login_page.soup

#get the login form 
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

#submit the login form 
profiles_page = browser.submit(form,login_page.url)

#check if you have successfully logged in 
print(profiles_page.url)