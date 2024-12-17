from extensions import db

class Penyewa(db.Model):
    __tablename__ = 'penyewa'
    id = db.Column(db.Integer, primary_key=True)
    nama_penyewa = db.Column(db.String(80), nullable=False, unique=False)
    no_hp = db.Column(db.String(80), nullable=False, unique=False)
    alamat = db.Column(db.String(80), nullable=False, unique=False)
    banyak_box = db.Column(db.Integer, nullable=False, unique=False)
    tipe_box = db.Column(db.String(80), nullable=False, unique=False)
    tanggal_penyewaan = db.Column(db.String(80), nullable=False, unique=False)
    lama_penitipan = db.Column(db.Integer, nullable=False, unique=False)
    
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
            'lama_penitipan': self.lama_penitipan
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