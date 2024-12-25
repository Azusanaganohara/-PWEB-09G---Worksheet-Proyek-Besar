from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from controllers.user import add_penyewa_function, edit_penyewa_function, delete_penyewa_function
from models.user import Penyewa, Users
from extensions import db
from werkzeug.security import check_password_hash
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/testdb', methods=['GET'])
def test_db():
    data = Penyewa.get_all()
    print(data)
    return "Database connection works!"

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Users.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['username'] = user.username
            flash('Login successful!', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Invalid username or password. Please try again.', 'danger')
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

@main.route('/')
def home():
    if 'username' not in session:
        return redirect(url_for('main.login'))
    username = session['username']
    user = Users.query.filter_by(username=username).first()
    data = Penyewa.query.all() if user else None
    return render_template('index.html', user=user, data=data)

@main.route('/datapenyewa', methods=['GET'])
def view_penyewa():
    penyewa_data = Penyewa.get_all()
    return render_template('datapenyewa.html', data=penyewa_data)

@main.route('/addpenyewa', methods=['GET', 'POST'])
def add_penyewa():
    if request.method == 'POST':
        new_penyewa = Penyewa(
            nama_penyewa=request.form['nama_penyewa'],
            no_hp=request.form['no_hp'],
            alamat=request.form['alamat'],
            banyak_box=request.form['banyak_box'],
            tipe_box=request.form['tipe_box'],
            tanggal_penyewaan=datetime.strptime(request.form['tanggal_penyewaan'], '%Y-%m-%d'),
            lama_penitipan=request.form['lama_penitipan'],
            penanggung_jawab=session.get('username')
        )
        db.session.add(new_penyewa)
        db.session.commit()
        flash('Data penyewa berhasil ditambahkan.', 'success')
        return redirect(url_for('main.home'))
    return render_template('addpenyewa.html')

@main.route('/editpenyewa/<int:id>', methods=['GET', 'POST'])
def edit_penyewa(id):
    penyewa = Penyewa.query.get_or_404(id)
    if request.method == 'POST':
        penyewa.nama_penyewa = request.form['nama_penyewa']
        penyewa.no_hp = request.form['no_hp']
        penyewa.alamat = request.form['alamat']
        penyewa.banyak_box = request.form['banyak_box']
        penyewa.tipe_box = request.form['tipe_box']
        penyewa.tanggal_penyewaan = datetime.strptime(request.form['tanggal_penyewaan'], '%Y-%m-%d')
        penyewa.lama_penitipan = request.form['lama_penitipan']
        penyewa.penanggung_jawab = session['username']
        db.session.commit()
        flash('Data penyewa berhasil diubah.', 'success')
        return redirect(url_for('main.home'))
    return render_template('editpenyewa.html', penyewa=penyewa)

@main.route('/deletepenyewa/<int:id>', methods=['POST'])
def delete_penyewa(id):
    penyewa = Penyewa.query.get_or_404(id)
    db.session.delete(penyewa)
    db.session.commit()
    flash('Data penyewa berhasil dihapus.', 'success')
    return redirect(url_for('main.home'))

@main.route('/payment', methods=['POST'])
def payment():
    data = {
        "nama_penyewa": request.form.get('nama_penyewa'),
        "no_hp": request.form.get('no_hp'),
        "alamat": request.form.get('alamat'),
        "banyak_box": request.form.get('banyak_box'),
        "tipe_box": request.form.get('tipe_box'),
        "tanggal_penyewaan": request.form.get('tanggal_penyewaan'),
        "lama_penitipan": request.form.get('lama_penitipan')
    }
    flash('Payment successful!', 'success')
    return render_template('payment.html', data=data)
