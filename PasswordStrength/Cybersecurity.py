from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML template for the web page
HTML = '''


<!doctype html>
<title>Is Your password strong enough?</title>
<style>
    body { display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background: #f7f7f7; }
    .center-box {
        background: #fff;
        padding: 2rem 3rem;
        border-radius: 10px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.08);
        text-align: center;
    }

    input[type="password"] {
        padding: 0.5rem;
        margin-right: 0.5rem;
        border-radius: 5px;
        border: 1px solid #ccc;
    }
    input[type="submit"] {
        padding: 0.5rem 1rem;
        border-radius: 5px;
        border: none;
        background: #0078d7;
        color: #fff;
        cursor: pointer;
    }
</style>
<div class="center-box">
    <h2>Check Your Password Strength</h2>
    <form method="post">
        <input type="password" name="password" placeholder="Enter password" required>
        <input type="submit" value="Check">
    </form>
    {% if strength %}
        <p>Password strength: <b>{{ strength }}</b></p>
    {% endif %}
</div>
'''

# Simple password strength checking function
def check_strength(password):
    if len(password) < 6:
        return "Weak"
    elif len(password) < 10:
        return "Medium"
    else:
        return "Strong"
    

# route to handle form submission and then displays the result

@app.route('/', methods=['GET', 'POST'])
def index():
    strength = None
    if request.method == 'POST':
        pwd = request.form['password']
        strength = check_strength(pwd)

    return render_template_string(HTML, strength=strength)
# runs the application
if __name__ == '__main__':
    app.run(debug=True)
