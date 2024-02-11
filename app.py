from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    zahl1= float(request.form['1.Zahl'])
    zahl2= float=(request.form['2.Zahl'])
    ergebnis=zahl1+zahl2
    
    return f'Der eingegebene Benutzername ist: {ergebnis}'

if __name__ == '__main__':
    app.run(debug=True)
