from flask import Flask, render_template, request, redirect, url_for, session, flash
import time
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, EmailField, IntegerField, validators
from wtforms.validators import DataRequired, NumberRange
from sendmail import generate_otp, send_mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisidsecreatkey'


# creating forms
class regestrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    somthing = StringField('somthing', validators=[DataRequired()])
    company = StringField('Company', validators=[DataRequired()])
    submit = SubmitField('Submit')


class otpForm(FlaskForm):
    otp = IntegerField('OTP', validators=[DataRequired(), NumberRange(min=100000, max=999999)])
    submit = SubmitField('Submit')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    new_form = regestrationForm()
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['email'] = request.form['email']
        session['somthing'] = request.form['somthing']
        session['company'] = request.form['company']
        return redirect(url_for('verify_email'))
    else:
        return render_template('register.html', form=new_form)


@app.route('/verificatiton', methods=['GET', 'POST'])
def verify_email():
    if 'email' in session.keys():
        form = otpForm()
        if request.method == 'POST':
            otp = request.form.get('otp')
            if int(session['otp']) == int(otp):
                with open(file='user.txt', mode='a+') as f:
                    f.write(f"{session['name']} {session['email']} {session['somthing']} {session['company']}\n")
                session.pop('name', None)
                session.pop('email', None)
                session.pop('somthing', None)
                session.pop('company', None)
                return "<h1>OTP verified</h1>"
            else:
                session.pop('name', None)
                session.pop('email', None)
                session.pop('somthing', None)
                session.pop('company', None)
                return "<h1>OTP verification failed</h1>"
        else:
            session['otp'] = generate_otp().get_otp()
            send_mail(session['email'], 
                      f'Your otp is {session["otp"]} ,please dont share it with anyone')

            return render_template('verification.html', form=form)
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
