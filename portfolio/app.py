from flask import Flask, render_template, request, redirect, flash, url_for
import smtplib
import sqlite3
from email.mime.text import MIMEText

app = Flask(__name__)
app.secret_key = '7571a735345b7840559d68662cc153f6'  # Replace with your actual secret key

@app.route('/')
def home():
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/projects')
def projects():
    return render_template('projects.html', title='Projects')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Prepare email
        if not name or not email or not message:
            flash('All fields are required!', 'error')
            return redirect(url_for('contact'))
        
        send_email(name, email, message)
        flash('Message sent successfully!', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html', title='Contact')

def send_email(name, email, message):
    sender_email = "mzaid7913@gmail.com"
    sender_password = "czqv vgtp ubjt hrvn"
    recipient_email = "mzaid7913@gmail.com"

    subject = f"New contact form submission from {name}"
    body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == '__main__':
    app.run(debug=True)