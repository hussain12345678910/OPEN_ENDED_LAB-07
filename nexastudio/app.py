from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'nexastudio-secret-key'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        first_name  = request.form.get('first_name')
        last_name   = request.form.get('last_name')
        email       = request.form.get('email')
        service     = request.form.get('service')
        message     = request.form.get('message')

        flash(f"Thanks {first_name}, your message has been sent!", "success")
        return redirect(url_for('contact'))

    return render_template('contact.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        flash("Logged in successfully!", "success")
        return redirect(url_for('index'))

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        email     = request.form.get('email')
        username  = request.form.get('username')
        password  = request.form.get('password')

        flash("Account created! Please log in.", "success")
        return redirect(url_for('login'))

    return render_template('register.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
