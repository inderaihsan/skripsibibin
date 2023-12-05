from rest_framework import serializers
from . models import Pelatihan
    
    
class PelatihanSerializer(serializers.ModelSerializer) : 
    status = serializers.SerializerMethodField()
    class Meta : 
        model = Pelatihan 
        fields = '__all__'
    def get_status(self, obj) : 
        if (obj.tanggal_selesai < obj.tanggal_mulai) : 
            return 1 
        else : 
            return 0
        