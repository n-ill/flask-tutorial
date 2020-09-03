from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'fe225f22ad6157b6c1dae8f79c359bdb' #key created by secrets module using
                                                                #secrets.token_hex(16) - 16 is num of bytes

posts = [
    {
        'author': 'Bob Smith',
        'title': 'Blog Post 1',
        'content': 'first post content',
        'date_posted': 'September 1, 2020'
    },
    {
        'author': 'Rob White',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'date_posted': 'September 2, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts) # posts= allows us to access the value of that variable from
                                                        # the template, using the posts variable

@app.route('/about')
def about():
    return render_template('about.html', title='About')

#methods are the allowed methods, POST is the method used when we sumbit a register form
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success') #second arg is the type of message, eg error etc
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('Login Successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)