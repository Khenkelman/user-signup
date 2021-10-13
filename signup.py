from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>
<html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 440px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                form input {{
                    margin: 5px 0;
                }}
                form span {{
                    font-size: 8pt;
                }}
            </style>
        </head>
        <body>
            <form action = "http://localhost:5000/validate" method = "POST">
                    <label>Email:</label>
                    <input name="email" type="text" value={0}><span> {1}</span><br>
                    <label>Username:</label>
                    <input name="username" type="text" value={2}><span> {3}</span><br>
                    <label>Password:</label>
                    <input name="password" type="password" value=""><span> {4}</span><br>
                    <label>Verify Password:</label>
                    <input name="vPassword" type="password" value=""><span> {5}</span><br>
                     <button type="submit" name="submit" value="submit">Submit Query</button>
            </form> 
        </body>
    </html>
"""
welcome = """
<!DOCTYPE html>
<html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 440px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                    text-align: center;
                }}
            </style>
        </head>
        <body>
            <form>
                <label>Welcome {0}!</label>
            </form> 
        </body>
    </html>
"""
@app.route("/", methods = ["POST", "GET"] )
def index():
    return form.format("","","","","")


@app.route('/validate', methods = ["POST", "GET"])
def encrypt():
    validEmail= 1
    validUsername= 1
    validPassword= 1
    validVPassword= 1
    email= request.form.get('email')
    username= request.form.get('username')
    password= request.form.get('password')
    vPassword= request.form.get('vPassword')
    if not email:                  # if empty string
        validEmail= 1
    elif "@" in email:                  # if "@" in string
        if "." in email:                  # if "." in string
            if not " " in email:             # if no " " in string
                if 3<= len(email) <= 20:    # if 3-20 char long
                    validEmail = 1
                else:
                    validEmail=0
            else:
                validEmail = 0
        else:
            validEmail = 0
    else:
        validEmail = 0
    if " " in username:                 # if space is in string
        validUsername = 0
    elif not username:                  # if empty string
        validUsername = 0
    elif not 3 <= len(username) <= 20:  # if 3 - 20 char long
        validUsername = 0
    else:
        validUsername = 1
    if " " in password:                 # if space is in string
        validPassword = 0
    elif not password:                  # if empty string
        validPassword = 0
    elif not 3 <= len(password) <= 20:  # if 3 - 20 char long
        validPassword = 0
    else:
        validPassword = 1
    if vPassword == password:
        validVPassword = 1
    else:
        validVPassword = 0
    if validEmail == 0:
        emailTxt = "Incorrect E-mail Format"
    elif validEmail == 1:
        emailTxt = ""
    if validUsername == 0:
        usernameTxt = "Incorrect Username Format"
    elif validUsername == 1:
        usernameTxt = ""
    if validPassword == 0:
        passwordTxt = "Incorrect Password Format"
    elif validPassword == 1:
        passwordTxt = ""
    if validVPassword == 0:
        vPasswordTxt = "Your Passwords Don't Match"
    elif validVPassword == 1:
        vPasswordTxt = ""
    if validEmail == 1:
        if validUsername == 1:
            if validPassword == 1:
                if validVPassword == 1:
                    return welcome.format(username)
    return form.format(email, emailTxt, username, usernameTxt, passwordTxt, vPasswordTxt)
    
    
app.run()