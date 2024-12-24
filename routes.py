from flask import Blueprint, render_template, request, redirect, url_for
from controllers.user import add_penyewa_function, edit_penyewa_function, delete_penyewa_function
import sys
from models.user import Penyewa

main = Blueprint('main', __name__) # routename = main

@main.route('/testdb', methods=['GET'])
def test_db():
    data = Penyewa.get_all()
    print(data)
    return "Database connection works!" # akses http://127.0.0.1:5000/testdb untuk tes db

@main.route('/', methods=['GET'])
def home():
    data = Penyewa.get_all()
    return render_template('index.html', data=data)

@main.route('/addpenyewa', methods=['GET', 'POST'])
def add_penyewa():
    if request.method == 'POST':
        nama_penyewa = request.form.get('nama_penyewa')
        no_hp = request.form.get('no_hp')
        alamat = request.form.get('alamat')
        banyak_box = request.form.get('banyak_box')
        tipe_box = request.form.get('tipe_box')
        tanggal_penyewaan = request.form.get('tanggal_penyewaan')
        lama_penitipan = request.form.get('lama_penitipan')

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
        return redirect('/')
    return render_template('addpenyewa.html')


@main.route('/editpenyewa/<int:id>', methods=['GET','POST'])
def edit_penyewa(id):
    penyewa = Penyewa.get_by_id(id)
    data =  edit_penyewa_function(penyewa)
    return render_template('editpenyewa.html', penyewa=penyewa, data=data)

@main.route('/deletepenyewa/<int:id>', methods=['GET', 'POST'])
def delete_penyewa(id):
    penyewa = Penyewa.get_by_id(id)
    data = delete_penyewa_function(penyewa)
    return redirect(url_for('main.home'))    
