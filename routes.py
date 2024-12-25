from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from controllers.user import add_penyewa_function, edit_penyewa_function, delete_penyewa_function
import sys
from models.user import Penyewa, Users
from werkzeug.security import check_password_hash
from extensions import db
from datetime import datetime


main = Blueprint('main', __name__)

@main.route('/testdb', methods=['GET'])
def test_db():
    data = Penyewa.get_all()
    print(data)
    return "Database connection works!"

@main.route('/', methods=['GET'])
def home():
    data = Penyewa.get_all()
    return render_template('index.html', data=data)

@main.route('/datapenyewa', methods=['GET'])
def view_penyewa():
    penyewa_data = Penyewa.get_all()
    return render_template('datapenyewa.html', data=penyewa_data)

def save_penyewa(form_data):
    nama_penyewa = form_data.get('nama_penyewa')
    no_hp = form_data.get('no_hp')
    alamat = form_data.get('alamat')
    banyak_box = form_data.get('banyak_box')
    tipe_box = form_data.get('tipe_box')
    tanggal_penyewaan = form_data.get('tanggal_penyewaan')
    lama_penitipan = form_data.get('lama_penitipan')

    new_penyewa = Penyewa(
        nama_penyewa=nama_penyewa,
        no_hp=no_hp,
        alamat=alamat,
        banyak_box=banyak_box,
        tipe_box=tipe_box,
        tanggal_penyewaan=tanggal_penyewaan,
        lama_penitipan=lama_penitipan
    )
    new_penyewa.save()

@main.route('/addpenyewa', methods=['GET', 'POST'])
def add_penyewa():
    if request.method == 'POST':
        save_penyewa(request.form)
        return redirect('/')
    return render_template('addpenyewa.html')

@main.route('/payment', methods=['POST'])
def payment():
    if request.method == 'POST':
        save_penyewa(request.form)
    data = {
        "nama_penyewa": request.form.get('nama_penyewa'),
        "no_hp": request.form.get('no_hp'),
        "alamat": request.form.get('alamat'),
        "banyak_box": request.form.get('banyak_box'),
        "tipe_box": request.form.get('tipe_box'),
        "tanggal_penyewaan": request.form.get('tanggal_penyewaan'),
        "lama_penitipan": request.form.get('lama_penitipan')
    }
    return render_template('payment.html', data=data)

@main.route('/editpenyewa/<int:id>', methods=['GET', 'POST'])
def edit_penyewa(id):
    penyewa = Penyewa.get_by_id(id)
    data = edit_penyewa_function(penyewa)
    return render_template('editpenyewa.html', penyewa=penyewa, data=data)

@main.route('/deletepenyewa/<int:id>', methods=['POST'])
def delete_penyewa(id):
    penyewa = Penyewa.get_by_id(id)
    if penyewa:
        try:
            Penyewa.delete(penyewa)
            print(f"Penyewa with ID {id} deleted successfully.")
        except Exception as e:
            print(f"Error deleting penyewa with ID {id}: {e}")
            return "Internal Server Error", 500
        return redirect('/')
    print(f"Penyewa with ID {id} not found.")
    return "Data tidak ditemukan", 404



@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Users.query.filter_by(username=username).first()

        if user and user.password == password: 
            session['username'] = user.username
            flash('Login successful!', 'success')
            
            print(f"Current session after login: {session}")

            return redirect(url_for('main.home')) 
        else:
            flash('Invalid username or password. Please try again.', 'danger')
            print("Invalid login attempt")  
    return render_template('login.html')

@main.route('/registrasi', methods=['GET', 'POST'])
def registrasi():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        new_user = Users(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registrasi berhasil! Silakan login.', 'success')
        return redirect(url_for('main.login'))

    return render_template('registrasi.html')


@main.route('/logout', methods=['POST'])
def logout():
    session.clear() 
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.login'))  

