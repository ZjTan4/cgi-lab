import templates, secret
import cgi, cgitb
from http.cookies import SimpleCookie
import os

cgitb.enable()

form = cgi.FieldStorage()
cookie = SimpleCookie(os.environ["HTTP_COOKIE"])

cookie_username = cookie.get("Username").value if cookie.get("Username") else None
cookie_password = cookie.get("Password").value if cookie.get("Password") else None

# check match
if cookie_username == secret.username and cookie_password == secret.password:
    print(templates.secret_page(cookie_username, cookie_password))
else:
# no cookie or cookie incorrect, then have to ask user
    input_username = form.getvalue("username")
    input_password = form.getvalue("password")

    if (input_username == None) and (input_password == None):
        print(templates.login_page()) 
    elif (input_username == secret.username and input_password == secret.password):
        # Q4
        """
        print('''<html>
                    <body>
                    <p> <b>username</b>: {input_username}</p> 
                    <p> <b>password</b>: {input_password}</p>
                    </body>
                </html>'''
        )"""
        
        # Q5
        print ("Set-Cookie:Username = {username};")
        print ("Set-Cookie:Password = {password};")
        
        print(templates.secret_page(input_username, input_password))
    else:
        print(templates.after_login_incorrect())