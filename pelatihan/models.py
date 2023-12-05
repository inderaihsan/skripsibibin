from django.db import models
from django.utils.timezone import now
# Create your models here. 


class Bank(models.Model) : 
    nama = models.CharField(max_length = 221) 

    class Meta : 
        db_table = 'bank' 
        
    def __str__(self) : 
        return self.nama
        
class Kecamatan(models.Model) : 
    nama = models.CharField(max_length=221)

    class Meta : 
        db_table = 'kecamatan'
    
    def __str__(self):
        return self.nama 
class Kelurahan(models.Model) : 
    nama = models.CharField(max_length = 221) 
    kecamatan = models.ForeignKey(Kecamatan, on_delete=models.CASCADE)
    
    class Meta : 
        db_table = 'kelurahan'
        
    def __str__(self):
        return self.nama 

class Peserta(models.Model):
    nama = models.CharField(max_length=221) 
    no_kontak = models.CharField(max_length = 221)
    nik = models.CharField(max_length=221)
    no_kk = models.CharField(max_length=221) 
    no_rekening = models.CharField(max_length=221)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    pendidikan = models.CharField(max_length=221) #bikin master
    tempat_lahir = models.CharField(max_length=221) #tempat lahir
    tanggal_lahir = models.DateField() #tanggal lahir
    status = models.CharField(max_length=221) #status
    pekerjaan = models.CharField(max_length=221) #pekerjaaan
    alamat = models.CharField(max_length = 221)   
    keterangan = models.CharField(max_length = 221)
    kelurahan = models.ForeignKey(Kelurahan, on_delete = models.CASCADE)    
    honor = models.IntegerField()
    
    
    def __str__(self):
        return self.nama 
    
    class Meta : 
        db_table = 'peserta'
    
        
class Jenis_pelatihan(models.Model) : 
    nama = models.CharField(max_length = 221)
    
    class Meta : 
        db_table = 'jenis_pelatihan'
        
    def __str__(self):
        return self.nama 

class Pelatihan(models.Model) : 
    nama = models.CharField(max_length =221) 
    jenis_pelatihan = models.ForeignKey(Jenis_pelatihan, on_delete=models.CASCADE)
    keterangan = models.CharField(max_length = 221) 
    lokasi = models.CharField(max_length=221)
    tanggal_mulai = models.DateField()
    tanggal_selesai = models.DateField()  
    
    class Meta : 
        db_table = 'pelatihan' 
    
    def __str__(self):
        return self.nama 
    
class Status_pendaftaran(models.Model) : 
    nama_status = models.CharField(max_length=221)  
    
    class Meta : 
        db_table = 'status_pendaftaran' 
    
    def __str__(self) : 
        return self.nama_status
    
class Pendaftaran(models.Model) : 
    peserta = models.ForeignKey(Peserta, on_delete=models.CASCADE)
    pelatihan = models.ForeignKey(Pelatihan, on_delete=models.CASCADE) 
    status = models.ForeignKey(Status_pendaftaran, on_delete=models.CASCADE) 
    registered_at = models.DateTimeField(default = now) 
    
    class Meta : 
        db_table = 'pendaftaran' 
    
    # def __str__(self) : 
    #     return self.peserta
    