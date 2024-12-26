from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from controllers.user import add_penyewa_function, edit_penyewa_function, delete_penyewa_function
from models.user import Penyewa, Users
from werkzeug.security import check_password_hash
from extensions import db
from datetime import datetime
from werkzeug.security import generate_password_hash

main = Blueprint('main', __name__)  # routename = main

@main.route('/testdb', methods=['GET'])
def test_db():
    try:
        data = Penyewa.get_all()
        print(data)
        return "Database connection works!"
    except Exception as e:
        print(f"Database connection error: {e}")
        return "Database connection failed!", 500

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
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = Users(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registrasi berhasil! Silakan login.', 'success')
        return redirect(url_for('main.login'))
    return render_template('registrasi.html')

@main.route('/datapenyewa', methods=['GET'])
def view_penyewa():
    penyewa_data = Penyewa.query.all()
    return render_template("datapenyewa.html", data=penyewa_data)  

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

@main.route('/addpenyewa', methods=['GET', 'POST'])
def add_penyewa():
    if request.method == 'POST':
        try:
            nama_penyewa = request.form.get('nama_penyewa')
            no_hp = request.form.get('no_hp')
            alamat = request.form.get('alamat')
            banyak_box = int(request.form.get('banyak_box'))
            tipe_box = request.form.get('tipe_box')
            tanggal_penyewaan = datetime.strptime(request.form.get('tanggal_penyewaan'), '%Y-%m-%d')
            lama_penitipan = int(request.form.get('lama_penitipan'))
            penanggung_jawab = session.get('username')

            new_penyewa = Penyewa(
                nama_penyewa=nama_penyewa,
                no_hp=no_hp,
                alamat=alamat,
                banyak_box=banyak_box,
                tipe_box=tipe_box,
                tanggal_penyewaan=tanggal_penyewaan,
                lama_penitipan=lama_penitipan,
                penanggung_jawab=penanggung_jawab
            )
            db.session.add(new_penyewa)
            db.session.commit()
            flash('Penyewa berhasil ditambahkan.', 'success')
            return redirect(url_for('main.home'))
        except Exception as e:
            flash(f'Error: {e}', 'danger')
    
    return render_template('addpenyewa.html')


@main.route('/editpenyewa/<int:id>', methods=['GET', 'POST'])
def edit_penyewa(id):
    penyewa = Penyewa.query.get_or_404(id)
    if request.method == 'POST':
        try:
            penyewa.nama_penyewa = request.form['nama_penyewa']
            penyewa.no_hp = request.form['no_hp']
            penyewa.alamat = request.form['alamat']
            penyewa.banyak_box = int(request.form['banyak_box'])
            penyewa.tipe_box = request.form['tipe_box']
            penyewa.tanggal_penyewaan = datetime.strptime(request.form['tanggal_penyewaan'], '%Y-%m-%d')
            penyewa.lama_penitipan = int(request.form['lama_penitipan'])
            penyewa.penanggung_jawab = session['username']

            db.session.commit()
            flash('Data penyewa berhasil diubah.', 'success')
            return redirect(url_for('main.home'))
        except Exception as e:
            flash(f'Error: {e}', 'danger')
    return render_template('editpenyewa.html', penyewa=penyewa)

@main.route('/deletepenyewa/<int:id>', methods=['POST'])
def delete_penyewa(id):
    try:
        penyewa = Penyewa.query.get_or_404(id)
        db.session.delete(penyewa)
        db.session.commit()
        flash('Data penyewa berhasil dihapus.', 'success')
    except Exception as e:
        flash(f'Error: {e}', 'danger')
    return redirect(url_for('main.home'))

@main.route('/payment', methods=['POST'])
def payment():
    if request.method == 'POST':
        try:

            nama_penyewa = request.form.get('nama_penyewa')
            no_hp = request.form.get('no_hp')
            alamat = request.form.get('alamat')
            banyak_box = request.form.get('banyak_box')
            tipe_box = request.form.get('tipe_box')
            tanggal_penyewaan = request.form.get('tanggal_penyewaan')
            lama_penitipan = request.form.get('lama_penitipan')
            penanggung_jawab = session.get('username')


            if not all([nama_penyewa, no_hp, alamat, banyak_box, tipe_box, tanggal_penyewaan, lama_penitipan]):
                flash('Semua field harus diisi.', 'error')
                return render_template('payment.html')

            banyak_box = int(banyak_box)
            lama_penitipan = int(lama_penitipan)

            new_penyewa = Penyewa(
                nama_penyewa=nama_penyewa,
                no_hp=no_hp,
                alamat=alamat,
                banyak_box=banyak_box,
                tipe_box=tipe_box,
                tanggal_penyewaan=tanggal_penyewaan,  
                lama_penitipan=lama_penitipan,
                penanggung_jawab=penanggung_jawab
            )
            db.session.add(new_penyewa)
            db.session.commit()

            flash('Penyewa berhasil ditambahkan.', 'success')

            data = {
                "nama_penyewa": nama_penyewa,
                "no_hp": no_hp,
                "alamat": alamat,
                "banyak_box": banyak_box,
                "tipe_box": tipe_box,
                "tanggal_penyewaan": tanggal_penyewaan,
                "lama_penitipan": lama_penitipan,
                "penanggung_jawab": penanggung_jawab
            }
            return render_template('payment.html', data=data)

        except ValueError:
            flash('Data yang dimasukkan tidak valid.', 'error')
            return render_template('payment.html')
        except Exception as e:
            flash(f'Terjadi kesalahan: {str(e)}', 'error')
            return render_template('payment.html')

    flash('Metode tidak valid.', 'error')
    return render_template('payment.html')
