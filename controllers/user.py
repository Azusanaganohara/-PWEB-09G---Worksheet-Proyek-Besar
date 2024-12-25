from flask import request, session, flash, url_for, redirect, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import Penyewa, Users
from extensions import db

def add_penyewa_function():
    if request.method == 'POST':
        nama_penyewa = request.form['nama_penyewa']
        no_hp = request.form['no_hp']
        alamat = request.form['alamat']
        banyak_box = request.form['banyak_box']
        tipe_box = request.form['tipe_box']
        tanggal_penyewaan = request.form['tanggal_penyewaan']
        lama_penitipan = request.form['lama_penitipan']
        penanggung_jawab = session.get('username')  

        penyewa = Penyewa(
            nama_penyewa=nama_penyewa,
            no_hp=no_hp,
            alamat=alamat,
            banyak_box=banyak_box,
            tipe_box=tipe_box,
            tanggal_penyewaan=tanggal_penyewaan,
            lama_penitipan=lama_penitipan,
            penanggung_jawab=penanggung_jawab
        )
        
        penyewa.save()
        data = {
            'id': penyewa.id,
            'nama_penyewa': penyewa.nama_penyewa,
            'no_hp': penyewa.no_hp,
            'alamat': penyewa.alamat,
            'banyak_box': penyewa.banyak_box,
            'tipe_box': penyewa.tipe_box,
            'tanggal_penyewaan': penyewa.tanggal_penyewaan,
            'lama_penitipan': penyewa.lama_penitipan,
            'penanggung_jawab': penyewa.penanggung_jawab
        }
        return data

        
def edit_penyewa_function(data):
    if request.method == 'POST':
        data.nama_penyewa = request.form['nama_penyewa']
        data.no_hp = request.form['no_hp']
        data.alamat = request.form['alamat']
        data.banyak_box = request.form['banyak_box']
        data.tipe_box = request.form['tipe_box']
        data.tanggal_penyewaan = request.form['tanggal_penyewaan']
        data.lama_penitipan = request.form['lama_penitipan']
        data.penanggung_jawab = session.get('username') 
        
        db.session.commit()
        return data

    
def delete_penyewa_function(penyewa):
    db.session.delete(penyewa)  
    db.session.commit()
    pass