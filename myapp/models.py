from django.db import models
import face_recognition

# Create your models here.
class Criminal(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='criminal_photos/')
    description = models.TextField()
    date_of_birth = models.DateField()
    address = models.TextField()
    criminal_record = models.TextField()
    face_encoding = models.BinaryField(null=True, blank=True)

    def save(self, *args, **kwargs):
        image = face_recognition.load_image_file(self.photo)
        encodings = face_recognition.face_encodings(image)
        if encodings:
            self.face_encoding = encodings[0].tobytes()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Complaint(models.Model):

    criminal = models.ForeignKey(Criminal, on_delete=models.CASCADE)
    complaint_no = models.IntegerField()
    crime_date = models.DateField()
    complaint_by = models.CharField(max_length=100)
    crime_location = models.TextField()
    criminal_contact = models.BigIntegerField()
    


