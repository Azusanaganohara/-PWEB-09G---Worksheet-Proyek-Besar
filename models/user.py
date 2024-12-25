from extensions import db
from flask import session, flash, url_for, redirect, render_template, request
from werkzeug.security import check_password_hash, generate_password_hash

def login_user():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = Users.query.filter_by(username=username).first()  
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Login berhasil!', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Username atau password salah!', 'danger')
    return render_template('login.html')

def register_user():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        level = request.form.get('level')

        existing_user = Users.query.filter_by(username=username).first()  
        if existing_user:
            flash('Username sudah terdaftar!', 'danger')
        else:
            new_user = Users(
                username=username,
                password=generate_password_hash(password),
                level=level
            )
            db.session.add(new_user)
            db.session.commit()
            flash('Registrasi berhasil! Silakan login.', 'success')
            return redirect(url_for('main.login'))
    return render_template('registrasi.html')


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()
        

class Penyewa(db.Model):
    __tablename__ = 'penyewa'
    id = db.Column(db.Integer, primary_key=True)
    nama_penyewa = db.Column(db.String(80), nullable=False, unique=False)
    no_hp = db.Column(db.String(80), nullable=False, unique=False)
    alamat = db.Column(db.String(80), nullable=False, unique=False)
    banyak_box = db.Column(db.Integer, nullable=False, unique=False)
    tipe_box = db.Column(db.String(80), nullable=False, unique=False)
    tanggal_penyewaan = db.Column(db.Date, nullable=False)
    lama_penitipan = db.Column(db.Integer, nullable=False, unique=False)
    penanggung_jawab = db.Column(db.String(50), nullable=True, unique=False)
    
    @property
    def data(self):
        return {
            'id': self.id,
            'nama_penyewa': self.nama_penyewa,
            'no_hp': self.no_hp,
            'alamat': self.alamat,
            'banyak_box': self.banyak_box,
            'tipe_box': self.tipe_box,
            'tanggal_penyewaan': self.tanggal_penyewaan,
            'lama_penitipan': self.lama_penitipan,
            'penanggung_jawab': self.penanggung_jawab
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()   
        
    @classmethod
    def get_all(cls):
        r = cls.query.all()
        result = []
        
        for i in r:
            result.append(i.data)
        return result
    
    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()