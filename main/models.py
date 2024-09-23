from django.contrib.auth.models import User
import uuid  # tambahkan baris ini di paling atas
from django.db import models

class PesananEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    pesanan = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    keterangan = models.TextField()
    quantitas = models.IntegerField()

    @property
    def is_mood_strong(self):
        return self.quantitas > 5