from flask import Flask, render_template,request

app=Flask(__name__)

@app.route("/register", methods=['GET','POST'])
def register():
    if request.method=='POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        fullname=request.form['fullname']
        username=request.form['username']
        password=request.form['password']
        email=request.form['email']
        print(fullname)
        print(username)
        print(password)
        print(email) 
        
    return render_template("register.html")

if __name__=="__main__":
    app.run(debug=True)