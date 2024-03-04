from flask import Flask, render_template, request, session
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route('/', methods=["GET", "POST"])
def index():
    if 'notes' not in session:
        session['notes'] = []

    if request.method == "POST":
        note = request.form.get("note")
        session['notes'].append(note)
        print("Notes in session:", session['notes'])  
    
    return render_template("home.html", notes=session.get('notes', []))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
