## Email OTP Verification using the flask and SMTPLIB module of Python
Set up send_mail.py by adding sender's email address and app password (Only work for Gmail accounts).
Install flask, wtf-flask, and other necessary modlues

# Two-Factor Authentication Web Application

This is a simple Flask-based web application that implements Two-Factor Authentication (2FA) using email for additional security during user login. When a user attempts to log in, a unique authentication code is sent to their email, which must be entered to complete the login process.

## Requirements

- Flask
- Flask-Login
- smtplib (Python standard library)

You can install the necessary dependencies by running the following command:

```bash
pip install Flask Flask-Login
```

## Steps to Run

### 1. **Create an App Password for Gmail**  
If you're using Gmail to send the 2FA code, you'll need to create an **App Password**.  
- Go to your [Google Account Settings](https://myaccount.google.com).
- Under the **Security** section, turn on **2-Step Verification** (if you haven’t already).
- Create an **App Password** for sending emails.

### 2. **Add the Gmail Sender and App Password**  
After you have the app password, add the email sender (your Gmail address) and the generated app password to the `sendmail.py` file.

```python
# sendmail.py
sender_email = "your-email@gmail.com"
app_password = "your-app-password"
```

### 3. **Run the Application**  
Start the Flask application by running the following command:

```bash
python web.py
```


- The application uses Flask-Login for session management and user authentication built from scratch.

