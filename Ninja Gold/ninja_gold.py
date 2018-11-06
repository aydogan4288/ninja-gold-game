from flask import Flask, render_template, request, redirect, session
import random
app= Flask (__name__)
app.secret_key = 'VeryVerySecret'

@app.route('/', methods = ['GET'])
def index():
    if 'total' not in session:
        session['total'] = 0
    return render_template('index.html')

@app.route('/process_money', methods = ['POST'])
def process_money():
    if request.form['building'] == 'farm':
        session['total']+= random.randint(10,20)
        print('FARM!!!')
        print(random.randint(10,20))
    elif request.form['building'] == 'Cave':
        print("CAVE!!!")
        session['total'] += random.randint(5,10)
    elif request.form['building'] == 'House':
        print('HOUSE!!!')
        session['total'] += random.randint(2,5)
    elif request.form['building'] == 'Casino':
        session['total'] += random.randint(-50,50)
        
    return redirect('/')

@app.route('/reset', methods = ['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)