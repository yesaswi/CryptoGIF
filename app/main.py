# main.py

from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from cryptosteganography import CryptoSteganography
# import requests

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/encrypt')
@login_required
def encrypt():
    return render_template('encrypt.html')

@main.route('/decrypt')
@login_required
def decrypt():
    return render_template('decrypt.html')

@main.route('/success', methods = ['POST'])
@login_required
def success():
    if request.method == 'POST':  
        f = request.files['file']  
        filename = 'Encrypted.png'
        f.save(f.filename)
        secret = request.form['secret']
        print(secret)
        message = request.form['message']
        print(message)
        crypto_steganography = CryptoSteganography(secret)  
        crypto_steganography.hide(f.filename, filename, message)
        return render_template("success.html", name = filename)

@main.route('/decryptsuccess', methods = ['POST'])
@login_required
def decryptsuccess():
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)
        secret = request.form['secret']
        print(secret)
        crypto_steganography = CryptoSteganography(secret)  
        decryptsecret = crypto_steganography.retrieve(f.filename)
        return render_template("decryptsuccess.html", name = decryptsecret)