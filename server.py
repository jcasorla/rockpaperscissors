from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'     # Create a new instance of the Flask class called "app"
import random

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    
    
    return render_template("index.html")

@app.route('/results', methods = ["POST"])          # The "@" decorator associates this route with the function immediately following
def results():

    
    rpsDict={ "rock": {"paper":"lose", "scissors": "win","rock":"tie"},
            "paper": {"paper": "tie", "scissors": "win","rock": "lose"},
            "scissors": {"paper": "win", "scissors": "tie","rock": "lose"}
    }
    
    p1= request.form["p1"]
    random_key = random.choice(list(rpsDict.keys()))
    print(rpsDict[p1][random_key] )
    session['result'] = rpsDict[p1][random_key]
    session['p1'] = p1
    session['p2'] = random_key
    return redirect("/")

@app.route('/destroy')
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.